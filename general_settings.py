"""
------------------------------------------------GENERAL SETTINGS--------------------------------------------------------
    WALLETS_TO_WORK = 0 | The software will select wallets from the table according to the rules described below
    0       = all wallets in sequence
    3       = only wallet #3
    4, 20   = wallet #4 and #20
    [[5, 25]] = wallets from #5 to #25
    [[5, 25], [30, 35]] = wallets from #5 to #25 and from #30 to #35

    WALLETS_TO_EXCLUDE = 0 | The software will exclude wallets from the table according to the rules described below
    0       = no wallets will be excluded
    3       = only wallet #3
    4, 20   = wallet #4 and #20
    [5, 25] = wallets from #5 to #25
    [[5, 25], [30, 35]] = wallets from #5 to #25 and from #30 to #35

    ACCOUNTS_IN_STREAM      | Number of wallets in the execution stream. If there are 100 wallets total and you set 10,
                             the software will make 10 runs with 10 wallets each

    EXCEL_PASSWORD          | Enables password request when entering the software. First set the password in the table
    EXCEL_PAGE_NAME         | Sheet name in the table. Example: 'BeraChain'

"""

SOFTWARE_MODE = 0              # 0 - sequential execution / 1 - parallel execution
ACCOUNTS_IN_STREAM = 1         # Number of accounts per stream when SOFTWARE_MODE = 1
WALLETS_TO_WORK = 0            # 0 / 3 / 3, 20 / [[3, 20]]
WALLETS_TO_EXCLUDE = 0         # 0 / 3 / 3, 20 / [[3, 20]]
SHUFFLE_WALLETS = True         # Shuffles wallets before execution

BREAK_ROUTE = False            # Stops route execution if an error occurs
SAVE_PROGRESS = True           # Enables account progress saving for Classic-routes
TELEGRAM_NOTIFICATIONS = True  # Enables Telegram notifications

'------------------------------------------------SLEEP CONTROL---------------------------------------------------------'

SLEEP_MODE = True              # Enables sleep after each module and account
SLEEP_TIME_MODULES = (10, 25)  # (minimum, maximum) seconds | Sleep time between modules
SLEEP_TIME_ACCOUNTS = (150, 210) # (minimum, maximum) seconds | Sleep time between accounts

INFINITY_MODE = True           # Restarts accounts in a new cycle. Allows to loop the entire work process
SLEEP_TIME_FOR_NEW_RUN = (60 * 60 * 3, 60 * 60 * 7)  # (minimum, maximum) seconds | Sleep time between repeated runs

'------------------------------------------------RETRY CONTROL---------------------------------------------------------'
MAXIMUM_RETRY = 5              # Number of retries on errors
SLEEP_TIME_RETRY = (5, 15)     # (minimum, maximum) seconds | Sleep time after each retry

'-----------------------------------------------------GAS CONTROL------------------------------------------------------'

GAS_CONTROL = False            # Enables gas control
MAXIMUM_GWEI = 10              # Maximum GWEI for software operation, can be changed during runtime in maximum_gwei.json
SLEEP_TIME_GAS = 100           # Time between gas checks
CONTROL_TIMES_FOR_SLEEP = 5    # Number of checks
GAS_LIMIT_MULTIPLIER = 1.3     # Gas limit multiplier for transactions. Helps save on transaction costs
GAS_PRICE_MULTIPLIER = 1.5     # Gas price multiplier for transactions. Speeds up execution or reduces transaction cost
UNLIMITED_APPROVE = True       # Enables unlimited token approvals

'------------------------------------------------PROXY CONTROL---------------------------------------------------------'
PROXY_REPLACEMENT_COUNT = 20    # Number of possible proxy replacements during operation, after which the account stops
USE_PROXY = True               # Enables proxy usage

'------------------------------------------------SECURE DATA-----------------------------------------------------------'

CAPTCHA_SOLVER = '2captcha'     # Service used for solving captchas (2captcha or capmonster)
# https://2captcha.com/enterpage
TWO_CAPTCHA_API_KEY = ""

# BINANCE API KEYS https://www.binance.com/ru/my/settings/api-management
BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""

# EXCEL INFO
EXCEL_PASSWORD = False
EXCEL_PAGE_NAME = "EVM"
EXCEL_FILE_PATH = "./data/accounts_data.xlsx"  # You can keep the default table location if it suits you

# TELEGRAM DATA
TG_TOKEN = ""  # https://t.me/BotFather
TG_ID = ""  # https://t.me/getmyid_bot
