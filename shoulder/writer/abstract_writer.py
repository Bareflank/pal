from typing import List

from shoulder.writer.language.language import LanguageWriter
from shoulder.writer.access_mechanism.access_mechanism \
        import AccessMechanismWriter
from shoulder.writer.printer.printer import PrinterWriter
from shoulder.writer.file_format.file_format import FileFormatWriter

from shoulder.gadget.gadget_properties import GadgetProperties
from shoulder.gadget import create_gadget_properties

class AbstractWriter(LanguageWriter, AccessMechanismWriter, PrinterWriter,
                     FileFormatWriter):

    @property
    def gadgets(self) -> List[GadgetProperties]:
        """ Returns a dictionary of gadget properties, keyed by gadget name """
        if not hasattr(self, "_gadgets"):
            self._gadgets = create_gadget_properties()
        return self._gadgets

    def get_writer(self):
        return self
