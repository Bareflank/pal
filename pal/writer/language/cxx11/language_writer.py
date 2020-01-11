from pal.writer.language.language import LanguageWriter
from pal.writer.language.cxx11.register_dependency import Cxx11RegisterDependencyWriter
from pal.writer.language.cxx11.register_accessor import Cxx11RegisterAccessorWriter
from pal.writer.language.cxx11.field_accessor import Cxx11FieldAccessorWriter
from pal.writer.language.cxx11.printer import Cxx11PrinterWriter
from pal.writer.language.cxx11.comment import Cxx11CommentWriter
from pal.writer.language.cxx11.helper import Cxx11HelperWriter


class Cxx11LanguageWriter(
        Cxx11CommentWriter,
        Cxx11RegisterDependencyWriter,
        Cxx11RegisterAccessorWriter,
        Cxx11FieldAccessorWriter,
        Cxx11PrinterWriter,
        Cxx11HelperWriter,
        LanguageWriter
        ):
    pass
