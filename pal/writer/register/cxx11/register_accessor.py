import pal.gadget


class Cxx11RegisterAccessorWriter():

    def declare_register_accessors(self, outfile, register):
        self._declare_register_constants(outfile, register)

        if register.is_readable():
            self._declare_register_get(outfile, register)
        if register.is_writeable():
            self._declare_register_set(outfile, register)

    def call_register_get(self, outfile, register, destination, index="index"):
        call = "auto {dest} = {read}({view}{comma}{index});".format(
            dest=destination,
            read=self._register_read_function_name(register),
            view="view" if register.component else "",
            comma=", " if register.component and register.is_indexed else "",
            index=str(index) if register.is_indexed else ""
        )
        outfile.write(call)
        self.write_newline(outfile)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------

    def _declare_register_constants(self, outfile, register):
        self._declare_string_constant(outfile, "name", register.name.lower())
        self.write_newline(outfile)

        if register.long_name:
            self._declare_string_constant(outfile, "long_name", register.long_name)
            self.write_newline(outfile)

        if register.access_mechanisms.get("rdmsr"):
            addr = register.access_mechanisms["rdmsr"][0].address
            self._declare_hex_integer_constant(outfile, "address", addr)
            self.write_newline(outfile)

        if register.access_mechanisms.get("ldr"):
            offset = register.access_mechanisms["ldr"][0].offset
            self._declare_hex_integer_constant(outfile, "offset", offset)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("str"):
            offset = register.access_mechanisms["str"][0].offset
            self._declare_hex_integer_constant(outfile, "offset", offset)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("vmread"):
            encoding = register.access_mechanisms["vmread"][0].encoding
            self._declare_hex_integer_constant(outfile, "encoding", encoding)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("vmwrite"):
            encoding = register.access_mechanisms["vmwrite"][0].encoding
            self._declare_hex_integer_constant(outfile, "encoding", encoding)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("read"):
            offset = register.access_mechanisms["read"][0].offset
            self._declare_hex_integer_constant(outfile, "offset", offset)
            self.write_newline(outfile)
        elif register.access_mechanisms.get("write"):
            offset = register.access_mechanisms["write"][0].offset
            self._declare_hex_integer_constant(outfile, "offset", offset)
            self.write_newline(outfile)


        self.write_newline(outfile)

    def _declare_register_get(self, outfile, register):
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = "get"
        gadget.return_type = self._register_size_type(register)
        gadget.args = []

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_register_get_details(outfile, register)

    @pal.gadget.cxx.function_definition
    def _declare_register_get_details(self, outfile, register):
        offset_name = "offset"

        for am_key, am_list in register.access_mechanisms.items():
            for am in am_list:
                if am.is_read():
                    reg_size_type = self._register_size_type(register)
                    addr_size_type = self._address_size_type(am)
                    if am.is_memory_mapped():
                        addr_calc = 'view.base_address + ' + offset_name
                        if register.is_indexed:
                            addr_calc += " + (index * sizeof(" + reg_size_type + "))"

                        self._declare_variable(outfile, "address", addr_calc, keywords=[addr_size_type])

                    self._declare_variable(outfile, "value", 0, [reg_size_type])

                    self.call_readable_access_mechanism(
                        outfile, register, am, "value"
                    )
                    outfile.write("return value;")

                    return

    def _declare_register_set(self, outfile, register):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = "set"
        gadget.return_type = "void"
        gadget.args = []

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        gadget.args.append((size_type, "value"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_register_set_details(outfile, register)

    @pal.gadget.cxx.function_definition
    def _declare_register_set_details(self, outfile, register):
        offset_name = "offset"

        for am_key, am_list in register.access_mechanisms.items():
            for am in am_list:
                if am.is_write():
                    reg_size_type = self._register_size_type(register)
                    addr_size_type = self._address_size_type(am)
                    if am.is_memory_mapped():
                        addr_calc = 'view.base_address + ' + offset_name
                        if register.is_indexed:
                            addr_calc += " + (index * sizeof(" + reg_size_type + "))"

                        self._declare_variable(outfile, "address", addr_calc, keywords=[addr_size_type])

                    self.call_writable_access_mechanism(
                        outfile, register, am, "value"
                    )

                    return
