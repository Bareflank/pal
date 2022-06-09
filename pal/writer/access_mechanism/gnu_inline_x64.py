from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter
from pal.logger import logger
from pal.exception import PalWriterException


class GnuInlineX64AccessMechanismWriter(AccessMechanismWriter):

    def declare_access_mechanism_dependencies(self, outfile, register,
                                       access_mechanism):
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
        elif access_mechanism.name == "vmread":
            self._call_vmread_access_mechanism(outfile, register,
                                               access_mechanism, result)
        elif access_mechanism.name == "xgetbv":
            self._call_xgetbv_access_mechanism(outfile, register,
                                               access_mechanism, result)
        elif access_mechanism.name == "read":
            self._call_memory_read_access_mechanism(outfile, register,
                                               access_mechanism, result)
        elif access_mechanism.name == "read_pci_config":
            self._call_read_pci_config_access_mechanism(outfile, register,
                                               access_mechanism, result)
        else:
            msg = "Access mechnism {am} is not supported using "
            msg += "Intel x86_64 gas att assembler syntax"
            msg = msg.format(
                am=access_mechanism.name
            )
            raise PalWriterException(msg)

    def call_writable_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        if access_mechanism.name == "mov_write":
            self._call_mov_write_access_mechanism(outfile, register,
                                                  access_mechanism, value)
        elif access_mechanism.name == "wrmsr":
            self._call_wrmsr_access_mechanism(outfile, register,
                                              access_mechanism, value)
        elif access_mechanism.name == "vmwrite":
            self._call_vmwrite_access_mechanism(outfile, register,
                                                access_mechanism, value)
        elif access_mechanism.name == "xsetbv":
            self._call_xsetbv_access_mechanism(outfile, register,
                                               access_mechanism, value)
        elif access_mechanism.name == "write":
            self._call_memory_write_access_mechanism(outfile, register,
                                               access_mechanism, value)
        elif access_mechanism.name == "write_pci_config":
            self._call_write_pci_config_access_mechanism(outfile, register,
                                               access_mechanism, value)
        else:
            msg = "Access mechnism {am} is not supported using "
            msg += "Intel x86_64 gas att assembler syntax"
            msg = msg.format(
                am=access_mechanism.name
            )
            raise PalWriterException(msg)

    def _call_mov_read_access_mechanism(self, outfile, register,
                                        access_mechanism, result):
        mnemonic = access_mechanism.source_mnemonic
        self._write_inline_assembly(outfile, [
                "mov {%%" + mnemonic + ", %[v] | %[v], " + mnemonic + "}"
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_cpuid_access_mechanism(self, outfile, register, access_mechanism,
                                     result):
        if register.arch == "intel":
            leaf_mnemonic = str(hex(access_mechanism.leaf))
        elif register.arch == "amd64":
            leaf_mnemonic = str(hex(access_mechanism.function))
        else:
            msg = "CPUID access mechanism not supported for architecture {arch}"
            msg = msg.format(
                arch=str(register.arch)
            )
            raise PalWriterException(msg)

        if register.is_indexed:
            subleaf_mnemonic_att = "%[subleaf]"
            subleaf_mnemonic_intel = "%[subleaf]"
            subleaf_input = '[subleaf] "r"(index)'
        else:
            subleaf_mnemonic_att = "$0"
            subleaf_mnemonic_intel = "0"
            subleaf_input = ""

        self._write_inline_assembly(outfile, [
                "mov {$" + leaf_mnemonic + ", %%eax | eax, " + leaf_mnemonic + "}",
                "mov {" + subleaf_mnemonic_att + ", %%ecx | ecx, " + subleaf_mnemonic_intel + "}",
                "cpuid",
                "mov {%%" + access_mechanism.output + ", %[out] | %[out], " + access_mechanism.output + "}"
            ],
            outputs='[out] "=r"(' + result + ')',
            inputs=subleaf_input,
            clobbers='"eax", "ebx", "ecx", "edx"'
        )

    def _call_rdmsr_access_mechanism(self, outfile, register, access_mechanism,
                                     result):
        address = str(hex(access_mechanism.address))
        self._write_inline_assembly(outfile, [
                "mov {$" + address + ", %%rcx | rcx, " + address + "}",
                "rdmsr",
                "shl {$32, %%rdx | rdx, 32}",
                "or {%%rdx, %%rax | rax, rdx}",
                "mov {%%rax, %[v] | %[v], rax}",
            ],
            outputs='[v] "=r"(' + result + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_vmread_access_mechanism(self, outfile, register,
                                      access_mechanism, result):
        encoding = str(hex(access_mechanism.encoding))
        self._write_inline_assembly(outfile, [
                "mov {$" + encoding + ", %%rdi | rdi, " + encoding + "}",
                "vmread {%%rdi, %q[v] | %q[v], rdi}",
            ],
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"rdi"'
        )

    def _call_xgetbv_access_mechanism(self, outfile, register,
                                      access_mechanism, result):
        register = str(hex(access_mechanism.register))
        self._write_inline_assembly(outfile, [
                "mov {$" + register + ", %%rcx | rcx, " + register + "}",
                "xgetbv",
                "shl {$32, %%rdx | rdx, 32}",
                "or {%%rdx, %%rax | rax, rdx}",
                "mov {%%rax, %[v] | %[v], rax}",
            ],
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_memory_read_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 8:
            mov_suffix = "b"
            access_size = "BYTE"
        elif register.size == 16:
            mov_suffix = "w"
            access_size = "WORD"
        elif register.size == 32:
            mov_suffix = "l"
            access_size = "DWORD"
        elif register.size == 64:
            mov_suffix = "q"
            access_size = "QWORD"
        else:
            msg = "Reading memory-mapped register {name}{component} with irregular "
            msg += "size {size} is not supported through the x86_64 gnu "
            msg += "inline-assembler access mechanism"
            msg = msg.format(
                name=register.name,
                component= " in component " + register.component if register.component else "",
                size=str(register.size)
            )
            raise PalWriterException(msg)

        self._write_inline_assembly(outfile, [
                "{mov" + mov_suffix + " (%[a]), %[v] | mov %[v], " + access_size + " [%[a]]}",
            ],
            inputs='[a] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_read_pci_config_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if access_mechanism.offset % 4 == 0:
            shift_instruction_att = ""
            shift_instruction_intel = ""
        elif access_mechanism.offset % 4 == 1:
            shift_instruction_att = "shr $8, %[v]"
            shift_instruction_intel = "shr %[v], 8"
        elif access_mechanism.offset % 4 == 2:
            shift_instruction_att = "shr $16, %[v]"
            shift_instruction_intel = "shr %[v], 16"
        elif access_mechanism.offset % 4 == 3:
            shift_instruction_att = "shr $24, %[v]"
            shift_instruction_intel = "shr %[v], 24"
        else:
            raise PalWriterException("Invalid offset for read_pci_config access mechanism: " + str(access_mechanism.offest))

        if register.size == 8:
            mask_instruction_att = "and $0xFF, %[v]"
            mask_instruction_intel = "and %[v], 0xFF"
        elif register.size == 16:
            mask_instruction_att = "and $0xFFFF, %[v]"
            mask_instruction_intel = "and %[v], 0xFFFF"
        elif register.size == 32:
            mask_instruction_att = ""
            mask_instruction_intel = ""
        else:
            raise PalWriterException("Invalid register size for read_pci_config access mechanism: " + str(register.size))

        self._write_inline_assembly(outfile, [
                "mov {$0xCF8, %%dx | dx, 0xCF8}",
                "mov {%[a], %%eax | eax, %[a]}",
                "{outl %%eax, %%dx | out dx, eax}",
                "mov {$0xCFC, %%dx | dx, 0xCFC}",
                "{inl %%dx, %%eax | in eax, dx}",
                "mov {%%eax, %[v] | %[v], eax}",
                "{" + shift_instruction_att + " | " + shift_instruction_intel + "}",
                "{" + mask_instruction_att + " | " + mask_instruction_intel + "}",
            ],
            inputs='[a] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"eax", "dx"'
        )

    def _call_mov_write_access_mechanism(self, outfile, register,
                                         access_mechanism, value):
        mnemonic = access_mechanism.destination_mnemonic
        self._write_inline_assembly(outfile, [
                "mov {%[v], %%" + mnemonic + " | " + mnemonic + ", %[v]}",
            ],
            inputs='[v] "r"(' + value + ')'
        )

    def _call_wrmsr_access_mechanism(self, outfile, register, access_mechanism,
                                     value):
        address = str(hex(access_mechanism.address))
        self._write_inline_assembly(outfile, [
                "mov {$" + address + ", %%rcx | rcx, " + address + "}",
                "mov {%[v], %%rax | rax, %[v]}",
                "mov {%[v], %%rdx | rdx, %[v]}",
                "shr {$32, %%rdx | rdx, 32}",
                "wrmsr",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_vmwrite_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        encoding = str(hex(access_mechanism.encoding))
        self._write_inline_assembly(outfile, [
                "mov {$" + encoding + ", %%rdi | rdi, " + encoding + "}",
                "vmwrite {%q[v], %%rdi | rdi, %q[v]}",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rdi"'
        )

    def _call_xsetbv_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        register = str(hex(access_mechanism.register))
        self._write_inline_assembly(outfile, [
                "mov {$" + register + ", %%rcx | rcx, " + register + "}",
                "mov {%[v], %%rax | rax, %[v]}",
                "mov {%[v], %%rdx | rdx, %[v]}",
                "shr {$32, %%rdx | rdx, 32}",
                "xsetbv",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_memory_write_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 8:
            mov_suffix = "b"
            access_size = "BYTE"
        elif register.size == 16:
            mov_suffix = "w"
            access_size = "WORD"
        elif register.size == 32:
            mov_suffix = "l"
            access_size = "DWORD"
        elif register.size == 64:
            mov_suffix = "q"
            access_size = "QWORD"
        else:
            msg = "Writing memory-mapped register {name}{component} with irregular "
            msg += "size {size} is not supported through the x86_64 gnu "
            msg += "inline-assembler access mechanism"
            msg = msg.format(
                name=register.name,
                component= " in component " + register.component if register.component else "",
                size=str(register.size)
            )
            raise PalWriterException(msg)

        self._write_inline_assembly(outfile, [
                "{mov" + mov_suffix + " %[v], (%[a]) | mov " + access_size + " [%[a]], %[v]}",
            ],
            inputs='[a] "r"(address), [v] "r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_write_pci_config_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 32 and access_mechanism.offset % 4 == 0:
            self._write_inline_assembly(outfile, [
                    "mov {$0xCF8, %%dx | dx, 0xCF8}",
                    "mov {%[a], %%eax | eax, %[a]}",
                    "{outl %%eax, %%dx | out dx, eax}",
                    "mov {$0xCFC, %%dx | dx, 0xCFC}",
                    "mov {%[v], %%eax | eax, %[v]}",
                    "{outl %%eax, %%dx | out dx, eax}",
                ],
                inputs='[a] "r"(address), [v] "r"(' + str(result) + ')',
                clobbers='"eax", "dx"'
            )
        else:
            if access_mechanism.offset % 4 == 0:
                shift_instruction_att = ""
                shift_instruction_intel = ""
            elif access_mechanism.offset % 4 == 1:
                shift_instruction_att = "shl $8, %[v]"
                shift_instruction_intel = "shl %[v], 8"
            elif access_mechanism.offset % 4 == 2:
                shift_instruction_att = "shl $16, %[v]"
                shift_instruction_intel = "shl %[v], 16"
            elif access_mechanism.offset % 4 == 3:
                shift_instruction_att = "shl $24, %[v]"
                shift_instruction_intel = "shl %[v], 24"
            else:
                raise PalWriterException("Invalid offset for write_pci_config access mechanism: " + str(access_mechanism.offest))

            if register.size == 8:
                mask_instruction_att = "and $0xFF, %[v]"
                mask_instruction_intel = "and %[v], 0xFF"
            elif register.size == 16:
                mask_instruction_att = "and $0xFFFF, %[v]"
                mask_instruction_intel = "and %[v], 0xFFFF"
            elif register.size == 32:
                mask_instruction_att = ""
                mask_instruction_intel = ""
            else:
                raise PalWriterException("Invalid register size for write_pci_config access mechanism: " + str(register.size))

            self._write_inline_assembly(outfile, [
                    "mov {$0xCF8, %%dx | dx, 0xCF8}",
                    "mov {%[a], %%eax | eax, %[a]}",
                    "{outl %%eax, %%dx | out dx, eax}",
                    "mov {$0xCFC, %%dx | dx, 0xCFC}",
                    "{inl %%dx, %%eax | in eax, dx}",
                    "{" + mask_instruction_att + " | " + mask_instruction_intel + "}",
                    "{" + shift_instruction_att + " | " + shift_instruction_intel + "}",
                    "or {%k[v], %%eax | eax, %k[v]}",
                    "{outl %%eax, %%dx | out dx, eax}",
                ],
                inputs='[a] "r"(address)',
                outputs='[v] "+r"(' + str(result) + ')',
                clobbers='"eax", "dx"'
            )

    def _write_inline_assembly(self, outfile, statements, outputs="",
                               inputs="", clobbers=""):
        outfile.write("__asm__ __volatile__(")
        self.write_newline(outfile)
        for statement in statements:
            if statement:
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
