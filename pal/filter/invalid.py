from pal.filter.abstract_filter import AbstractFilter

class InvalidRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "invalid registers"

    def do_filter(self, reg):
        return reg.is_valid()
