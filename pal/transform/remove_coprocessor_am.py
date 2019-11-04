from pal.transform.abstract_transform import AbstractTransform


class RemoveCoprocessorAM(AbstractTransform):
    @property
    def description(self):
        d = "removing coprocessor access mechanisms"
        return d

    def do_transform(self, reg):
        reg.access_mechanisms["mrc"] = []
        reg.access_mechanisms["mrrc"] = []
        reg.access_mechanisms["mcr"] = []
        reg.access_mechanisms["mcrr"] = []

        return reg
