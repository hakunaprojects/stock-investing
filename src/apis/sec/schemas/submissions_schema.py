"""
Submissions Schema
Definition of the json-schema for the submissions response.
"""
SUBMISSIONS_SCHEMA = {
    "type": "object",
    "properties": {
        "cik": {"type": "string"},
        "entityName": {"type": "string"},
        "sic": {"type": "string"},
        "sicDescription": {"type": "string"},
        "insiderTransactionForOwnerExists": {"type": "number"},
        "insiderTransactionForIssuerExists": {"type": "number"},
        "name": {"type": "string"},
        "tickers": {"type": "array"},
        "exchanges": {"type": "array"},
        "ein": {"type": "string"},
        "description": {"type": "string"},
        "website": {"type": "string"},
        "investorWebsite": {"type": "string"},
        "category": {"type": "string"},
        "fiscalYearEnd": {"type": "string"},
        "stateOfIncorporation": {"type": "string"},
        "stateOfIncorporationDescription": {"type": "string"},
        "addresses": {"type": "object",
                      "properties": {
                          "mailing": {"type": "object",
                                      "properties": {
                                          "street1": {"type": "string"},
                                          "street2": {"type": ["string", "null"]},
                                          "city": {"type": "string"},
                                          "stateOrCountry": {"type": "string"},
                                          "zipCode": {"type": "string"},
                                          "stateOrCountryDescription": {"type": "string"},
                                      }},
                          "business": {"type": "object",
                                       "properties": {
                                           "street1": {"type": "string"},
                                           "street2": {"type": ["string", "null"]},
                                           "city": {"type": "string"},
                                           "stateOrCountry": {"type": "string"},
                                           "zipCode": {"type": "string"},
                                           "stateOrCountryDescription": {"type": "string"},
                                       }}
                      }},
        "phone": {"type": "string"},
        "flags": {"type": "string"},
        "formerNames": {"type": "array",
                        "items": {"type": "object",
                                  "properties":
                                      {
                                          "name": {"type": "string"},
                                          "from": {"type": "string", "format": "date-time"},
                                          "to": {"type": "string", "format": "date-time"}
                                      }}},
        "filings": {"type": "object"}
    }
}
