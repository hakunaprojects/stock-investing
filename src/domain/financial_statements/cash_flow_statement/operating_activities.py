from dataclasses import dataclass, field

from src.shared.general_functions import sum_all_initialized_int_attributes


@dataclass
class OperatingActivities:
    """Operating cash flow (OCF) is a measure of the amount of cash generated by a company's normal business
    operations. Operating cash flow indicates whether a company can generate sufficient positive cash flow to
    maintain and grow its operations """
    net_income: int
    depreciation: int
    amortization: int
    deferred_income_tax: int
    stock_based_compensation: int
    change_in_working_capital: int
    other_non_cash_items: int
    net_cash_provided_by_operating_activities: int = field(init=False)

    def __post_init__(self):
        self.net_cash_provided_by_operating_activities = sum_all_initialized_int_attributes(self)
