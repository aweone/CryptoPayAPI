from ..base import BaseType


class ExchangeRate(BaseType):
    def __init__(
        self,
        is_valid: bool,
        is_crypto: bool,
        is_fiat: bool,
        source: str,
        target: str,
        rate: str
    ):
        self.is_valid = is_valid
        self.is_crypto = is_crypto
        self.is_fiat = is_fiat
        self.source = source
        self.target = target
        self.rate = float(rate)
