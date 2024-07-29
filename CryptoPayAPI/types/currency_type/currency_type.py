from .base import BaseCurrencyType


class CryptoCurrencyType(BaseCurrencyType):
    name = "crypto"


class FiatCurrencyType(CryptoCurrencyType):
    name = "fiat"


CryptoCurrencyType = CryptoCurrencyType()
FiatCurrencyType = FiatCurrencyType()


currency_types = [CryptoCurrencyType, FiatCurrencyType]


def get_currency_type_by_name(currency_type_name: str):
    for currency_type in currency_types:
        if currency_type.name == currency_type_name:
            return currency_type
