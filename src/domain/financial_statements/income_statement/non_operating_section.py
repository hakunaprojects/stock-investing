from dataclasses import dataclass, field


@dataclass
class NonOperatingSection:
    """Revenue realized through secondary, non-core business activities is often referred to as non-operating,
    recurring revenue. This revenue is sourced from the earnings that are outside the purchase and sale of goods and
    services and may include income from interest earned on business capital parked in the bank, rental income from
    business property, income from strategic partnerships like royalty payment receipts, or income from an
    advertisement display placed on business property. Also, there are all expenses linked to non-core business
    activities, like interest paid on loan money."""

    interest_income: int
    interest_expense: int
    other_non_operating_income: int
    other_non_operating_expenses: int
    non_operating_income: int = field(init=False)

    def __post_init__(self):
        self.non_operating_income = (
            self.interest_income
            - self.interest_expense
            + self.other_non_operating_income
            - self.other_non_operating_expenses
        )
