from pal.filter.abstract_filter import AbstractFilter


class IrregularSizeFilter(AbstractFilter):
    @property
    def description(self):
        return "registers with a size other than 8, 16, 32, 64 bits"

    def do_filter(self, reg):
        regular_sizes = [8, 16, 32, 64]
        if reg.size not in regular_sizes:
            return False
        else:
            return True
