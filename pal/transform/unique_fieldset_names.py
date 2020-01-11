from pal.transform.abstract_transform import AbstractTransform


class UniqueFieldsetNames(AbstractTransform):
    @property
    def description(self):
        d = "assigning unique names to fields accross all field sets"
        return d

    def do_transform(self, reg):
        if len(reg.fieldsets) > 1:
            for idx, fs in enumerate(reg.fieldsets):
                for f in fs.fields:
                    if fs.name:
                        f.name = fs.name.lower() + "_" + f.name
                    else:
                        f.name = "fieldset_" + str(idx + 1) + "_" + f.name
        return reg
