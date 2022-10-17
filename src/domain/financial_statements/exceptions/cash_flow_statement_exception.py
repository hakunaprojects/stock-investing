"""
Cash Flow Statement Exceptions
It contains all exceptions related with the domain Cash Flow Statement from Financial Statements.
"""
from src.domain.financial_statements.exceptions.financial_statements_exception import (
    FinancialStatementsException,
)


class CashFlowStatementException(FinancialStatementsException):
    """Exception for cases related with Cash Flow Statement."""

    def __init__(self):
        super().__init__()
        self.code += ".CASH_FLOW_STATEMENT"


class NotFoundCapitalExpenditureException(CashFlowStatementException):
    """Exception raised when capital expenditure is required but not found."""

    def __init__(self, message):
        super().__init__()
        self.message = message
