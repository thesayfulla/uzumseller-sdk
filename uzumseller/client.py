from typing import NoReturn


class UzumSellerClient:
    """
    A client for interacting with the Uzum Seller API.
    Attributes:
        token (str): The authentication token for accessing the API.
    """
    def __init__(self, token: str) -> NoReturn:
        self.token = token
