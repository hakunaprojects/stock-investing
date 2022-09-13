from dataclasses import dataclass

from src.domain.balance_sheet_statement.assets import Assets
from src.domain.balance_sheet_statement.shareholders_equity import ShareholdersEquity
from src.domain.balance_sheet_statement.liabilities import Liabilities


@dataclass
class BalanceSheetStatement:
    assets: Assets
    liabilities: Liabilities
    shareholders_equity: ShareholdersEquity

    def total_liabilities_and_total_equity(self):
        return self.liabilities.total_liabilities + self.shareholders_equity.total_shareholders_equity
