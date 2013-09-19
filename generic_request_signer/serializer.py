from datetime import datetime
import json


def json_date_object_hook(obj):
    result = {}

    for k, v in obj.items():
        try:
            result[k] = datetime.strptime(v, '%Y-%m-%d')
        except (TypeError, ValueError):
            result[k] = v
    return result


class JsonSerializer(object):

    def serialize(self, data):
        return json.loads(data, object_hook=json_date_object_hook)

