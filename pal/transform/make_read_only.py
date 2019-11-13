from pal.transform.abstract_transform import AbstractTransform


class MakeReadOnly(AbstractTransform):
    @property
    def description(self):
        d = "removing writeable access mechanisms"
        return d

    def do_transform(self, reg):
        writeable = [
            "msr_register",
            "mcr",
            "mcrr",
            "msr_banked",
            "msr_immediate",
            "vmsr",
            "str"
        ]

        for key in writeable:
            reg.access_mechanisms[key] = []

        return reg
