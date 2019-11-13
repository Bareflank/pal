from pal.filter.abstract_filter import AbstractFilter


class AArch32RegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "AArch32 (32-bit execution state) registers"

    def do_filter(self, reg):
        if(reg.execution_state == "aarch32"):
            return False
        else:
            return True
