import os 
import asyncio 
import logging 
import time 
from concurrent.futures import ThreadPoolExecutor
import random 

import web3 
from web3 import Web3 
from web3.eth import AsyncEth, Eth
from eth_account import Account
from eth_account.signers.local import LocalAccount

from src.swapper.log import get_logger
from src.swapper.utils import get_private_key
from src.swapper import config as conf 
from src.swapper.uniswap_sync import make_trade
from src.swapper.utils import addr_to_str


logger: logging.Logger = get_logger(__name__)
provider = Web3.HTTPProvider(conf.NETWORKS[conf.ACTIVE_NETWORK].rpc_address)
w3 = Web3(
    provider,
    middlewares=provider.middlewares
)
eth_default_address = "0x0000000000000000000000000000000000000000"

def main(private_key: str):

    is_connected = w3.is_connected()
    logger.info("Connected: %s. Chain id: %d", is_connected, w3.eth.chain_id)

    account: LocalAccount = Account.from_key(private_key)
    account_balance = w3.eth.get_balance(account.address)
    logger.debug("Account: %s", account.address)
    logger.info("Balance of %s is: %s eth", account.address, account_balance / (10**18))

    
    tokens = conf.NETWORKS[conf.ACTIVE_NETWORK].tokens
    random.shuffle(tokens)
    tokens = tokens[0:conf.TOKEN_PAIR_NUMBER]

    for pair in tokens:
        try:
            amount = random.uniform(*pair[2])
            amount = web3.Web3.to_wei(amount, 'ether')
            logger.info("[%s] Exchange pair: %s with amount: %s", account.address, pair, amount)

            if amount > account_balance:
                raise ValueError(f"[%s] Balance less than amount!".format(account.address))
            logger.debug("[%s] Sleeping..", account.address)
            make_trade(
                addr_to_str(pair[0]),
                addr_to_str(pair[1]),
                account,
                amount, 
                conf.NETWORKS[conf.ACTIVE_NETWORK].rpc_address
            )
            time.sleep(random.randint(*conf.TIME_SLEEP_INTERVAL))
        except Exception as e:
            logger.warn("[%s] Failed to make trade: %s", account.address, e)

    logger.info("[%s] Successfully exchanged", account.address)

def run(private_key):
    try:
        main(private_key)
    except Exception as e:
        logger.error(e)
    
if __name__ == "__main__":
    results = []
    with ThreadPoolExecutor(max_workers=conf.MAX_WORKERS) as executor:
        for private_key in get_private_key():
            result = executor.submit(run, private_key)
            results.append(result)
            time.sleep(random.randint(*conf.TIME_SLEEP_INTERVAL))

    for res in results:
        while not res.done():
            pass 
