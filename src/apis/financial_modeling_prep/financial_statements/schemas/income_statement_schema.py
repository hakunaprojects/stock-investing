"""
Income Statement Schema
Definition of the json-schema for the income statement response.
"""

INCOME_STATEMENT_SCHEMA = {
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
                      "revenue": {"type": "number"},
                      "costOfRevenue": {"type": "number"},
                      "grossProfit": {"type": "number"},
                      "grossProfitRatio": {"type": "number"},
                      "researchAndDevelopmentExpenses": {"type": "number"},
                      "generalAndAdministrativeExpenses": {"type": "number"},
                      "sellingAndMarketingExpenses": {"type": "number"},
                      "sellingGeneralAndAdministrativeExpenses": {"type": "number"},
                      "otherExpenses": {"type": "number"},
                      "operatingExpenses": {"type": "number"},
                      "costAndExpenses": {"type": "number"},
                      "interestIncome": {"type": "number"},
                      "interestExpense": {"type": "number"},
                      "depreciationAndAmortization": {"type": "number"},
                      "ebitda": {"type": "number"},
                      "ebitdaratio": {"type": "number"},
                      "operatingIncome": {"type": "number"},
                      "operatingIncomeRatio": {"type": "number"},
                      "totalOtherIncomeExpensesNet": {"type": "number"},
                      "incomeBeforeTax": {"type": "number"},
                      "incomeBeforeTaxRatio": {"type": "number"},
                      "incomeTaxExpense": {"type": "number"},
                      "netIncome": {"type": "number"},
                      "netIncomeRatio": {"type": "number"},
                      "eps": {"type": "number"},
                      "epsdiluted": {"type": "number"},
                      "weightedAverageShsOut": {"type": "number"},
                      "weightedAverageShsOutDil": {"type": "number"},
                      "link": {"type": "string"},
                      "finalLink": {"type": "string"}
                  },
              "additionalProperties": False,
              "minProperties": 38
              }
}
