from ..base import BaseType
from ..asset import BaseAsset


class Check(BaseType):
    def __init__(
        self,
        check_id: int,
        hash: str,
        asset: BaseAsset,
        amount: str,
        bot_check_url: str,
        status: str,
        created_at: str,
        activated_at: str = None,
    ):
        self.check_id = check_id
        self.hash = hash
        self.asset = asset
        self.amount = amount
        self.bot_check_url = bot_check_url
        self.status = status
        self.created_at = created_at
        self.activated_at = activated_at
