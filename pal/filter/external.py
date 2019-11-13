from pal.filter.abstract_filter import AbstractFilter


class ExternalRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "external (memory mapped) registers"

    def do_filter(self, reg):
        if not reg.is_internal:
            return False
        else:
            return True
