from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter


class GasARMv8aIntelSyntaxAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register):
        pass

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, var):
        pass

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        pass
