from dataclasses import dataclass, field

from src.shared.general_functions import sum_all_initialized_int_attributes


@dataclass
class ShareholdersEquity:
    """Shareholders' equity is the amount that the owners of a company have invested in their business. This includes
    the money they've directly invested and the accumulation of income the company has earned and that has been
    reinvested since inception."""

    preferred_Stock: int
    common_stock: int
    retained_earnings: int
    accumulated_other_comprehensive_income_loss: int
    other_total_stockholders_equity: int
    minority_interest: int
    total_shareholders_equity: int = field(init=False)

    def __post_init__(self):
        self.total_shareholders_equity = sum_all_initialized_int_attributes(self)
