from dataclasses import dataclass, field
from typing import Optional

from src.domain.financial_statements.income_statement.non_operating_section import NonOperatingSection
from src.domain.financial_statements.income_statement.operating_section import OperatingSection


@dataclass
class IncomeStatement:
    """The income statement, also known as the profit and loss (P&L) statement or the statement of revenue and
    expense, the income statement primarily focuses on the company’s revenue and expenses during a particular period.
    The best way to analyze a company and decide whether you should invest is to know how to dissect its income
    statement."""
    operating_section: OperatingSection
    non_operating_section: NonOperatingSection
    income_tax_expense: int
    income_before_tax: field(init=False)  # Earnings before Tax (EBT)
    net_income: field(init=False)

    shares_outstanding: int
    earnings_per_share: Optional[int]
    earnings_per_share_diluted: Optional[int]

    def __post_init__(self):
        self.income_before_tax = \
            self.operating_section.operating_income + \
            self.non_operating_section.non_operating_income
        self.net_income = self.income_before_tax - self.income_tax_expense

    def calculate_earnings_per_share(self, initial_shares_outstanding: int):
        """Basic Earnings Per Share (EPS) is a calculation that attempts to take the net income applicable to common
        shares for a period and divide it by the average number of shares outstanding for that same period. """
        avg_shares_outstanding = (initial_shares_outstanding + self.shares_outstanding)/2
        self.earnings_per_share = self.net_income / avg_shares_outstanding

    def calculate_earnings_per_share_diluted(self, initial_shares_outstanding: int, additional_dilution: int):
        """Diluted earnings per share adjust the basic EPS figure by including all potential dilution that would
        result in the reported earnings per share being lower than they might have been if triggered at current
        prices and conditions. As an example of an additional dilution: an early investor holds a convertible
        security that could result in five million more shares being issued when the investor wants to convert it. """
        avg_shares_outstanding = (initial_shares_outstanding + self.shares_outstanding)/2
        self.earnings_per_share = self.net_income / (avg_shares_outstanding + additional_dilution)

