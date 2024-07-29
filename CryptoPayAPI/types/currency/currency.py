from typing import Optional

from ..base import BaseType


class Currency(BaseType):
    def __init__(
            self,
            is_blockchain: bool,
            is_stablecoin: bool,
            is_fiat: bool,
            name: str,
            code: str,
            decimals: int,
            url: Optional[str] = None
    ):
        self.is_blockchain = is_blockchain
        self.is_stablecoin = is_stablecoin
        self.is_fiat = is_fiat
        self.name = name
        self.code = code
        self.decimals = decimals
        self.url = url
