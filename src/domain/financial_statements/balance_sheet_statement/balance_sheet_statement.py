from dataclasses import dataclass

from src.domain.financial_statements.balance_sheet_statement.assets import Assets
from src.domain.financial_statements.balance_sheet_statement.shareholders_equity import ShareholdersEquity
from src.domain.financial_statements.balance_sheet_statement.liabilities import Liabilities
from src.domain.financial_statements.exceptions.balance_sheet_statement_exception import IsNotBalancedException


@dataclass
class BalanceSheetStatement:
    """The term balance sheet refers to a financial statement that reports a company's assets, liabilities,
    and shareholder equity at a specific point in time. Balance sheets provide the basis for computing rates of
    return for investors and evaluating a company's capital structure. """
    assets: Assets
    liabilities: Liabilities
    shareholders_equity: ShareholdersEquity

    def __post_init__(self):
        self.check_is_balanced()

    def total_liabilities_and_total_equity(self) -> int:
        """Liabilities plus owners' equity."""
        return self.liabilities.total_liabilities + self.shareholders_equity.total_shareholders_equity

    def check_is_balanced(self):
        """A balance sheet should always balance. Assets must always equal liabilities plus owners' equity."""
        if self.assets.total_assets != self.total_liabilities_and_total_equity():
            raise IsNotBalancedException(f"Balance sheet is not balanced. Assets must always equal liabilities plus "
                                         f"owners' equity.")

    @staticmethod
    def net_working_capital_1(total_current_assets: int, total_current_liabilities: int):
        """Broadest net working capital (NWC) calculation as it includes all accounts."""
        return total_current_assets - total_current_liabilities

    @staticmethod
    def net_working_capital_2(total_current_assets: int, cash: int, total_current_liabilities: int, debt: int):
        """Net working capital (NWC) calculation subtracting cash from total_current_assets and debt from
        total_current_liabilities."""
        return (total_current_assets - cash) - (total_current_liabilities - debt)

    @staticmethod
    def net_working_capital_3(accounts_receivables: int, inventory: int, accounts_payable: int,
                              other_working_capital: int = 0):
        """Narrowest net working capital (NWC) since it only includes few accounts (mainly three)."""
        return accounts_receivables + inventory - accounts_payable + other_working_capital
