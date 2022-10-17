import json


def load_json_file(filename: str) -> dict:
    with open(filename) as fp:
        data = json.load(fp)
    fp.close()
    return data


def save_to_json(filename: str, dict_to_save: dict):
    with open(filename, "w") as fp:
        json.dump(dict_to_save, fp, sort_keys=True, indent=4)
    fp.close()
