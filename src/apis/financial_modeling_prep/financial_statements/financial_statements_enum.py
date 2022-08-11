"""
FinancialStatementsEnum
It contains all required information to retrieve and verify the Financial Statements Data from the Financial Modeling
Prep Api.
"""
from src.apis.financial_modeling_prep.financial_modeling_prep_enum import FinancialModelingPrepEnum
from src.apis.financial_modeling_prep.financial_statements.schemas.company_balance_sheet_statement_schema import \
    COMPANY_BALANCE_SHEET_STATEMENT_SCHEMA
from src.apis.financial_modeling_prep.financial_statements.schemas.company_cash_flow_statement_schema import \
    COMPANY_CASH_FLOW_STATEMENT_SCHEMA
from src.apis.financial_modeling_prep.financial_statements.schemas.company_income_statement_schema import \
    COMPANY_INCOME_STATEMENT_SCHEMA


class FinancialStatementsEnum(FinancialModelingPrepEnum):
    """Defines the enum values with concept, path_concept and validation_schema."""
    INCOME_STATEMENT = {'concept': 'CompanyIncomeStatement', 'path_concept': 'income-statement',
                        'validation_schema': COMPANY_INCOME_STATEMENT_SCHEMA}
    BALANCE_SHEET_STATEMENT = {'concept': 'CompanyBalanceSheetStatement', 'path_concept': 'balance-sheet-statement',
                               'validation_schema': COMPANY_BALANCE_SHEET_STATEMENT_SCHEMA}
    CASH_FLOW_STATEMENT = {'concept': 'CompanyCashFlowStatement', 'path_concept': 'cash-flow-statement',
                           'validation_schema': COMPANY_CASH_FLOW_STATEMENT_SCHEMA}
