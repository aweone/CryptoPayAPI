import aiohttp

from ..types import *
from ..exceptions import *


class AioCryptoPay(BaseCryptoPay):
    base_url = "https://pay.crypt.bot/api/"

    def __init__(self, token: str):
        super().__init__(token)
        self.session = aiohttp.ClientSession(
            headers={
                "Host": "pay.crypt.bot",
                "Crypto-Pay-API-Token": token
            }
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

        response = await self._make_request(
            "createInvoice",
            "get",
            **params
        )

        return Invoice(**response)

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
            "get",
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
            if type(invoice_ids) == int:
                invoice_ids = str(invoice_ids)

        params = self._get_params(locals(), "createInvoice")

        response = await self._make_request(
            "getInvoices",
            "get",
            **params
        )

        invoices = [Invoice(**invoice) for invoice in response.get("items")]

        return invoices

    async def get_balance(self) -> List[Wallet]:
        response = await self._make_request("getBalance", "get")
        wallets = [Wallet(**wallet) for wallet in response]

        return wallets

    async def get_exchange_rates(self) -> List[ExchangeRate]:
        response = await self._make_request("getExchangeRates", "get")
        exchange_rates = [ExchangeRate(**exchange_rate) for exchange_rate in response]

        return exchange_rates

    async def get_currencies(self) -> List[Currency]:
        response = await self._make_request("getCurrencies", "get")
        print(response)
        currencies = [Currency(**currency) for currency in response]

        return currencies


'''
Передаю привет:
https://t.me/LordS_LOLZ
https://t.me/MOLUTBA
https://t.me/derkonw
https://t.me/mrrooooopert
https://t.me/zen220
https://t.me/Warkraftboy
https://t.me/Reboler
https://t.me/rage_nosoft
https://t.me/crypt0xTG
https://t.me/lolzwork
Horosh(oleg383 вроде хз убрал юзернейм)
https://t.me/raptinside

Ascii-арт с валему (https://t.me/walemu1337 (пес)):

┈╱╲┏┓▕╲▂▂▂╱▏
╱┏┓╲▏┈▏┻╯▃┻╲
╭━━╮╲┈▏╭┳┻┳╮▏
┃╭╮┃▕┈▏┣╮┈┈┃▏
┃┃╰╯▕╱╲╰┻┻┻╱
┃┃╱▔▔▕▕▔▕▔▔
┃╰▏▔╲▕▕╱▏▏
╰━╲▂▂▕▂▏▂▏

'''
