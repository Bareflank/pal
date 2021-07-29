from pal.writer.access_mechanism.access_mechanism \
    import AccessMechanismWriter
from pal.logger import logger
from pal.exception import PalWriterException


class GasX86_64AttSyntaxAccessMechanismWriter(AccessMechanismWriter):

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

    def _call_vmread_access_mechanism(self, outfile, register,
                                      access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.encoding)) + ", %%rdi",
                "vmread %%rdi, %q[v]",
            ],
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"rdi"'
        )

    def _call_xgetbv_access_mechanism(self, outfile, register,
                                      access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.register)) + ", %%rcx",
                "xgetbv",
                "shl $32, %%rdx",
                "or %%rdx, %%rax",
                "mov %%rax, %[v]",
            ],
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_memory_read_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 8:
            mov_suffix = "b"
        elif register.size == 16:
            mov_suffix = "w"
        elif register.size == 32:
            mov_suffix = "l"
        elif register.size == 64:
            mov_suffix = "q"
        else:
            msg = "Reading memory-mapped register {name}{component} with irregular "
            msg += "size {size} is not supported through the x86_64 gnu "
            msg += "inline-assembler (AT&T syntax) access mechanism"
            msg = msg.format(
                name=register.name,
                component= " in component " + register.component if register.component else "",
                size=str(register.size)
            )
            raise PalWriterException(msg)

        self._write_inline_assembly(outfile, [
                "mov" + mov_suffix + " (%[a]), %[v]",
            ],
            inputs='[a] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_read_pci_config_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if access_mechanism.offset % 4 == 0:
            shift_instruction = ""
        elif access_mechanism.offset % 4 == 1:
            shift_instruction = "shr $8, %[v]"
        elif access_mechanism.offset % 4 == 2:
            shift_instruction = "shr $16, %[v]"
        elif access_mechanism.offset % 4 == 3:
            shift_instruction = "shr $24, %[v]"
        else:
            raise PalWriterException("Invalid offset for read_pci_config access mechanism: " + str(access_mechanism.offest))

        if register.size == 8:
            mask_instruction = "and $0xFF, %[v]"
        elif register.size == 16:
            mask_instruction = "and $0xFFFF, %[v]"
        elif register.size == 32:
            mask_instruction = ""
        else:
            raise PalWriterException("Invalid register size for read_pci_config access mechanism: " + str(register.size))

        self._write_inline_assembly(outfile, [
                "mov $0xCF8, %%dx",
                "mov %[a], %%eax",
                "outl %%eax, %%dx",
                "mov $0xCFC, %%dx",
                "inl %%dx, %%eax",
                "mov %%eax, %[v]",
                shift_instruction,
                mask_instruction,
            ],
            inputs='[a] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"eax", "dx"'
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

    def _call_vmwrite_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.encoding)) + ", %%rdi",
                "vmwrite %q[v], %%rdi",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rdi"'
        )

    def _call_xsetbv_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "mov $" + str(hex(access_mechanism.register)) + ", %%rcx",
                "mov %[v], %%rax",
                "mov %[v], %%rdx",
                "shr $32, %%rdx",
                "xsetbv",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_memory_write_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 8:
            mov_suffix = "b"
        elif register.size == 16:
            mov_suffix = "w"
        elif register.size == 32:
            mov_suffix = "l"
        elif register.size == 64:
            mov_suffix = "q"
        else:
            msg = "Writing memory-mapped register {name}{component} with irregular "
            msg += "size {size} is not supported through the x86_64 gnu "
            msg += "inline-assembler (AT&T Syntax) access mechanism"
            msg = msg.format(
                name=register.name,
                component= " in component " + register.component if register.component else "",
                size=str(register.size)
            )
            raise PalWriterException(msg)

        self._write_inline_assembly(outfile, [
                "mov" + mov_suffix + " %[v], (%[a])",
            ],
            inputs='[a] "r"(address), [v] "r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_write_pci_config_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 32 and access_mechanism.offset % 4 == 0:
            self._write_inline_assembly(outfile, [
                    "mov $0xCF8, %%dx",
                    "mov %[a], %%eax",
                    "outl %%eax, %%dx",
                    "mov $0xCFC, %%dx",
                    "mov %[v], %%eax",
                    "outl %%eax, %%dx",
                ],
                inputs='[a] "r"(address), [v] "r"(' + str(result) + ')',
                clobbers='"eax", "dx"'
            )
        else:
            if access_mechanism.offset % 4 == 0:
                shift_instruction = ""
            elif access_mechanism.offset % 4 == 1:
                shift_instruction = "shl $8, %[v]"
            elif access_mechanism.offset % 4 == 2:
                shift_instruction = "shl $16, %[v]"
            elif access_mechanism.offset % 4 == 3:
                shift_instruction = "shl $24, %[v]"
            else:
                raise PalWriterException("Invalid offset for write_pci_config access mechanism: " + str(access_mechanism.offest))

            if register.size == 8:
                mask_instruction = "and $0xFF, %[v]"
            elif register.size == 16:
                mask_instruction = "and $0xFFFF, %[v]"
            elif register.size == 32:
                mask_instruction = ""
            else:
                raise PalWriterException("Invalid register size for write_pci_config access mechanism: " + str(register.size))

            self._write_inline_assembly(outfile, [
                    "mov $0xCF8, %%dx",
                    "mov %[a], %%eax",
                    "outl %%eax, %%dx",
                    "mov $0xCFC, %%dx",
                    "inl %%dx, %%eax",
                    mask_instruction,
                    shift_instruction,
                    "or %k[v], %%eax",
                    "outl %%eax, %%dx",
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
