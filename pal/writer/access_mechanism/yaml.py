from pal.writer.access_mechanism.access_mechanism import AccessMechanismWriter


class YamlAccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register):
        outfile.write("  access_mechanisms:")
        self.write_newline(outfile)

        for am_name, am_list in register.access_mechanisms.items():
            for am in am_list:
                self.write_indent(outfile, count=3)
                outfile.write("- name: " + str(am.name))
                self.write_newline(outfile)

                if am.name == "ldr" or am.name == "str":
                    self.write_indent(outfile, count=4)
                    outfile.write("component: " + str(am.component))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("offset: " + str(hex(am.offset)))
                    self.write_newline(outfile)

                if am.name == "mcr" or am.name == "mrc":
                    self.write_indent(outfile, count=4)
                    outfile.write("coproc: " + str(hex(am.coproc)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("opc1: " + str(hex(am.opc1)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("opc2: " + str(hex(am.opc2)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("crm: " + str(hex(am.crm)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("crn: " + str(hex(am.crn)))
                    self.write_newline(outfile)

                if am.name == "mcrr" or am.name == "mrrc":
                    self.write_indent(outfile, count=4)
                    outfile.write("coproc: " + str(hex(am.coproc)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("opc1: " + str(hex(am.opc1)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("crm: " + str(hex(am.crm)))
                    self.write_newline(outfile)

                if am.name == "mrs_banked" or am.name == "msr_banked":
                    self.write_indent(outfile, count=4)
                    outfile.write("m: " + str(hex(am.m)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("r: " + str(hex(am.r)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("m1: " + str(hex(am.m1)))
                    self.write_newline(outfile)

                if am.name == "msr_register" or am.name == "mrs_register":
                    self.write_indent(outfile, count=4)
                    outfile.write("op0: " + str(hex(am.op0)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("op1: " + str(hex(am.op1)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("op2: " + str(hex(am.op2)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("crm: " + str(hex(am.crm)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("crn: " + str(hex(am.crn)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("operand_mnemonic: " + str(am.operand_mnemonic))
                    self.write_newline(outfile)

                if am.name == "vmsr" or am.name == "vmrs":
                    self.write_indent(outfile, count=4)
                    outfile.write("reg: " + str(am.reg))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("operand_mnemonic: " + str(am.operand_mnemonic))
                    self.write_newline(outfile)

                if am.name == "mov_read":
                    self.write_indent(outfile, count=4)
                    outfile.write("source_mnemonic: " + str(am.source_mnemonic))
                    self.write_newline(outfile)

                if am.name == "mov_write":
                    self.write_indent(outfile, count=4)
                    outfile.write("destination_mnemonic: " + str(am.destination_mnemonic))
                    self.write_newline(outfile)

                if am.name == "cpuid":
                    self.write_indent(outfile, count=4)
                    outfile.write("leaf: " + str(hex(am.leaf)))
                    self.write_newline(outfile)

                    self.write_indent(outfile, count=4)
                    outfile.write("output: " + str(am.output))
                    self.write_newline(outfile)

                if am.name == "rdmsr" or am.name == "wrmsr":
                    self.write_indent(outfile, count=4)
                    outfile.write("address: " + str(hex(am.address)))
                    self.write_newline(outfile)

                if am.name == "vmread" or am.name == "vmwrite":
                    self.write_indent(outfile, count=4)
                    outfile.write("encoding: " + str(hex(am.encoding)))
                    self.write_newline(outfile)

                self.write_newline(outfile)

    def call_readable_access_mechanism(self, outfile, register,
                                       access_mechanism, var):
        pass

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        pass
