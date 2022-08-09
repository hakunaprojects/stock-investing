COMPANY_TICKERS_EXCHANGE_SCHEMA = {
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
