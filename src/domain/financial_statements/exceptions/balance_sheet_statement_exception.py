"""
Balance Sheet Statement Exceptions
It contains all exceptions related with the domain Balance Sheet Statement from Financial Statements.
"""
from src.domain.financial_statements.exceptions.financial_statements_exception import (
    FinancialStatementsException,
)


class BalanceSheetStatementException(FinancialStatementsException):
    """Exception for cases related with Balance Sheet Statement."""

    def __init__(self):
        super().__init__()
        self.code += ".BALANCE_SHEET_STATEMENT"


class IsNotBalancedException(BalanceSheetStatementException):
    """Exception raised when the balance sheet is not balanced."""

    def __init__(self, message):
        super().__init__()
        self.message = message
