COMPANY_FACTS_SCHEMA = {
    "type": "object",
    "properties": {
        "cik": {"type": "number"},
        "entityName": {"type": "string"},
        "facts": {"type": "object",
                  "properties": {
                      "dei": {"type": "object"},
                      "us-gaap": {"type": "object"},
                  }}
    },
    "additionalProperties": False,
    "minProperties": 3
}
