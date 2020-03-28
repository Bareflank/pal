from pal.transform.abstract_transform import AbstractTransform
from pal.logger import logger

class InsertValidFirstCharacter(AbstractTransform):
    def __init__(self):
        self.special_chars = "0123456789"

    @property
    def description(self):
        d = "inserting a valid character \"_\" for identifiers that begin with ({chars})".format(
            chars = self.special_chars
        )
        return d

    def do_transform(self, reg):
        first_char = reg.name[0]
        if first_char in self.special_chars:
            reg.name = "_" + reg.name

        for fs in reg.fieldsets:
            for f in fs.fields:
                first_char = f.name[0]
                if first_char in self.special_chars:
                    f.name = "_" + f.name

        return reg
