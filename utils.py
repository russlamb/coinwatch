import json
from datetime import datetime, timedelta
from time import sleep


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


def friendly_name_decorator(name):
    """gives a function a friendly_name attribute"""

    def real_decorator(func):
        def wrapper(*args, **kwargs):
            # print("Wrapping function {} with friendly name {}".format(func.__name__,name))
            return func(*args, **kwargs)

        wrapper.friendly_name = name
        return wrapper

    return real_decorator


class SleepCheck():
    last_call = datetime.min  # default time


def get_time_to_wait(wait_time_in_milliseconds):
    """determines how long it is necessary to wait before calling a function wrapped by sleep_decorator"""
    time_since_last_call = datetime.now() - SleepCheck.last_call
    min_call_wait = timedelta(microseconds=wait_time_in_milliseconds*1000)
    if time_since_last_call < min_call_wait:
        return (min_call_wait - time_since_last_call)
    else:
        return timedelta(seconds=0)


def sleep_decorator(sleep_time):
    """Ensures subsequent function calls are delayed by the number of miliseconds passed in to the decorator """

    def real_decorator(func):
        def wrapper(*args, **kwargs):
            wait_time=get_time_to_wait(sleep_time).total_seconds()
            sleep(wait_time)
            result = func(*args, **kwargs)
            SleepCheck.last_call = datetime.now()
            return result
        return wrapper

    return real_decorator

if __name__=="__main__":
    print(datetime.min)
    SleepCheck.last_call=datetime.now()
    print(get_time_to_wait(100))