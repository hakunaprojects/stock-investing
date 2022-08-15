import json

from src.shared.config import FINANCIAL_STATEMENTS_SCHEMAS_PATH


def _load_schema(filename: str) -> dict:
    with open(filename) as fp:
        data = json.load(fp)
    fp.close()
    return data


COMPANY_BALANCE_SHEET_STATEMENT_SCHEMA = _load_schema(
    filename=f"{FINANCIAL_STATEMENTS_SCHEMAS_PATH}/company_balance_sheet_statement_schema.json")
COMPANY_CASH_FLOW_STATEMENT_SCHEMA = _load_schema(
    filename=f"{FINANCIAL_STATEMENTS_SCHEMAS_PATH}/company_cash_flow_statement_schema.json")
COMPANY_INCOME_STATEMENT_SCHEMA = _load_schema(
    filename=f"{FINANCIAL_STATEMENTS_SCHEMAS_PATH}/company_income_statement_schema.json")
