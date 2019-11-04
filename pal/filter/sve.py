from pal.filter.abstract_filter import AbstractFilter

class SVERegisterFilter(AbstractFilter):
    def __init__(self):
        self.registers = [
            "zcr_el1",
            "zcr_el2",
            "zcr_el3",
            "id_aa64zfr0_el1"
        ]

    @property
    def description(self):
        return "scalable vector extension (SVE) registers"

    def do_filter(self, reg):
        if(reg.name.lower() in self.registers):
            return False
        else:
            return True
