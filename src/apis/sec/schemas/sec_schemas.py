from src.shared.config import SEC_SCHEMAS_PATH
from src.shared.io_files import load_json_file

COMPANY_CONCEPT_SCHEMA = load_json_file(
    filename=f"{SEC_SCHEMAS_PATH}/company_concept_schema.json")
COMPANY_FACTS_SCHEMA = load_json_file(
    filename=f"{SEC_SCHEMAS_PATH}/company_facts_schema.json")
COMPANY_TICKERS_EXCHANGE_SCHEMA = load_json_file(
    filename=f"{SEC_SCHEMAS_PATH}/company_tickers_exchange_schema.json")
SUBMISSIONS_SCHEMA = load_json_file(
    filename=f"{SEC_SCHEMAS_PATH}/submissions_schema.json")
