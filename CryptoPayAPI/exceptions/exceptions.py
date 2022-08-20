
class CryptoPayException(Exception):
    def __init__(self, error: dict):
        self.message = f"Code: {error['code']}. Name: {error['name']}"
        super().__init__(self.message)
