import pal.gadget
from pal.config import config


class RustRegisterAccessorWriter():

    def declare_register_accessors(self, outfile, register):
        self._declare_register_constants(outfile, register)

        if register.is_readable():
            self._declare_register_get(outfile, register)
        if register.is_writeable():
            self._declare_register_set(outfile, register)

    def call_register_get(self, outfile, register, destination, index="index"):
        call = "let {dest} = {read}({index});".format(
            dest=destination,
            read=self._register_read_function_name(register),
            index=str(index) if register.is_indexed else ""
        )
        outfile.write(call)
        self.write_newline(outfile)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------

    def _declare_register_constants(self, outfile, register):
        prefix = self._register_prefix(register)
        self._declare_string_constant(outfile, prefix + "name", register.name.lower())
        self.write_newline(outfile)

        if register.long_name:
            self._declare_string_constant(outfile, prefix + "long_name", register.long_name)
            self.write_newline(outfile)

        if register.access_mechanisms.get("rdmsr"):
            addr = register.access_mechanisms["rdmsr"][0].address
            self._declare_hex_integer_constant(outfile, prefix + "address", addr, n_bits=32)
            self.write_newline(outfile)

        if register.access_mechanisms.get("ldr"):
            offset = register.access_mechanisms["ldr"][0].offset
            self._declare_hex_integer_constant(outfile, prefix + "offset", offset)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("str"):
            offset = register.access_mechanisms["str"][0].offset
            self._declare_hex_integer_constant(outfile, prefix + "offset", offset)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("vmread"):
            encoding = register.access_mechanisms["vmread"][0].encoding
            self._declare_hex_integer_constant(outfile, prefix + "encoding", encoding, n_bits=64)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("vmwrite"):
            encoding = register.access_mechanisms["vmwrite"][0].encoding
            self._declare_hex_integer_constant(outfile, prefix + "encoding", encoding, n_bits=64)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("read"):
            offset = register.access_mechanisms["read"][0].offset
            self._declare_hex_integer_constant(outfile, prefix + "offset", offset)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("write"):
            offset = register.access_mechanisms["write"][0].offset
            self._declare_hex_integer_constant(outfile, prefix + "offset", offset)
            self.write_newline(outfile)


        self.write_newline(outfile)

    def _declare_register_get(self, outfile, register):
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.name = self._register_read_function_name(register)
        gadget.return_type = self._register_size_type(register)
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_register_get_details(outfile, register)

    @pal.gadget.rust.function_definition
    def _declare_register_get_details(self, outfile, register):
        prefix = self._register_prefix(register)
        offset_name = prefix + "offset"

        for am_key, am_list in register.access_mechanisms.items():
            for am in am_list:
                if am.is_read():
                    self.call_readable_access_mechanism(
                        outfile, register, am, "value"
                    )
                    return

    def _declare_register_set(self, outfile, register):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.name = self._register_write_function_name(register)
        gadget.return_type = None
        gadget.args = [(size_type, "value")]

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_register_set_details(outfile, register)

    @pal.gadget.rust.function_definition
    def _declare_register_set_details(self, outfile, register):
        prefix = self._register_prefix(register)
        offset_name = prefix + "offset"

        for am_key, am_list in register.access_mechanisms.items():
            for am in am_list:
                if am.is_write():
                    self.call_writable_access_mechanism(
                        outfile, register, am, "value"
                    )
                    return
