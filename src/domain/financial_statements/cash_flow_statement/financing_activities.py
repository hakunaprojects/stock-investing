from dataclasses import dataclass


@dataclass
class FinancingActivities:
    """Cash flow from financing activities (CFF) shows the net flows of cash that are used to fund the company.
    Financing activities include transactions involving debt, equity, and dividends. It provides investors with
    insight into a company’s financial strength and how well a company's capital structure is managed. """
    debt_repayment: int
    common_stock_issued: int
    common_stock_repurchased: int
    dividends_paid: int
    other_financing_activities: int
    net_cash_used_provided_by_financing_activities: int
