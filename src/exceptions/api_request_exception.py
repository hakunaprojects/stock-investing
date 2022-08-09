"""
Api Request Exceptions
It contains all exceptions related with Api Requests interactions.
"""
from datetime import datetime
from src.exceptions.stock_investing_exception import StockInvestingException


class ApiRequestException(StockInvestingException):
    def __init__(self):
        super().__init__()
        self.code = "ERROR.API_REQUEST"
        self.timestamp = datetime.now()


class NotValidUrlException(ApiRequestException):
    def __init__(self, message):
        super().__init__()
        self.message = message


class NonJsonDataFoundException(ApiRequestException):
    def __init__(self, message):
        super().__init__()
        self.message = message


class NotValidSchemaException(ApiRequestException):
    def __init__(self, message):
        super().__init__()
        self.message = message
