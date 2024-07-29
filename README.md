# CryptoPayAPI
Simple library for https://t.me/CryptoBot
### Installation
```
$ pip install CryptoPayAPI
```

### Usage
#### Asynchronous
```Python
from CryptoPayAPI.AioCryptoPay import AioCryptoPay
from CryptoPayAPI.types.asset import USDT

import asyncio

async def main():
    # create session
    cryptopay = AioCryptoPay(
        token="token",
        is_test_net=True
    )

    await cryptopay.get_balance()

    invoice = await cryptopay.create_invoice(amount=1, asset=USDT)
    print(invoice.bot_invoice_url)

    await cryptopay.close()

asyncio.run(main())

```

#### Synchronous
```Python
from CryptoPayAPI.CryptoPay import CryptoPay
from CryptoPayAPI.types.asset import BTC

# create session
cryptopay = CryptoPay(
    token="token"
)

cryptopay.get_balance()

invoice = cryptopay.create_invoice(amount=0.3, asset=BTC)
print(invoice.bot_invoice_url)


```

### Docs
The library is fully compatible with the official api - https://help.crypt.bot/crypto-pay-api
