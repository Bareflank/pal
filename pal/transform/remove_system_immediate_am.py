from pal.transform.abstract_transform import AbstractTransform


class RemoveSystemImmediateAM(AbstractTransform):
    @property
    def description(self):
        d = "removing immediate system register access mechanisms"
        return d

    def do_transform(self, reg):
        reg.access_mechanisms["msr_immediate"] = []

        return reg
