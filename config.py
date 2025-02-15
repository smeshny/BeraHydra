from dev import GeneralSettings
from utils.tools import get_accounts_data

TOTAL_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

ERC20_ABI = [{'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}, {'internalType': 'string', 'name': '_symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': '_initialSupply', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'name': 'setupDecimals', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}]

WETH_ABI = [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'BridgeBurn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'l1Token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'BridgeInitialize', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'BridgeMint', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'Initialize', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'version', 'type': 'uint8'}], 'name': 'Initialized', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [], 'name': 'DOMAIN_SEPARATOR', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'bridgeBurn', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'bridgeMint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'deposit', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}], 'name': 'depositTo', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'l1Address', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'l2Bridge', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdrawTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'stateMutability': 'payable', 'type': 'receive'}]

MULTICALL3_ABI = [{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes[]","name":"returnData","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3[]","name":"calls","type":"tuple[]"}],"name":"aggregate3","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3Value[]","name":"calls","type":"tuple[]"}],"name":"aggregate3Value","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"blockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBasefee","outputs":[{"internalType":"uint256","name":"basefee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBlockNumber","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"chainid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockCoinbase","outputs":[{"internalType":"address","name":"coinbase","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockDifficulty","outputs":[{"internalType":"uint256","name":"difficulty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockGasLimit","outputs":[{"internalType":"uint256","name":"gaslimit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryAggregate","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryBlockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"}]


ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

ETH_MASK = '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'

MULTICALL3_CONTRACTS = {
    'Arbitrum'                   : '0xcA11bde05977b3631167028862bE2a173976CA11',
    'Berachain'                  : '0xcA11bde05977b3631167028862bE2a173976CA11',
}

TOKENS_PER_CHAIN = {
    'Ethereum': {
        'ETH': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
        'WETH': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
        'ZRO': '0x6985884C4392D348587B19cb9eAAf157F13271cd',
        'USDC': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
        'USDT': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
        'TIA.n': '0x15b5D6B614242B118AA404528A7f3E2Ad241e4A4',
        'STG': '0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6',
        'USDV': '0x0E573Ce2736Dd9637A0b21058352e1667925C7a8',
        'MAV': '0x7448c7456a97769F6cD04F1E83A4a23cCdC46aBD',
        'ezETH': '0xbf5495Efe5DB9ce00f80364C8B423567e58d2110'
    },
    'Arbitrum': {
        "ETH"                    : "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "WETH"                   : "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        # "ZRO": "0x6985884C4392D348587B19cb9eAAf157F13271cd",
        'USDC'                   : '0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
        'USDC.e'                 : '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        'USDT'                   : '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
        # 'fUSDC': '0x4CFA50B7Ce747e2D61724fcAc57f24B748FF2b2A',
        # 'TIA.n': '0xD56734d7f9979dD94FAE3d67C7e928234e71cD4C',
        # 'STG': '0x6694340fc020c5E6B96567843da2df01b2CE1eb6',
        # 'USDV': '0x323665443CEf804A3b5206103304BD4872EA4253',
        # 'ezETH': '0x2416092f143378750bb29b79eD961ab195CcEea5'
    },

}

COTRACTS_PER_CHAIN = {
    'HyperTestnet': {
        'HUPURR_FI':{
            'deposit_pool'      : '0x4073283812dfD8fff8430c1Ec8f88A68f984Aec3',
            'oracle'            : '0x9E9613D29e15d6fa01bcbAc39550d0194d03310a'
            }                   
    }
}

TOKEN_API_INFO = {
    'coingecko': {
        'COREDAO': 'coredaoorg',
        'JEWEL': 'defi-kingdoms',
        'SMR': 'shimmer',
        'TOMOE': 'tomoe',
        'ZBC': 'zebec-protocol'
    },
    'binance': [
        'ETH',
        'ASTR',
        'AVAX',
        'BNB',
        'WBNB',
        'CELO',
        'CFX',
        'FTM',
        'GETH'
        'ONE',
        'ZEN',
        'KAVA',
        'KLAY',
        'AGLD',
        'METIS',
        'GLMR',
        'MOVR',
        'MATIC',
        'WMATIC'
        'BEAM',
        'INJ',
        'WETH',
        'WETH.e',
        'STG',
        'MAV',
        'ARB',
        'OP',
        'TIA',
        'TIA.n',
        'NTRN',
        'ZRO',
        'SOL',
        'ezETH',
        'wrsETH'
    ],
    'gate': [
        'CANTO',
        'FUSE',
        'MNT',
        'MTR',
        'OKT',
        'TLOS',
        'TENET',
        'XPLA',
        'CORE'
    ],
    'stables': [
        'xDAI',
        'DAI',
        'USDT',
        'USDC',
        'USDC.e',
        'BUSD',
        'USDbC',
        'fUSDC',
        'USDB'
    ]
}

OKX_NETWORKS_NAME = {
    1                       : 'ETH-ERC20',
    2                       : 'ETH-Arbitrum One',
    3                       : 'ETH-Optimism',
    4                       : 'ETH-zkSync Era',
    5                       : 'ETH-Linea',
    6                       : 'ETH-Base',
    7                       : 'AVAX-Avalanche C-Chain',
    8                       : 'BNB-BSC',
    # 9                     : 'BNB-OPBNB',
    10                      : 'CELO-CELO',
    11                      : 'GLMR-Moonbeam',
    12                      : 'MOVR-Moonriver',
    13                      : 'METIS-Metis',
    14                      : 'CORE-CORE',
    15                      : 'CFX-CFX_EVM',
    16                      : 'KLAY-Klaytn',
    17                      : 'FTM-Fantom',
    18                      : 'POL-Polygon',
    19                      : 'USDT-Arbitrum One',
    20                      : 'USDT-Avalanche C-Chain',
    21                      : 'USDT-Optimism',
    22                      : 'USDT-Polygon',
    23                      : 'USDT-BSC',
    24                      : 'USDT-ERC20',
    25                      : 'USDC-Arbitrum One',
    26                      : 'USDC-Avalanche C-Chain',
    27                      : 'USDC-Optimism',
    28                      : 'USDC-Polygon',
    29                      : 'USDC-Optimism (Bridged)',
    30                      : 'USDC-Polygon (Bridged)',
    31                      : 'USDC-BSC',
    32                      : 'USDC-ERC20',
    # 33                      : 'STG-Arbitrum One',
    # 34                      : 'STG-BSC',
    # 35                      : 'STG-Avalanche C-Chain',
    # 36                      : 'STG-Fantom',
    # 37                      : 'USDV-BSC',
    38                       : 'ARB-Arbitrum One',
    # 39                      : "MAV-BASE",
    # 40                      : "MAV-ZKSYNCERA",
    41                      : "OP-Optimism",
    42                      : "INJ-INJ",
    43                      : "TIA-Celestia",
    # 44                      : "NTRN-NTRN",
    47                      : "SOL-Solana",
    48                      : "OKB-X Layer",
}

BINANCE_NETWORKS_NAME = {
    1                       : "ETH-ETH",
    2                       : "ETH-ARBITRUM",
    3                       : "ETH-OPTIMISM",
    4                       : "ETH-ZKSYNCERA",
    # 5                     : "ETH-LINEA",
    6                       : "ETH-BASE",
    7                       : 'AVAX-AVAXC',
    8                       : 'BNB-BSC',
    9                       : 'BNB-OPBNB',
    10                      : 'CELO-CELO',
    11                      : 'GLMR-Moonbeam',
    12                      : 'MOVR-Moonriver',
    # 13                    : 'METIS-METIS',
    # 14                    : 'CORE-CORE',
    15                      : 'CFX-CFX',
    16                      : 'KLAY-KLAYTN',
    17                      : 'FTM-FANTOM',
    18                      : 'POL-MATIC',
    19                      : 'USDT-ARBITRUM',
    20                      : 'USDT-AVAXC',
    21                      : 'USDT-OPTIMISM',
    22                      : 'USDT-MATIC',
    23                      : 'USDT-BSC',
    24                      : 'USDT-ETH',
    25                      : 'USDC-ARBITRUM',
    26                      : 'USDC-AVAXC',
    27                      : 'USDC-OPTIMISM',
    28                      : 'USDC-MATIC',
    # 29                    : 'USDC-Optimism (Bridged)',
    # 30                    : 'USDC-Polygon (Bridged)',
    31                      : 'USDC-BSC',
    32                      : 'USDC-ETH',
    33                      : 'STG-ARBITRUM',
    34                      : 'STG-BSC',
    35                      : 'STG-AVAXC',
    36                      : 'STG-FTM',
    # 37                      : 'USDV-BSC',
    38                      : 'ARB-ARBITRUM',
    39                      : "MAV-BASE",
    40                      : "MAV-ZKSYNCERA",
    41                      : "OP-OPTIMISM",
    42                      : "INJ-INJ",
    43                      : "TIA-TIA",
    44                      : "NTRN-NTRN",
    45                      : "ETH-MANTA",
    46                      : "ETH-BSC",
    47                      : "SOL-SOL",
}


CEX_WRAPPED_ID = {
     1                          : "Ethereum",
     2                          : "Arbitrum",
     3                          : "Optimism",
     4                          : "zkSync",
     5                          : "Linea",
     6                          : "Base",
     7                          : "Avalanche",
     8                          : "BNB Chain",
     9                          : "OpBNB",
     10                         : "Celo",
     11                         : "Moonbeam",
     12                         : "Moonriver",
     13                         : "Metis",
     14                         : "CoreDAO",
     15                         : "Conflux",
     16                         : "Klaytn",
     17                         : "Fantom",
     18                         : "Polygon",
     19                         : "Arbitrum",
     20                         : "Avalanche",
     21                         : "Optimism",
     22                         : "Polygon",
     23                         : "BNB Chain",
     24                         : "Ethereum",
     25                         : "Arbitrum",
     26                         : "Avalanche",
     27                         : "Optimism",
     28                         : "Polygon",
     29                         : "Optimism",
     30                         : "Polygon",
     31                         : "BNB Chain",
     32                         : "Ethereum",
     33                         : "Arbitrum",
     34                         : "BNB Chain",
     35                         : "Avalanche",
     36                         : "Fantom",
     37                         : "BNB Chain",
     38                         : "Arbtirum",
     39                         : "Base",
     40                         : "zkSync",
     41                         : "Optimism",
     42                         : "Injective",
     43                         : "Celestia",
     44                         : "Neutron",
     45                         : "Manta",
     46                         : "BNB Chain",
     47                         : "Solana",
     48                         : "xLayer",
}



CHAIN_NAME_FROM_ID = {
    42161: 'Arbitrum',
    42170: 'Arbitrum Nova',
    8453: 'Base',
    59144: 'Linea',
    169: 'Manta',
    56: 'BNB Chain',
    137: 'Polygon',
    10: 'Optimism',
    534352: 'Scroll',
    1101: 'Polygon zkEVM',
    324: 'zkSync',
    7777777: 'Zora',
    1: 'Ethereum',
    43114: 'Avalanche'
}

CHAIN_IDS = {
    'Arbitrum':  42161,
    'Arbitrum Nova':  42170,
    'Base':  8453,
    'Linea':  59144,
    'Manta':  169,
    'BNB Chain':  56,
    'Polygon':  137,
    'Optimism':  10,
    'Scroll': 534352,
    'Polygon zkEVM': 1101,
    'zkSync': 324,
    'Zora': 7777777,
    'Ethereum': 1,
    'Avalanche': 43114
}

IMAP_CONFIG = {
    'outlook.com': 'outlook.office365.com',
    'hotmail.com': 'imap-mail.outlook.com',
}

GeneralSettings.prepare_general_settings()
ACCOUNTS_DATA = get_accounts_data()


TITLE = """


██████╗ ███████╗██████╗  █████╗     ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝█████╗  ██████╔╝███████║    ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
██╔══██╗██╔══╝  ██╔══██╗██╔══██║    ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
██████╔╝███████╗██║  ██║██║  ██║    ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                             
                                                           
"""
