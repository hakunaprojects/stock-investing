import os
from pathlib import Path

_CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
APIS_FOLDER = "apis"

FINANCIAL_MODELING_PREP_FOLDER = "financial_modeling_prep"
FINANCIAL_STATEMENTS_FOLDER = "financial_statements"
FINANCIAL_STATEMENTS_SCHEMAS_FOLDER = "schemas"

FUNDAMENTALS_ANALYSIS_FOLDER = "fundamentals_analysis"
FUNDAMENTALS_ANALYSIS_SCHEMAS_FOLDER = "schemas"

SEC_FOLDER = "sec"
SEC_SCHEMAS_FOLDER = "schemas"

PROJECT_PATH = Path(_CURRENT_FOLDER).absolute().parent
APIS_PATH = os.path.join(PROJECT_PATH, APIS_FOLDER)
FINANCIAL_STATEMENTS_SCHEMAS_PATH = os.path.join(PROJECT_PATH,
                                                 APIS_PATH,
                                                 FINANCIAL_MODELING_PREP_FOLDER,
                                                 FINANCIAL_STATEMENTS_FOLDER,
                                                 FINANCIAL_STATEMENTS_SCHEMAS_FOLDER)

FUNDAMENTALS_ANALYSIS_SCHEMAS_PATH = os.path.join(PROJECT_PATH,
                                                  APIS_PATH,
                                                  FINANCIAL_MODELING_PREP_FOLDER,
                                                  FUNDAMENTALS_ANALYSIS_FOLDER,
                                                  FUNDAMENTALS_ANALYSIS_SCHEMAS_FOLDER)

SEC_SCHEMAS_PATH = os.path.join(PROJECT_PATH,
                                APIS_PATH,
                                SEC_FOLDER,
                                SEC_SCHEMAS_FOLDER)
