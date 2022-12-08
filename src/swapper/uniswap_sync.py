from eth_typing.evm import ChecksumAddress
from eth_account.signers.local import LocalAccount

from uniswap import Uniswap


def make_trade(
    address_from: ChecksumAddress, 
    address_to: ChecksumAddress,
    account: LocalAccount, 
    amount: int,
    provider: str
) -> None:
    uniswap = Uniswap(address=account.address, private_key=account.privateKey, version=3, provider=provider)
    uniswap.make_trade(address_from, address_to, amount)
