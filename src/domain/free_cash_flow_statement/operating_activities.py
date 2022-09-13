from dataclasses import dataclass


@dataclass
class OperatingActivities:
    """Operating cash flow (OCF) is a measure of the amount of cash generated by a company's normal business
    operations. Operating cash flow indicates whether a company can generate sufficient positive cash flow to
    maintain and grow its operations """
    net_income: int
    depreciation_and_amortization: int
    deferred_income_tax: int
    stock_based_compensation: int
    change_in_working_capital: int
    accounts_receivables: int
    inventory: int
    accounts_payables: int
    other_working_capital: int
    other_non_cash_items: int
    net_cash_provided_by_operating_activities: int
