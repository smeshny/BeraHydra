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
            await self.client.send_transaction(transaction)
        except Exception as error:
            raise SoftwareException(
                f"Error claiming free pass for main Bullas NFT: {main_bullas_nft_id}",
                error,
            )

    @helper
    async def purchase_upgrade_for_moola(self):
        print(await self.check_if_main_bullas_nft_is_not_used())
        pass
