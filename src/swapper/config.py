import os 

from src.swapper.models import NetworkConfig

base_dir = os.getcwd()
private_keys_file = os.path.join(base_dir, 'private_keys.txt')

# Потоков 
MAX_WORKERS = 1
# Интервал ожидания перед совершением обмена и переходом к след. кошельку 
TIME_SLEEP_INTERVAL = [10, 30]

# Диапазон газа за транзакцию (мин макс)
GAS_AMOUNT_RANGE = []

# Типы сетей  
MAINNET = "mainnet"
DEVNET = "devnet"

ACTIVE_NETWORK = os.getenv("network", MAINNET)

# mainnet arbitrum addresses 
arbitrum_rpc_mainnet = "https://arb1.arbitrum.io/rpc"
uniswap_router_address_mainnet = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
uniswap_quoter_address_mainnet = "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6"
 
"""
Пары токенов для которых будет совершаться обмен.
TOKENS = [
    (адрес0, адрес1, диапазон),
    ...
]
адрес0 - токен, который меняем
адрес1 - токен, на который меняем
диапазон - [0.000001, 0.000005] суммы в ether 

Для справки: адрес ETH = 0x0000000000000000000000000000000000000000 
"""
tokens = [
#GMX
    ("0x0000000000000000000000000000000000000000", "0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a", [0.00003, 0.0001]),
#USDC
    ("0x0000000000000000000000000000000000000000", "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8", [0.00003, 0.0001]),
    #STG
   ("0x0000000000000000000000000000000000000000", "0x6694340fc020c5e6b96567843da2df01b2ce1eb6", [0.00003, 0.0001]),
    #USDT
    ("0x0000000000000000000000000000000000000000", "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9", [0.00003, 0.0001]),
    #MAGIC
    ("0x0000000000000000000000000000000000000000", "0x539bdE0d7Dbd336b79148AA742883198BBF60342", [0.00003, 0.0001]),
  #DODO
    ("0x0000000000000000000000000000000000000000", "0x69Eb4FA4a2fbd498C257C57Ea8b7655a2559A581", [0.00003, 0.0001]),
      #UNI
    ("0x0000000000000000000000000000000000000000", "0xFa7F8980b0f1E64A2062791cc3b0871572f1F7f0", [0.00003, 0.0001]),
      #COMP
    ("0x0000000000000000000000000000000000000000", "0x354A6dA3fcde098F8389cad84b0182725c6C91dE", [0.00003, 0.0001]),
      #BAL
    ("0x0000000000000000000000000000000000000000", "0x040d1EdC9569d4Bab2D15287Dc5A4F10F56a56B8", [0.00003, 0.0001]),
]
# Сколько пар токенов выбирать
TOKEN_PAIR_NUMBER = 1


# devnet arbitrum addresses 
# 
# 
# --------- skip -----------

NETWORKS: dict[str, NetworkConfig] = {
    MAINNET: NetworkConfig(
        uniswap_router_address=uniswap_router_address_mainnet, 
        uniswap_quoter_address=uniswap_quoter_address_mainnet,
        rpc_address=arbitrum_rpc_mainnet,
        tokens=tokens,
    ), 
}
