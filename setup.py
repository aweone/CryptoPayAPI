from setuptools import setup

from CryptoPayAPI import __version__


def read_requirements():
    with open("requirements.txt", "r") as f:
        return [r for r in f.read().split("\n") if r]


def read_file(filename):
    with open(filename) as file:
        return file.read()


setup(
    name="CryptoPayAPI",
    version=__version__,
    packages=[
        "CryptoPayAPI",
        "CryptoPayAPI.AioCryptoPay",
        "CryptoPayAPI.CryptoPay",
        "CryptoPayAPI.exceptions",
        "CryptoPayAPI.types.app",
        "CryptoPayAPI.types.app_stats",
        "CryptoPayAPI.types.asset",
        "CryptoPayAPI.types.balance",
        "CryptoPayAPI.types.base",
        "CryptoPayAPI.types.check",
        "CryptoPayAPI.types.cryptopay",
        "CryptoPayAPI.types.base",
        "CryptoPayAPI.types.currency",
        "CryptoPayAPI.types.currency_type",
        "CryptoPayAPI.types.exchange_rate",
        "CryptoPayAPI.types.fiat",
        "CryptoPayAPI.types.invoice",
        "CryptoPayAPI.types.transfer",
    ],
    url="https://github.com/aweone/CryptoPayAPI",
    license="MIT License",
    author="aweone",
    author_email="aweonegithub@gmail.com",
    description="Simple library for https://t.me/CryptoBot",
    install_requires=read_requirements(),
    project_urls={
        "Source Code": "https://github.com/aweone/CryptoPayAPI",
        "API Docs": "https://help.crypt.bot/crypto-pay-api"
    },
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    keywords="crypto api pay p2p wrapper async cryptopay cryptopayapi",
)
