"""
StockInvesting Exception Class
All exceptions from the project inherit from this custom exception
"""


class StockInvestingException(Exception):
    """Main Project Exception Class"""

    def __init__(self):
        super().__init__()
        self.code = None
        self.message = None
