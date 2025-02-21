"""------------------------------------––––––ORIGINAL ASTRUM CLAIMER CONTROLS-–––-----------------------------------"""

"""
-------------------------------------------------------CEX CONTROL-----------------------------------------------------
    Select networks/amounts for withdrawals and deposits from CEX. Don't forget to insert API keys in general_settings.py.
    Deposits and withdrawals only work with spot balance on the exchange.

    1 - ETH-ERC20                          
    2 - ETH-Arbitrum One                           
    3 - ETH-Optimism                       
    4 - ETH-zkSync Era                           
    5 - ETH-Linea              
    6 - ETH-Base               

    ⚠️ The software automatically deducts the commission from the deposit amount when working with native tokens ⚠️

    Amount in quantity  - (0.01, 0.02)
    Amount in percent   - ("10", "20") ⚠️ Values in quotes.

    OKX_WITHDRAW_DATA | Each list is one module for withdrawal from the exchange. Usage examples are shown below:
                        For each withdrawal, specify [withdrawal network, (min and max amount)]

    Examples of randomizing exchange withdrawals:

    [[17, (1, 1.011)], None] | Example of setting None for random choice (executing action or skipping it)
    [[2, (0.48, 0.5)], [3, (0.48, 0.5)]] | Example of setting two networks, software will choose one randomly.
    
    Limiter configuration. Specify in ETH
    limiterX - minimum balance in the account for the software to start the bridge process
    limiterY - min. and max. amount that should remain in balance for commission.
"""

BINANCE_WITHDRAW_DATA = [
    [[2, (0.006, 0.007)], [3, (0.006, 0.007)], [6, (0.006, 0.007)]]
]

RELAY_CHAIN_FROM_NAMES = ['Arbitrum', 'Optimism', 'Base']  # source networks for bridging
RELAY_CHAIN_TO_NAMES = ['Ethereum']    # destination networks for bridging
RELAY_BRIDGE_AMOUNT = ['100', '100']   # bridge amount, in quotes - %, without quotes - exact amount. Example in CEX CONTROL
RELAY_TOKEN_NAME = 'ETH'               # token for bridging
RELAY_AMOUNT_LIMITER = 0, (0.00005, 0.00007)  # bridge limiter. Description in CEX CONTROL

TRANSFER_ETH_AMOUNT = ['100', '100']  # ETH transfer amount to "Transfer address" wallet

TOTAL_DECIMALS = 18  # number of decimal places for all transactions

"""---------------------------------------–––––––––MODULES SETTINGS-–––---------------------------------------------"""

#####################################################  BULLAS #######################################################
# https://game.bullas.xyz/

#ROUTES MODULES:
    # ['bullas_purchase_tools_for_moola'],
    # ['bullas_upgrade_tools_for_moola'],
    
    # ['bullas_claim_free_gamepass_for_main_bullas_nft'],
    # ['bullas_make_first_click_only_once_for_start_mining_moola'],  
    
#######################################################################################################################


CLASSIC_ROUTES_MODULES_USING = [
    # ['bullas_claim_free_gamepass_for_main_bullas_nft'],
    # ['bullas_make_first_click_only_once_for_start_mining_moola'],
    ['bullas_purchase_tools_for_moola'],
    ['bullas_upgrade_tools_for_moola', None, None, None,],
]
