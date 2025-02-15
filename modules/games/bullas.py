import asyncio
import time
import random
from random import random as rand_random

from modules.interfaces import SoftwareExceptionWithoutRetry, SoftwareException
from modules import RequestClient, Logger, Client
from utils.tools import helper
from config import BULLAS_ABI, ERC721MInitializableV1_0_1_ABI, TOKENS_PER_CHAIN, CONTRACTS_PER_CHAIN, NFTS_PER_CHAIN


class Bullas(Logger, RequestClient):
    def __init__(self, client: Client):
        self.client = client
        Logger.__init__(self)
        RequestClient.__init__(self, client)
        self.network = self.client.network.name

        self.multicall_contract = self.client.get_contract(
            CONTRACTS_PER_CHAIN[self.network]['BULLAS']['Multicall'], BULLAS_ABI['Multicall']
            )
        self.factory_contract = self.client.get_contract(
            CONTRACTS_PER_CHAIN[self.network]['BULLAS']['Factory'], BULLAS_ABI['Factory']
            )
        self.bullish_contract = self.client.get_contract(
            CONTRACTS_PER_CHAIN[self.network]['BULLAS']['Bullish'], BULLAS_ABI['Bullish']
            )
        
        self.queue_plugin_contract = self.client.get_contract(
            CONTRACTS_PER_CHAIN[self.network]['BULLAS']['QueuePlugin'], BULLAS_ABI['QueuePlugin']
            )

        self.bullas_nft_ME_contract = self.client.get_contract(
            NFTS_PER_CHAIN[self.network]['Bullas'], ERC721MInitializableV1_0_1_ABI
            )

    async def get_main_bullas_nft_id(self):
        call = await self.bullas_nft_ME_contract.functions.tokensOfOwner(self.client.address).call()

        if len(call) == 0:
            self.logger_msg(
                *self.client.acc_info,
                msg=f"You don't have any Bullas NFT",
                type_msg="warning",
            )
            return None
        elif len(call) > 1:
            self.logger_msg(
                *self.client.acc_info,
                msg=f"You have more than 1 Bullas NFT",
                type_msg="warning",
            )
            return None
        else:
            return int(call[0])

    async def check_if_main_bullas_nft_is_not_used(self):
        main_bullas_nft_id = await self.get_main_bullas_nft_id()
        if not main_bullas_nft_id:
            raise SoftwareExceptionWithoutRetry(f"Problem with your Bullas NFT")

        call = await self.bullish_contract.functions.bullas_Claimed(main_bullas_nft_id).call()

        if call == True:
            raise SoftwareExceptionWithoutRetry(
                f"Your main Bullas NFT ({main_bullas_nft_id}) is already used for pass minting"
            )

        return True, main_bullas_nft_id

    @helper
    async def claim_free_gamepass_for_main_bullas_nft(self):
        _, main_bullas_nft_id = await self.check_if_main_bullas_nft_is_not_used()

        self.logger_msg(
            *self.client.acc_info,
            msg=f"Claiming free pass for main Bullas NFT: {main_bullas_nft_id}",
            type_msg="info",
        )
        try:
            transaction = await self.bullish_contract.functions.claim(
                main_bullas_nft_id
            ).build_transaction(await self.client.prepare_transaction(value=0))
            return await self.client.send_transaction(transaction)
        except Exception as error:
            raise SoftwareException(
                f"Error claiming free pass for main Bullas NFT: {main_bullas_nft_id}",
                error,
            )

    async def get_game_pass_id(self):
        try:
            nft_id = await self.bullish_contract.functions.tokenOfOwnerByIndex(self.client.address, 0).call()
            return nft_id
        except Exception as error:
            if 'owner index out of bounds' in str(error):
                raise SoftwareExceptionWithoutRetry(f"You don't have any game pass for Bullas")
            else:
                raise error
            
    async def get_power_of_nft_id(self, nft_id: int):
        power_wei = await self.queue_plugin_contract.functions.getPower(nft_id).call()
        power_ether = self.client.from_wei(power_wei)
        return power_ether

    async def _make_click(self, game_pass_id: int):
        messages = ['BULL ISH', 'MOOOO!', 'OOGA MOOLA']
        random_message = random.choice(messages)
        click_value_wei = await self.queue_plugin_contract.functions.entryFee().call()
        click_value_ether = self.client.from_wei(click_value_wei)
        
        self.logger_msg(
            *self.client.acc_info,
            msg=f"Start to make bullas click for game pass {game_pass_id} with value: {click_value_ether} $BERA",
            type_msg="info",
        )
        
        try:
            transaction = await self.multicall_contract.functions.click(
                game_pass_id,
                1,
                random_message,
                ).build_transaction(await self.client.prepare_transaction(value=click_value_wei))
            return await self.client.send_transaction(transaction)
        except Exception as error:
            raise SoftwareException(f"Error making click: {error}")


    @helper
    async def make_first_click_only_once_for_start_mining_moola(self):
        moola_balance_wei, moola_balance_ether, _ = await self.client.get_token_balance('MOOLA')

        if moola_balance_wei > 0:
            raise SoftwareExceptionWithoutRetry(
                f"You already have Moola: {moola_balance_ether} MOOLA. Don't need to pay for start mining"
            )

        game_pass_id = await self.get_game_pass_id()
        return await self._make_click(game_pass_id)

    @helper
    async def purchase_upgrade_for_moola(self):
        print(await self.check_if_main_bullas_nft_is_not_used())
        pass
