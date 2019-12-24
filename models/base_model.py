class base_model:
    def __init__(self):
        self.bool_values = {"bool": {True, False}}

    def value_set(self, type):
        return self.bool_values[type]
