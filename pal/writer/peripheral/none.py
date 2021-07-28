from pal.writer.peripheral.peripheral import PeripheralWriter

from typing import TextIO


class NonePeripheralWriter(PeripheralWriter):

    def declare_peripheral_dependencies(self, outfile, registers, config):
        pass

    def declare_peripheral_views(self, outfile, registers):
        pass
