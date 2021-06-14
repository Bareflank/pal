from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter
from pal.logger import logger

class RustLibpalAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register,
                                       access_mechanism):
        pass

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        access_mechanisms = {
            'cpuid': self.__call_cpuid_access_mechanism,
            'rdmsr': self.__call_rdmsr_access_mechanism,
            'vmread': self.__call_vmread_access_mechanism,
            'mov_read': self.__call_mov_read_access_mechanism,
            'xgetbv': self.__call_xgetbv_read_access_mechanism,
        }

        if access_mechanism.name not in access_mechanisms:
            msg = "Access mechnism {am} is not supported using libpal from Rust"
            msg = msg.format(am=access_mechanism.name)
            logger.warn(msg)

            return

        access_mechanisms[access_mechanism.name](outfile, register, access_mechanism)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        access_mechanisms = {
            'mov_write': self.__call_mov_write_access_mechanism,
            'wrmsr': self.__call_wrmsr_access_mechanism,
            'vmwrite': self.__call_vmwrite_access_mechanism,
            'xsetbv': self.__call_xsetbv_access_mechansim,
        }

        if access_mechanism.name not in access_mechanisms:
            msg = "Access mechnism {am} is not supported using libpal from Rust"
            msg = msg.format(am=access_mechanism.name)
            logger.warn(msg)

            return

        access_mechanisms[access_mechanism.name](outfile,register,
                                                 access_mechanism, value)

    def __call_cpuid_access_mechanism(self, outfile, register, access_mechanism):

        cpuid_args = [str(access_mechanism.leaf), '0']

        if register.is_indexed:
            cpuid_args[1] = 'index as u32'

        output_variable_names = "_eax, _ebx, _ecx, _edx"
        if(access_mechanism.output == "eax"):
            output_variable_names = output_variable_names.replace("_eax", "eax")
        if(access_mechanism.output == "ebx"):
            output_variable_names = output_variable_names.replace("_ebx", "ebx")
        if(access_mechanism.output == "ecx"):
            output_variable_names = output_variable_names.replace("_ecx", "ecx")
        if(access_mechanism.output == "edx"):
            output_variable_names = output_variable_names.replace("_edx", "edx")

        outfile.write('let ({}) = instruction::execute_cpuid({});'.format(
            output_variable_names,
            ','.join(cpuid_args)
        ))
        self.write_newline(outfile)
        outfile.write(str(access_mechanism.output))
        self.write_newline(outfile)

    def __call_rdmsr_access_mechanism(self, outfile, reigster, access_mechanism):
        outfile.write('instruction::execute_rdmsr({})'.format(hex(access_mechanism.address)))
        self.write_newline(outfile)

    def __call_vmread_access_mechanism(self, outfile, register, access_mechanism):
        outfile.write('instruction::execute_vmread({}){}'.format(
            hex(access_mechanism.encoding),
            "" if register.size == 64 else "as u" + str(register.size)
        ))
        self.write_newline(outfile)

    def __call_mov_read_access_mechanism(self, outfile, register, access_mechanism):
        outfile.write('instruction::execute_read_{}()'.format(access_mechanism.source_mnemonic))
        self.write_newline(outfile)

    def __call_mov_write_access_mechanism(self, outfile, register, access_mechanism, value):
        outfile.write('instruction::execute_write_{}({})'.format(access_mechanism.destination_mnemonic, value))
        self.write_newline(outfile)

    def __call_wrmsr_access_mechanism(self, outfile, register, access_mechanism, value):
        outfile.write('instruction::execute_wrmsr({}, {})'.format(hex(access_mechanism.address),value))
        self.write_newline(outfile)

    def __call_vmwrite_access_mechanism(self, outfile, register, access_mechanism, value):
        outfile.write('instruction::execute_vmwrite({}, {}{})'.format(
            hex(access_mechanism.encoding),
            value,
            "" if register.size == 64 else " as u64"
        ))
        self.write_newline(outfile)

    def __call_xgetbv_read_access_mechanism(self, outfile, register, access_mechanism):

        outfile.write('instruction::execute_xgetbv({})'.format(hex(access_mechanism.register)))
        self.write_newline(outfile)

    def __call_xsetbv_access_mechansim(self, outfile, register, access_mechanism, value):
        outfile.write('instruction::execute_xsetbv({}, {})'.format(hex(access_mechanism.register),value))
        self.write_newline(outfile)
