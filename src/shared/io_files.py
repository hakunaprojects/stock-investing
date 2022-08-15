import json


def load_json_file(filename: str) -> dict:
    with open(filename) as fp:
        data = json.load(fp)
    fp.close()
    return data
