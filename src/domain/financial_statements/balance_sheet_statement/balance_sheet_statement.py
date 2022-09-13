from dataclasses import dataclass

from src.domain.financial_statements.balance_sheet_statement.assets import Assets
from src.domain.financial_statements.balance_sheet_statement.shareholders_equity import ShareholdersEquity
from src.domain.financial_statements.balance_sheet_statement.liabilities import Liabilities


@dataclass
class BalanceSheetStatement:
    """The term balance sheet refers to a financial statement that reports a company's assets, liabilities,
    and shareholder equity at a specific point in time. Balance sheets provide the basis for computing rates of
    return for investors and evaluating a company's capital structure. """
    assets: Assets
    liabilities: Liabilities
    shareholders_equity: ShareholdersEquity

    def total_liabilities_and_total_equity(self) -> int:
        """Liabilities plus owners' equity."""
        return self.liabilities.total_liabilities + self.shareholders_equity.total_shareholders_equity

    def is_balanced(self) -> bool:
        """A balance sheet should always balance. Assets must always equal liabilities plus owners' equity."""
        return self.assets.total_assets == self.total_liabilities_and_total_equity
