

class BuilderBaseClass:

    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            tmp = self.result
            for item in keys[:-1]:
                if item not in tmp.keys():
                    tmp[item] = {}
                tmp = tmp[item]
            tmp[keys[-1]] = value
        return self

    def build(self):
        return self.result
