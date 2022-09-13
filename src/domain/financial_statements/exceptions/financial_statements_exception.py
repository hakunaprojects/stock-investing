"""
Financial Statements Exceptions
It contains the main exception related with the domain Financial Statements.
"""

from src.exceptions.stock_investing_exception import StockInvestingException


class FinancialStatementsException(StockInvestingException):
    """Financial statements exception inherits from the main project exception, it sets the code and all other
    exceptions related with financial statements inherit from this."""

    def __init__(self):
        super().__init__()
        self.code = "ERROR.FINANCIAL_STATEMENTS"
