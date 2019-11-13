from pal.transform.abstract_transform import AbstractTransform


class RemoveSystemRegisterAM(AbstractTransform):
    @property
    def description(self):
        d = "removing system register access mechanisms"
        return d

    def do_transform(self, reg):
        reg.access_mechanisms["mrs_register"] = []
        reg.access_mechanisms["msr_register"] = []

        return reg
