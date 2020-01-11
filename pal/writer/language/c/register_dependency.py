class CRegisterDependencyWriter():

    def declare_register_dependencies(self, outfile, register):
        if register.size == 32:
            size_t = "uint32_t"
        else:
            size_t = "uint64_t"

        mock_reg_name = "pal_" + register.name.lower() + "_mock_register"
        self._declare_variable(outfile, mock_reg_name, value=0,
                               keywords=["static", size_t])

        if not register.is_internal:
            for am_key, am_list in register.access_mechanisms.items():
                for am in am_list:
                    if am.is_memory_mapped():
                        get_base = "pal_" + str(am.component) + '_base_address'
                        outfile.write("uintptr_t " + get_base + "(void);")
                        self.write_newline(outfile)
                        return
