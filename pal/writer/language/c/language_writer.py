from pal.writer.language.language import LanguageWriter
from pal.writer.language.c.register_dependency import CRegisterDependencyWriter
from pal.writer.language.c.register_accessor import CRegisterAccessorWriter
from pal.writer.language.c.field_accessor import CFieldAccessorWriter
from pal.writer.language.c.printer import CPrinterWriter
from pal.writer.language.c.comment import CCommentWriter
from pal.writer.language.c.helper import CHelperWriter


class CLanguageWriter(
        CCommentWriter,
        CRegisterDependencyWriter,
        CRegisterAccessorWriter,
        CFieldAccessorWriter,
        CPrinterWriter,
        CHelperWriter,
        LanguageWriter
        ):
    pass
