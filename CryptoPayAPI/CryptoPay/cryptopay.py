import httpx

from typing import Optional, List, Union


from ..exceptions import CryptoPayException

from ..types.app import App
from ..types.app_stats import AppStats
from ..types.asset import BaseAsset
from ..types.balance import Balance
from ..types.check import Check
from ..types.cryptopay import BaseCryptoPay
from ..types.currency import Currency
from ..types.currency_type import BaseCurrencyType, CryptoCurrencyType
from ..types.exchange_rate import ExchangeRate
from ..types.fiat import BaseFiat
from ..types.invoice import Invoice
from ..types.transfer import Transfer


class CryptoPay(BaseCryptoPay):
    def __init__(self, token: str, is_test_net: bool = False, **kwargs):
        super().__init__(token, is_test_net)
        self.session = httpx.Client(
            headers={
                "Host": "pay.crypt.bot",
                "Crypto-Pay-API-Token": token
            },
            **kwargs
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
        amount: float,
        currency_type: Optional[BaseCurrencyType] = CryptoCurrencyType,
        asset: Optional[BaseAsset] = None,
        fiat: Optional[BaseFiat] = None,
        accepted_assets: List[BaseAsset] = None,
        description: Optional[str] = None,
        hidden_message: Optional[str] = None,
        paid_btn_name: Optional[str] = None,
        paid_btn_url: Optional[str] = None,
        payload: Optional[str] = None,
        allow_comments: Optional[bool] = True,
        allow_anonymous: Optional[bool] = True,
        expires_in: Optional[int] = None,
    ) -> Invoice:
        params = self._get_params(locals(), "createInvoice")

        response = self._make_request(
            "createInvoice",
            "post",
            **params
        )

        return Invoice(**response)

    def delete_invoice(
        self,
        invoice_id: int,
    ) -> bool:
        params = self._get_params(locals(), "deleteInvoice")

        response = self._make_request(
            "deleteInvoice",
            "post",
            **params
        )

        return bool(response)

    def create_check(
        self,
        asset: int,
        amount: float,
        pin_to_user_id: Optional[int] = None,
        pin_to_username: Optional[str] = None
    ) -> Check:
        params = self._get_params(locals(), "createCheck")

        response = self._make_request(
            "createCheck",
            "post",
            **params
        )
        (response)

        return Check(**response)

    def delete_check(
        self,
        check_id: int
    ):
        params = self._get_params(locals(), "deleteCheck")

        response = self._make_request(
            "deleteCheck",
            "post",
            **params
        )

        return bool(response)

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
            invoice_ids = list(map(str, invoice_ids))

        params = self._get_params(locals(), "createInvoice")

        response = self._make_request(
            "getInvoices",
            "post",
            **params
        )

        invoices = [Invoice(**invoice) for invoice in response.get("items")]

        return invoices

    def get_checks(
        self,
        asset: Optional[str] = None,
        check_ids: Optional[List[int]] = None,
        status: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None
    ) -> List[Check]:
        if check_ids:
            check_ids = list(map(str, check_ids))

        params = self._get_params(locals(), "getChecks")

        response = self._make_request(
            "getChecks",
            "post",
            **params
        )

        checks = [Check(**invoice) for invoice in response.get("items")]

        return checks

    def get_transfers(
        self,
        asset: Optional[str] = None,
        transfers_id: Optional[List[int]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None
    ) -> List[Transfer]:
        if transfers_id:
            transfers_id = list(map(str, transfers_id))

        params = self._get_params(locals(), "getTransfers")

        response = self._make_request(
            "getTransfers",
            "get",
            **params
        )

        transfers = [Transfer(**invoice) for invoice in response.get("items")]

        return transfers

    def get_balance(self) -> List[Balance]:
        response = self._make_request("getBalance", "get")
        balances = [Balance(**balance) for balance in response]

        return balances

    def get_exchange_rates(self) -> List[ExchangeRate]:
        response = self._make_request("getExchangeRates", "get")
        exchange_rates = [ExchangeRate(**exchange_rate) for exchange_rate in response]

        return exchange_rates

    def get_currencies(self) -> List[Currency]:
        response = self._make_request("getCurrencies", "get")
        currencies = [Currency(**currency) for currency in response]

        return currencies

    def get_stats(
        self,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None
    ) -> AppStats:
        params = self._get_params(locals(), "getStats")

        response = self._make_request("getStats", "get", **params)

        return AppStats(**response)
