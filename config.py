from dev import GeneralSettings
from utils.tools import get_accounts_data

TOTAL_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

ERC20_ABI = [{'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}, {'internalType': 'string', 'name': '_symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': '_initialSupply', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'name': 'setupDecimals', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}]

WETH_ABI = [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'BridgeBurn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'l1Token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'BridgeInitialize', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': '_account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'BridgeMint', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'Initialize', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'version', 'type': 'uint8'}], 'name': 'Initialized', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [], 'name': 'DOMAIN_SEPARATOR', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_from', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'bridgeBurn', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'bridgeMint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'deposit', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}], 'name': 'depositTo', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'l1Address', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'l2Bridge', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdrawTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'stateMutability': 'payable', 'type': 'receive'}]

MULTICALL3_ABI = [{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes[]","name":"returnData","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3[]","name":"calls","type":"tuple[]"}],"name":"aggregate3","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3Value[]","name":"calls","type":"tuple[]"}],"name":"aggregate3Value","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"blockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBasefee","outputs":[{"internalType":"uint256","name":"basefee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBlockNumber","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"chainid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockCoinbase","outputs":[{"internalType":"address","name":"coinbase","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockDifficulty","outputs":[{"internalType":"uint256","name":"difficulty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockGasLimit","outputs":[{"internalType":"uint256","name":"gaslimit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryAggregate","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryBlockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"}]

BULLAS_ABI = {
    'Multicall': [{"inputs":[{"internalType":"address","name":"_base","type":"address"},{"internalType":"address","name":"_units","type":"address"},{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_key","type":"address"},{"internalType":"address","name":"_plugin","type":"address"},{"internalType":"address","name":"_oBERO","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"base","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"string","name":"message","type":"string"}],"name":"click","outputs":[{"internalType":"uint256","name":"mintAmount","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getFactory","outputs":[{"components":[{"internalType":"uint256","name":"unitsBalance","type":"uint256"},{"internalType":"uint256","name":"ups","type":"uint256"},{"internalType":"uint256","name":"upc","type":"uint256"},{"internalType":"uint256","name":"capacity","type":"uint256"},{"internalType":"uint256","name":"claimable","type":"uint256"},{"internalType":"bool","name":"full","type":"bool"}],"internalType":"struct Multicall.FactoryState","name":"factoryState","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getGauge","outputs":[{"components":[{"internalType":"uint256","name":"rewardPerToken","type":"uint256"},{"internalType":"uint256","name":"totalSupply","type":"uint256"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"earned","type":"uint256"},{"internalType":"uint256","name":"oBeroBalance","type":"uint256"}],"internalType":"struct Multicall.GaugeState","name":"gaugeState","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"toolId","type":"uint256"},{"internalType":"uint256","name":"purchaseAmount","type":"uint256"}],"name":"getMultipleToolCost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getTools","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"cost","type":"uint256"},{"internalType":"uint256","name":"ups","type":"uint256"},{"internalType":"uint256","name":"upsTotal","type":"uint256"},{"internalType":"uint256","name":"percentOfProduction","type":"uint256"},{"internalType":"bool","name":"maxed","type":"bool"}],"internalType":"struct Multicall.ToolState[]","name":"toolState","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getUpgrades","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"cost","type":"uint256"},{"internalType":"bool","name":"upgradeable","type":"bool"}],"internalType":"struct Multicall.ToolUpgradeState[]","name":"toolUpgradeState","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"key","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"oBERO","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"plugin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"units","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}],
    
    'Factory': [{"inputs":[{"internalType":"address","name":"_units","type":"address"},{"internalType":"address","name":"_key","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"Factory__AmountMaxed","type":"error"},{"inputs":[],"name":"Factory__CannotEvolve","type":"error"},{"inputs":[],"name":"Factory__InvalidInput","type":"error"},{"inputs":[],"name":"Factory__InvalidLength","type":"error"},{"inputs":[],"name":"Factory__InvalidTokenId","type":"error"},{"inputs":[],"name":"Factory__LevelMaxed","type":"error"},{"inputs":[],"name":"Factory__NotAuthorized","type":"error"},{"inputs":[],"name":"Factory__ToolDoesNotExist","type":"error"},{"inputs":[],"name":"Factory__UpgradeLocked","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Factory__Claimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"lvl","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"cost","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"unlock","type":"uint256"}],"name":"Factory__LvlSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"multiplier","type":"uint256"}],"name":"Factory__ToolMultiplierSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"toolId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"newAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"cost","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"ups","type":"uint256"}],"name":"Factory__ToolPurchased","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"toolId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"baseUps","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"baseCost","type":"uint256"}],"name":"Factory__ToolSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"toolId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"newLevel","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"cost","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"ups","type":"uint256"}],"name":"Factory__ToolUpgraded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"amountIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"amount_CostMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"toolId","type":"uint256"},{"internalType":"uint256","name":"initialAmount","type":"uint256"},{"internalType":"uint256","name":"finalAmount","type":"uint256"}],"name":"getMultipleToolCost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"toolId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getToolCost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"toolId","type":"uint256"},{"internalType":"uint256","name":"lvl","type":"uint256"}],"name":"getToolUps","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"key","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lvlIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lvl_CostMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lvl_Unlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"toolId","type":"uint256"},{"internalType":"uint256","name":"toolAmount","type":"uint256"}],"name":"purchaseTool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"cost","type":"uint256[]"},{"internalType":"uint256[]","name":"unlock","type":"uint256[]"}],"name":"setLvl","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"baseUps","type":"uint256[]"},{"internalType":"uint256[]","name":"baseCost","type":"uint256[]"}],"name":"setTool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"multipliers","type":"uint256[]"}],"name":"setToolMultipliers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenId_Last","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenId_Ups","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenId_toolId_Amount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenId_toolId_Lvl","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"toolId_BaseCost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"toolId_BaseUps","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"toolIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"units","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"toolId","type":"uint256"}],"name":"upgradeTool","outputs":[],"stateMutability":"nonpayable","type":"function"}],

}

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

ETH_MASK = '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'

MULTICALL3_CONTRACTS = {
    'Arbitrum'                   : '0xcA11bde05977b3631167028862bE2a173976CA11',
    'Berachain'                  : '0xcA11bde05977b3631167028862bE2a173976CA11',
}

TOKENS_PER_CHAIN = {
    'Ethereum': {
        'ETH'                   : '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
        'WETH'                  : '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
        'USDC'                  : '0xdAC17F958D2ee523a2206206994597C13D831ec7',
        'USDT'                  : '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
    },
    'Arbitrum': {
        "ETH"                    : "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "WETH"                   : "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        'USDC'                   : '0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
        'USDC.e'                 : '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        'USDT'                   : '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
    },
    'Berachain': {
        'BERA'                   : '0x6969696969696969696969696969696969696969',
        'WBERA'                  : '0x6969696969696969696969696969696969696969',
        # 'BGT'                    : '0x656b95E550C07a9ffe548bd4085c72418Ceb1dba',
        # 'HONEY'                  : '0xFCBD14DC51f0A4d49d5E53C2E0950e0bC26d0Dce',
        # 'BYUSD'                  : '0x688e72142674041f8f6Af4c808a4045cA1D6aC82',
        # 'USDC.e'                 : '0x549943e04f40284185054145c6E4e9568C1D3241',
        # 'USDT0'                  : '0x779Ded0c9e1022225f8E0630b35a9b54bE713736',
        # 'WBTC'                   : '0x0555E30da8f98308EdB960aa94C0Db47230d2B9c',
        # 'WETH'                   : '0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590',
        # 'iBERA'                  : '0x9b6761bf2397Bb5a6624a856cC84A3A14Dcd3fe5',
        # 'iBGT'                   : '0xac03CABA51e17c86c921E1f6CBFBdC91F8BB2E6b',
        'MOOLA'                  : '0x331865bF2eA19E94bBF438Cf4ee590cB6392E5A9',
        
    }

}

NFTS_PER_CHAIN = {
    'Berachain' :{
        'Bullas'                 : '0x333814f5E16EEE61d0c0B03a5b6ABbD424B381c2',
        'THC Podcast'            : '0x229F67d36BF9BEB006302d800CCeF660D75bA339'
    }
}

COTRACTS_PER_CHAIN = {
    'Berachain': {
        'BULLAS':{
            'Multicall'          : '0x2972e38A38956148AA93801A8A78459020a34523',
            'Factory'            : '0x8d15Db9CeE68beF3beb65c576180e6D83F5c431D',
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
