"""---------------------------------------–––––––––MODULES SETTINGS-–––----------------------------------------------"""

"""
-------------------------------------------------------CEX CONTROL------------------------------------------------------
    Выберите сети/суммы для вывода и ввода с CEX. Не забудьте вставить API ключи в general_settings.py.
    Депозиты и выводы работают только со спотовым балансом на бирже.

    1 - ETH-ERC20                          
    2 - ETH-Arbitrum One                           
    3 - ETH-Optimism                       
    4 - ETH-zkSync Era                           
    5 - ETH-Linea              
    6 - ETH-Base               

    ⚠️ Софт сам отнимает комиссию от суммы депозита, при работе с нативными токенами ⚠️

    Сумма в количестве  - (0.01, 0.02)
    Сумма в процентах   - ("10", "20") ⚠️ Значения в кавычках.

    OKX_WITHDRAW_DATA | Каждый список - один модуль для вывода из биржи. Примеры работы указаны ниже:
                        Для каждого вывода указывайте [сеть вывода, (мин и макс сумма)]

    Примеры рандомизации вывода с биржи:

    [[17, (1, 1.011)], None] | Пример установки None, для случайного выбора (выполнение действия или его пропуск)
    [[2, (0.48, 0.5)], [3, (0.48, 0.5)]] | Пример установки двух сетей, софт выберет одну случайную.
    
    Настройка лимитера. Указывать в ETH
    лимитерX - это минимальный баланс на аккаунте, чтобы софт начал процесс бриджа
    лимитерY - это мин. и макс. сумма, которая должна остаться на балансе для комиссии.
"""

BINANCE_WITHDRAW_DATA = [
    [[2, (0.006, 0.007)], [3, (0.006, 0.007)], [6, (0.006, 0.007)]]
]

RELAY_CHAIN_FROM_NAMES = ['Arbitrum', 'Optimism', 'Base']  # исходящие сети для бриджа
RELAY_CHAIN_TO_NAMES = ['Ethereum']    # входящие сетя для бриджа
RELAY_BRIDGE_AMOUNT = ['100', '100']   # сумма для бриджа, в кавычках - %, без них - четкая сумма. Пример в CEX CONTROL
RELAY_TOKEN_NAME = 'ETH'               # токен для бриджа
RELAY_AMOUNT_LIMITER = 0, (0.00005, 0.00007)  # лимитер для бриджа. Описание в CEX CONTROL

TRANSFER_ETH_AMOUNT = ['100', '100']  # сумма трансфера ETH на кошелек "Transfer address"

TOTAL_DECIMALS = 18  # количество знаков после запятой для всех транзакций



#####################################################  HYPURRFI #######################################################
# https://app.hypurr.fi/dashboard
# Deposit settings
HYPURR_DEPOSIT_AMOUNT_USDC = ('70', '100')
HYPURR_DEPOSIT_AMOUNT_sUSDe = ('70', '100')
HYPURR_DEPOSIT_AMOUNT_SolvBTC = ('70', '100')
# Borrow settings
HYPURR_BORROW_HEALTH_FACTOR_MIN = 5 # minimum health factor, if less, the borrow will be skipped
HYPURR_BORROW_AMOUNT_FROM_AVAILABLE = ('5', '20')

#ROUTES MODULES:
    # ['claim_tokens_on_hypurr:HyperTestnet'],   
    
    # ['borrow_whype_from_hupurr:HyperTestnet'],
    # ['borrow_usdxl_from_hupurr:HyperTestnet'],
    # ['borrow_usdc_from_hupurr:HyperTestnet'],
    # ['borrow_susde_from_hupurr:HyperTestnet'],
    # ['borrow_solvbtc_from_hupurr:HyperTestnet'],
    
    # ['deposit_usdc_to_hypurr:HyperTestnet'],
    # ['deposit_susde_to_hypurr:HyperTestnet'],
    # ['deposit_solvbtc_to_hypurr:HyperTestnet'],
#######################################################################################################################

####################################################  HYPERLEND #######################################################
# https://testnet.hyperlend.finance/dashboard

#ROUTES MODULES:
    # ['claim_hype_on_hyperlend_once:HyperTestnet'],
    # ['claim_MBTC_on_hyperlend_once:HyperTestnet'],

############################################  Hyperliquid Exchange testnet ############################################
USDC_AMOUNT_TO_TRANSFER_FROM_HL_TO_EVM = ('5', '20') # amount of USDC to transfer from HL exchange to HL EVM
USDC_AMOUNT_TO_OPEN_RANDOM_PERP_POSITION = ('3', '12') # amount of USDC to open random perp position

#ROUTES MODULES:
    # ['claim_usdc_from_hl_exchange_testnet_once:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['close_random_perp_position_on_hl:HyperTestnet'],
    # ['close_all_perp_positions_on_hl:HyperTestnet'],

    

#######################################################################################################################

CLASSIC_ROUTES_MODULES_USING = [
    ######################### HYPERLIQUID EXCHANGE TESTNET ###########################
    # ['claim_usdc_from_hl_exchange_testnet_once:HyperTestnet'],
    
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['open_random_perp_position_on_hl:HyperTestnet'],
    # ['close_all_perp_positions_on_hl:HyperTestnet'],
    # ['close_random_perp_position_on_hl:HyperTestnet'],
    # ['close_random_perp_position_on_hl:HyperTestnet'],
    # ['close_random_perp_position_on_hl:HyperTestnet'],
    
    
    ######################### EVM ###########################
    # ['claim_hype_on_hyperlend_once:HyperTestnet'],
    # ['claim_MBTC_on_hyperlend_once:HyperTestnet'],
    
    # ['claim_tokens_on_hypurr:HyperTestnet'],
    
    # ['deposit_usdc_to_hypurr:HyperTestnet', 'deposit_susde_to_hypurr:HyperTestnet', 'deposit_solvbtc_to_hypurr:HyperTestnet', None,],
    # ['deposit_usdc_to_hypurr:HyperTestnet', 'deposit_susde_to_hypurr:HyperTestnet', 'deposit_solvbtc_to_hypurr:HyperTestnet', None,],
    # ['deposit_usdc_to_hypurr:HyperTestnet', 'deposit_susde_to_hypurr:HyperTestnet', 'deposit_solvbtc_to_hypurr:HyperTestnet', None,],
    
    # ['borrow_whype_from_hupurr:HyperTestnet', 'borrow_usdxl_from_hupurr:HyperTestnet', 'borrow_usdc_from_hupurr:HyperTestnet', 'borrow_susde_from_hupurr:HyperTestnet', 'borrow_solvbtc_from_hupurr:HyperTestnet', None,None,],
    # ['borrow_whype_from_hupurr:HyperTestnet', 'borrow_usdxl_from_hupurr:HyperTestnet', 'borrow_usdc_from_hupurr:HyperTestnet', 'borrow_susde_from_hupurr:HyperTestnet', 'borrow_solvbtc_from_hupurr:HyperTestnet', None,None,],
    # ['borrow_whype_from_hupurr:HyperTestnet', 'borrow_usdxl_from_hupurr:HyperTestnet', 'borrow_usdc_from_hupurr:HyperTestnet', 'borrow_susde_from_hupurr:HyperTestnet', 'borrow_solvbtc_from_hupurr:HyperTestnet', None,None,],
    
    
    # ['claim_tokens_on_hypurr:HyperTestnet'],   
    
    # ['borrow_whype_from_hupurr:HyperTestnet'],
    # ['borrow_usdxl_from_hupurr:HyperTestnet'],
    # ['borrow_usdc_from_hupurr:HyperTestnet'],
    # ['borrow_susde_from_hupurr:HyperTestnet'],
    # ['borrow_solvbtc_from_hupurr:HyperTestnet'],
    
    # ['deposit_usdc_to_hypurr:HyperTestnet'],
    # ['deposit_susde_to_hypurr:HyperTestnet'],
    # ['deposit_solvbtc_to_hypurr:HyperTestnet'],
]
