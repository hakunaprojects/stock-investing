import json
import os
import unittest
from typing import Callable
from unittest import mock
from unittest.mock import patch

from src.apis.sec.api_sec import ApiSEC
from src.apis.sec.company_concept_enum import CompanyConceptEnum
from tests.unit.apis.test_api import mock_response

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_json_file(file_name: str):
    return json.dumps(json.load(open(f'{CURRENT_FOLDER}/fixtures/{file_name}.json')))


class TestApiSec(unittest.TestCase):
    def test_given_get_company_tickers_exchange_response_when_call_method_then_validate_and_return_json(self):
        # Prepare api_sec_method to be called
        def get_company_tickers_exchange_method():
            return ApiSEC().get_company_tickers_exchange()

        # Build mock, call method and assert response
        self.given_json_response_when_call_api_sec_method_then_validate_and_return_json(
            api_sec_method=get_company_tickers_exchange_method,
            json_file_path='company_tickers_exchange_response'
        )

    def test_given_company_facts_response_when_call_method_then_validate_and_return_json(self):
        # Prepare api_sec_method to be called
        def get_company_facts_method():
            return ApiSEC().get_company_facts(cik=1318605)

        # Build mock, call method and assert response
        self.given_json_response_when_call_api_sec_method_then_validate_and_return_json(
            api_sec_method=get_company_facts_method,
            json_file_path='company_facts_response'
        )

    def test_given_submissions_response_when_call_method_then_validate_and_return_json(self):
        # Prepare api_sec_method to be called
        def get_submissions_method():
            return ApiSEC().get_submissions(cik=1318605)

        # Build mock, call method and assert response
        self.given_json_response_when_call_api_sec_method_then_validate_and_return_json(
            api_sec_method=get_submissions_method,
            json_file_path='submissions_response'
        )

    def test_given_company_concepts_enum_and_responses_when_call_method_then_validate_and_return_jsons(self):
        company_concept_list = list(CompanyConceptEnum)
        for company_concept_enum in company_concept_list:
            # Prepare api_sec_method to be called
            def get_company_concept_method(company_concept):
                return ApiSEC().get_company_concept(company_concept=company_concept, cik=1318605)

            # Build mock, call method and assert response
            self.given_json_response_when_call_api_sec_method_then_validate_and_return_json(
                api_sec_method=get_company_concept_method,
                json_file_path='company_concepts_response',
                company_concept=company_concept_enum
            )

    @mock.patch.dict(os.environ, {'SEC_USER_EMAIL': 'fake_email@gmail.com'})
    @patch('src.apis.api.requests')
    def given_json_response_when_call_api_sec_method_then_validate_and_return_json(self, mock_requests,
                                                                                   api_sec_method: Callable,
                                                                                   json_file_path: str,
                                                                                   company_concept: CompanyConceptEnum = None):
        # Specify the return value of the get() method
        mocked_response = mock_response(status_code=200,
                                        text=get_json_file(json_file_path))
        mock_requests.get.return_value = mocked_response
        # Call the method
        response = api_sec_method(company_concept) if company_concept else api_sec_method()
        # Asserts
        expected_response = json.loads(mocked_response.text)
        self.assertEqual(expected_response, response)
