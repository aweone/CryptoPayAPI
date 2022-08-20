from typing import Optional


class BaseType:
    def __str__(self):
        return str(self.__dict__)


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


class Invoice(BaseType):
    def __init__(
            self,
            invoice_id: int,
            status: str,
            hash: str,
            asset: str,
            amount: str,
            pay_url: str,
            created_at: str,
            allow_comments: bool,
            allow_anonymous: bool,
            description: Optional[str] = None,
            expiration_date: Optional[str] = None,
            paid_at: Optional[str] = None,
            paid_anonymously: Optional[str] = None,
            comment: Optional[str] = None,
            hidden_message: Optional[str] = None,
            payload: Optional[str] = None,
            paid_btn_name: Optional[str] = None,
            paid_btn_url: Optional[str] = None
    ):
        self.invoice_id = invoice_id
        self.status = status
        self.hash = hash
        self.asset = asset
        self.amount = amount
        self.pay_url = pay_url
        self.description = description
        self.created_at = created_at
        self.allow_comments = allow_comments
        self.allow_anonymous = allow_anonymous
        self.expiration_date = expiration_date
        self.paid_at = paid_at
        self.paid_anonymously = paid_anonymously
        self.comment = comment
        self.hidden_message = hidden_message
        self.payload = payload
        self.paid_btn_name = paid_btn_name
        self.paid_btn_url = paid_btn_url


class Transfer(BaseType):
    def __init__(
            self,
            transfer_id: int,
            user_id: int,
            asset: str,
            amount: str,
            status: str,
            completed_at: str,
            comment: str
    ):
        self.transfer_id = transfer_id
        self.user_id = user_id
        self.asset = asset
        self.amount = amount
        self.status = status
        self.completed_at = completed_at
        self.comment = comment


class ExchangeRate(BaseType):
    def __init__(
            self,
            is_valid: bool,
            source: str,
            target: str,
            rate: str
    ):
        self.is_valid = is_valid
        self.source = source
        self.target = target
        self.rate = float(rate)


class Wallet(BaseType):
    def __init__(
            self,
            currency_code: str,
            available: str
    ):
        self.currency_code = currency_code
        self.available = float(available)


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
        self.decimals = decimals
        self.url = url


class Asset:
    BTC = "BTC"
    TON = "ETH"
    USDT = "USDT"
    USDC = "USDC"
    BUSD = "BUSD"

