from pal.transform.abstract_transform import AbstractTransform
from pal.logger import logger

class SpecialToUnderscore(AbstractTransform):
    def __init__(self):
        self.special_chars = " !@#$%^&*()[]{};:,./<>?\|`~-=+"

    @property
    def description(self):
        d = "replacing special characters ({chars}) with \"_\"".format(
            chars = self.special_chars
        )
        return d

    def do_transform(self, reg):
        new_name = reg.name.translate({ord(c): "_" for c in self.special_chars})
        if new_name != reg.name:
            logger.debug("Replaced special characters in register: {name} -> {new_name}".format(
                name = reg.name,
                new_name = new_name
            ))
            reg.name = new_name

        for fs in reg.fieldsets:
            for f in fs.fields:
                new_name = f.name.translate({ord(c): "_" for c in self.special_chars})
                if new_name != f.name:
                    logger.debug("Replaced special characters in field: {name} -> {new_name}".format(
                        name = f.name,
                        new_name = new_name
                    ))
                    f.name = new_name

        return reg
