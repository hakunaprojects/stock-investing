import json
import pytest
import unittest
from unittest.mock import patch, MagicMock
from src.apis.api import Api
from src.exceptions.api_request_exception import NotValidUrlException


def mock_response(status_code: int, text: str = None) -> MagicMock:
    mock = MagicMock()
    mock.status_code = status_code
    mock.text = text
    return mock


class TestApi(unittest.TestCase):
    @patch('src.apis.api.requests')
    def test_given_response_when_call_api_then_return_valid_json(self, mock_requests):
        # Specify the return value of the get() method
        mocked_response = mock_response(status_code=200,
                                        text='{ "name":"John", "age":30, "city":"New York"}')
        mock_requests.get.return_value = mocked_response
        # Call the api
        api = Api()
        response = api.call_api(url="https://fake_url_1.com")
        # Asserts
        expected_response = json.loads(mocked_response.text)
        self.assertEqual(expected_response, response)

    @patch('src.apis.api.requests')
    def test_given_response_with_status_404_when_call_api_then_throw_exception(self, mock_requests):
        # Specify the return value of the get() method
        mocked_response = mock_response(status_code=404)
        mock_requests.get.return_value = mocked_response
        # Call the api
        with pytest.raises(NotValidUrlException) as exc_info:
            api = Api()
            api.call_api(url="https://fake_url_2.com")
        # Asserts
        self.assertEqual('ERROR.API_REQUEST', exc_info.value.code)
        self.assertEqual('Url ``https://fake_url.com`` not found.', exc_info.value.message)

    @patch('src.apis.api.requests')
    def test_given_response_with_status_500_when_call_api_then_throw_exception(self, mock_requests):
        # Specify the return value of the get() method
        mocked_response = mock_response(status_code=500)
        mock_requests.get.return_value = mocked_response
        # Call the api
        with pytest.raises(NotValidUrlException) as exc_info:
            api = Api()
            api.call_api(url="https://fake_url_3.com")
        # Asserts
        self.assertEqual('ERROR.API_REQUEST', exc_info.value.code)
        self.assertRegex(exc_info.value.message, r'^Error when requests url ``https://fake_url.com``. Response:')
