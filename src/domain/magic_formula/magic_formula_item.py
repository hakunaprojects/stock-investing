from dataclasses import dataclass
from typing import Optional


@dataclass
class MagicFormulaItem:
    """MagicFormulaItem is used for applying effectively the magic formula class, only storing the necessary data to
    rank the items (companies)."""

    ticker: str
    return_on_capital: float
    earnings_yield: float
    ranking_return_on_capital: Optional[int] = None
    ranking_earnings_yield: Optional[int] = None
    ranking_sum_factors: Optional[int] = None
    ranking_position: Optional[int] = None
