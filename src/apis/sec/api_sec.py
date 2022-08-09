"""
Api SEC Class
It retrieves data from the U.S. Securities and Exchange Commission (SEC). For additional information
you can visit: https://www.sec.gov/edgar/sec-api-documentation
"""
import os
from typing import Union
from src.apis.api import Api
from src.apis.sec.company_concept_enum import CompanyConceptEnum
from src.apis.sec.validate_functions import _validate_company_tickers_exchange_response, \
    _validate_company_concept_response, _validate_company_facts_response


def _cik_to_ten_digits_str(cik: int):
    """Return an entity’s 10-digit Central Index Key (CIK), including leading zeros"""
    return str(cik).zfill(10)


class ApiSEC(Api):
    def __init__(self):
        super().__init__()
        self.headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": os.environ['SEC_USER_EMAIL'],
            "Host": "data.sec.gov"
        }

    def get_company_tickers_exchange(self):
        """This API returns all companies in SEC, where the fields are cik, name, ticker (symbol) and exchange."""
        url = 'https://www.sec.gov/files/company_tickers_exchange.json'
        company_tickers_exchange_data = self.call_api(url=url)
        _validate_company_tickers_exchange_response(company_tickers_exchange_response=company_tickers_exchange_data)
        return company_tickers_exchange_data

    def get_company_concept(self, company_concept: CompanyConceptEnum, cik: Union[int, str]):
        """The company-concept API returns all the XBRL disclosures from a single company (CIK) and concept (a
        taxonomy and tag) into a single JSON file, with a separate array of facts for each units on measure that the
        company has chosen to disclose (e.g. net profits reported in U.S. dollars and in Canadian dollars)."""
        url = f'https://data.sec.gov/api/xbrl/companyconcept/CIK{_cik_to_ten_digits_str(cik)}/' \
              f'{company_concept.get_taxonomy()}/{company_concept.get_concept()}.json'
        company_concept_data = self.call_api(url=url, headers=self.headers)
        _validate_company_concept_response(company_concept_response=company_concept_data)
        return company_concept_data

    def get_company_facts(self, cik: Union[int, str]):
        """This API returns all the company concepts data for a company into a single API call."""
        url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{_cik_to_ten_digits_str(cik)}.json'
        company_facts_data = self.call_api(url=url, headers=self.headers)
        _validate_company_facts_response(company_facts_response=company_facts_data)
        return company_facts_data
