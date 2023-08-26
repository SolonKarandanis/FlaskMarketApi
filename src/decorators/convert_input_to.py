# This decorator takes the class/namedtuple to convert any JSON
# data in incoming request to.
from flask import request


def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            print(f'class: {type(class_)}')
            if type(class_) == list:
                print(f'class: {type(class_)}')
            else:
                obj = class_(**request.get_json())
                return f(obj)
        return decorator
    return wrap
