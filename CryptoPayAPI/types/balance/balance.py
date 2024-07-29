from ..base import BaseType
from ..asset import BaseAsset


class Balance(BaseType):
    def __init__(
        self,
        currency_code: BaseAsset,
        available: str,
        onhold: str
    ):
        self.currency_code = currency_code
        self.available = available
        self.onhold = onhold
