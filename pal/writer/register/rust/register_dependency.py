class RustRegisterDependencyWriter():

    def declare_register_dependencies(self, outfile, register, config):
        # TODO: Rust support for ARMv8A/A64 instructions is still under construction
        if not register.arch == "armv8a":
            outfile.write("use crate::instruction;")
            self.write_newline(outfile)
