from pal.filter.abstract_filter import AbstractFilter

class DeprecatedRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "deprecated registers"

    def do_filter(self, reg):
        if(reg.name == "SPSR_hyp"):
            return False
        elif(reg.name == "SPSR_svc"):
            return False
        else:
            return True

