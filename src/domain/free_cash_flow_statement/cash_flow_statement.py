from dataclasses import dataclass

from src.domain.free_cash_flow_statement.financing_activities import FinancingActivities
from src.domain.free_cash_flow_statement.investing_activities import InvestingActivities
from src.domain.free_cash_flow_statement.operating_activities import OperatingActivities


@dataclass
class CashFlowStatement:
    """The cash flow statement (CFS), is a financial statement that summarizes the movement of cash and cash
    equivalents (CCE) that come in and go out of a company. The CFS measures how well a company manages its cash
    position, meaning how well the company generates cash to pay its debt obligations and fund its operating
    expenses. """
    operating_activities: OperatingActivities
    investing_activities: InvestingActivities
    financing_activities: FinancingActivities
    cash_at_beginning_of_period: int
    cash_at_end_of_period: int
