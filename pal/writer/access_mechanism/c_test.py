from pal.writer.access_mechanism.access_mechanism \
        import AccessMechanismWriter


class CTestAccessMechanismWriter(AccessMechanismWriter):

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        mock_reg_name = "pal_" + register.name.lower() + "_mock_register"
        outfile.write(str(result) + " = " + mock_reg_name + ";")
        self.write_newline(outfile)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        mock_reg_name = "pal_" + register.name.lower() + "_mock_register"
        outfile.write(mock_reg_name + " = " + str(value) + str(";"))
        self.write_newline(outfile)
