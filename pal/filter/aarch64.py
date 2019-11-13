from pal.filter.abstract_filter import AbstractFilter


class AArch64RegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "AArch64 (64-bit execution state) registers"

    def do_filter(self, reg):
        if(reg.execution_state == "aarch64"):
            return False
        else:
            return True
