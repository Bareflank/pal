from dataclasses import dataclass, field as dataclass_field
from typing import List

from pal.logger import logger
from pal.model.field import Field


@dataclass
class Fieldset():
    """ Models a collection of named fields that apply to a register either """
    """ always or under a particular condition """

    size: int = 0
    """ The size (width) of this fieldset """

    name: str = ""
    """ The name of this fieldset """

    condition: str = ""
    """ A text description of conditions under which this fieldset is valid """

    fields: List[Field] = dataclass_field(default_factory= lambda: [])
    """ A list of fields that make up this fieldset """

    def __str__(self):
        if self.condition is not None:
            msg = "Fieldset when {condition}: ".format(condition=self.condition)
        else:
            msg = "Fieldset: "

        for field in self.fields:
            msg += "{name}=({msb}:{lsb}) ".format(
                name=field.name,
                msb=field.msb,
                lsb=field.lsb
            )

        return msg

    def add_field(self, name, msb, lsb):
        self.fields.append(Field(str(name), int(msb), int(lsb)))

    def is_valid(self):
        expected_total_set = set(range(0, self.size))
        total_set = set()

        for f_idx, f in enumerate(self.fields):
            # Check individual field ranges
            if not (0 <= f.lsb <= f.msb < self.size):
                logger.debug(
                    "Invalid field position for \"{name}\" ({msb}:{lsb})".format(
                        name=f.name,
                        msb=f.msb,
                        lsb=f.lsb
                ))
                return False

            # Check for intersections with other fields in this fieldset
            f_set = set(range(f.lsb, f.msb + 1))
            total_set = total_set.union(f_set)
            for x_idx, x in enumerate(self.fields):
                if f_idx == x_idx: continue
                x_set = set(range(x.lsb, x.msb + 1))
                intersect = f_set.intersection(x_set)
                if len(intersect) > 0:
                    logger.debug(
                        "Invalid field overlap, \"{f_name}\" ({f_msb}:{f_lsb}) "
                        "overlaps with \"{x_name}\" ({x_msb}:{x_lsb})".format(
                            f_name = f.name, f_msb = f.msb, f_lsb = f.lsb,
                            x_name = x.name, x_msb = x.msb, x_lsb = x.lsb
                    ))
                    return False

        return True
