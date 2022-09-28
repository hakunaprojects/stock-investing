import json
import os
from unittest.mock import patch

import pytest

from src.infrastructure.apis.financial_modeling_prep.api_financial_modeling_prep import ApiFinancialModelingPrep
from src.infrastructure.apis.financial_modeling_prep.financial_modeling_prep_enum import FinancialModelingPrepEnum
from src.infrastructure.apis.financial_modeling_prep.financial_statements.financial_statements_enum import FinancialStatementsEnum
from src.infrastructure.apis.financial_modeling_prep.fundamentals_analysis.fundamentals_analysis_enum import FundamentalsAnalysisEnum
from tests.unit.apis.test_api import mock_response

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

FINANCIAL_STATEMENTS_JSON_FILES = [
    {'concept': 'CompanyBalanceSheetStatement', 'file_name': 'company_balance_sheet_statement_response'},
    {'concept': 'CompanyIncomeStatement', 'file_name': 'company_income_statement_statement_response'},
    {'concept': 'CompanyCashFlowStatement', 'file_name': 'company_cash_flow_statement_response'}]

FUNDAMENTALS_ANALYSIS_JSON_FILES = [
    {'concept': 'CompanyFinancialRatios', 'file_name': 'company_financial_ratios_response'},
    {'concept': 'CompanyFinancialGrowth', 'file_name': 'company_financial_growth_response'},
    {'concept': 'CompanyIncomeStatementGrowth', 'file_name': 'company_income_statement_growth_response'},
    {'concept': 'CompanyKeyMetrics', 'file_name': 'company_key_metrics_response'}]


def get_json_file(file_name: str, file_directory: str):
    return json.dumps(json.load(open(f'{CURRENT_FOLDER}/fixtures/{file_directory}/{file_name}.json')))


class TestApiFinancialModelingPrep:
    api = ApiFinancialModelingPrep(api_key='65753465454843')

    @pytest.mark.parametrize("enum", list(FinancialStatementsEnum))
    def test_given_financial_statements_enum_and_responses_when_call_method_then_validate_and_return_jsons(self,
                                                                                                           enum: FinancialStatementsEnum):
        json_file = [json_file.get('file_name') for json_file in FINANCIAL_STATEMENTS_JSON_FILES if
                     enum.get_concept() == json_file.get('concept')][0]
        # Build mock, call method and assert response
        self._given_json_response_when_call_api_method_then_validate_and_return_json(
            json_file_name=json_file,
            file_directory='financial_statements',
            symbol='AAPL',
            fundamental=enum)

    @pytest.mark.parametrize("enum", list(FundamentalsAnalysisEnum))
    def test_given_fundamental_analysis_enum_and_responses_when_call_method_then_validate_and_return_jsons(self,
                                                                                                           enum: FundamentalsAnalysisEnum):
        json_file = [json_file.get('file_name') for json_file in FUNDAMENTALS_ANALYSIS_JSON_FILES if
                     enum.get_concept() == json_file.get('concept')][0]
        # Build mock, call method and assert response
        self._given_json_response_when_call_api_method_then_validate_and_return_json(
            json_file_name=json_file,
            file_directory='fundamentals_analysis',
            symbol='AAPL',
            fundamental=enum)

    @patch('src.infrastructure.apis.api.requests')
    def _given_json_response_when_call_api_method_then_validate_and_return_json(self, mock_requests,
                                                                                json_file_name: str,
                                                                                file_directory: str,
                                                                                symbol: str,
                                                                                fundamental: FinancialModelingPrepEnum):
        # Specify the return value of the get() method
        mocked_response = mock_response(status_code=200,
                                        text=get_json_file(file_name=json_file_name,
                                                           file_directory=file_directory))
        mock_requests.get.return_value = mocked_response
        # Call the method
        response = self.api.get_stock_fundamentals(symbol=symbol, fundamental=fundamental)
        # Asserts
        expected_response = json.loads(mocked_response.text)
        assert expected_response == response
