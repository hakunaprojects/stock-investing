COMPANY_CONCEPT_SCHEMA = {
        "type": "object",
        "properties": {
            "cik": {"type": "number"},
            "taxonomy": {"type": "string"},
            "tag": {"type": "string"},
            "label": {"type": "string"},
            "description": {"type": "string"},
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
                                }}
        },
        "additionalProperties": False,
        "minProperties": 7
    }
