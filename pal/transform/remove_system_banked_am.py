from pal.transform.abstract_transform import AbstractTransform


class RemoveSystemBankedAM(AbstractTransform):
    @property
    def description(self):
        d = "removing banked system register access mechanisms"
        return d

    def do_transform(self, reg):
        reg.access_mechanisms["msr_banked"] = []
        reg.access_mechanisms["mrs_banked"] = []

        return reg
