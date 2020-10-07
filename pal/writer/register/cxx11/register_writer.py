from pal.writer.register.register import RegisterWriter
from pal.writer.register.cxx11.register_dependency import Cxx11RegisterDependencyWriter
from pal.writer.register.cxx11.register_accessor import Cxx11RegisterAccessorWriter
from pal.writer.register.cxx11.field_accessor import Cxx11FieldAccessorWriter
from pal.writer.register.cxx11.printer import Cxx11PrinterWriter
from pal.writer.register.cxx11.helper import Cxx11HelperWriter


class Cxx11RegisterWriter(
        Cxx11RegisterDependencyWriter,
        Cxx11RegisterAccessorWriter,
        Cxx11FieldAccessorWriter,
        Cxx11PrinterWriter,
        Cxx11HelperWriter,
        RegisterWriter
        ):
    pass
