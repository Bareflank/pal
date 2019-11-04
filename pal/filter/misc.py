from pal.filter.abstract_filter import AbstractFilter

class MiscelaneousRegisterFilter(AbstractFilter):
    def __init__(self):
        self.exclusions = [
            "ccsidr2_el1",
            "id_pfr2_el1",
            "id_isar6_el1",
            "pmmir_el1",
            "erxmisc2_el1",
            "tfsr_el3",
            "erxpfgcdn_el1",
            "rndr",
            "erxpfgctl_el1",
            "tfsr_el2",
            "s3_<op1>_c<cn>_c<cm>_<op2>",
            "erxmisc3_el1",
            "tfsre0_el1",
            "ssbs",
            "erxpfgf_el1",
            "rndrrs",
            "tfsr_el1",
            "tco",
            "gcr_el1",
            "rgsr_el1"
        ]

    @property
    def description(self):
        return "miscelaneous not-yet-supported registers"

    def do_filter(self, reg):
        if(reg.name.lower() in self.exclusions):
            return False
        elif(reg.name.lower().startswith("s3_")):
            return False
        else:
            return True
