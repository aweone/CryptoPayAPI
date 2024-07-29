from typing import Optional, Union, List

from ..base import BaseType

from ..currency_type import BaseCurrencyType, CryptoCurrencyType, FiatCurrencyType, get_currency_type_by_name
from ..asset import BaseAsset, get_asset_by_name
from ..fiat import BaseFiat


class Invoice(BaseType):
    def __init__(
        self,
        invoice_id: int,
        hash: str,
        amount: int,
        pay_url: str,
        bot_invoice_url: str,
        mini_app_invoice_url: str,
        web_app_invoice_url: str,
        status: str,
        created_at: str,
        allow_comments: bool,
        allow_anonymous: bool,
        currency_type: str = None,
        paid_anonymously: bool = None,
        payload: Optional[str] = None,
        asset: Optional[BaseAsset] = None,
        fiat: Optional[BaseFiat] = None,
        paid_asset: Optional[BaseAsset] = None,
        paid_amount: Optional[int] = None,
        paid_fiat_rate: Optional[str] = None,
        accepted_assets: Optional[List[BaseAsset]] = None,
        fee_asset: Optional[BaseAsset] = None,
        fee_amount: Optional[int] = None,
        fee: Optional[str] = None,
        description: Optional[str] = None,
        paid_usd_rate: Optional[str] = None,
        usd_rate: Optional[str] = None,
        expiration_date: Optional[str] = None,
        paid_at: Optional[str] = None,
        comment: Optional[str] = None,
        hidden_message: Optional[str] = None,
        paid_btn_name: Optional[str] = None,
        paid_btn_url: Optional[str] = None,
        *args,
        **kwargs,
    ):
        self.invoice_id = invoice_id
        self.hash = hash
        self.currency_type = get_currency_type_by_name(currency_type)
        self.asset = get_asset_by_name(asset)
        self.fiat = fiat
        self.amount = amount
        self.paid_asset = paid_asset
        self.paid_amount = paid_amount
        self.paid_fiat_rate = paid_fiat_rate
        self.accepted_assets = accepted_assets
        self.fee_asset = fee_asset
        self.fee_amount = fee_amount
        self.fee = fee
        self.pay_url = pay_url
        self.bot_invoice_url = bot_invoice_url
        self.mini_app_invoice_url = mini_app_invoice_url
        self.web_app_invoice_url = web_app_invoice_url
        self.description = description
        self.status = status
        self.created_at = created_at
        self.paid_usd_rate = paid_usd_rate
        self.usd_rate = usd_rate
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

        if not self.currency_type:
            if self.asset:
                self.currency_type = CryptoCurrencyType
            elif self.fiat:
                self.currency_type = FiatCurrencyType
