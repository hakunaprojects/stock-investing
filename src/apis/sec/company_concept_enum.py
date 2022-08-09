"""
"""
from enum import Enum


class CompanyConceptEnum(Enum):
    EARNINGS_PER_SHARE_DILUTED = {'concept': 'EarningsPerShareDiluted', 'taxonomy': 'us-gaap'}
    COMPREHENSIVE_INCOME_NET_OF_TAX = {'concept': 'ComprehensiveIncomeNetOfTax', 'taxonomy': 'us-gaap'}

    def get_concept(self):
        return self.value.get('concept')

    def get_taxonomy(self):
        return self.value.get('taxonomy')
