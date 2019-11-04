from pal.transform.abstract_transform import AbstractTransform


class RemoveMemoryMappedAM(AbstractTransform):
    @property
    def description(self):
        d = "removing memory mapped access mechanisms"
        return d

    def do_transform(self, reg):
        reg.access_mechanisms["ldr"] = []
        reg.access_mechanisms["str"] = []

        return reg
