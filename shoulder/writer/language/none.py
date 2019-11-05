from shoulder.config import config
from shoulder.writer.language.language import LanguageWriter


class NoneLanguageWriter(LanguageWriter):

    def declare_register_constants(self, outfile, register):
        pass

    def declare_comment(self, outfile, comment, wrap=79):
        pass

    def declare_register_get(self, outfile, register):
        pass

    def declare_register_set(self, outfile, register):
        pass

    def declare_field_constants(self, outfile, register, field):
        pass

    def declare_field_accessors(self, outfile, register, field):
        pass

    def call_register_get(self, outfile, register, destination, index="index"):
        pass

    def call_field_get(self, outfile, register_value, field, destination):
        pass
