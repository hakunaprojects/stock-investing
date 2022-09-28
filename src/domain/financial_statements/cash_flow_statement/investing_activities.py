from dataclasses import dataclass, field

from src.shared.general_functions import sum_all_initialized_int_attributes


@dataclass
class InvestingActivities:
    """Cash flow from investing activities (CFI) reports how much cash has been generated or spent from various
    investment-related activities in a specific period. Investing activities include purchases of physical assets,
    investments in securities, or the sale of securities or assets. """
    investments_in_property_plant_and_equipment: int
    acquisitions_net: int
    purchases_of_investments: int
    sales_maturities_of_investments: int
    other_investing_activities: int
    net_cash_used_for_investing_activities: int = field(init=False)

    def __post_init__(self):
        self.net_cash_used_for_investing_activities = sum_all_initialized_int_attributes(self)
