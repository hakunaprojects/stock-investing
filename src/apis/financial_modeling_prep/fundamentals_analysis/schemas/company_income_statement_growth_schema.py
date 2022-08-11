"""
Company Income Statement Growth Schema
Definition of the json-schema for the income statement growth response.
"""
COMPANY_INCOME_STATEMENT_GROWTH_SCHEMA = {
    "type": "array",
    "items": {"type": "object",
              "properties":
                  {
                      "date": {"type": "string"},
                      "symbol": {"type": "string"},
                      "period": {"type": "string"},
                      "growthRevenue": {"type": "number"},
                      "growthCostOfRevenue": {"type": "number"},
                      "growthGrossProfit": {"type": "number"},
                      "growthGrossProfitRatio": {"type": "number"},
                      "growthResearchAndDevelopmentExpenses": {"type": "number"},
                      "growthGeneralAndAdministrativeExpenses": {"type": "number"},
                      "growthSellingAndMarketingExpenses": {"type": "number"},
                      "growthOtherExpenses": {"type": "number"},
                      "growthOperatingExpenses": {"type": "number"},
                      "growthCostAndExpenses": {"type": "number"},
                      "growthInterestExpense": {"type": "number"},
                      "growthDepreciationAndAmortization": {"type": "number"},
                      "growthEBITDA": {"type": "number"},
                      "growthEBITDARatio": {"type": "number"},
                      "growthOperatingIncome": {"type": "number"},
                      "growthOperatingIncomeRatio": {"type": "number"},
                      "growthTotalOtherIncomeExpensesNet": {"type": "number"},
                      "growthIncomeBeforeTax": {"type": "number"},
                      "growthIncomeBeforeTaxRatio": {"type": "number"},
                      "growthIncomeTaxExpense": {"type": "number"},
                      "growthNetIncome": {"type": "number"},
                      "growthNetIncomeRatio": {"type": "number"},
                      "growthEPS": {"type": "number"},
                      "growthEPSDiluted": {"type": "number"},
                      "growthWeightedAverageShsOut": {"type": "number"},
                      "growthWeightedAverageShsOutDil": {"type": "number"}
                  },
              "additionalProperties": False,
              "minProperties": 29
              }
}
