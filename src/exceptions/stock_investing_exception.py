"""
StockInvesting Exception Class
All exceptions from the project inherit from this custom exception
"""


class StockInvestingException(Exception):
    def __init__(self):
        self.code = None
        self.message = None
