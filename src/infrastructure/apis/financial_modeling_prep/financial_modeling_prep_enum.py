"""
Financial Modeling Prep Enum
Parent enum with specific methods for financial modeling prep. It is inherited.
"""
from enum import Enum

from jsonschema.validators import validate


class FinancialModelingPrepEnum(Enum):
    """It contains the three main methods required to centralize all actions for financial modeling prep api"""

    def get_concept(self):
        """Retrieve the concept property from the current enum."""
        return self.value.get("concept")

    def get_path_concept(self):
        """Retrieve the path_concept property from the current enum."""
        return self.value.get("path_concept")

    def get_validate_data(self, data_to_validate):
        """Validate the data taking the validation schema from the current enum."""
        validate(instance=data_to_validate, schema=self.value.get("validation_schema"))
