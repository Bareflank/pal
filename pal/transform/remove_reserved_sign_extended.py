from pal.transform.abstract_transform import AbstractTransform
from pal.logger import logger

class RemoveReservedSignExtended(AbstractTransform):
    @property
    def description(self):
        d = "removing reserved sign extended (RESS) fields"
        return d

    def do_transform(self, reg):
        for fs in reg.fieldsets:
            fs_len = len(fs.fields)
            fs.fields = [field for field in fs.fields if not field.name.startswith("RESS")]

            count = fs_len - len(fs.fields)
            if count:
                logger.debug("Removed {count} field{s} from {reg}".format(
                    count = count,
                    reg = reg.name,
                    s = "" if count == 1 else "s"
                ))

        return reg
