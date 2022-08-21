# CryptoPayAPI
Simple library for https://t.me/CryptoBot

### Usage
```Python
from CryptoPayAPI.AioCryptoPay import AioCryptoPay
from CryptoPayAPI.types import Asset

import asyncio

async def main():
    #create session
    cryptopay = AioCryptoPay(token="token")

    #get balance wallets
    await cryptopay.get_balance()

    #create invoice
    invoice = await cryptopay.create_invoice(asset=Asset.BTC, amount=10)
    print(invoice.pay_url)

    #get list of inovices
    invoices = await cryptopay.get_invoices(asset=Asset.TON)

    #close session
    await cryptopay.close()

asyncio.run(main())

```

### Docs
The library is fully compatible with the official api - https://help.crypt.bot/crypto-pay-api

### Donation
BTC - bc1qltq6d7lzprr9hhpya4pptwj3997gpwkzhulksh
ETH - 0x6727e912855A289A340Ba1213E1038AdB0E3CDb9
USDT (TRC20) - TH5JtPd7siwCb4AnHyGniMz52gtysY3zEJ