from pal.logger import logger
from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter


class GasAarch64AccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register,
                                       access_mechanism):
        pass


    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        if access_mechanism.name == "mrs_register":
            self._call_mrs_register_access_mechanism(outfile, register,
                                                     access_mechanism, result)
        elif access_mechanism.name == "ldr":
            self._call_ldr_access_mechanism(outfile, register,
                                            access_mechanism, result)
        else:
            msg = "Access mechnism {am} is not supported using "
            msg += "aarch64 gas intel assembler syntax ({register})"
            msg = msg.format(
                am=access_mechanism.name,
                register=register.name
            )
            logger.warn(msg)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        if access_mechanism.name == "msr_register":
            self._call_msr_register_access_mechanism(outfile, register,
                                                     access_mechanism, result)
        elif access_mechanism.name == "str":
            self._call_str_access_mechanism(outfile, register,
                                            access_mechanism, result)
        else:
            msg = "Access mechnism {am} is not supported using "
            msg += "aarch64 gas intel assembler syntax ({register})"
            msg = msg.format(
                am=access_mechanism.name,
                register=register.name
            )
            logger.warn(msg)

    def _call_mrs_register_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mrs %[v], " + access_mechanism.operand_mnemonic
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_ldr_access_mechanism(self, outfile, register,
                                   access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "ldr %[v], [%[addr]]"
            ],
            inputs='[addr] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_msr_register_access_mechanism(self, outfile, register,
                                            access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "msr " + access_mechanism.operand_mnemonic + ", %[v]",
            ],
            inputs='[v] "r"(' + value + ')'
        )

    def _call_str_access_mechanism(self, outfile, register,
                                   access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "str %[v], [%[addr]]"
            ],
            inputs='[addr] "r"(address), [v] "r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _write_inline_assembly(self, outfile, statements, outputs="",
                               inputs="", clobbers=""):
        outfile.write("__asm__ __volatile__(\n")
        for statement in statements:
            outfile.write("    \"" + str(statement) + ";\"\n")

        outfile.write("    : " + str(outputs) + "\n")
        outfile.write("    : " + str(inputs) + "\n")
        outfile.write("    : " + str(clobbers) + "\n")
        outfile.write(");")
        self.write_newline(outfile)
