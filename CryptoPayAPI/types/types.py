from typing import Optional, Union, List


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
        self.code = code
        self.decimals = decimals
        self.url = url


class Asset:
    BTC = "BTC"
    TON = "ETH"
    USDT = "USDT"
    USDC = "USDC"
    BUSD = "BUSD"


class BaseCryptoPay:
    base_url = "https://pay.crypt.bot/api/"

    def __init__(self, token: str):
        self.token = token

    def _make_request(self, method, method_type, **kwargs) -> dict:
        pass

    @staticmethod
    def _get_params(func_locals: dict, method) -> dict:
        params = {}

        methods_params = {
            "createInvoice": [
                "asset",
                "amount",
                "description",
                "hidden_message",
                "paid_btn_name",
                "paid_btn_url",
                "payload",
                "allow_comments",
                "allow_anonymous",
                "expires_in",
            ],
            "getInvoices": [
                "asset",
                "invoice_ids",
                "status",
                "offset",
                "count"
            ],
            "transfer": [
                "user_id",
                "asset",
                "amount",
                "spend_id",
                "comment",
                "disable_send_notification"
            ]
        }

        method_params = methods_params.get(method)

        for key, value in func_locals.items():
            if key in method_params and value is not None:
                params[key] = value

        return params

    def get_me(self) -> App:
        pass

    def create_invoice(
            self,
            asset: str,
            amount: float,
            description: Optional[str] = None,
            hidden_message: Optional[str] = None,
            paid_btn_name: Optional[str] = None,
            paid_btn_url: Optional[str] = None,
            payload: Optional[str] = None,
            allow_comments: Optional[bool] = True,
            allow_anonymous: Optional[bool] = True,
            expires_in: Optional[int] = None
    ) -> Invoice:
        pass

    def transfer(
            self,
            user_id: int,
            asset: str,
            amount: float,
            spend_id: str,
            comment: Optional[str] = None,
            disable_send_notification: Optional[bool] = False
    ) -> Transfer:
        pass

    def get_invoices(
            self,
            asset: Optional[str] = None,
            invoice_ids: Optional[Union[int, List[int]]] = "",
            status: Optional[str] = None,
            offset: Optional[str] = None,
            count: Optional[str] = None
    ) -> List[Invoice]:
        pass

    def get_balance(self) -> List[Wallet]:
        pass

    def get_exchange_rates(self) -> List[ExchangeRate]:
        pass

    def get_currencies(self) -> List[Currency]:
        pass
