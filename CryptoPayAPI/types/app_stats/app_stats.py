from ..base import BaseType


class AppStats(BaseType):
    def __init__(
        self,
        volume: int,
        conversion: int,
        unique_users_count: int,
        created_invoice_count: int,
        paid_invoice_count: int,
        start_at: str,
        end_at: str
    ):
        self.volume = volume
        self.conversion = conversion
        self.unique_users_count = unique_users_count
        self.created_invoice_count = created_invoice_count
        self.paid_invoice_count = paid_invoice_count
        self.start_at = start_at
        self.end_at = end_at
