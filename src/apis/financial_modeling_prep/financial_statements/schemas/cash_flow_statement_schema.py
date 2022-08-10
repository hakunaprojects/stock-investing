"""
Cash Flow Statement Schema
Definition of the json-schema for the cash flow statement response.
"""

CASH_FLOW_STATEMENT_SCHEMA = {
    "type": "array",
    "items": {"type": "object",
              "properties":
                  {
                      "date": {"type": "string"},
                      "symbol": {"type": "string"},
                      "reportedCurrency": {"type": "string"},
                      "cik": {"type": "string"},
                      "fillingDate": {"type": "string"},
                      "acceptedDate": {"type": "string"},
                      "calendarYear": {"type": "string"},
                      "period": {"type": "string"},
                      "netIncome": {"type": "number"},
                      "depreciationAndAmortization": {"type": "number"},
                      "deferredIncomeTax": {"type": "number"},
                      "stockBasedCompensation": {"type": "number"},
                      "changeInWorkingCapital": {"type": "number"},
                      "accountsReceivables": {"type": "number"},
                      "inventory": {"type": "number"},
                      "accountsPayables": {"type": "number"},
                      "otherWorkingCapital": {"type": "number"},
                      "otherNonCashItems": {"type": "number"},
                      "netCashProvidedByOperatingActivities": {"type": "number"},
                      "investmentsInPropertyPlantAndEquipment": {"type": "number"},
                      "acquisitionsNet": {"type": "number"},
                      "purchasesOfInvestments": {"type": "number"},
                      "salesMaturitiesOfInvestments": {"type": "number"},
                      "otherInvestingActivites": {"type": "number"},
                      "netCashUsedForInvestingActivites": {"type": "number"},
                      "debtRepayment": {"type": "number"},
                      "commonStockIssued": {"type": "number"},
                      "commonStockRepurchased": {"type": "number"},
                      "dividendsPaid": {"type": "number"},
                      "otherFinancingActivites": {"type": "number"},
                      "netCashUsedProvidedByFinancingActivities": {"type": "number"},
                      "effectOfForexChangesOnCash": {"type": "number"},
                      "netChangeInCash": {"type": "number"},
                      "cashAtEndOfPeriod": {"type": "number"},
                      "cashAtBeginningOfPeriod": {"type": "number"},
                      "operatingCashFlow": {"type": "number"},
                      "capitalExpenditure": {"type": "number"},
                      "freeCashFlow": {"type": "number"},
                      "link": {"type": "string"},
                      "finalLink": {"type": "string"}
                  },
              "additionalProperties": False,
              "minProperties": 40
              }
}
