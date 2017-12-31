import json


def print_json(input_text):
    """Print Json to standard output in a pretty way """
    jdata = json.loads(input_text)
    print(json.dumps(jdata, indent=4, sort_keys=False))


def value_search(mydict, search_value):
    """Find the key for a given value in a dictionary"""
    return list(mydict.keys())[list(mydict.values()).index(search_value)]


def is_number(s):
    """Check if a varible is a number.  Return True if it is.  False if not"""
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False