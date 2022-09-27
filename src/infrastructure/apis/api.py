"""
Api Request Class
Main Api class where the different APIs inherit from this.
"""
import json
import time
from datetime import datetime
from typing import Dict, Optional

import requests

from src.exceptions.api_request_exception import NotValidUrlException, NonJsonDataFoundException


class Api:
    """Main Api Class to inherit from other apis"""

    def __init__(self):
        self.last_call = None

    def call_api(self, url: str, delay: bool = True, headers: Dict[str, str] = None) -> Optional[Dict]:
        """Receive the content of ``url``, parse it as JSON and return the object."""
        # Add delay if necessary
        if delay:
            self.delay()
        # Get response
        response = requests.get(url=url, headers=headers)
        # Check status response and raise exceptions if necessary
        if response.status_code == 200:
            self.last_call = datetime.now()
            try:
                return json.loads(response.text)
            except Exception as exception:
                raise NonJsonDataFoundException(f"The response from ``{url}`` is not a valid json") from exception
        elif response.status_code == 404:
            raise NotValidUrlException(f"Url ``{url}`` not found.")
        else:
            raise NotValidUrlException(f"Error when requests url ``{url}``. Response: {response.__dict__}")

    def delay(self) -> None:
        """Subroutine to delay between successive calls to a data source url like SEC or fin mod prep, if needed.
        The purpose is to use these resources respectfully."""
        if self.last_call:
            elapsed_time = datetime.now() - self.last_call
            elapsed_sec = elapsed_time.seconds + elapsed_time.microseconds / 1000000
            if elapsed_sec < 1.0:
                add_delay = 1.0 - elapsed_sec
                time.sleep(add_delay)
