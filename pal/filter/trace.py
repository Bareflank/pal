from pal.filter.abstract_filter import AbstractFilter

class TraceRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "trace registers"

    def do_filter(self, reg):
        if(reg.name.lower().startswith("trfcr")):
            return False
        elif(reg.name.lower().startswith("htrfcr")):
            return False
        else:
            return True
