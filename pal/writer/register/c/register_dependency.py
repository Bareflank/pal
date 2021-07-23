class CRegisterDependencyWriter():

    def declare_register_dependencies(self, outfile, register, config):
        if config.stdint_header:
            outfile.write('#include "' + str(config.stdint_header) + '"')
        else:
            outfile.write("#include <stdint.h>")
        self.write_newline(outfile)

        if register.component:
            outfile.write('#include "' + str(register.component) + '.h"')
            self.write_newline(outfile)
