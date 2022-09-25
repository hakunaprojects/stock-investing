import pytest

from src.domain.financial_statements.balance_sheet_statement.assets import Assets, CurrentAssets, NonCurrentAssets
from src.domain.financial_statements.balance_sheet_statement.balance_sheet_statement import BalanceSheetStatement
from src.domain.financial_statements.balance_sheet_statement.liabilities import CurrentLiabilities, \
    NonCurrentLiabilities, Liabilities
from src.domain.financial_statements.balance_sheet_statement.shareholders_equity import ShareholdersEquity
from src.domain.financial_statements.exceptions.balance_sheet_statement_exception import IsNotBalancedException


def build_assets():
    current_assets = CurrentAssets(
        cash_and_cash_equivalents=34940000000,
        short_term_investments=27699000000,
        net_receivables=51506000000,
        inventory=6580000000,
        other_current_assets=14111000000
    )

    non_current_assets = NonCurrentAssets(
        property_plant_equipmentNet=39440000000,
        goodwill=0,
        intangible_assets=0,
        long_term_investments=127877000000,
        tax_assets=0,
        other_non_current_assets=48849000000
    )

    return Assets(
        current_assets=current_assets,
        non_current_assets=non_current_assets)


def build_liabilities():
    current_liabilities = CurrentLiabilities(
        account_payables=54763000000,
        short_term_Debt=15613000000,
        tax_payables=0,
        deferred_revenue=7612000000,
        other_current_liabilities=47493000000
    )

    non_current_liabilities = NonCurrentLiabilities(
        long_term_debt=109106000000,
        deferred_revenue_non_current=0,
        deferred_tax_liabilities_non_current=0,
        other_non_current_liabilities=53325000000
    )

    return Liabilities(
        current_liabilities=current_liabilities,
        non_current_liabilities=non_current_liabilities,
        other_liabilities=0,
        capital_lease_obligations=0
    )


def build_shareholders_equity(alter_value=False):
    return ShareholdersEquity(
        preferred_Stock=0,
        common_stock=57365000000,
        retained_earnings=5562000000,
        accumulated_other_comprehensive_income_loss=163000000,
        other_total_stockholders_equity=0,
        minority_interest=(50 if alter_value else 0)
    )


class TestBalanceSheetStatement:

    def test_given_all_components_when_build_balance_sheet_object_then_it_should_be_balanced(self):
        BalanceSheetStatement(
            assets=build_assets(),
            liabilities=build_liabilities(),
            shareholders_equity=build_shareholders_equity()
        )

    def test_given_incorrect_components_when_build_balance_sheet_object_then_it_should_throw_exception(self):
        with pytest.raises(IsNotBalancedException) as exc_info:
            BalanceSheetStatement(
                assets=build_assets(),
                liabilities=build_liabilities(),
                shareholders_equity=build_shareholders_equity(alter_value=True)
            )
        # Asserts
        assert exc_info.value.code == 'ERROR.FINANCIAL_STATEMENTS.BALANCE_SHEET_STATEMENT'
        assert exc_info.value.message == ('Balance sheet is not balanced. Assets must always equal liabilities plus '
                                          "owners' equity.")

    def test_given_variables_when_call_net_working_capital_1_then_it_should_be_calculated(self):
        net_working_capital_1 = BalanceSheetStatement.net_working_capital_1(
            total_current_assets=134836000000,
            total_current_liabilities=125481000000
        )
        expected_net_working_capital_1 = 9355000000
        # Asserts
        assert net_working_capital_1 == expected_net_working_capital_1

    def test_given_variables_when_call_net_working_capital_2_then_it_should_be_calculated(self):
        net_working_capital_2 = BalanceSheetStatement.net_working_capital_2(
            total_current_assets=134836000000,
            cash=34940000000,
            total_current_liabilities=125481000000,
            debt=35040000000
        )
        expected_net_working_capital_2 = 9455000000
        # Asserts
        assert net_working_capital_2 == expected_net_working_capital_2

    def test_given_variables_when_call_net_working_capital_3_then_it_should_be_calculated(self):
        net_working_capital_3 = BalanceSheetStatement.net_working_capital_3(
            accounts_receivables=51506000000,
            inventory=6580000000,
            accounts_payable=54763000000,
            other_working_capital=0
        )
        expected_net_working_capital_3 = 3323000000
        # Asserts
        assert net_working_capital_3 == expected_net_working_capital_3
