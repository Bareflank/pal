from pal.writer.access_mechanism.access_mechanism \
        import AccessMechanismWriter
from pal.logger import logger
from pal.exception import PalWriterException


class GasX86_64IntelSyntaxAccessMechanismWriter(AccessMechanismWriter):

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
            msg += "Intel x86_64 gas intel assembler syntax"
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
            msg += "Intel x86_64 gas intel assembler syntax"
            msg = msg.format(
                am=access_mechanism.name
            )
            raise PalWriterException(msg)

    def _call_mov_read_access_mechanism(self, outfile, register,
                                        access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mov %[v], " + access_mechanism.source_mnemonic
            ],
            outputs='[v] "=r"(' + str(result) + ')'
        )

    def _call_cpuid_access_mechanism(self, outfile, register, access_mechanism,
                                     result):
        if register.is_indexed:
            subleaf_mnemonic = "%[subleaf]"
            subleaf_input = '[subleaf] "r"(index)'
        else:
            subleaf_mnemonic = "0"
            subleaf_input = ""

        self._write_inline_assembly(outfile, [
                "mov eax, " + str(hex(access_mechanism.leaf)),
                "mov ecx, " + subleaf_mnemonic,
                "cpuid",
                "mov %[out], " + access_mechanism.output
            ],
            outputs='[out] "=r"(' + result + ')',
            inputs=subleaf_input,
            clobbers='"eax", "ebx", "ecx", "edx"'
        )

    def _call_rdmsr_access_mechanism(self, outfile, register, access_mechanism,
                                     result):
        self._write_inline_assembly(outfile, [
                "mov rcx, " + str(hex(access_mechanism.address)),
                "rdmsr",
                "shl rdx, 32",
                "or rax, rdx",
                "mov %[v], rax",
            ],
            outputs='[v] "=r"(' + result + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_vmread_access_mechanism(self, outfile, register,
                                      access_mechanism, result):
        self._write_inline_assembly(outfile, [
                "mov rdi, " + str(hex(access_mechanism.encoding)),
                "vmread %q[v], rdi",
            ],
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"rdi"'
        )

    def _call_xgetbv_access_mechanism(self, outfile, register, access_mechanism,
                                      result):
        self._write_inline_assembly(outfile, [
                "mov rcx, " + str(hex(access_mechanism.register)),
                "xgetbv",
                "shl rdx, 32",
                "or rax, rdx",
                "mov %[v], rax",
            ],
            outputs='[v] "=r"(' + result + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_memory_read_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 8:
            access_size = "BYTE"
        elif register.size == 16:
            access_size = "WORD"
        elif register.size == 32:
            access_size = "DWORD"
        elif register.size == 64:
            access_size = "QWORD"
        else:
            msg = "Reading memory-mapped register {name}{component} with irregular "
            msg += "size {size} is not supported through the x86_64 gnu "
            msg += "inline-assembler (Intel syntax) access mechanism"
            msg = msg.format(
                name=register.name,
                component= " in component " + register.component if register.component else "",
                size=str(register.size)
            )
            raise PalWriterException(msg)

        self._write_inline_assembly(outfile, [
                "mov %[v], " + access_size + " [%[a]]",
            ],
            inputs='[a] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_mov_write_access_mechanism(self, outfile, register,
                                         access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "mov " + access_mechanism.destination_mnemonic + ", %[v]",
            ],
            inputs='[v] "r"(' + value + ')'
        )

    def _call_read_pci_config_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if access_mechanism.offset % 4 == 0:
            shift_instruction = ""
        elif access_mechanism.offset % 4 == 1:
            shift_instruction = "shr %[v], 8"
        elif access_mechanism.offset % 4 == 2:
            shift_instruction = "shr %[v], 16"
        elif access_mechanism.offset % 4 == 3:
            shift_instruction = "shr %[v], 24"
        else:
            raise PalWriterException("Invalid offset for read_pci_config access mechanism: " + str(access_mechanism.offest))

        if register.size == 8:
            mask_instruction = "and %[v], 0xFF"
        elif register.size == 16:
            mask_instruction = "and %[v], 0xFFFF"
        elif register.size == 32:
            mask_instruction = ""
        else:
            raise PalWriterException("Invalid register size for read_pci_config access mechanism: " + str(register.size))

        self._write_inline_assembly(outfile, [
                "mov dx, 0xCF8",
                "mov eax, %[a]",
                "out dx, eax",
                "mov dx, 0xCFC",
                "in eax, dx",
                "mov %[v], eax",
                shift_instruction,
                mask_instruction,
            ],
            inputs='[a] "r"(address)',
            outputs='[v] "=r"(' + str(result) + ')',
            clobbers='"eax", "dx"'
        )

    def _call_wrmsr_access_mechanism(self, outfile, register, access_mechanism,
                                     value):
        self._write_inline_assembly(outfile, [
                "mov rcx, " + str(hex(access_mechanism.address)),
                "mov rax, %[v]",
                "mov rdx, %[v]",
                "shr rdx, 32",
                "wrmsr",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_vmwrite_access_mechanism(self, outfile, register,
                                       access_mechanism, value):
        self._write_inline_assembly(outfile, [
                "mov rdi, " + str(hex(access_mechanism.encoding)),
                "vmwrite rdi, %q[v]",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rdi"'
        )

    def _call_xsetbv_access_mechanism(self, outfile, register, access_mechanism,
                                      value):
        self._write_inline_assembly(outfile, [
                "mov rcx, " + str(hex(access_mechanism.register)),
                "mov rax, %[v]",
                "mov rdx, %[v]",
                "shr rdx, 32",
                "xsetbv",
            ],
            inputs='[v] "r"(' + value + ')',
            clobbers='"rax", "rcx", "rdx"'
        )

    def _call_memory_write_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 8:
            access_size = "BYTE"
        elif register.size == 16:
            access_size = "WORD"
        elif register.size == 32:
            access_size = "DWORD"
        elif register.size == 64:
            access_size = "QWORD"
        else:
            msg = "Writing memory-mapped register {name}{component} with irregular "
            msg += "size {size} is not supported through the x86_64 gnu "
            msg += "inline-assembler (Intel Syntax) access mechanism"
            msg = msg.format(
                name=register.name,
                component= " in component " + register.component if register.component else "",
                size=str(register.size)
            )
            raise PalWriterException(msg)

        self._write_inline_assembly(outfile, [
                "mov " + access_size + " [%[a]], %[v]",
            ],
            inputs='[a] "r"(address), [v] "r"(' + str(result) + ')',
            clobbers='"memory"'
        )

    def _call_write_pci_config_access_mechanism(self, outfile, register,
                                            access_mechanism, result):
        if register.size == 32:
            self._write_inline_assembly(outfile, [
                    "mov dx, 0xCF8",
                    "mov eax, %[a]",
                    "out dx, eax",
                    "mov dx, 0xCFC",
                    "mov eax, %[v]",
                    "out dx, eax",
                ],
                inputs='[a] "r"(address), [v] "r"(' + str(result) + ')',
                clobbers='"eax", "dx"'
            )
        else:
            if access_mechanism.offset % 4 == 0:
                shift_instruction = ""
            elif access_mechanism.offset % 4 == 1:
                shift_instruction = "shl %[v], 8"
            elif access_mechanism.offset % 4 == 2:
                shift_instruction = "shl %[v], 16"
            elif access_mechanism.offset % 4 == 3:
                shift_instruction = "shl %[v], 24"
            else:
                raise PalWriterException("Invalid offset for write_pci_config access mechanism: " + str(access_mechanism.offest))

            if register.size == 8:
                mask_instruction = "and %[v], 0xFF"
            elif register.size == 16:
                mask_instruction = "and %[v], 0xFFFF"
            elif register.size == 32:
                mask_instruction = ""
            else:
                raise PalWriterException("Invalid register size for write_pci_config access mechanism: " + str(register.size))

            self._write_inline_assembly(outfile, [
                    "mov dx, 0xCF8",
                    "mov eax, %[a]",
                    "out dx, eax",
                    "mov dx, 0xCFC",
                    "in eax, dx",
                    mask_instruction,
                    shift_instruction,
                    "or eax, %k[v]",
                    "out dx, eax",
                ],
                inputs='[a] "r"(address)',
                outputs='[v] "+r"(' + str(result) + ')',
                clobbers='"eax", "dx"'
            )

    def _write_inline_assembly(self, outfile, statements, outputs="",
                               inputs="", clobbers=""):
        outfile.write("__asm__ __volatile__(\n")
        for statement in statements:
            if statement:
                outfile.write("    \"" + str(statement) + ";\"\n")

        outfile.write("    : " + str(outputs) + "\n")
        outfile.write("    : " + str(inputs) + "\n")
        outfile.write("    : " + str(clobbers) + "\n")
        outfile.write(");")
        self.write_newline(outfile)
