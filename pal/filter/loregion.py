from pal.filter.abstract_filter import AbstractFilter

class LORegionRegisterFilter(AbstractFilter):
    @property
    def description(self):
        return "limited order region (LORegion) registers"

    def do_filter(self, reg):
        if(reg.name.lower().startswith("lor")):
            return False
        else:
            return True
