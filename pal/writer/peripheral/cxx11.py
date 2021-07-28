from pal.writer.peripheral.peripheral import PeripheralWriter

from typing import TextIO


class Cxx11PeripheralWriter(PeripheralWriter):

    def declare_peripheral_dependencies(self, outfile, registers, config):
        if config.stdint_header:
            outfile.write('#include "' + str(config.stdint_header) + '"')
        else:
            outfile.write("#include <stdint.h>")

        self.write_newline(outfile)
        self.write_newline(outfile)

    def declare_peripheral_views(self, outfile, registers):
        reg = registers[0]
        view_declaration = "struct view {{ {size_type} base_address; }};"
        size_type = "uintptr_t"

        for am_key, am_list in reg.access_mechanisms.items():
            for am in am_list:
                size_type = self._address_size_type(am)

        outfile.write(view_declaration.format(
            size_type=size_type,
        ))
        self.write_newline(outfile, count=2)
