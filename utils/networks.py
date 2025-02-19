class Network:
    def __init__(
            self,
            name: str,
            rpc: list,
            chain_id: int,
            eip1559_support: bool,
            token: str,
            explorer: str,
            decimals: int = 18
    ):
        self.name = name
        self.rpc = rpc
        self.chain_id = chain_id
        self.eip1559_support = eip1559_support
        self.token = token
        self.explorer = explorer
        self.decimals = decimals

    def __repr__(self):
        return f'{self.name}'


BerachainRPC = Network(
    name='Berachain',
    rpc=[
        'https://rpc.berachain.com'
    ],
    chain_id=80094,
    eip1559_support=True,
    token='BERA',
    explorer='https://berascan.com/'
)

BlockchainLOLRPC = Network(
    name='BlockchainLOL',
    rpc=[
        'https://block-chain.alt.technology'
    ],
    chain_id=6231991,
    eip1559_support=True,
    token='BITCOIN',
    explorer='https://explorer.block-chain.lol/'
)

EthereumRPC = Network(
    name='Ethereum',
    rpc=[
        'https://rpc.ankr.com/eth',
        'https://eth.drpc.org'
    ],
    chain_id=1,
    eip1559_support=False,
    token='ETH',
    explorer='https://etherscan.io/'
)

ScrollRPC = Network(
    name='Scroll',
    rpc=[
        'https://rpc.scroll.io',
        'https://rpc.ankr.com/scroll',
    ],
    chain_id=534352,
    eip1559_support=False,
    token='ETH',
    explorer='https://scrollscan.com/'
)

ArbitrumRPC = Network(
    name='Arbitrum',
    rpc=[
        'https://arbitrum.llamarpc.com',
    ],
    chain_id=42161,
    eip1559_support=False,
    token='ETH',
    explorer='https://arbiscan.io/',
)

PolygonRPC = Network(
    name='Polygon',
    rpc=[
        'https://polygon-rpc.com',
    ],
    chain_id=137,
    eip1559_support=False,
    token='MATIC',
    explorer='https://polygonscan.com/',
)

AvalancheRPC = Network(
    name='Avalanche',
    rpc=[
        'https://avalanche.drpc.org'
    ],
    chain_id=43114,
    eip1559_support=False,
    token='AVAX',
    explorer='https://snowtrace.io/',
)

Arbitrum_novaRPC = Network(
    name='Arbitrum Nova',
    rpc=[
        'https://rpc.ankr.com/arbitrumnova',
        'https://arbitrum-nova.publicnode.com',
        'https://arbitrum-nova.drpc.org',
        'https://nova.arbitrum.io/rpc'
    ],
    chain_id=42170,
    eip1559_support=False,
    token='ETH',
    explorer='https://nova.arbiscan.io/'
)

BaseRPC = Network(
    name='Base',
    rpc=[
        'https://mainnet.base.org',
    ],
    chain_id=8453,
    eip1559_support=False,
    token='ETH',
    explorer='https://basescan.org/'
)

LineaRPC = Network(
    name='Linea',
    rpc=[
        # 'https://linea.drpc.org',
        'https://rpc.linea.build'
    ],
    chain_id=59144,
    eip1559_support=False,
    token='ETH',
    explorer='https://lineascan.build/'
)

ZoraRPC = Network(
    name='Zora',
    rpc=[
        'https://rpc.zora.energy'
    ],
    chain_id=7777777,
    eip1559_support=False,
    token='ETH',
    explorer='https://zora.superscan.network/'
)

Polygon_ZKEVM_RPC = Network(
    name='Polygon zkEVM',
    rpc=[
        'https://1rpc.io/polygon/zkevm',
        'https://zkevm-rpc.com',
        'https://rpc.ankr.com/polygon_zkevm'
    ],
    chain_id=1101,
    eip1559_support=False,
    token='ETH',
    explorer='https://zkevm.polygonscan.com/'
)

BSC_RPC = Network(
    name='BNB Chain',
    rpc=[
        'https://rpc.ankr.com/bsc',
        'https://binance.llamarpc.com',
    ],
    chain_id=56,
    eip1559_support=False,
    token='BNB',
    explorer='https://bscscan.com/'
)

MantaRPC = Network(
    name='Manta',
    rpc=[
        'https://pacific-rpc.manta.network/http'
        'https://1rpc.io/manta'
    ],
    chain_id=169,
    eip1559_support=False,
    token='ETH',
    explorer='https://pacific-explorer.manta.network/'
)

OptimismRPC = Network(
    name='Optimism',
    rpc=[
        'https://optimism.llamarpc.com',
        # 'https://optimism.drpc.org',
    ],
    chain_id=10,
    eip1559_support=False,
    token='ETH',
    explorer='https://optimistic.etherscan.io/',
)

zkSyncEraRPC = Network(
    name='zkSync',
    rpc=[
        'https://mainnet.era.zksync.io',
    ],
    chain_id=324,
    eip1559_support=False,
    token='ETH',
    explorer='https://era.zksync.network/',
)
