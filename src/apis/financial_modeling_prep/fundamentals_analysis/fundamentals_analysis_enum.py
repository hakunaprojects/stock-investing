"""
"""
from enum import Enum
from jsonschema.validators import validate
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_financial_growth import \
    COMPANY_FINANCIAL_GROWTH_SCHEMA
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_financial_ratios_schema import \
    COMPANY_FINANCIAL_RATIOS_SCHEMA
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.income_statement_growth import \
    INCOME_STATEMENT_GROWTH_SCHEMA
from src.apis.financial_modeling_prep.fundamentals_analysis.schemas.company_key_metrics import \
    COMPANY_KEY_METRICS_SCHEMA


class FundamentalsAnalysisEnum(Enum):
    COMPANY_FINANCIAL_RATIOS = {'concept': 'CompanyFinancialRatios', 'path_concept': 'ratios',
                                'validation_schema': COMPANY_FINANCIAL_RATIOS_SCHEMA}
    INCOME_STATEMENT_GROWTH = {'concept': 'IncomeStatementGrowth', 'path_concept': 'income-statement-growth',
                               'validation_schema': INCOME_STATEMENT_GROWTH_SCHEMA}
    COMPANY_FINANCIAL_GROWTH = {'concept': 'IncomeStatementGrowth', 'path_concept': 'financial-growth',
                                'validation_schema': COMPANY_FINANCIAL_GROWTH_SCHEMA}
    COMPANY_KEY_METRICS_SCHEMA = {'concept': 'CompanyKeyMetrics', 'path_concept': 'key-metrics',
                                  'validation_schema': COMPANY_KEY_METRICS_SCHEMA}

    def get_concept(self):
        return self.value.get('concept')

    def get_path_concept(self):
        return self.value.get('path_concept')

    def get_validate_data(self, data_to_validate):
        validate(instance=data_to_validate, schema=self.value.get('validation_schema'))
