from dataclasses import dataclass, field
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

    def __post_init__(self):
        self.income_before_tax = \
            self.operating_section.operating_income + \
            self.non_operating_section.non_operating_income
        self.net_income = self.income_before_tax - self.income_tax_expense
