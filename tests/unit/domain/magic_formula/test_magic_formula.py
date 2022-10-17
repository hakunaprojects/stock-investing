from src.domain.magic_formula.magic_formula import MagicFormula


# TODO Redo and add more testing
class TestMagicFormula:
    class MagicFormulaImplementation(MagicFormula):
        def get_total_assets(self, **kwargs) -> int:
            return 1000

        def get_total_current_assets(self, **kwargs) -> int:
            return 1000

        def get_excess_cash(self, **kwargs) -> int:
            return 1000

        def get_accounts_payable(self, **kwargs) -> int:
            return 1000

        def get_intangibles(self, **kwargs) -> int:
            return 1000

        def get_goodwill(self, **kwargs) -> int:
            return 1000

        def get_long_term_debt(self, **kwargs) -> int:
            return 1000

        def get_total_current_liabilities(self, **kwargs) -> int:
            return 1000

        def get_market_capitalization(self, **kwargs) -> int:
            return 1000

        def get_cash(self, **kwargs) -> int:
            return 1000

        def get_ebitda(self, **kwargs) -> int:
            return 1000

        def get_maintenance_capex(self, **kwargs) -> float:
            return 0

    def test_given_all_components_when_build_balance_sheet_object_then_it_should_be_balanced(
        self,
    ):
        magic_formula = self.MagicFormulaImplementation()
        magic_formula.execute(tickers=["APPL"])
