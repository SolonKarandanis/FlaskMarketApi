# This decorator takes the class/namedtuple to convert any JSON
# data in incoming request to.
from flask import request


def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            json_request = request.get_json()
            if type(json_request) == list:
                objects = [class_(**o) for o in json_request]
                return f(objects)
            else:
                obj = class_(**json_request)
                return f(obj)

        return decorator

    return wrap
