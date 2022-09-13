from dataclasses import dataclass


@dataclass
class CurrentLiabilities:
    account_payables: int
    short_term_Debt: int
    tax_payables: int
    deferred_revenue: int
    other_current_liabilities: int
    total_current_liabilities: int


@dataclass
class NonCurrentLiabilities:
    long_term_debt: int
    deferred_revenue_non_current: int
    deferred_tax_liabilities_non_current: int
    other_non_current_liabilities: int
    total_non_current_liabilities: int


@dataclass
class Liabilities:
    current_liabilities: CurrentLiabilities
    non_current_liabilities: NonCurrentLiabilities
    other_liabilities: int
    capital_lease_obligations: int
    total_liabilities: int
