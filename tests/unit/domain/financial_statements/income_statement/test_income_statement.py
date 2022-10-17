from src.domain.financial_statements.income_statement.income_statement import (
    IncomeStatement,
)
from src.domain.financial_statements.income_statement.non_operating_section import (
    NonOperatingSection,
)
from src.domain.financial_statements.income_statement.operating_section import (
    OperatingExpensesSection,
    OperatingRevenueSection,
    OperatingSection,
)


def build_operating_section():
    operating_revenue_section = OperatingRevenueSection(
        revenue=365817000000, cost_of_revenue=212981000000
    )

    operating_expenses_section = OperatingExpensesSection(
        research_and_development_expenses=21914000000,
        general_and_administrative_expenses=0,
        selling_and_marketing_expenses=0,
        selling_general_and_administrative_Expenses=21973000000,
        other_operating_expenses=0,
    )

    return OperatingSection(
        operating_revenue_section=operating_revenue_section,
        operating_expenses_section=operating_expenses_section,
        depreciation_and_amortization_expense=11284000000,
    )


def build_non_operating_section():
    return NonOperatingSection(
        interest_income=2843000000,
        interest_expense=2645000000,
        other_non_operating_income=0,
        other_non_operating_expenses=258000000,
    )


class TestIncomeStatement:
    def test_given_all_components_when_build_income_statement_object_then_it_should_be_built_as_expected(
        self,
    ):
        income_statement = IncomeStatement(
            operating_section=build_operating_section(),
            non_operating_section=build_non_operating_section(),
            income_before_tax=109207000000,
            income_tax_expense=14527000000,
            shares_outstanding=16701272000,
            earnings_per_share=5.67,
            earnings_per_share_diluted=5.61,
        )
        expected_gross_profit = 152836000000
        expected_total_operating_expenses = 43887000000
        expected_income_before_tax = 109207000000
        expected_net_income = 94680000000

        # Asserts
        assert (
            income_statement.operating_section.operating_revenue_section.gross_profit
            == expected_gross_profit
        )
        assert (
            income_statement.operating_section.operating_expenses_section.total_operating_expenses
            == expected_total_operating_expenses
        )
        assert income_statement.income_before_tax == expected_income_before_tax
        assert income_statement.net_income == expected_net_income

    def test_given_variables_when_call_earnings_per_share_then_it_should_be_calculated(
        self,
    ):
        income_statement = IncomeStatement(
            operating_section=build_operating_section(),
            non_operating_section=build_non_operating_section(),
            income_before_tax=109207000000,
            income_tax_expense=14527000000,
            shares_outstanding=2000,
        )
        income_statement.calculate_earnings_per_share(initial_shares_outstanding=1000)
        expected_net_income = 94680000000
        expected_earnings_per_share = 63120000

        # Asserts
        assert income_statement.net_income == expected_net_income
        assert income_statement.earnings_per_share == expected_earnings_per_share

    def test_given_variables_when_call_earnings_per_share_diluted_then_it_should_be_calculated(
        self,
    ):
        income_statement = IncomeStatement(
            operating_section=build_operating_section(),
            non_operating_section=build_non_operating_section(),
            income_before_tax=109207000000,
            income_tax_expense=14527000000,
            shares_outstanding=2000,
        )
        income_statement.calculate_earnings_per_share_diluted(
            initial_shares_outstanding=1000, additional_dilution=500
        )
        expected_net_income = 94680000000
        expected_earnings_per_share_diluted = 47340000

        # Asserts
        assert income_statement.net_income == expected_net_income
        assert (
            income_statement.earnings_per_share_diluted
            == expected_earnings_per_share_diluted
        )
