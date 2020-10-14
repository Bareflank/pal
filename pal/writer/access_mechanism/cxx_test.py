from pal.writer.access_mechanism.access_mechanism \
        import AccessMechanismWriter


class CxxTestAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register,
                                       access_mechanism):
        if register.size == 32:
            size_t = "uint32_t"
        else:
            size_t = "uint64_t"

        mock_reg_name = register.name.lower() + "_mock_register"
        self._declare_variable(outfile, mock_reg_name, value=0,
                               keywords=["static", size_t])



    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        mock_reg_name = register.name.lower() + "_mock_register"
        outfile.write(str(result) + " = " + mock_reg_name + ";")
        self.write_newline(outfile)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        mock_reg_name = register.name.lower() + "_mock_register"
        outfile.write(mock_reg_name + " = " + str(value) + str(";"))
        self.write_newline(outfile)
