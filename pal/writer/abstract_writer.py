from typing import List

from pal.writer.language.language import LanguageWriter
from pal.writer.access_mechanism.access_mechanism \
        import AccessMechanismWriter
from pal.writer.printer.printer import PrinterWriter
from pal.writer.file_format.file_format import FileFormatWriter

from pal.gadget.gadget_properties import GadgetProperties
from pal.gadget import create_gadget_properties

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
