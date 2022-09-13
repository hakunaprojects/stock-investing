from dataclasses import dataclass


@dataclass
class CurrentAssets:
    cash_and_cash_equivalents: int
    short_term_investments: int
    net_receivables: int
    inventory: int
    other_current_assets: int
    total_current_assets: int


@dataclass
class NonCurrentAssets:
    property_plant_equipmentNet: int
    goodwill: int
    intangible_assets: int
    long_term_investments: int
    tax_assets: int
    other_non_current_assets: int
    total_non_current_assets: int


@dataclass
class Assets:
    current_assets: CurrentAssets
    non_current_assets: NonCurrentAssets
    total_assets: int
