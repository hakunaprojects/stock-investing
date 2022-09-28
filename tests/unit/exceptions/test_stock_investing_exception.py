from src.domain.stock_investing_exception import StockInvestingException


def test_given_class_stock_investing_exception_when_initializing_then_code_and_message_are_none():
    # Initialize the exception
    stock_investing_exception = StockInvestingException()
    # Asserts
    assert stock_investing_exception.code is None
    assert stock_investing_exception.message is None
