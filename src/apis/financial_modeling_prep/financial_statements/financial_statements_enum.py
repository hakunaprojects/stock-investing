"""
FinancialStatementsEnum
It contains all required information to retrieve and verify the Financial Statements Data from the Financial Modeling
Prep Api.
"""
from enum import Enum
from jsonschema.validators import validate
from src.apis.financial_modeling_prep.financial_statements.schemas.balance_sheet_statement_schema import \
    BALANCE_SHEET_STATEMENT_SCHEMA
from src.apis.financial_modeling_prep.financial_statements.schemas.cash_flow_statement_schema import \
    CASH_FLOW_STATEMENT_SCHEMA
from src.apis.financial_modeling_prep.financial_statements.schemas.income_statement_schema import \
    INCOME_STATEMENT_SCHEMA


class FinancialStatementsEnum(Enum):
    INCOME_STATEMENT = {'concept': 'IncomeStatement', 'path_concept': 'income-statement',
                        'validation_schema': INCOME_STATEMENT_SCHEMA}
    BALANCE_SHEET_STATEMENT = {'concept': 'BalanceSheetStatement', 'path_concept': 'balance-sheet-statement',
                               'validation_schema': BALANCE_SHEET_STATEMENT_SCHEMA}
    CASH_FLOW_STATEMENT = {'concept': 'CashFlowStatement', 'path_concept': 'cash-flow-statement',
                           'validation_schema': CASH_FLOW_STATEMENT_SCHEMA}

    def get_concept(self):
        """Retrieve the concept property from the current enum."""
        return self.value.get('concept')

    def get_path_concept(self):
        """Retrieve the path_concept property from the current enum."""
        return self.value.get('path_concept')

    def get_validate_data(self, data_to_validate):
        """Validate the data taking the validation schema from the current enum."""
        validate(instance=data_to_validate, schema=self.value.get('validation_schema'))


