from shoulder.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter
from shoulder.logger import logger


class GasX86_64AttSyntaxAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register):
        pass

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        if access_mechanism.name == "mov_read":
            self._call_mov_read_access_mechanism(outfile, register,
                                                 access_mechanism, result)
        elif access_mechanism.name == "cpuid":
            self._call_cpuid_access_mechanism(outfile, register,
                                              access_mechanism, result)
        elif access_mechanism.name == "rdmsr":
            self._call_rdmsr_access_mechanism(outfile, register,
                                              access_mechanism, result)
        else:
            msg = "Access mechnism {am} is not supported using "
            msg += "Intel x86_64 gas att assembler syntax".format(
                am=access_mechanism.name
            )
            logger.warn(msg)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        if access_mechanism.name == "mov_write":
            self._call_mov_write_access_mechanism(outfile, register,
                                                  access_mechanism, value)
        elif access_mechanism.name == "wrmsr":
            self._call_wrmsr_access_mechanism(outfile, register,
                                              access_mechanism, value)
        else:
            msg = "Access mechnism {am} is not supported using "
            msg += "Intel x86_64 gas att assembler syntax".format(
                am=access_mechanism.name
            )
            logger.warn(msg)

    def _call_mov_read_access_mechanism(self, outfile, register,
                                        access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mov %%" + access_mechanism.source_mnemonic + ", %[v]"
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_cpuid_access_mechanism(self, outfile, register, access_mechanism,
                                     result):
        if register.is_indexed:
            subleaf_mnemonic = "%[subleaf]"
            subleaf_input = '[subleaf] "r"(index)'
        else:
            subleaf_mnemonic = "$0"
            subleaf_input = ""

        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.leaf)) + ", %%eax",
                "mov " + subleaf_mnemonic + ", %%ecx",
                "cpuid",
                "mov %%" + access_mechanism.output + ", %[out]"
            ],
            outputs='[out] "=r"(' + result + ')',
            inputs=subleaf_input,
            clobbers='"eax", "ebx", "ecx", "edx"'
        )

    def _call_rdmsr_access_mechanism(self, outfile, register, access_mechanism,
                                     result):
        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.address)) + ", %%rcx",
                "rdmsr",
                "shl $32, %%rdx",
                "or %%rdx, %%rax",
                "mov %%rax, %[v]",
            ],
            outputs='[v] "=r"(' + result + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_mov_write_access_mechanism(self, outfile, register,
                                         access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "mov %[v], %%" + access_mechanism.destination_mnemonic,
            ],
            inputs='[v] "r"(' + value + ')'
        )

    def _call_wrmsr_access_mechanism(self, outfile, register, access_mechanism,
                                     value):
        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.address)) + ", %%rcx",
                "mov %[v], %%rax",
                "mov %[v], %%rdx",
                "shr $32, %%rdx",
                "wrmsr",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _write_inline_assembly(self, outfile, statements, outputs="",
                               inputs="", clobbers=""):
        outfile.write("__asm__ __volatile__(")
        self.write_newline(outfile)
        for statement in statements:
            self.write_indent(outfile)
            outfile.write("\"" + str(statement) + ";\"")
            self.write_newline(outfile)

        self.write_indent(outfile)
        outfile.write(": " + str(outputs))
        self.write_newline(outfile)

        self.write_indent(outfile)
        outfile.write(": " + str(inputs))
        self.write_newline(outfile)

        self.write_indent(outfile)
        outfile.write(": " + str(clobbers))
        self.write_newline(outfile)

        outfile.write(");")
        self.write_newline(outfile)
