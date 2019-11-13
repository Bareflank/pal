from pal.filter.abstract_filter import AbstractFilter

class MPAMRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "memory partitioning and monitoring (MPAM) registers"

    def do_filter(self, reg):
        regname = reg.name.lower()
        if(regname.startswith("mpam")):
            return False
        else:
            return True
