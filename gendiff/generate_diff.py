from gendiff.json_to_str import get_json_to_str
from gendiff.yml_to_str import get_yml_to_str


def get_diff_if_same(data1, data2, diff, key):
    if key in data1.keys() and key in data2.keys():
        if data1[key] == data2[key]:
            diff.append({
                "key": key,
                "value": data1[key],
                "type": ' '
            })
        elif data1[key] != data2[key]:
            diff.append({
                "key": key,
                "value": data1[key],
                "type": '-'
            })
            diff.append({
                "key": key,
                "value": data2[key],
                "type": '+'
            })
    return diff


def get_diff_if_in_first(data1, data2, diff, key):
    if key in data1.keys() and key not in data2.keys():
        diff.append({
            "key": key,
            "value": data1[key],
            "type": '-'
        })
    return diff


def get_diff_if_in_second(data1, data2, diff, key):
    if key in data2.keys() and key not in data1.keys():
        diff.append({
            "key": key,
            "value": data2[key],
            "type": '+'
        })
    return diff


def get_diff(filepath1: str, filepath2: str):
    path = [filepath1, filepath2]
    for i in path:
        if i.endswith("yaml") or i.endswith(".yml"):
            data1 = get_yml_to_str(filepath1)
            data2 = get_yml_to_str(filepath2)
        elif i.endswith(".json"):
            data1 = get_json_to_str(filepath1)
            data2 = get_json_to_str(filepath2)
    diff = []
    for key in sorted(set([*data1.keys(), *data2.keys()])):
        get_diff_if_same(data1, data2, diff, key)
        get_diff_if_in_first(data1, data2, diff, key)
        get_diff_if_in_second(data1, data2, diff, key)
    return format_diff(diff)


def format_diff(diff: dict):
    result = ''
    for i in diff:
        result += f"{i['type']} {i['key']}: {i['value']}\n"
    return result
