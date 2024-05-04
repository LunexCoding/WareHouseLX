from collections import namedtuple


class TYPES_UI_MARKUP:
    PACK = 0
    GRID = 1


class TkinterMarkup:
    def __init__(self, typename, required_fields, **kwargs):
        self.typename = typename
        self.fields = tuple(required_fields) + tuple(kwargs.keys())
        self.defaults = kwargs
        self.NamedTuple = namedtuple(typename, self.fields)

    def __call__(self, **kwargs):
        all_kwargs = self.defaults.copy()
        all_kwargs.update(kwargs)
        missing_fields = [field for field in self.fields if field not in all_kwargs]
        if missing_fields and len(missing_fields) > len(self.fields) - len(self.defaults):
            raise ValueError("Not all required fields are provided.")
        return self.NamedTuple(**all_kwargs)


MARCUP = TkinterMarkup('Markup', ["element", "type"], padx=None, pady=None, row=None, column=None)
