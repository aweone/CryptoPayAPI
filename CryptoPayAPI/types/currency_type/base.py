from ..base import BaseType


class BaseCurrencyType(BaseType):
    name: str

    def __repr__(self):
        return self.name
