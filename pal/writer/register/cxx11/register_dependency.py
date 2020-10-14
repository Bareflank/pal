import pal.gadget


class Cxx11RegisterDependencyWriter():

    def declare_register_dependencies(self, outfile, register):
        outfile.write("#include <stdint.h>")
        self.write_newline(outfile)

        if not register.is_internal:
            gadget = self.gadgets["pal.cxx.namespace"]
            gadget.name = "pal"
            self.__declare_memory_mapped_dependencies(outfile, register)
            self.write_newline(outfile)


    @pal.gadget.cxx.namespace
    def __declare_memory_mapped_dependencies(self, outfile, register):
        for am_key, am_list in register.access_mechanisms.items():
            for am in am_list:
                if am.is_memory_mapped():
                    get_base = str(am.component) + '_base_address'
                    outfile.write("uintptr_t " + get_base + "(void);")
                    self.write_newline(outfile)
                    return
