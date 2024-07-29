from ..base import BaseType


class App(BaseType):
    def __init__(
        self,
        app_id: int,
        name: str,
        payment_processing_bot_username: str
    ):
        self.app_id = app_id
        self.name = name
        self.payment_processing_bot_username = payment_processing_bot_username
