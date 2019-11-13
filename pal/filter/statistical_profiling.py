from pal.filter.abstract_filter import AbstractFilter

class StatisticalProfilingRegisterFilter(AbstractFilter):
    def __init__(self):
        self.exclusions = [
            "pmsidr_el1",
            "pmsfcr_el1",
            "pmsicr_el1",
            "pmscr_el2",
            "pmbptr_el1",
            "pmbsr_el1",
            "pmsirr_el1",
            "pmscr_el1",
            "pmblimitr_el1",
            "pmslatfr_el1",
            "pmmir_el1"
        ]

    @property
    def description(self):
        return "statistical profiling registers"

    def do_filter(self, reg):
        if(reg.name.lower() in self.exclusions):
            return False
        else:
            return True
