from dataclasses import dataclass, field

from src.shared.general_functions import sum_all_initialized_int_attributes


@dataclass
class CurrentAssets:
    """Current assets accounts for all company-owned assets that can be converted to cash within one year."""
    cash_and_cash_equivalents: int
    short_term_investments: int
    net_receivables: int
    inventory: int
    other_current_assets: int
    total_current_assets: field(init=False)

    def __post_init__(self):
        self.total_current_assets = sum_all_initialized_int_attributes(self)


@dataclass
class NonCurrentAssets:
    """Non-current assets are a company’s long-term investments that have a useful life of more than one year.
    Non-current assets cannot be converted to cash easily. They are required for the long-term needs of a business """
    property_plant_equipmentNet: int
    goodwill: int
    intangible_assets: int
    long_term_investments: int
    tax_assets: int
    other_non_current_assets: int
    total_non_current_assets: field(init=False)

    def __post_init__(self):
        self.total_non_current_assets = sum_all_initialized_int_attributes(self)


@dataclass
class Assets:
    """Assets are resources with economic value with the expectation that it will provide a future benefit. They are
    bought or created to increase a firm's value or benefit the firm's operations. """
    current_assets: CurrentAssets
    non_current_assets: NonCurrentAssets
    total_assets: field(init=False)

    def __post_init__(self):
        self.total_assets = self.current_assets.total_current_assets + self.non_current_assets.total_non_current_assets
