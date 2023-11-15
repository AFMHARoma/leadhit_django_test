import re


def validate_through_regexp(v):
    test = {
        'date': r'^((\d{2}.\d{2}.\d{4})|(\d{4}\-\d{2}\-\d{2}))$',
        'phone': r'^(\+7|7|8)?[\s\-]?[0-9]{3,5}[\s\-]?[0-9]{1,3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        'email': r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    }
    for t, r in test.items():
        if re.fullmatch(r, v):
            return t

    return 'text'


def get_params_types(d):
    res = {}
    d = d.dict()
    for k, v in d.items():
        res[k] = validate_through_regexp(v)

    return res
