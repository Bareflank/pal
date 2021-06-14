from pal.writer.register.register import RegisterWriter
from pal.writer.register.rust.register_dependency import RustRegisterDependencyWriter
from pal.writer.register.rust.register_accessor import RustRegisterAccessorWriter
from pal.writer.register.rust.field_accessor import RustFieldAccessorWriter
from pal.writer.register.rust.printer import RustPrinterWriter
from pal.writer.register.rust.helper import RustHelperWriter


class RustRegisterWriter(
        RustRegisterDependencyWriter,
        RustRegisterAccessorWriter,
        RustFieldAccessorWriter,
        RustPrinterWriter,
        RustHelperWriter,
        RegisterWriter
        ):
    pass
