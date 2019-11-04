from pal.transform.abstract_transform import AbstractTransform
from pal.logger import logger

class Quirks(AbstractTransform):
    @property
    def description(self):
        return "fixing miscellaneous quirks from the XML specification"

    def do_transform(self, reg):
        if(reg.name == "FPEXC32_EL2"):
            for fs in reg.fieldsets:
                fs.fields = set([field for field in fs.fields if fs.fields.count(field.name) == "UFF"])
                logger.debug("Removed overlapping field \"UFF\" from register FPEXC32_EL2")

        if(reg.name == "HCR_EL2"):
            for fs in reg.fieldsets:
                for f_idx, f in enumerate(fs.fields):
                    if f.name == "TPC":
                        del fs.fields[f_idx]
                        logger.debug("Removed duplicate field \"TPC\" from register HCR_EL2")

        if(reg.name == "EDECCR"):
            for fs in reg.fieldsets:
                for f_idx, f in enumerate(fs.fields):
                    if f.name == "NSE":
                        del fs.fields[f_idx]
                        logger.debug("Removed overlapping field \"NSE\" from register EDECCR")

                for f_idx, f in enumerate(fs.fields):
                    if f.name == "SE":
                        del fs.fields[f_idx]
                        logger.debug("Removed overlapping field \"SE\" from register EDECCR")

        return reg
