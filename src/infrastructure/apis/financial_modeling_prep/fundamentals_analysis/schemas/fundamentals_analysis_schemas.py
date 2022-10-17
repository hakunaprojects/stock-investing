from src.shared.config import FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH
from src.shared.io_files import load_json_file

COMPANY_FINANCIAL_GROWTH_SCHEMA = load_json_file(
    filename=f"{FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH}/company_financial_growth_schema.json"
)
COMPANY_FINANCIAL_RATIOS_SCHEMA = load_json_file(
    filename=f"{FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH}/company_financial_ratios_schema.json"
)
COMPANY_INCOME_STATEMENT_GROWTH_SCHEMA = load_json_file(
    filename=f"{FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH}/company_income_statement_growth_schema.json"
)
COMPANY_KEY_METRICS_SCHEMA = load_json_file(
    filename=f"{FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH}/company_key_metrics_schema.json"
)
