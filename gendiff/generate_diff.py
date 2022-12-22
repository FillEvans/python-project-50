from gendiff.json_to_str import get_json_to_str
from gendiff.yml_to_str import get_yml_to_str


def get_diff_if_same(data1, data2, diff):
    for key in sorted(set([*data1.keys(), *data2.keys()])):
        if key in data1.keys() and key in data2.keys():
            if data1[key] == data2[key]:
                if type(data1[key]) == dict:
                    new_diff = []
                    new_data1 = data1[key]
                    new_data2 = data2[key]
                    get_diff_if_same(new_data1, new_data2, new_diff)
                diff.append({
                    "key": key,
                    "value": data1[key],
                    "type": ' '
                })
            elif data1[key] != data2[key]:
                if type(data1[key]) == dict and type(data2[key]) == dict:
                    new_diff = []
                    new_data1 = data1[key]
                    new_data2 = data2[key]
                    get_diff_if_same(new_data1, new_data2, new_diff)
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


def format_diff(diff: dict):
    result = ''
    for i in diff:
        result += f"{i['type']} {i['key']}: {i['value']}\n"
    return result


def probezhka(data: dict):
        for i in data.values():
            if type(i) == dict:
                probezhka(i)


def get_diff(filepath1: str, filepath2: str):
    path = [filepath1, filepath2]
    diff = []
    for i in path:
        if i.endswith(".yaml") or i.endswith(".yml"):
            data1 = get_yml_to_str(filepath1)
            data2 = get_yml_to_str(filepath2)
        elif i.endswith(".json"):
            data1 = get_json_to_str(filepath1)
            data2 = get_json_to_str(filepath2)
        get_diff_if_same(data1, data2, diff, key)
        get_diff_if_in_first(data1, data2, diff, key)
        get_diff_if_in_second(data1, data2, diff, key)
    return format_diff(diff)


print(get_diff("python-project-50/tests/fixtures/file1_for_test.json", "python-project-50/tests/fixtures/file2_for_test.json"))