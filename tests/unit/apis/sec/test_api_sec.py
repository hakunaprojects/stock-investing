import json
import os
from typing import Callable
from unittest.mock import patch

import pytest

from src.infrastructure.apis.sec.api_sec import ApiSEC
from src.infrastructure.apis.sec.company_concept_enum import CompanyConceptEnum
from tests.unit.apis.test_api import mock_response

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_json_file(file_name: str):
    return json.dumps(json.load(open(f'{CURRENT_FOLDER}/fixtures/{file_name}.json')))


class TestApiSec:
    api = ApiSEC(user_email='fake_email@gmail.com')

    def test_given_get_company_tickers_exchange_response_when_call_method_then_validate_and_return_json(self):
        # Prepare api_sec_method to be called
        def get_company_tickers_exchange_method(api_sec: ApiSEC):
            return api_sec.get_company_tickers_exchange()

        # Build mock, call method and assert response
        self._given_json_response_when_call_api_method_then_validate_and_return_json(
            api_method=get_company_tickers_exchange_method,
            json_file_path='company_tickers_exchange_response'
        )

    def test_given_company_facts_response_when_call_method_then_validate_and_return_json(self):
        # Prepare api_sec_method to be called
        def get_company_facts_method(api_sec: ApiSEC):
            return api_sec.get_company_facts(cik=1318605)

        # Build mock, call method and assert response
        self._given_json_response_when_call_api_method_then_validate_and_return_json(
            api_method=get_company_facts_method,
            json_file_path='company_facts_response'
        )

    def test_given_submissions_response_when_call_method_then_validate_and_return_json(self):
        # Prepare api_sec_method to be called
        def get_submissions_method(api_sec: ApiSEC):
            return api_sec.get_submissions(cik=1318605)

        # Build mock, call method and assert response
        self._given_json_response_when_call_api_method_then_validate_and_return_json(
            api_method=get_submissions_method,
            json_file_path='submissions_response'
        )

    @pytest.mark.parametrize("company_concept_enum", list(CompanyConceptEnum))
    def test_given_company_concepts_enum_and_responses_when_call_method_then_validate_and_return_jsons(self,
                                                                                                       company_concept_enum):
        # Prepare api_sec_method to be called
        def get_company_concept_method(api_sec: ApiSEC, company_concept: CompanyConceptEnum):
            return api_sec.get_company_concept(company_concept=company_concept, cik=1318605)

        # Build mock, call method and assert response
        self._given_json_response_when_call_api_method_then_validate_and_return_json(
            api_method=get_company_concept_method,
            json_file_path='company_concepts_response',
            company_concept=company_concept_enum
        )

    @patch('src.infrastructure.apis.api.requests')
    def _given_json_response_when_call_api_method_then_validate_and_return_json(self, mock_requests,
                                                                                api_method: Callable,
                                                                                json_file_path: str,
                                                                                company_concept: CompanyConceptEnum = None):
        # Specify the return value of the get() method
        mocked_response = mock_response(status_code=200,
                                        text=get_json_file(json_file_path))
        mock_requests.get.return_value = mocked_response
        # Call the method
        if company_concept:
            response = api_method(api_sec=self.api, company_concept=company_concept)
        else:
            response = api_method(api_sec=self.api)
        # Asserts
        expected_response = json.loads(mocked_response.text)
        assert expected_response == response
