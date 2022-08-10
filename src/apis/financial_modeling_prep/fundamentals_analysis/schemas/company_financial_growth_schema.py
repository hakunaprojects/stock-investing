"""
Company Financial Growth Schema
Definition of the json-schema for the company financial growth response.
"""

COMPANY_FINANCIAL_GROWTH_SCHEMA = {
    "type": "array",
    "items": {"type": "object",
              "properties":
                  {
                      "date": {"type": "string"},
                      "symbol": {"type": "string"},
                      "period": {"type": "string"},
                      "revenueGrowth": {"type": "number"},
                      "grossProfitGrowth": {"type": "number"},
                      "ebitgrowth": {"type": "number"},
                      "operatingIncomeGrowth": {"type": "number"},
                      "netIncomeGrowth": {"type": "number"},
                      "epsgrowth": {"type": "number"},
                      "epsdilutedGrowth": {"type": "number"},
                      "weightedAverageSharesGrowth": {"type": "number"},
                      "weightedAverageSharesDilutedGrowth": {"type": "number"},
                      "dividendsperShareGrowth": {"type": "number"},
                      "operatingCashFlowGrowth": {"type": "number"},
                      "freeCashFlowGrowth": {"type": "number"},
                      "tenYRevenueGrowthPerShare": {"type": "number"},
                      "fiveYRevenueGrowthPerShare": {"type": "number"},
                      "threeYRevenueGrowthPerShare": {"type": "number"},
                      "tenYOperatingCFGrowthPerShare": {"type": "number"},
                      "fiveYOperatingCFGrowthPerShare": {"type": "number"},
                      "threeYOperatingCFGrowthPerShare": {"type": "number"},
                      "tenYNetIncomeGrowthPerShare": {"type": "number"},
                      "fiveYNetIncomeGrowthPerShare": {"type": "number"},
                      "threeYNetIncomeGrowthPerShare": {"type": "number"},
                      "tenYShareholdersEquityGrowthPerShare": {"type": "number"},
                      "fiveYShareholdersEquityGrowthPerShare": {"type": "number"},
                      "threeYShareholdersEquityGrowthPerShare": {"type": "number"},
                      "tenYDividendperShareGrowthPerShare": {"type": "number"},
                      "fiveYDividendperShareGrowthPerShare": {"type": "number"},
                      "threeYDividendperShareGrowthPerShare": {"type": "number"},
                      "receivablesGrowth": {"type": "number"},
                      "inventoryGrowth": {"type": "number"},
                      "assetGrowth": {"type": "number"},
                      "bookValueperShareGrowth": {"type": "number"},
                      "debtGrowth": {"type": "number"},
                      "rdexpenseGrowth": {"type": "number"},
                      "sgaexpensesGrowth": {"type": "number"},
                  },
              "additionalProperties": False,
              "minProperties": 37
              }
}
