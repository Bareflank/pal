from pal.filter.abstract_filter import AbstractFilter

class SCXTNUMRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "software context number (SCXTNUM) registers"

    def do_filter(self, reg):
        regname = reg.name.lower()
        if(regname.startswith("scxtnum")):
            return False
        else:
            return True
