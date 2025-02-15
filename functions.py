from modules import *
from utils.networks import *


def get_client(module_input_data) -> Client:
    return Client(module_input_data)


def get_rpc_by_chain_name(chain_name):
    return {
        0: BerachainRPC,
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
        "Berachain": BerachainRPC,
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

async def bullas_purchase_upgrade_for_moola(module_input_data):
    worker = Bullas(get_client(module_input_data))
    return await worker.purchase_upgrade_for_moola()

async def bullas_claim_free_gamepass_for_main_bullas_nft(module_input_data):
    worker = Bullas(get_client(module_input_data))
    return await worker.claim_free_gamepass_for_main_bullas_nft()

async def bullas_make_first_click_only_once_for_start_mining_moola(module_input_data):
    worker = Bullas(get_client(module_input_data))
    return await worker.make_first_click_only_once_for_start_mining_moola()
