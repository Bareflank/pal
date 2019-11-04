from pal.filter.abstract_filter import AbstractFilter

class ActivityMonitorRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "activity monitor registers"

    def do_filter(self, reg):
        regname = reg.name.lower()
        if(regname.startswith("am") and not regname.startswith("amair")):
            return False
        else:
            return True
