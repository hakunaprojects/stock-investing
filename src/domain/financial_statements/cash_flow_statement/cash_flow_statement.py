from dataclasses import dataclass, field
from typing import Optional

from src.domain.financial_statements.cash_flow_statement.financing_activities import (
    FinancingActivities,
)
from src.domain.financial_statements.cash_flow_statement.investing_activities import (
    InvestingActivities,
)
from src.domain.financial_statements.cash_flow_statement.operating_activities import (
    OperatingActivities,
)
from src.domain.financial_statements.exceptions.cash_flow_statement_exception import (
    NotFoundCapitalExpenditureException,
)


@dataclass
class CashFlowStatement:
    """The cash flow statement (CFS), is a financial statement that summarizes the movement of cash and cash
    equivalents (CCE) that come in and go out of a company. The CFS measures how well a company manages its cash
    position, meaning how well the company generates cash to pay its debt obligations and fund its operating
    expenses."""

    operating_activities: OperatingActivities
    investing_activities: InvestingActivities
    financing_activities: FinancingActivities
    cash_at_beginning_of_period: int
    net_change_in_cash_flow: int = field(init=False)
    cash_at_end_of_period: int = field(init=False)
    capital_expenditure: Optional[int] = None
    free_cash_flow: Optional[int] = None

    def __post_init__(self):
        self._calculate_net_change_in_cash_flow()
        self.cash_at_end_of_period = (
            self.cash_at_beginning_of_period + self.net_change_in_cash_flow
        )

    def _calculate_net_change_in_cash_flow(self):
        """Net cash flow is a variable and a profitability metric that represents the amount of money produced
        or lost by a business during a given period."""
        self.net_change_in_cash_flow = (
            self.operating_activities.net_cash_provided_by_operating_activities
            + self.investing_activities.net_cash_used_for_investing_activities
            + self.financing_activities.net_cash_used_provided_by_financing_activities
        )

    def calculate_capital_expenditure(
        self, previous_year_investments_in_property_plant_and_equipment: int
    ):
        """Capital expenditure or capital expense (capex or CAPEX) is the money an organization or corporate entity
        spends to buy, maintain, or improve its fixed assets, such as buildings, vehicles, equipment, or land.
        It is considered a capital expenditure when the asset is newly purchased or when money is used towards
        extending the useful life of an existing asset, such as repairing the roof..."""
        net_increase_in_property_plant_and_equipment = (
            self.investing_activities.investments_in_property_plant_and_equipment
            - previous_year_investments_in_property_plant_and_equipment
        )
        self.capital_expenditure = (
            net_increase_in_property_plant_and_equipment
            + self.operating_activities.depreciation
        )

    def calculate_free_cash_flow(self, interest_expense: int, tax_shield: int):
        """Free cash flow (FCF) represents the cash a company generates after accounting for cash outflows to support
        operations and maintain its capital assets. Unlike earnings or net income, free cash flow is a measure of
        profitability that excludes the non-cash expenses of the income statement and includes spending on equipment
        and assets as well as changes in working capital from the balance sheet. Interest expense and tax shield come
        from the income statement."""
        if self.capital_expenditure is None:
            raise NotFoundCapitalExpenditureException(
                "Capital Expenditure (Capex) is required to calculate the free cash flow."
            )

        self.free_cash_flow = (
            self.operating_activities.net_cash_provided_by_operating_activities
            + interest_expense
            - tax_shield
            - self.capital_expenditure
        )
