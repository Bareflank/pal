from pal.logger import logger
from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter


class GasAarch32AccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register):
        pass

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, result):
        if access_mechanism.name == "mrc":
            self._call_mrc_access_mechanism(outfile, register,
                                            access_mechanism, result)
        elif access_mechanism.name == "mrrc":
            self._call_mrrc_access_mechanism(outfile, register,
                                             access_mechanism, result)
        elif access_mechanism.name == "vmrs":
            self._call_vmrs_access_mechanism(outfile, register,
                                             access_mechanism, result)
        elif access_mechanism.name == "mrs_banked":
            self._call_mrs_banked_access_mechanism(outfile, register,
                                                   access_mechanism, result)
        elif access_mechanism.name == "ldr":
            self._call_ldr_access_mechanism(outfile, register,
                                            access_mechanism, result)
        else:
            msg = "Access mechanism {am} is not supported using "
            msg += "aarch32 gas intel assembler syntax ({register})"
            msg = msg.format(
                am=access_mechanism.name,
                register=register.name
            )
            logger.warn(msg)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        if access_mechanism.name == "mcr":
            self._call_mcr_access_mechanism(outfile, register,
                                            access_mechanism, value)
        elif access_mechanism.name == "mcrr":
            self._call_mcrr_access_mechanism(outfile, register,
                                             access_mechanism, value)
        elif access_mechanism.name == "vmsr":
            self._call_vmsr_access_mechanism(outfile, register,
                                             access_mechanism, value)
        elif access_mechanism.name == "msr_banked":
            self._call_msr_banked_access_mechanism(outfile, register,
                                                   access_mechanism, value)
        elif access_mechanism.name == "str":
            self._call_str_access_mechanism(outfile, register,
                                            access_mechanism, value)
        else:
            msg = "Access mechanism {am} is not supported using "
            msg += "aarch32 gas intel assembler syntax ({register})"
            msg = msg.format(
                am=access_mechanism.name,
                register=register.name
            )
            logger.warn(msg)

    def _call_mrc_access_mechanism(self, outfile, register,
                                   access_mechanism, result):
        mrc_mnemonic = "mrc p{coproc} #{opc1} %[v] c{crn} c{crm} #{opc2}".format(
            coproc=access_mechanism.coproc,
            opc1=access_mechanism.opc1,
            opc2=access_mechanism.opc2,
            crn=access_mechanism.crn,
            crm=access_mechanism.crm,
        )
        self._write_inline_assembly(outfile, [
                str(mrc_mnemonic)
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_mrrc_access_mechanism(self, outfile, register,
                                    access_mechanism, result):
        self._declare_variable(outfile, "r1", 0, keywords=["volatile", "uint32_t"])
        self._declare_variable(outfile, "r2", 0, keywords=["volatile", "uint32_t"])
        mrrc_mnemonic = "mrrc p{coproc} #{opc1} %[v1] %[v2] c{crm}".format(
            coproc=access_mechanism.coproc,
            opc1=access_mechanism.opc1,
            crm=access_mechanism.crm,
        )
        self._write_inline_assembly(outfile, [
                str(mrrc_mnemonic)
            ],
            outputs='[v1] "=r"(r1), [v2] "=r"(r2)'
        )
        outfile.write(str(result) + " = (uint64_t)r1 & ((uint64_t)r2 << 32);")
        self.write_newline(outfile)

    def _call_vmrs_access_mechanism(self, outfile, register,
                                    access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "vmrs %[v], " + access_mechanism.operand_mnemonic
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_mrs_banked_access_mechanism(self, outfile, register,
                                          access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mrs %[v], " + access_mechanism.operand_mnemonic
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_mcr_access_mechanism(self, outfile, register,
                                   access_mechanism, value):
        mcr_mnemonic = "mcr p{coproc} #{opc1} %[v] c{crn} c{crm} #{opc2}".format(
            coproc=access_mechanism.coproc,
            opc1=access_mechanism.opc1,
            opc2=access_mechanism.opc2,
            crn=access_mechanism.crn,
            crm=access_mechanism.crm,
        )
        self._write_inline_assembly(outfile, [
                str(mcr_mnemonic),
            ],
            inputs='[v] "r"(' + value + ')'
        )

    def _call_mcrr_access_mechanism(self, outfile, register,
                                    access_mechanism, value):
        self._declare_variable(outfile, "r1", 0, keywords=["volatile", "uint32_t"])
        self._declare_variable(outfile, "r2", 0, keywords=["volatile", "uint32_t"])
        outfile.write("r1 = (uint64_t)" + str(value) + " & 0x00000000FFFFFFFF;")
        outfile.write("r2 = ((uint64_t)" + str(value) + " & 0xFFFFFFFF00000000) >> 32;")
        self.write_newline(outfile)
        mrrc_mnemonic = "mrrc p{coproc} #{opc1} %[v1] %[v2] c{crm}".format(
            coproc=access_mechanism.coproc,
            opc1=access_mechanism.opc1,
            crm=access_mechanism.crm,
        )
        self._write_inline_assembly(outfile, [
                str(mrrc_mnemonic)
            ],
            inputs='[v1] "r"(r1), [v2] "r"(r2)'
        )

    def _call_vmsr_access_mechanism(self, outfile, register,
                                    access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "vmsr " + access_mechanism.operand_mnemonic + ", %[v]",
            ],
            inputs='[v] "r"(' + value + ')'
        )

    def _call_msr_banked_access_mechanism(self, outfile, register,
                                    access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "msr " + access_mechanism.operand_mnemonic + ", %[v]",
            ],
            inputs='[v] "r"(' + value + ')'
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
