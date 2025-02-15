from modules import *
from utils.networks import *


def get_client(module_input_data) -> Client:
    return Client(module_input_data)


def get_rpc_by_chain_name(chain_name):
    return {
        0: BeraChainRPC,
        "Arbitrum": ArbitrumRPC,
        "Arbitrum Nova": Arbitrum_novaRPC,
        "Base": BaseRPC,
        "Linea": LineaRPC,
        "Manta": MantaRPC,
        "Polygon": PolygonRPC,
        "Optimism": OptimismRPC,
        "Scroll": ScrollRPC,
        "Polygon zkEVM": Polygon_ZKEVM_RPC,
        "zkSync": zkSyncEraRPC,
        "Zora": ZoraRPC,
        "Ethereum": EthereumRPC,
        "Avalanche": AvalancheRPC,
        "BNB Chain": BSC_RPC,
        "BeraChain": BeraChainRPC,
        "HyperTestnet": HyperTestnetRPC
    }[chain_name]


async def bridge_utils(current_client, dapp_id, bridge_data, need_fee=False):
    class_bridge = {
        # 1: Across,
        # 2: Bungee,
        3: Relay,
    }[dapp_id]

    return await class_bridge(current_client).bridge(bridge_data, need_check=need_fee)


async def binance_withdraw(module_input_data):
    worker = Custom(get_client(module_input_data))
    return await worker.smart_cex_withdraw(dapp_id=3)


async def bridge_relay(module_input_data):
    worker = Custom(get_client(module_input_data))
    return await worker.smart_bridge(dapp_id=3)

async def wrap_native(module_input_data):
    worker = Custom(get_client(module_input_data))
    return await worker.wrap_native()


async def unwrap_native(module_input_data):
    worker = Custom(get_client(module_input_data))
    return await worker.unwrap_native()


async def transfer_eth(module_input_data):
    module_input_data['network'] = EthereumRPC
    worker = Custom(Client(module_input_data))
    return await worker.transfer_eth()

async def claim_tokens_on_hypurr(module_input_data):
    worker = HupurrFaucet(get_client(module_input_data))
    return await worker.claim_tokens_on_hypurr()

async def claim_hype_on_hyperlend_once(module_input_data):
    worker = HyperlendFaucet(get_client(module_input_data))
    return await worker.claim_hype_on_hyperlend_once()

async def claim_MBTC_on_hyperlend_once(module_input_data):
    worker = HyperlendFaucet(get_client(module_input_data))
    return await worker.claim_MBTC_on_hyperlend_once()

async def deposit_usdc_to_hypurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.deposit_usdc_to_hypurr()

async def deposit_susde_to_hypurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.deposit_susde_to_hypurr()

async def deposit_solvbtc_to_hypurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.deposit_solvbtc_to_hypurr()

async def borrow_usdc_from_hupurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.borrow_usdc_from_hupurr()

async def borrow_usdxl_from_hupurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.borrow_usdxl_from_hupurr()

async def borrow_whype_from_hupurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.borrow_whype_from_hupurr()

async def borrow_susde_from_hupurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.borrow_susde_from_hupurr()

async def borrow_solvbtc_from_hupurr(module_input_data):
    worker = HupurrFi(get_client(module_input_data))
    return await worker.borrow_solvbtc_from_hupurr()

async def claim_usdc_from_hl_exchange_testnet_once(module_input_data):
    worker = HlExchangeTestnet(get_client(module_input_data))
    return await worker.claim_usdc_from_hl_exchange_testnet_once()

async def open_random_perp_position_on_hl(module_input_data):
    worker = HlExchangeTestnet(get_client(module_input_data))
    return await worker.open_random_perp_position()

async def close_all_perp_positions_on_hl(module_input_data):
    worker = HlExchangeTestnet(get_client(module_input_data))
    return await worker.close_all_perp_positions()

async def close_random_perp_position_on_hl(module_input_data):
    worker = HlExchangeTestnet(get_client(module_input_data))
    return await worker.close_random_perp_position()