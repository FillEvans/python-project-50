data1 = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}
data2 = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": 0,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}


def diff(data1, data2, diff, result):
    for key in sorted(set([*data1.keys(), data2.keys])):
        if data1[key] == data2[key]:
            if data1[key] == dict:
                new_data1 = data1[key]
                new_data2 = data2[key]
                child = diff(new_data1, new_data2, new_diff=[], new_result='')
            diff.append({
                    "key": key,
                    "value": data1[key],
                    "type": ' '
            })
        elif data1[key] != data2[key]:
            if data1[key] == dict and data2[key] == dict:
                new_data1 = data1[key]
                new_data2 = data2[key]
                diff(new_data1, new_data2, new_diff=[], new_result='')
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
    return format(diff, result)


def get_diff_if_in_first(data1, data2, diff):
    for key in sorted(set([*data1.keys(), data2.keys])):
        if key in data1.keys() and key not in data2.keys():
            diff.append({
                "key": key,
                "value": data1[key],
                "type": '-'
            })
    return diff


def get_diff_if_in_second(data1, data2, diff):
    for key in sorted(set([*data1.keys(), data2.keys])):
        if key in data2.keys() and key not in data1.keys():
            diff.append({
                "key": key,
                "value": data2[key],
                "type": '+'
            })
    return diff
        

def format(diff, result):
    for i in diff:
        result += f"{i['type']} {i['key']}: {i['value']}\n"
    return result

def get_difff(data1: dict, data2: dict):
    result = ''
    difff = []
    diff(data1, data2, difff)
    get_diff_if_in_first(data1, data2, difff)
    get_diff_if_in_second(data1, data2, difff)

get_difff(data1, data2)