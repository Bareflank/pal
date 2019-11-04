from pal.filter.abstract_filter import AbstractFilter


class NoAccessMechanismFilter(AbstractFilter):
    @property
    def description(self):
        return "registers with no access mechanism"

    def do_filter(self, reg):
        for key, am_list in reg.access_mechanisms.items():
            if am_list:
                return True

        return False
