from .base import BaseAsset


class USDT(BaseAsset):
    name = "USDT"


class TON(BaseAsset):
    name = "TON"


class BTC(BaseAsset):
    name = "BTC"


class ETH(BaseAsset):
    name = "ETH"


class LTC(BaseAsset):
    name = "LTC"


class BNB(BaseAsset):
    name = "BNB"


class TRX(BaseAsset):
    name = "TRX"


class USDC(BaseAsset):
    name = "USDC"


USDT = USDT()
TON = TON()
BTC = BTC()
ETH = ETH()
LTC = LTC()
BNB = BNB()
TRX = TRX()
USDC = USDC()


assets = [USDT, TON, BTC, ETH, LTC, BNB, TRX, USDC]


def get_asset_by_name(asset_name):
    for asset in assets:
        if asset.name == asset_name:
            return asset
