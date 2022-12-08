from typing import Generator 

import web3 

from src.swapper.config import private_keys_file
from src.swapper.log import get_logger

logger = get_logger(__name__)

def get_private_key() -> Generator[str, None, None]:
    with open(private_keys_file, 'r') as f:
        while (line := f.readline()):
            private_key = line.rstrip()
            logger.info("Get private key: %s" % private_key[0:4])
            yield private_key 

def addr_to_str(a) -> str:
    if isinstance(a, bytes):
        addr: str = web3.Web3.toChecksumAddress("0x" + bytes(a).hex())
        return addr
    elif isinstance(a, str) and a.startswith("0x"):
        addr = web3.Web3.toChecksumAddress(a)
        return addr