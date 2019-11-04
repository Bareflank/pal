from pal.filter.abstract_filter import AbstractFilter

class GICRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "generic interrupt controller (GIC) registers"

    def do_filter(self, reg):
        regname = reg.name.lower()
        if(regname.startswith("gic")):
            return False
        elif(regname.startswith("icc_")):
            return False
        elif(regname.startswith("icv_")):
            return False
        elif(regname.startswith("ich_")):
            return False
        else:
            return True
