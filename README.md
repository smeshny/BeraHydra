# BeraHydra
Asynchronous interaction software for Berachain mainnet.

### 🔗 Social Links
- [Mimble Wimble LAB Telegram Channel](https://t.me/MimbleWimbleLAB)
- [Mimble Wimble LAB Telegram Chat](https://t.me/MimbleWimbleLAB_chat)

## ⚠️ DISCLAIMER

**This project is based on [AstrumClaimer](https://github.com/realaskaer/AstrumClaimer) opensource project.**

This software is provided "as is", without warranty of any kind. By using this software, you acknowledge and agree that:
- This is an experimental tool and you use it at your own risk
- The authors are not responsible for any potential losses, damages, or unexpected behavior
- You understand the risks associated with automated blockchain interactions
- This software is for educational purposes only

## 🧩 Modules

### 🐂 Bullas Game
- Claim Free Gamepass for Main Bullas NFT
- Make First Click Only Once for Start Mining Moola
- Automatic Purchases Upgrades for Moola

### TODO:
- Kodiak DEX swaps
- OogaBooga DEX swaps
- [Add your feature requests here]

## ♾️ Core Features

### 🚀 Run All Accounts Through Classic Routes
Execute prepared classic routes for all accounts. Requires pre-generated routes using Feature #2 (Route Generation).

### 📄 Generate Classic Routes per Account
Classic route generator using traditional methodology. Configure routes in CLASSIC_ROUTES_MODULES_USING settings. Supports 'None' in module lists to skip specific route segments.

### ✅ Proxy Validation
Rapid proxy verification system (extremely fast performance).

## 📄 Data Input
Configure all required data in the accounts_data table within the `/data` directory:

- **Name**: Unique identifiers for each account
- **Private Key**: Wallet private keys
- **Proxy**: Account proxies (supports fewer proxies than accounts with cycling, single mobile proxy supported)

🔒 Enable EXCEL_PASSWORD = True to password-protect your data table. When active, software requires password entry for operation - recommended for server use.

## 🛠️ Installation & Setup

⚠️ By installing this project, you acknowledge the risks associated with automated financial software (potential losses of assets, data, or resources).

**Requirements**: Python 3.10.11

1. Clone repository:
    ```
    git clone https://github.com/smeshny/BeraHydra.git
    ```

2. Create and activate virtual environment:
    ```
    python3.10 -m venv my_venv
    
    # For Windows
    .\my_venv\Scripts\activate
    
    # For Linux/Mac
    source my_venv/bin/activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run software:
    ```
    cd path/to/BeraHydra
    python main.py
    ```

