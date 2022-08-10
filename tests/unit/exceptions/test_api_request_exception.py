import pytest
from datetime import date
from src.exceptions.api_request_exception import NotValidUrlException, NonJsonDataFoundException, \
    NotValidSchemaException

API_REQUEST_EXCEPTIONS = [{'exception': NotValidUrlException, 'message': 'Not valid url'},
                          {'exception': NonJsonDataFoundException, 'message': 'Non json data found'},
                          {'exception': NotValidSchemaException, 'message': 'Not valid schema'}]
TODAY = date.today()


def test_given_request_exceptions_when_raising_then_throw_exception_with_its_code_message_and_timestamp():
    for api_request_exception in API_REQUEST_EXCEPTIONS:
        # Retrieve data from the item
        exception = api_request_exception.get('exception')
        message = api_request_exception.get('message')
        # Raises the exception
        with pytest.raises(exception) as exc_info:
            raise exception(message)
        # Asserts
        assert exc_info.value.code == 'ERROR.API_REQUEST'
        assert exc_info.value.message == message
        assert exc_info.value.timestamp.date() == TODAY
