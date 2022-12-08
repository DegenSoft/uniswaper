from dataclasses import dataclass 

@dataclass 
class NetworkConfig:

    uniswap_quoter_address: str 
    uniswap_router_address: str 
    rpc_address: str 
    tokens: list[tuple]


@dataclass 
class UniswapExchangeData:

    input_token_address: str 
    out_token_address: str 
    input_quantity_wei: str 
    deadline: int
    slippage: float  