import aiohttp

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


class AioCryptoPay(BaseCryptoPay):
    def __init__(self, token: str, is_test_net: bool = False, **kwargs):
        super().__init__(token, is_test_net)
        self.session = aiohttp.ClientSession(
            headers={
                "Host": "pay.crypt.bot",
                "Crypto-Pay-API-Token": token
            },
            **kwargs
        )

    async def close(self):
        await self.session.close()

    async def _make_request(self, method, method_type, **kwargs) -> dict:
        request = getattr(self.session, method_type)

        response = await request(self.base_url + method, json=kwargs)
        response = await response.json()

        if response.get("ok"):
            return response.get("result")

        else:
            error = response.get("error")
            raise CryptoPayException(error)

    async def get_me(self) -> App:
        response = await self._make_request("getMe", "get")
        return App(**response)

    async def create_invoice(
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

        response = await self._make_request(
            "createInvoice",
            "post",
            **params
        )

        return Invoice(**response)

    async def delete_invoice(
        self,
        invoice_id: int,
    ) -> bool:
        params = self._get_params(locals(), "deleteInvoice")

        response = await self._make_request(
            "deleteInvoice",
            "post",
            **params
        )

        return bool(response)

    async def create_check(
        self,
        asset: int,
        amount: float,
        pin_to_user_id: Optional[int] = None,
        pin_to_username: Optional[str] = None
    ) -> Check:
        params = self._get_params(locals(), "createCheck")

        response = await self._make_request(
            "createCheck",
            "post",
            **params
        )

        return Check(**response)

    async def delete_check(
        self,
        check_id: int
    ):
        params = self._get_params(locals(), "deleteCheck")

        response = await self._make_request(
            "deleteCheck",
            "post",
            **params
        )

        return bool(response)

    async def transfer(
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

        response = await self._make_request(
            "transfer",
            "post",
            **params
        )

        return Transfer(**response)

    async def get_invoices(
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

        response = await self._make_request(
            "getInvoices",
            "post",
            **params
        )

        invoices = [Invoice(**invoice) for invoice in response.get("items")]

        return invoices

    async def get_checks(
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

        response = await self._make_request(
            "getChecks",
            "post",
            **params
        )

        checks = [Check(**invoice) for invoice in response.get("items")]

        return checks

    async def get_transfers(
        self,
        asset: Optional[str] = None,
        transfers_id: Optional[List[int]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None
    ) -> List[Transfer]:
        if transfers_id:
            transfers_id = list(map(str, transfers_id))

        params = self._get_params(locals(), "getTransfers")

        response = await self._make_request(
            "getTransfers",
            "get",
            **params
        )

        transfers = [Transfer(**invoice) for invoice in response.get("items")]

        return transfers

    async def get_balance(self) -> List[Balance]:
        response = await self._make_request("getBalance", "get")
        balances = [Balance(**balance) for balance in response]

        return balances

    async def get_exchange_rates(self) -> List[ExchangeRate]:
        response = await self._make_request("getExchangeRates", "get")
        exchange_rates = [ExchangeRate(**exchange_rate) for exchange_rate in response]

        return exchange_rates

    async def get_currencies(self) -> List[Currency]:
        response = await self._make_request("getCurrencies", "get")
        currencies = [Currency(**currency) for currency in response]

        return currencies

    async def get_stats(
        self,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None
    ) -> AppStats:
        params = self._get_params(locals(), "getStats")

        response = await self._make_request("getStats", "get", **params)

        return AppStats(**response)
