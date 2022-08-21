"""
Api SEC Class
It retrieves data from the U.S. Securities and Exchange Commission (SEC). For additional information
you can visit: https://www.sec.gov/edgar/sec-api-documentation
"""
import os
from typing import Union

from jsonschema.validators import validate

from src.apis.api import Api
from src.apis.sec.company_concept_enum import CompanyConceptEnum
from src.apis.sec.schemas.sec_schemas import SUBMISSIONS_SCHEMA, COMPANY_CONCEPT_SCHEMA, COMPANY_FACTS_SCHEMA, \
    COMPANY_TICKERS_EXCHANGE_SCHEMA


def _cik_to_ten_digits_str(cik: int):
    """Return an entity’s 10-digit Central Index Key (CIK), including leading zeros"""
    return str(cik).zfill(10)


class ApiSEC(Api):
    """Api to retrieve data from financial modeling prep. For some requests is required an email."""

    def __init__(self, user_email=None):
        super().__init__()
        self.headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": user_email if user_email else os.environ['SEC_USER_EMAIL'],
            "Host": "data.sec.gov"
        }

    def get_company_tickers_exchange(self):
        """This API returns all companies in SEC, where the fields are cik, name, ticker (symbol) and exchange."""
        url = 'https://www.sec.gov/files/company_tickers_exchange.json'
        company_tickers_exchange_data = self.call_api(url=url)
        validate(instance=company_tickers_exchange_data, schema=COMPANY_TICKERS_EXCHANGE_SCHEMA)
        return company_tickers_exchange_data

    def get_company_concept(self, company_concept: CompanyConceptEnum, cik: Union[int, str]):
        """The company-concept API returns all the XBRL disclosures from a single company (CIK) and concept (a
        taxonomy and tag) into a single JSON file, with a separate array of facts for each units on measure that the
        company has chosen to disclose."""
        url = f'https://data.sec.gov/api/xbrl/companyconcept/CIK{_cik_to_ten_digits_str(cik)}/' \
              f'{company_concept.get_taxonomy()}/{company_concept.get_concept()}.json'
        company_concept_data = self.call_api(url=url, headers=self.headers)
        validate(instance=company_concept_data, schema=COMPANY_CONCEPT_SCHEMA)
        return company_concept_data

    def get_company_facts(self, cik: Union[int, str]):
        """This API returns all the company concepts data for a company into a single API call."""
        url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{_cik_to_ten_digits_str(cik)}.json'
        company_facts_data = self.call_api(url=url, headers=self.headers)
        validate(instance=company_facts_data, schema=COMPANY_FACTS_SCHEMA)
        return company_facts_data

    def get_submissions(self, cik: Union[int, str]):
        """This API returns all the company concepts data for a company into a single API call."""
        url = f'https://data.sec.gov/submissions/CIK{_cik_to_ten_digits_str(cik)}.json'
        submissions_data = self.call_api(url=url, headers=self.headers)
        validate(instance=submissions_data, schema=SUBMISSIONS_SCHEMA)
        return submissions_data
