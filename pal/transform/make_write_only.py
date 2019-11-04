from pal.transform.abstract_transform import AbstractTransform


class MakeWriteOnly(AbstractTransform):
    @property
    def description(self):
        d = "removing readable access mechanisms"
        return d

    def do_transform(self, reg):
        readable = [
            "mrs_register",
            "mrs_banked",
            "mrc",
            "mrrc",
            "vmrs",
            "ldr"
        ]

        for key in readable:
            reg.access_mechanisms[key] = []

        return reg
