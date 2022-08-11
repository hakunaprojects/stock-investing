"""
Fundamentals Analysis Enum
It contains all required information to retrieve and verify Fundamentals Analysis Data from the Financial Modeling
Prep Api.
"""

from src.apis.financial_modeling_prep.financial_modeling_prep_enum import FinancialModelingPrepEnum
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_financial_growth_schema import \
    COMPANY_FINANCIAL_GROWTH_SCHEMA
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_financial_ratios_schema import \
    COMPANY_FINANCIAL_RATIOS_SCHEMA
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_income_statement_growth_schema import \
    COMPANY_INCOME_STATEMENT_GROWTH_SCHEMA
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_key_metrics_schema import \
    COMPANY_KEY_METRICS_SCHEMA


class FundamentalsAnalysisEnum(FinancialModelingPrepEnum):
    """Defines the enum values with concept, path_concept and validation_schema."""
    COMPANY_FINANCIAL_RATIOS = {'concept': 'CompanyFinancialRatios', 'path_concept': 'ratios',
                                'validation_schema': COMPANY_FINANCIAL_RATIOS_SCHEMA}
    INCOME_STATEMENT_GROWTH = {'concept': 'CompanyIncomeStatementGrowth', 'path_concept': 'income-statement-growth',
                               'validation_schema': COMPANY_INCOME_STATEMENT_GROWTH_SCHEMA}
    COMPANY_FINANCIAL_GROWTH = {'concept': 'CompanyFinancialGrowth', 'path_concept': 'financial-growth',
                                'validation_schema': COMPANY_FINANCIAL_GROWTH_SCHEMA}
    COMPANY_KEY_METRICS_SCHEMA = {'concept': 'CompanyKeyMetrics', 'path_concept': 'key-metrics',
                                  'validation_schema': COMPANY_KEY_METRICS_SCHEMA}
