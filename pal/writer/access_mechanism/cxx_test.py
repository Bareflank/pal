from pal.writer.access_mechanism.access_mechanism \
        import AccessMechanismWriter


class CxxTestAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register):
        if register.size == 32:
            size_t = "uint32_t"
        else:
            size_t = "uint64_t"

        self._declare_variable(outfile, "mock_register", value=0,
                               keywords=["static", size_t])

        self.write_newline(outfile)

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        outfile.write(str(result) + " = mock_register;")
        self.write_newline(outfile)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        outfile.write("mock_register = " + str(value) + str(";"))
        self.write_newline(outfile)
