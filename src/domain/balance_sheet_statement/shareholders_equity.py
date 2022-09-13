from dataclasses import dataclass


@dataclass
class ShareholdersEquity:
    preferred_Stock: int
    common_stock: int
    retained_earnings: int
    accumulated_other_comprehensive_income_loss: int
    other_total_stockholders_equity: int
    total_stockholders_equity: int
    minority_interest: int
    total_shareholders_equity: int
