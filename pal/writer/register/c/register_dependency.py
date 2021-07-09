class CRegisterDependencyWriter():

    def declare_register_dependencies(self, outfile, register, config):
        if config.stdint_header:
            outfile.write('#include "' + str(config.stdint_header) + '"')
        else:
            outfile.write("#include <stdint.h>")
        self.write_newline(outfile)

        if not register.is_internal:
            for am_key, am_list in register.access_mechanisms.items():
                for am in am_list:
                    if am.is_memory_mapped():
                        get_base = "pal_" + str(am.component) + '_base_address'
                        outfile.write("uintptr_t " + get_base + "(void);")
                        self.write_newline(outfile)
                        return
