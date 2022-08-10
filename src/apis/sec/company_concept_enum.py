"""
Company Concept Enum
Class Enum with specific concept values to retrieve information from the SEC Api by concept.
"""

from enum import Enum


class CompanyConceptEnum(Enum):
    """Defines the enum values with concept and taxonomy."""
    EARNINGS_PER_SHARE_DILUTED = {'concept': 'EarningsPerShareDiluted', 'taxonomy': 'us-gaap'}
    COMPREHENSIVE_INCOME_NET_OF_TAX = {'concept': 'ComprehensiveIncomeNetOfTax', 'taxonomy': 'us-gaap'}

    def get_concept(self):
        """Retrieve value concept from the enum."""
        return self.value.get('concept')

    def get_taxonomy(self):
        """Retrieve value taxonomy from the enum."""
        return self.value.get('taxonomy')
