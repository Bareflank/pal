from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter
from pal.logger import logger
from pal.exception import PalWriterException

class LibpalAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register,
                                       access_mechanism):
        access_mechanisms = {
            'cpuid': self.__declare_cpuid_dependencies,
            'rdmsr': self.__declare_rdmsr_dependencies,
            'wrmsr': self.__declare_wrmsr_dependencies,
            'vmread': self.__declare_vmread_dependencies,
            'vmwrite': self.__declare_vmwrite_dependencies,
            'mov_read': self.__declare_mov_read_dependencies,
            'mov_write': self.__declare_mov_write_dependencies,
            'xgetbv': self.__declare_xgetbv_dependencies,
            'xsetbv': self.__declare_xsetbv_dependencies,
            'read': self.__declare_read_dependencies,
            'write': self.__declare_write_dependencies,
        }

        if access_mechanism.name not in access_mechanisms:
            return

        access_mechanisms[access_mechanism.name](outfile, register,
                                                 access_mechanism)

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        access_mechanisms = {
            'cpuid': self.__call_cpuid_access_mechanism,
            'rdmsr': self.__call_rdmsr_access_mechanism,
            'vmread': self.__call_vmread_access_mechanism,
            'mov_read': self.__call_mov_read_access_mechanism,
            'xgetbv': self.__call_xgetbv_read_access_mechanism,
            'read': self.__call_memory_read_access_mechanism,
        }

        if access_mechanism.name not in access_mechanisms:
            msg = "Access mechnism {am} is not supported using libpal"
            msg = msg.format(am=access_mechanism.name)
            raise PalWriterException(msg)

        access_mechanisms[access_mechanism.name](outfile,register,
                                                 access_mechanism, result)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        access_mechanisms = {
            'mov_write': self.__call_mov_write_access_mechanism,
            'wrmsr': self.__call_wrmsr_access_mechanism,
            'vmwrite': self.__call_vmwrite_access_mechanism,
            'xsetbv': self.__call_xsetbv_access_mechansim,
            'write': self.__call_memory_write_access_mechanism,
        }

        if access_mechanism.name not in access_mechanisms:
            msg = "Access mechnism {am} is not supported using libpal"
            msg = msg.format(am=access_mechanism.name)
            raise PalWriterException(msg)

        access_mechanisms[access_mechanism.name](outfile,register,
                                                 access_mechanism, value)

    def __declare_cpuid_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/cpuid.h>")
        self.write_newline(outfile)
        outfile.write("#include <string.h>")    # <-- For memset
        self.write_newline(outfile)


    def __declare_rdmsr_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/rdmsr.h>")
        self.write_newline(outfile)


    def __declare_wrmsr_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/wrmsr.h>")
        self.write_newline(outfile)


    def __declare_vmread_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/vmread.h>")
        self.write_newline(outfile)


    def __declare_vmwrite_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/vmwrite.h>")
        self.write_newline(outfile)


    def __declare_mov_read_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write('#include <pal/instruction/read_{}.h>'.format(access_mechanism.source_mnemonic))
        self.write_newline(outfile)


    def __declare_mov_write_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write('#include <pal/instruction/write_{}.h>'.format(access_mechanism.destination_mnemonic))
        self.write_newline(outfile)


    def __declare_xgetbv_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/xgetbv.h>")
        self.write_newline(outfile)


    def __declare_xsetbv_dependencies(self, outfile, register,
                                      access_mechanism):
        outfile.write("#include <pal/instruction/xsetbv.h>")
        self.write_newline(outfile)

    def __declare_read_dependencies(self, outfile, register,
                                      access_mechanism):
            if register.size == 8:
                outfile.write('#include "pal/instruction/read_mem8.h"')
                self.write_newline(outfile)
            elif register.size == 16:
                outfile.write('#include "pal/instruction/read_mem16.h"')
                self.write_newline(outfile)
            elif register.size == 32:
                outfile.write('#include "pal/instruction/read_mem32.h"')
                self.write_newline(outfile)
            elif register.size == 64:
                outfile.write('#include "pal/instruction/read_mem64.h"')
                self.write_newline(outfile)
            else:
                msg = "Reading memory-mapped register {name}{component} with irregular "
                msg += "size {size} is not yet supported by the libpal access mechanism"
                msg = msg.format(
                    name=register.name,
                    component= " in component " + register.component if register.component else "",
                    size=str(register.size)
                )
                raise PalWriterException(msg)

    def __declare_write_dependencies(self, outfile, register,
                                      access_mechanism):
            if register.size == 8:
                outfile.write('#include "pal/instruction/write_mem8.h"')
                self.write_newline(outfile)
            elif register.size == 16:
                outfile.write('#include "pal/instruction/write_mem16.h"')
                self.write_newline(outfile)
            elif register.size == 32:
                outfile.write('#include "pal/instruction/write_mem32.h"')
                self.write_newline(outfile)
            elif register.size == 64:
                outfile.write('#include "pal/instruction/write_mem64.h"')
                self.write_newline(outfile)
            else:
                msg = "Writing memory-mapped register {name}{component} with irregular "
                msg += "size {size} is not yet supported by the libal access mechanism"
                msg = msg.format(
                    name=register.name,
                    component= " in component " + register.component if register.component else "",
                    size=str(register.size)
                )
                raise PalWriterException(msg)


    def __call_cpuid_access_mechanism(self, outfile, register,
                                      access_mechanism, result):

        cpuid_args = [str(access_mechanism.leaf), '0']

        if register.is_indexed:
            cpuid_args[1] = 'index'

        self.write_newline(outfile);

        outfile.write('pal_cpuid_return_values cpuid_return_values;')
        self.write_newline(outfile);

        outfile.write('memset(&cpuid_return_values, 0, sizeof(cpuid_return_values));')
        self.write_newline(outfile);

        outfile.write('cpuid_return_values = pal_execute_cpuid({});'.format(','.join(cpuid_args)))
        self.write_newline(outfile);

        outfile.write('{} = cpuid_return_values.{};'.format(result,access_mechanism.output))
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
        outfile.write('{} = pal_execute_read_{}();'.format(result, access_mechanism.source_mnemonic))
        self.write_newline(outfile)
        self.write_newline(outfile)

    def __call_mov_write_access_mechanism(self, outfile, register,
                                          access_mechanism, value):
        outfile.write('pal_execute_write_{}({});'.format(access_mechanism.destination_mnemonic, value))
        self.write_newline(outfile)

    def __call_wrmsr_access_mechanism(self, outfile, register,
                                      access_mechanism, value):
        outfile.write('pal_execute_wrmsr({},{});'.format(hex(access_mechanism.address),value))
        self.write_newline(outfile)

    def __call_vmwrite_access_mechanism(self, outfile, register,
                                        access_mechanism, value):
        outfile.write('pal_execute_vmwrite({},{});'.format(hex(access_mechanism.encoding), value))
        self.write_newline(outfile)

    def __call_xgetbv_read_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        self.write_newline(outfile)
        outfile.write('{} = pal_execute_xgetbv({});'.format(result, hex(access_mechanism.register)))
        self.write_newline(outfile)
        self.write_newline(outfile)

    def __call_xsetbv_access_mechansim(self, outfile, register,
                                       access_mechanism, value):
        outfile.write('pal_execute_xsetbv({},{});'.format(hex(access_mechanism.register),value))
        self.write_newline(outfile)

    def __call_memory_read_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        self.write_newline(outfile)
        outfile.write('{} = pal_execute_read_mem{}(address);'.format(
            result,
            str(register.size),
        ))
        self.write_newline(outfile)
        self.write_newline(outfile)

    def __call_memory_write_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        self.write_newline(outfile)
        outfile.write('pal_execute_write_mem{}(address, {});'.format(
            str(register.size),
            result,
        ))
        self.write_newline(outfile)
        self.write_newline(outfile)
