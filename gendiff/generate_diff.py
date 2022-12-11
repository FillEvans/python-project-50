from gendiff.json_to_str import get_json_to_str

def get_diff(filepath1, filepath2):
    data1 = get_json_to_str(filepath1)
    data2 = get_json_to_str(filepath2)
    diff = []
    for key in sorted(set([*data1.keys(), *data2.keys()])):
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
    result = ''
    for i in diff:
        result += f"{i['type']} {i['key']}: {i['value']}\n"
    return result
