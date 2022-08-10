"""
Api Financial Modeling Prep Class
Main Enum where the different Enums inherit from this to use the different functions.
"""
from src.apis.api import Api
from src.apis.financial_modeling_prep.financial_modeling_prep_enum import FinancialModelingPrepEnum
import os


class ApiFinancialModelingPrep(Api):
    def __init__(self):
        super().__init__()
        self.api_key = os.environ['FINANCIAL_MODELING_PREP_API_KEY']

    def get_stock_fundamentals(self, symbol: str,
                               fundamental: FinancialModelingPrepEnum):
        """This API returns the stock fundamentals given a path_concept, symbol and api_key."""
        url = f'https://financialmodelingprep.com/api/v3/{fundamental.get_path_concept()}/' \
              f'{symbol}?apikey={self.api_key}'
        stock_fundamental = self.call_api(url=url)
        fundamental.get_validate_data(data_to_validate=stock_fundamental)
        return stock_fundamental
