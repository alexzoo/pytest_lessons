

class BaseModel:

    def validate(self, response, schema):
        response_json = response.json()
        if isinstance(response_json, list):
            for item in response_json:
                parsed_object = schema.parse_obj(item)
                return parsed_object
        else:
            return schema.parse_obj(response_json)
