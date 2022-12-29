import httpx

from ..types import *
from ..exceptions import *


class CryptoPay(BaseCryptoPay):
    base_url = "https://pay.crypt.bot/api/"

    def __init__(self, token: str):
        super().__init__(token)
        self.session = httpx.Client(
            headers={
                "Host": "pay.crypt.bot",
                "Crypto-Pay-API-Token": token
            }
        )

    def _make_request(self, method, method_type, **kwargs) -> dict:
        request = getattr(self.session, method_type)

        if kwargs:
            response = request(self.base_url + method, json=kwargs)

        else:
            response = request(self.base_url + method)

        response = response.json()

        if response.get("ok"):
            return response.get("result")

        else:
            error = response.get("error")
            raise CryptoPayException(error)

    def get_me(self) -> App:
        response = self._make_request("getMe", "get")
        return App(**response)

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
        amount = str(amount)

        params = self._get_params(locals(), "createInvoice")

        response = self._make_request(
            "createInvoice",
            "post",
            **params
        )

        return Invoice(**response)

    def transfer(
            self,
            user_id: int,
            asset: str,
            amount: float,
            spend_id: str,
            comment: Optional[str] = None,
            disable_send_notification: Optional[bool] = False
    ) -> Transfer:
        amount = str(amount)

        params = self._get_params(locals(), "transfer")

        response = self._make_request(
            "transfer",
            "post",
            **params
        )

        return Transfer(**response)

    def get_invoices(
            self,
            asset: Optional[str] = None,
            invoice_ids: Optional[Union[int, List[int]]] = "",
            status: Optional[str] = None,
            offset: Optional[str] = None,
            count: Optional[str] = None
    ) -> List[Invoice]:

        if invoice_ids:
            if type(invoice_ids) == int:
                invoice_ids = str(invoice_ids)

        params = self._get_params(locals(), "createInvoice")

        response = self._make_request(
            "getInvoices",
            "post",
            **params
        )

        invoices = [Invoice(**invoice) for invoice in response.get("items")]

        return invoices

    def get_balance(self) -> List[Wallet]:
        response = self._make_request("getBalance", "get")
        wallets = [Wallet(**wallet) for wallet in response]

        return wallets

    def get_exchange_rates(self) -> List[ExchangeRate]:
        response = self._make_request("getExchangeRates", "get")
        exchange_rates = [ExchangeRate(**exchange_rate) for exchange_rate in response]

        return exchange_rates

    def get_currencies(self) -> List[Currency]:
        response = self._make_request("getCurrencies", "get")
        currencies = [Currency(**currency) for currency in response]

        return currencies
