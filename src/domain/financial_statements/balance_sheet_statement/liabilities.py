from dataclasses import dataclass, field

from src.shared.general_functions import sum_all_initialized_int_attributes


@dataclass
class CurrentLiabilities:
    """Current or short-term liability is a financial obligation that is to be paid within one year. This type of
    liability is classified within the current liabilities section of an entity’s balance sheet."""
    account_payables: int
    short_term_Debt: int
    tax_payables: int
    deferred_revenue: int
    other_current_liabilities: int
    total_current_liabilities: field(init=False)

    def __post_init__(self):
        self.total_current_liabilities = sum_all_initialized_int_attributes(self)


@dataclass
class NonCurrentLiabilities:
    """Non-current or long-term liabilities are financial obligations of a company that are due more than one year in
    the future."""
    long_term_debt: int
    deferred_revenue_non_current: int
    deferred_tax_liabilities_non_current: int
    other_non_current_liabilities: int
    total_non_current_liabilities: field(init=False)

    def __post_init__(self):
        self.total_non_current_liabilities = sum_all_initialized_int_attributes(self)


@dataclass
class Liabilities:
    """Liabilities refer to things that you owe or have borrowed."""
    current_liabilities: CurrentLiabilities
    non_current_liabilities: NonCurrentLiabilities
    other_liabilities: int
    capital_lease_obligations: int
    total_liabilities: field(init=False)

    def __post_init__(self):
        self.total_liabilities = \
            self.current_liabilities.total_current_liabilities + \
            self.non_current_liabilities.total_non_current_liabilities + \
            self.other_liabilities + \
            self.capital_lease_obligations
