from src.exceptions.stock_investing_exception import StockInvestingException


def test_given_class_stock_investing_exception_when_initializing_it_should_have_code_and_message_as_none():
    stock_investing_exception = StockInvestingException()

    assert stock_investing_exception.code is None
    assert stock_investing_exception.message is None
