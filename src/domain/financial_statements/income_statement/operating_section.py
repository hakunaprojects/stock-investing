from dataclasses import dataclass, field

from src.shared.general_functions import sum_all_initialized_int_attributes


@dataclass
class OperatingRevenueSection:
    """This section includes revenue realized through primary activities and its main associate cost. For some
    companies, referred as cost of goods sold (COGS)"""

    revenue: int  # Or Sales
    cost_of_revenue: int  # In some companies: Cost of goods sold (cogs)
    gross_profit: int = field(init=False)

    def __post_init__(self):
        self.gross_profit = self.revenue - self.cost_of_revenue


@dataclass
class OperatingExpensesSection:
    """These are all expenses incurred for earning the normal operating revenue linked to the primary activity of the
    business, except cost of goods sold (COGS). They include selling, general and administrative (SG&A) expenses;
    depreciation or amortization; and research and development (R&D) expenses. Typical items that make up the list
    are employee wages, sales commissions, and expenses for utilities such as electricity and transportation."""

    research_and_development_expenses: int
    general_and_administrative_expenses: int
    selling_and_marketing_expenses: int
    selling_general_and_administrative_Expenses: int
    other_operating_expenses: int
    total_operating_expenses: int = field(init=False)

    def __post_init__(self):
        self.total_operating_expenses = sum_all_initialized_int_attributes(self)


@dataclass
class OperatingSection:
    """For a company manufacturing a product, or for a wholesaler, distributor, or retailer involved in the business
    of selling that product, the operating income from primary activities refers to revenue achieved from the sale of
    the product minus the primary expenses to create and sell it. Similarly, for a company (or its franchisees) in
    the business of offering services, revenue from primary activities would refer to the revenue or fees earned in
    exchange for offering those services."""

    operating_revenue_section: OperatingRevenueSection
    operating_expenses_section: OperatingExpensesSection
    depreciation_and_amortization_expense: int
    ebitda: int = field(init=False)
    operating_income: int = field(
        init=False
    )  # Also called Earnings before interest and taxes (EBIT)

    def __post_init__(self):
        self.ebitda = (
            self.operating_revenue_section.gross_profit
            - self.operating_expenses_section.total_operating_expenses
        )
        self.operating_income = self.ebitda - self.depreciation_and_amortization_expense
