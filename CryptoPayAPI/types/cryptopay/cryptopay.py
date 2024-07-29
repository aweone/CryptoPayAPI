from typing import Optional, Union, List

from ..invoice import Invoice
from ..currency_type import BaseCurrencyType
from ..asset import BaseAsset
from ..fiat import BaseFiat
from ..app import App
from ..transfer import Transfer
from ..balance import Balance
from ..exchange_rate import ExchangeRate
from ..currency import Currency
from ..check import Check
from ..app_stats import AppStats


class BaseCryptoPay:
    def __init__(self, token: str, is_test_net: bool = False):
        self.token = token

        if is_test_net:
            self.base_url = "https://testnet-pay.crypt.bot/api/"
        else:
            self.base_url = "https://pay.crypt.bot/api/"

    def _make_request(self, method, method_type, **kwargs) -> dict:
        pass

    @staticmethod
    def _get_params(func_locals: dict, method: str) -> dict:
        params = {}

        if func_locals.get("currency_type"):
            func_locals["currency_type"] = func_locals["currency_type"].name

        if func_locals.get("asset"):
            func_locals["asset"] = func_locals["asset"].name

        if func_locals.get("amount"):
            func_locals["amount"] = int(func_locals["amount"])

        methods_params = {
            "createInvoice": [
                "currency_type",
                "asset",
                "fiat",
                "accepted_assets",
                "amount",
                "description",
                "hidden_message",
                "paid_btn_name",
                "paid_btn_url",
                "payload",
                "allow_comments",
                "allow_anonymous",
                "expires_in"
            ],
            "deleteInvoice": [
                "invoice_id"
            ],
            "createCheck": [
                "asset",
                "amount",
                "pin_to_user_id",
                "pin_to_username"
            ],
            "deleteCheck": [
                "check_id"
            ],
            "transfer": [
                "user_id",
                "asset",
                "amount",
                "spend_id",
                "comment",
                "disable_send_notification"
            ],
            "getInvoices": [
                "asset",
                "invoice_ids",
                "status",
                "offset",
                "count"
            ],
            "getChecks": [
                "asset",
                "check_ids",
                "status",
                "offset",
                "count"
            ],
            "getTransfers": [
                "asset",
                "transfer_ids",
                "offset",
                "count"
            ],
            "getStats": [
                "start_at",
                "end_at"
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
        asset: int,
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

    def delete_invoice(
        self,
        invoice_id: int
    ) -> bool:
        pass

    def create_check(
        self,
        asset: int,
        amount: float,
        pin_to_user_id: Optional[int] = None,
        pin_to_username: Optional[str] = None
    ) -> Check:
        pass

    def delete_check(
        self,
        check_id: int
    ) -> bool:
        pass

    def transfer(
        self,
        user_id: int,
        asset: str,
        amount: BaseAsset,
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

    def get_checks(
        self,
        asset: Optional[str] = None,
        check_ids: Optional[List[int]] = None,
        status: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None
    ) -> List[Check]:
        pass

    def get_transfers(
        self,
        asset: Optional[str] = None,
        transfers_id: Optional[List[int]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None
    ):
        pass

    def get_balance(self) -> List[Balance]:
        pass

    def get_exchange_rates(self) -> List[ExchangeRate]:
        pass

    def get_currencies(self) -> List[Currency]:
        pass

    def get_stats(
        self,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None
    ) -> List[AppStats]:
        pass
