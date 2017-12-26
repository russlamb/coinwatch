import json


def print_json(input_text):
    jdata = json.loads(input_text)
    print(json.dumps(jdata, indent=4, sort_keys=False))


def value_search(mydict, search_value):
    return list(mydict.keys())[list(mydict.values()).index(search_value)]
