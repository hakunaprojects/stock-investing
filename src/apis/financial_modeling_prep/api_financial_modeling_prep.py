"""
Api Financial Modeling Prep Class
It retrieves data from a third party provider who gets the information from the U.S. Securities and Exchange Commission
(SEC). For additional information you can visit: https://site.financialmodelingprep.com/developer/docs/
"""
import os

from src.apis.api import Api
from src.apis.financial_modeling_prep.financial_modeling_prep_enum import FinancialModelingPrepEnum


class ApiFinancialModelingPrep(Api):
    """Api to retrieve data from financial modeling prep. It is required an api key."""

    def __init__(self, api_key=None):
        super().__init__()
        self.api_key = api_key if api_key else os.environ['FINANCIAL_MODELING_PREP_API_KEY']

    def get_stock_fundamentals(self, symbol: str,
                               fundamental: FinancialModelingPrepEnum):
        """This API returns the stock fundamentals given a path_concept, symbol and api_key."""
        url = f'https://financialmodelingprep.com/api/v3/{fundamental.get_path_concept()}/' \
              f'{symbol}?apikey={self.api_key}'
        stock_fundamental = self.call_api(url=url)
        fundamental.get_validate_data(data_to_validate=stock_fundamental)
        return stock_fundamental
