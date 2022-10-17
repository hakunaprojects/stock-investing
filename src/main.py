"""
Main Module
"""
from src.infrastructure.apis.financial_modeling_prep.api_financial_modeling_prep import (
    ApiFinancialModelingPrep,
)
from src.infrastructure.apis.financial_modeling_prep.financial_statements.financial_statements_enum import (
    FinancialStatementsEnum,
)
from src.infrastructure.apis.financial_modeling_prep.fundamentals_analysis.fundamentals_analysis_enum import (
    FundamentalsAnalysisEnum,
)
from src.infrastructure.apis.sec.api_sec import ApiSEC
from src.infrastructure.apis.sec.company_concept_enum import CompanyConceptEnum


def print_api_sec_responses():
    """
    Temporal test to print api sec responses
    """
    api_sec = ApiSEC()
    print(api_sec.get_company_tickers_exchange())
    print(
        api_sec.get_company_concept(
            company_concept=CompanyConceptEnum.EARNINGS_PER_SHARE_DILUTED, cik=1318605
        )
    )
    print(api_sec.get_company_facts(cik=1318605))
    print(api_sec.get_submissions(cik=1318605))


def print_api_financial_modeling_prep_responses():
    """
    Temporal test to print api financial modeling prep
    """
    api_financial_modeling_prep = ApiFinancialModelingPrep()
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL", fundamental=FinancialStatementsEnum.INCOME_STATEMENT
        )
    )
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL", fundamental=FinancialStatementsEnum.BALANCE_SHEET_STATEMENT
        )
    )
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL", fundamental=FinancialStatementsEnum.CASH_FLOW_STATEMENT
        )
    )
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL",
            fundamental=FundamentalsAnalysisEnum.COMPANY_KEY_METRICS_SCHEMA,
        )
    )
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL", fundamental=FundamentalsAnalysisEnum.COMPANY_FINANCIAL_GROWTH
        )
    )
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL", fundamental=FundamentalsAnalysisEnum.COMPANY_FINANCIAL_RATIOS
        )
    )
    print(
        api_financial_modeling_prep.get_stock_fundamentals(
            symbol="AAPL", fundamental=FundamentalsAnalysisEnum.INCOME_STATEMENT_GROWTH
        )
    )


if __name__ == "__main__":
    print_api_sec_responses()
    print_api_financial_modeling_prep_responses()
