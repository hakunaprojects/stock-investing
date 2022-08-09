"""
Financial Modeling Prep Enum
It retrieves data from a third party provider who gets the information from the U.S. Securities and Exchange Commission
(SEC). For additional information you can visit: https://site.financialmodelingprep.com/developer/docs/
"""
from enum import Enum
from jsonschema.validators import validate


class FinancialModelingPrepEnum(Enum):
    def get_concept(self):
        """Retrieve the concept property from the current enum."""
        return self.value.get('concept')

    def get_path_concept(self):
        """Retrieve the path_concept property from the current enum."""
        return self.value.get('path_concept')

    def get_validate_data(self, data_to_validate):
        """Validate the data taking the validation schema from the current enum."""
        validate(instance=data_to_validate, schema=self.value.get('validation_schema'))
