from pal.transform.abstract_transform import AbstractTransform


class RemoveRedundantAccessMechanisms(AbstractTransform):
    @property
    def description(self):
        d = "removing redundant access mechanisms"
        return d

    def do_transform(self, reg):
        for key, am_list in reg.access_mechanisms.items():
            reg.access_mechanisms[key] = am_list[:1]

        return reg
