"""
"""
from jsonschema import validate


def _validate_company_concept_response(company_concept_response):
    """"""
    company_concept_schema = {
        "type": "object",
        "properties": {
            "cik": {"type": "number"},
            "taxonomy": {"type": "string"},
            "tag": {"type": "string"},
            "label": {"type": "string"},
            "entityName": {"type": "string"},
            "units": {"type": "object",
                      "items": {"type": "array",
                                "items": {"type": "object",
                                          "properties":
                                              {
                                                  "start": {"type": "string"},
                                                  "end": {"type": "string"},
                                                  "val": {"type": "number"},
                                                  "accn": {"type": "string"},
                                                  "fy": {"type": "number"},
                                                  "fp": {"type": "string"},
                                                  "form": {"type": "string"},
                                                  "filed": {"type": "string"},
                                                  "frame": {"type": ["string", "null"]},
                                              },
                                          "required": [
                                              "start",
                                              "end",
                                              "val",
                                              "accn",
                                              "fy",
                                              "fp",
                                              "form",
                                              "filed"
                                          ]}
                                }}}
    }
    validate(instance=company_concept_response, schema=company_concept_schema)


def _validate_company_tickers_exchange_response(company_tickers_exchange_response):
    """"""
    company_tickers_exchange_schema = {
        "type": "object",
        "properties": {
            "fields": {"type": "array"},
            "data": {"type": "array",
                     "items": {"type": "array",
                               "prefixItems": [
                                   {"type": "number"},
                                   {"type": "string"},
                                   {"type": "string"},
                                   {"type": "string"}]
                               }}
        }
    }
    validate(instance=company_tickers_exchange_response, schema=company_tickers_exchange_schema)
    assert company_tickers_exchange_response['fields'] == ['cik', 'name', 'ticker', 'exchange']


def _validate_company_facts_response(company_facts_response):
    """"""
    company_facts_schema = {
        "type": "object",
        "properties": {
            "cik": {"type": "number"},
            "entityName": {"type": "string"},
            "facts": {"type": "object",
                      "properties": {
                          "dei": {"type": "object"},
                          "us-gaap": {"type": "object"},
                      }}
        }
    }
    validate(instance=company_facts_response, schema=company_facts_schema)
