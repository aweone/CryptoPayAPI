from typing import Optional

from ..base import BaseType
from ..asset import BaseAsset


class Transfer(BaseType):
    def __init__(
        self,
        transfer_id: int,
        user_id: int,
        asset: BaseAsset,
        amount: str,
        status: str,
        completed_at: str,
        comment: Optional[str] = None
    ):
        self.transfer_id = transfer_id
        self.user_id = user_id
        self.asset = asset
        self.amount = amount
        self.status = status
        self.completed_at = completed_at
        self.comment = comment
