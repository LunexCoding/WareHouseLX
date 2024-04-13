import json


class JsonTools:
    @staticmethod
    def serialize(obj):
        return json.dumps(obj, ensure_ascii=False)

    @staticmethod
    def deserialize(json_str):
        return json.loads(json_str)
