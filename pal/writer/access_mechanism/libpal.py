from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter
from pal.logger import logger

class LibpalAccessMechanismWriter(AccessMechanismWriter):

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        access_mechanisms = {
            'cpuid': self.__call_cpuid_access_mechanism,
            'rdmsr': self.__call_rdmsr_access_mechanism,
            'vmread': self.__call_vmread_access_mechanism,
            'mov_read': self.__call_mov_read_access_mechanism,
        }

        if access_mechanism.name not in access_mechanisms:
            msg = "Access mechnism {am} is not supported using libpal"
            msg = msg.format(am=access_mechanism.name)
            logger.warn(msg)

            return

        access_mechanisms[access_mechanism.name](outfile,register,
                                                 access_mechanism, result)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        access_mechanisms = {
            'mov_write': self.__call_mov_write_access_mechanism,
        }

        if access_mechanism.name not in access_mechanisms:
            msg = "Access mechnism {am} is not supported using libpal"
            msg = msg.format(am=access_mechanism.name)
            logger.warn(msg)

            return

        access_mechanisms[access_mechanism.name](outfile,register,
                                                 access_mechanism, value)

    def __call_cpuid_access_mechanism(self, outfile, register,
                                      access_mechanism, result):

        cpuid_args = [str(access_mechanism.leaf), '0']

        if register.is_indexed:
            cpuid_args[1] = 'index'

        self.write_newline(outfile);

        outfile.write('pal_cpuid_register_values cpuid_register_values;')
        self.write_newline(outfile);

        outfile.write('memset(&cpuid_register_values, 0, sizeof(cpuid_register_values));')
        self.write_newline(outfile);

        outfile.write('cpuid_register_values = pal_execute_cpuid({});'.format(','.join(cpuid_args)))
        self.write_newline(outfile);

        outfile.write('{} = cpuid_register_values.{};'.format(result,access_mechanism.output))
        self.write_newline(outfile);

        self.write_newline(outfile);

    def __call_rdmsr_access_mechanism(self, outfile, reigster,
                                      access_mechanism, result):
        self.write_newline(outfile)
        outfile.write('{} = pal_execute_rdmsr({});'.format(result, hex(access_mechanism.address)))
        self.write_newline(outfile)
        self.write_newline(outfile)

    def __call_vmread_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        self.write_newline(outfile)
        outfile.write('{} = pal_execute_vmread({});'.format(result, hex(access_mechanism.encoding)))
        self.write_newline(outfile)
        self.write_newline(outfile)

    def __call_mov_read_access_mechanism(self, outfile, register,
                                         access_mechanism, result):
        self.write_newline(outfile)
        outfile.write('{} = pal_execute_{}_read();'.format(result, access_mechanism.source_mnemonic))
        self.write_newline(outfile)
        self.write_newline(outfile)

    def __call_mov_write_access_mechanism(self, outfile, register,
                                          access_mechanism, value):
        outfile.write('pal_execute_{}_write({});'.format(access_mechanism.destination_mnemonic, value))
        self.write_newline(outfile)
