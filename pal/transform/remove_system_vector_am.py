from pal.transform.abstract_transform import AbstractTransform


class RemoveSystemVectorAM(AbstractTransform):
    @property
    def description(self):
        d = "removing system vector access mechanisms"
        return d

    def do_transform(self, reg):
        reg.access_mechanisms["vmsr"] = []
        reg.access_mechanisms["vmrs"] = []

        return reg
