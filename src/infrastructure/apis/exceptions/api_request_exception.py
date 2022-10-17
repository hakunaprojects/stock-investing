"""
Api Request Exceptions
It contains all exceptions related with Api Requests interactions.
"""
from datetime import datetime

from src.domain.stock_investing_exception import StockInvestingException


class ApiRequestException(StockInvestingException):
    """Api request exception inherits from the main project exception, it sets the code and all other exceptions
    inherit from this. Here, the code is set."""

    def __init__(self):
        super().__init__()
        self.code = "ERROR.API_REQUEST"
        self.timestamp = datetime.now()


class NotValidUrlException(ApiRequestException):
    """Exception for cases where the url is not found. Http responses with status_code 404 raises this error."""

    def __init__(self, message):
        super().__init__()
        self.message = message


class NonJsonDataFoundException(ApiRequestException):
    """Exception for cases where it is expected a json format in the response, but it is not found."""

    def __init__(self, message):
        super().__init__()
        self.message = message


class NotValidSchemaException(ApiRequestException):
    """Exception for cases where, given a json in the response, the schema is not valid."""

    def __init__(self, message):
        super().__init__()
        self.message = message
