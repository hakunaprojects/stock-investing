from src.shared.config import FINANCIAL_STATEMENTS_SCHEMAS_PATH
from src.shared.io_files import load_json_file

COMPANY_BALANCE_SHEET_STATEMENT_SCHEMA = load_json_file(
    filename=f"{FINANCIAL_STATEMENTS_SCHEMAS_PATH}/company_balance_sheet_statement_schema.json")
COMPANY_CASH_FLOW_STATEMENT_SCHEMA = load_json_file(
    filename=f"{FINANCIAL_STATEMENTS_SCHEMAS_PATH}/company_cash_flow_statement_schema.json")
COMPANY_INCOME_STATEMENT_SCHEMA = load_json_file(
    filename=f"{FINANCIAL_STATEMENTS_SCHEMAS_PATH}/company_income_statement_schema.json")
