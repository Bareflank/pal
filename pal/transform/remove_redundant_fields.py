from pal.transform.abstract_transform import AbstractTransform


class RemoveRedundantFields(AbstractTransform):
    @property
    def description(self):
        d = "removing redundant fields (by name) within each field set"
        return d

    def do_transform(self, reg):
        for idx, fs in enumerate(reg.fieldsets):
            unique_fields = {}

            for f in fs.fields:
                if f.name not in unique_fields:
                    unique_fields[f.name] = f

            reg.fieldsets[idx].fields = [v for v in unique_fields.values()]

        return reg
