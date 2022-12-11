import json


def get_json_to_str(filepath):
    return json.load(open(filepath))
