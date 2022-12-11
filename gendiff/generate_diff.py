from gendiff.json_to_str import get_json_to_str


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


def get_diff(filepath1, filepath2):
    data1 = get_json_to_str(filepath1)
    data2 = get_json_to_str(filepath2)
    diff = []
    for key in sorted(set([*data1.keys(), *data2.keys()])):
        get_diff_if_same(data1, data2, diff, key)
        if key in data1.keys() and key not in data2.keys():
            diff.append({
                "key": key,
                "value": data1[key],
                "type": '-'
            })
        if key in data2.keys() and key not in data1.keys():
            diff.append({
                "key": key,
                "value": data2[key],
                "type": '+'
            })
    return format_diff(diff)


def format_diff(diff: dict):
    result = ''
    for i in diff:
        result += f"{i['type']} {i['key']}: {i['value']}\n"
    return result


# def get_diff(filepath1, filepath2):
#     data1 = get_json_to_str(filepath1)
#     data2 = get_json_to_str(filepath2)
#     diff = []
#     for key in sorted(set([*data1.keys(), *data2.keys()])):
#         if data1[key] == data2[key]:
#             diff.append({
#                 "key": key,
#                 "value": data1[key],
#                 "type": ' ',
#             })
#         if data1[key] != data2[key]:
#             diff.append({
#                "key": key,
#                 "value": data1[key],
#                 "type": '-',
#             })
#             diff.append({
#                 "key": key,
#                 "value": data2[key],
#                 "type": '+',
#             })
#         if key in data1.keys() and key not in data2.keys():
#             diff.append({
#                 "key": key,
#                 "value": data1[key],
#                 "type": '-',
#             })
#         if key not in data1.keys() and key in data2.keys():
#             diff.append({
#                 "key": key,
#                 "value": data2[key],
#                 "type": '+',
#             })
#         return format_diff(diff)
