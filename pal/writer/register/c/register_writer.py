from pal.writer.register.register import RegisterWriter
from pal.writer.register.c.register_dependency import CRegisterDependencyWriter
from pal.writer.register.c.register_accessor import CRegisterAccessorWriter
from pal.writer.register.c.field_accessor import CFieldAccessorWriter
from pal.writer.register.c.printer import CPrinterWriter
from pal.writer.register.c.helper import CHelperWriter


class CRegisterWriter(
        CRegisterDependencyWriter,
        CRegisterAccessorWriter,
        CFieldAccessorWriter,
        CPrinterWriter,
        CHelperWriter,
        RegisterWriter
        ):
    pass
