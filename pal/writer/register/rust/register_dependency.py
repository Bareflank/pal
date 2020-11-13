class RustRegisterDependencyWriter():

    def declare_register_dependencies(self, outfile, register):
        outfile.write("use crate::instruction;")
        self.write_newline(outfile)
