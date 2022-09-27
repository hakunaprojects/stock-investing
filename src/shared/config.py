import os
from pathlib import Path

from dotenv import dotenv_values

_CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = Path(_CURRENT_FOLDER).absolute().parent

INFRASTRUCTURE_FOLDER = "infrastructure"
APIS_FOLDER = "apis"
APIS_PATH = os.path.join(PROJECT_PATH, INFRASTRUCTURE_FOLDER, APIS_FOLDER)

FINANCIAL_MODELING_PREP_FOLDER = "financial_modeling_prep"
FINANCIAL_STATEMENTS_FOLDER = "financial_statements"
FINANCIAL_STATEMENTS_SCHEMAS_FOLDER = "schemas"
FINANCIAL_STATEMENTS_SCHEMAS_PATH = os.path.join(APIS_PATH,
                                                 FINANCIAL_MODELING_PREP_FOLDER,
                                                 FINANCIAL_STATEMENTS_FOLDER,
                                                 FINANCIAL_STATEMENTS_SCHEMAS_FOLDER)


FUNDAMENTALS_ANALYSIS_FOLDER = "fundamentals_analysis"
FUNDAMENTALS_ANALYSIS_SCHEMAS_FOLDER = "schemas"
FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH = os.path.join(APIS_PATH,
                                                  FINANCIAL_MODELING_PREP_FOLDER,
                                                  FUNDAMENTALS_ANALYSIS_FOLDER,
                                                  FUNDAMENTALS_ANALYSIS_SCHEMAS_FOLDER)


SEC_FOLDER = "sec"
SEC_SCHEMAS_FOLDER = "schemas"
SEC_SCHEMAS_PATH = os.path.join(APIS_PATH,
                                SEC_FOLDER,
                                SEC_SCHEMAS_FOLDER)


ENV_CONFIG = {
    **dotenv_values(f"{PROJECT_PATH}/.env.secrets"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

