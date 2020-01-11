from pal.config import config
from pal.writer.language.language import LanguageWriter


class NoneLanguageWriter(LanguageWriter):

    def declare_comment(self, outfile, comment, wrap=79):
        pass

    def declare_register_dependencies(self, outfile, register):
        pass

    def declare_register_accessors(self, outfile, register):
        pass

    def declare_field_accessors(self, outfile, register, field):
        pass

    def call_register_get(self, outfile, register, destination, index="index"):
        pass

    def call_field_get(self, outfile, register, field, destination,
                       register_value):
        pass
