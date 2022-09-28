import pytest

from src.domain.financial_statements.cash_flow_statement.cash_flow_statement import CashFlowStatement
from src.domain.financial_statements.cash_flow_statement.financing_activities import FinancingActivities
from src.domain.financial_statements.cash_flow_statement.investing_activities import InvestingActivities
from src.domain.financial_statements.cash_flow_statement.operating_activities import OperatingActivities
from src.domain.financial_statements.exceptions.cash_flow_statement_exception import NotFoundCapitalExpenditureException

operating_activities = OperatingActivities(
    net_income=94680000000,
    depreciation=11284000000,
    amortization=0,
    deferred_income_tax=-4774000000,
    stock_based_compensation=7906000000,
    change_in_working_capital=-4911000000,
    other_non_cash_items=-147000000,
    net_cash_provided_by_operating_activities=104038000000
)

investing_activities = InvestingActivities(
    investments_in_property_plant_and_equipment=-11085000000,
    acquisitions_net=-33000000,
    purchases_of_investments=-109689000000,
    sales_maturities_of_investments=106870000000,
    other_investing_activities=-608000000
)

financing_activities = FinancingActivities(
    debt_repayment=-8750000000,
    common_stock_issued=1105000000,
    common_stock_repurchased=-85971000000,
    dividends_paid=-14467000000,
    other_financing_activities=14730000000
)


class TestCashFlowStatement:

    def test_given_components_when_build_cash_flow_then_it_should_be_built_as_expected(self):
        cash_flow_statement = CashFlowStatement(
            operating_activities=operating_activities,
            investing_activities=investing_activities,
            financing_activities=financing_activities,
            cash_at_beginning_of_period=39789000000,
            capital_expenditure=2000000,
            free_cash_flow=0
        )
        expected_net_cash_provided_by_operating_activities = 104038000000
        expected_net_cash_provided_by_investing_activities = -14545000000
        expected_net_cash_provided_by_financing_activities = -93353000000
        expected_net_change_in_cash_flow = -3860000000
        expected_cash_at_end_of_period = 35929000000
        # Asserts
        assert cash_flow_statement.operating_activities.net_cash_provided_by_operating_activities == expected_net_cash_provided_by_operating_activities
        assert cash_flow_statement.investing_activities.net_cash_used_for_investing_activities == expected_net_cash_provided_by_investing_activities
        assert cash_flow_statement.financing_activities.net_cash_used_provided_by_financing_activities == expected_net_cash_provided_by_financing_activities
        assert cash_flow_statement.net_change_in_cash_flow == expected_net_change_in_cash_flow
        assert cash_flow_statement.cash_at_end_of_period == expected_cash_at_end_of_period

    def test_given_variables_when_calculate_capital_expenditure_then_it_should_be_calculated(self):
        cash_flow_statement = CashFlowStatement(
            operating_activities=operating_activities,
            investing_activities=investing_activities,
            financing_activities=financing_activities,
            cash_at_beginning_of_period=39789000000
        )
        cash_flow_statement.calculate_capital_expenditure(previous_year_investments_in_property_plant_and_equipment=0)
        expected_capital_expenditure = 199000000

        # Asserts
        assert cash_flow_statement.capital_expenditure == expected_capital_expenditure

    def test_given_no_capital_expenditure_when_calculate_free_cash_flow_then_it_should_throw_an_exception(self):
        with pytest.raises(NotFoundCapitalExpenditureException) as exc_info:
            cash_flow_statement = CashFlowStatement(
                operating_activities=operating_activities,
                investing_activities=investing_activities,
                financing_activities=financing_activities,
                cash_at_beginning_of_period=39789000000
            )
            cash_flow_statement.calculate_free_cash_flow(interest_expense=0, tax_shield=0)

        # Asserts
        assert exc_info.value.code == 'ERROR.FINANCIAL_STATEMENTS.CASH_FLOW_STATEMENT'
        assert exc_info.value.message == 'Capital Expenditure (Capex) is required to calculate the free cash flow.' != (
            'Balance sheet is not balanced. Assets must always equal liabilities plus '
            "owners' equity.")

    def test_given_variables_when_calculate_free_cash_flow_then_it_should_be_calculated(self):
        cash_flow_statement = CashFlowStatement(
            operating_activities=operating_activities,
            investing_activities=investing_activities,
            financing_activities=financing_activities,
            cash_at_beginning_of_period=39789000000,
            capital_expenditure=199000000
        )
        cash_flow_statement.calculate_free_cash_flow(interest_expense=0, tax_shield=0)
        expected_free_cash_flow = 103839000000

        # Asserts
        assert cash_flow_statement.free_cash_flow == expected_free_cash_flow
