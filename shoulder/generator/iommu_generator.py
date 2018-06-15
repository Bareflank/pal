#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from shoulder.generator.abstract_generator import AbstractGenerator
from shoulder.register import Register
from shoulder.logger import logger
from shoulder.config import config
from shoulder.exception import *

class IommuGenerator(AbstractGenerator):
    def __init__(self):
        self.ifdef_name = "IOMMU_INTEL_X64_H"
        self._current_indent_level = 0

    def generate(self, objects, outpath):
        try:
            logger.info("Generating IOMMU Intrinsics to: " + str(outpath))
            with open(outpath, "w") as outfile:
                self._generate_license(outfile)
                self._generate_include_guard_open(outfile)
                self._generate_cxx_includes(outfile)
                self._generate_namespace_open(outfile)

                self._generate_global_namespace_content(objects, outfile)
                self._generate_objects(objects, outfile)

                self._generate_namespace_close(outfile)
                self._generate_include_guard_close(outfile)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g = str(type(self).__name__),
                out = outpath,
                exception = e
            )
            raise ShoulderGeneratorException(msg)

    def _generate_license(self, outfile):
        logger.debug("Writing license from: " + str(config.license_template_path))
        with open(config.license_template_path, "r") as license:
            for line in license:
                outfile.write("// " + line)
        outfile.write("\n")

    def _generate_cxx_includes(self, outfile):
        cxx_includes = "#include <stdint.h>\n"
        cxx_includes += "#include <bfgsl.h>\n"
        cxx_includes += "#include <bfbitmanip.h>\n"
        cxx_includes += "#include <bfdebug.h>\n"
        outfile.write(cxx_includes)
        outfile.write("\n")

    def _generate_include_guard_open(self, outfile):

        outfile.write("#ifndef {name}\n".format(name = self.ifdef_name))
        outfile.write("#define {name}\n".format(name = self.ifdef_name))
        outfile.write("\n")

    def _generate_include_guard_close(self, outfile):
        outfile.write("#endif\n\n")

    def _generate_namespace_open(self, outfile):
        if not config.cxx_namespace: return

        outfile.write("// *INDENT-OFF*\n\n")
        namespace_str = str(config.cxx_namespace)
        namespaces = namespace_str.split("::")
        if namespaces[0]:
            for namespace in namespaces:
                outfile.write("namespace " + namespace + "\n{\n")

    def _generate_namespace_close(self, outfile):
        if not config.cxx_namespace: return
        outfile.write("\n")
        namespace_str = str(config.cxx_namespace)
        namespaces = namespace_str.split("::")
        for namespace in namespaces:
            outfile.write("}\n")
        outfile.write("\n// *INDENT-ON*\n\n")

    def _generate_objects(self, objects, outfile):
        for obj in objects:
            if(isinstance(obj, Register)):
                logger.debug("Writing register: " + str(obj.name))
                self._generate_register(obj, outfile)
            else:
                msg = "Cannot generate object of unsupported {t} type".format(
                    t = type(obj)
                )
                raise ShoulderGeneratorException(msg)

    def _generate_global_namespace_content(self, reg, outfile):
        # IOMMU base address
        base_addr = "\n{indent}volatile uintptr_t iommu_base = 0;\n"
        base_addr = base_addr.format(
            indent = self._indent_string()
        )
        outfile.write(base_addr)

        # IOMMU getters
        accessor = "\n{indent}inline uint32_t read_iommu_32(uint32_t offset)\n"
        accessor += "{indent}{{ return *reinterpret_cast<uint32_t *>(iommu_base + offset); }}\n"
        accessor = accessor.format(
            indent = self._indent_string()
        )
        outfile.write(accessor)

        accessor = "\n{indent}inline uint64_t read_iommu_64(uint64_t offset)\n"
        accessor += "{indent}{{ return *reinterpret_cast<uint64_t *>(iommu_base + offset); }}\n"
        accessor = accessor.format(
            indent = self._indent_string()
        )
        outfile.write(accessor)

        # IOMMU setters
        accessor = "\n{indent}inline void write_iommu_32(uint32_t offset, uint32_t val)\n"
        accessor += "{indent}{{ *reinterpret_cast<uint32_t *>(iommu_base + offset) = val; }}\n"
        accessor = accessor.format(
            indent = self._indent_string()
        )
        outfile.write(accessor)

        accessor = "\n{indent}inline void write_iommu_32_preserved(uint32_t offset, uint32_t val, uint32_t mask)\n"
        accessor += "{indent}{{\n"
        accessor += "{indent}\tuint32_t reg = read_iommu_32(offset);\n"
        accessor += "{indent}\twrite_iommu_32(offset, (reg & mask) | val);\n"
        accessor += "{indent}}}\n"
        accessor = accessor.format(
            indent = self._indent_string()
        )
        outfile.write(accessor)

        accessor = "\n{indent}inline void write_iommu_64(uint64_t offset, uint64_t val)\n"
        accessor += "{indent}{{ *reinterpret_cast<uint64_t *>(iommu_base + offset) = val; }}\n"
        accessor = accessor.format(
            indent = self._indent_string()
        )
        outfile.write(accessor)

        accessor = "\n{indent}inline void write_iommu_64_preserved(uint64_t offset, uint64_t val, uint64_t mask)\n"
        accessor += "{indent}{{\n"
        accessor += "{indent}\tuint64_t reg = read_iommu_64(offset);\n"
        accessor += "{indent}\twrite_iommu_64(offset, (reg & mask) | val);\n"
        accessor += "{indent}}}\n"
        accessor = accessor.format(
            indent = self._indent_string()
        )
        outfile.write(accessor)

    def _generate_register(self, reg, outfile):
        outfile.write("\n")
        reg_namespace = "namespace {name}\n{{\n".format(name=str(reg.name).lower())
        outfile.write(reg_namespace)

        self._increase_indent()

        self._generate_constants(reg, outfile)
        self._generate_accessors(reg, outfile)
        self._generate_fieldsets(reg, outfile)
        self._generate_register_dump_function(reg, outfile)

        outfile.write("}\n")
        self._decrease_indent()

    def _generate_constants(self, reg, outfile):
        # Name
        name_val = "{indent}constexpr const auto name = \"{long_name}\";\n".format(
            indent = self._indent_string(),
            long_name = reg.long_name.lower()
        );
        outfile.write(name_val)

        # Preserved bits
        preserved_mask = self._get_preserved_mask(reg)
        if preserved_mask:
            preserved_mask_val = "{indent}constexpr const auto preserved_mask = {mask};\n".format(
                indent = self._indent_string(),
                mask = preserved_mask
            );
            outfile.write(preserved_mask_val)

        # Offset
        offset_val = "{indent}constexpr const auto offset = {offset};\n\n".format(
            indent = self._indent_string(),
            offset = reg.offset.lower()
        );
        outfile.write(offset_val)

        # Value type
        if reg.size == 32:
            t = "uint32_t"
        elif reg.size == 64:
            t = "uint64_t"
        elif reg.size % 64 == 0:
            t = "struct value_type {{ uint64_t data[{size}]{{0}}; }}".format(
                    size = int(reg.size / 64)
                )
        else:
            raise ShoulderGeneratorException("Unsupported register of size " + str(reg.size))
        valtype = "{indent}using value_type = {t};\n".format(
            indent = self._indent_string(),
            t = t
        );
        outfile.write(valtype)

    def _get_preserved_mask(self, reg):
        is_preserved = False
        mask_val = 0
        for field in reg.fieldsets[0].fields:
            if field.access == "rsvdp":
                is_preserved = True
                for i in range((field.lsb % 64), (field.msb % 64) + 1):
                    mask_val |= 1 << i

        return "0x" + format(mask_val, 'X') if is_preserved else None

    def _generate_accessors(self, reg, outfile):
        preserved_mask = self._get_preserved_mask(reg)
        is_readable = False
        is_writeable = False
        for field in reg.fieldsets[0].fields:
            if field.access in ["rw", "rw1c", "rw1cs", "ro", "ros", "wo"]:
                is_readable = True
            if field.access in ["rw", "rw1c", "rw1cs", "wo"]:
                is_writeable = True

        # Register getter
        if is_readable:
            accessor = "\n{indent}inline auto {func}() noexcept\n"
            accessor += "{indent}{{ return read_iommu_{size}(offset); }}\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.register_read_function,
                size = str(reg.size)
            )
            outfile.write(accessor)

        # Register setter
        if is_writeable:
            accessor = "\n{indent}inline auto {func}(value_type val) noexcept\n"
            accessor += "{indent}{{ return write_iommu_{size}{preserved}(offset, val{preserved_arg}); }}\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.register_write_function,
                size = str(reg.size),
                preserved = "_preserved" if preserved_mask else "",
                preserved_arg = ", preserved_mask" if preserved_mask else ""
            )
            outfile.write(accessor)

    def _generate_register_dump_function(self, reg, outfile):
        # If register has no readable fields, skip
        is_readable = False
        for field in reg.fieldsets[0].fields:
            if field.access in ["rw", "rw1c", "rw1cs", "ro", "ros"]:
                is_readable = True
                break
        if not is_readable: return

        # Function declaration
        dump_func = "\n{indent}inline void dump(int level, const value_type &{arg}, std::string *msg = nullptr)\n".format(
            indent = self._indent_string(),
            arg = reg.name.lower()
        )

        dump_func += "{indent}{{\n".format(indent = self._indent_string())
        self._increase_indent()

        # Whole-register dump
        dump_func += "{indent}bfdebug_nhex(level, name, {arg}, msg);\n".format(
            indent = self._indent_string(),
            arg = reg.name.lower()
        )

        # Dump each field individually
        dump_func += "\n"
        for field in reg.fieldsets[0].fields:
            if field.name.lower() in ["rz", "rp"] : continue
            if field.access in ["rw", "rw1c", "rw1cs", "ro", "ros"]:
                dump_func += "{indent}{fieldname}::dump(level, {arg}, msg);\n".format(
                    indent = self._indent_string(),
                    fieldname = field.name.lower(),
                    arg = reg.name.lower()
                )

        self._decrease_indent()
        dump_func += "{indent}}}\n".format(indent = self._indent_string())

        outfile.write(dump_func)

    def _generate_fieldsets(self, reg, outfile):
        if not reg.is_sysreg: return
        fieldsets = reg.fieldsets

        if len(fieldsets) == 1:
            self._generate_single_fieldset(reg, fieldsets[0], outfile)
        else:
            logger.debug("No fieldsets generated for system register " + str(reg.name))

    def _generate_single_fieldset(self, reg, fieldset, outfile):
        for field in fieldset.fields:
            field_cxx_name = field.name.lower()
            if field_cxx_name in ["rz", "rp"] : continue

            outfile.write("\n")
            field_namespace = "{indent}namespace {name}\n{indent}{{\n".format(
                indent = self._indent_string(),
                name = field_cxx_name
            )
            outfile.write(field_namespace)

            self._increase_indent()

            # Constants
            self._generate_field_constants(reg, field, outfile)

            # Accessors
            if(field.msb == field.lsb):
                self._generate_bitfield_accessors(reg, field, outfile)
            else:
                self._generate_field_accessors(reg, field, outfile)

            self._decrease_indent()

            field_namespace_close = "{indent}}}\n".format(
                indent = self._indent_string()
            )
            outfile.write(field_namespace_close)

    def _generate_field_constants(self, reg, field, outfile):
        prefix = "constexpr const auto"

        # Mask
        mask_val = 0
        for i in range((field.lsb % 64), (field.msb % 64) + 1):
            mask_val |= 1 << i
        mask_val = "0x" + format(mask_val, 'X')
        mask_const = "{indent}{prefix} mask = {mask_val}ULL;\n".format(
            indent = self._indent_string(),
            prefix = prefix,
            mask_val = mask_val
        )
        outfile.write(mask_const)

        # Index
        if reg.size > 64:
            index_val = int(field.lsb / 64)
            index_const = "{indent}{prefix} index = {index_val}ULL;\n".format(
                indent = self._indent_string(),
                prefix = prefix,
                index_val = index_val
            )
            outfile.write(index_const)

        # From
        from_const = "{indent}{prefix} from = {from_val}ULL;\n".format(
            indent = self._indent_string(),
            prefix = prefix,
            from_val = field.lsb % 64
        )
        outfile.write(from_const)

        # Name
        name_const = "{indent}{prefix} name = \"{name_val}\";\n".format(
            indent = self._indent_string(),
            prefix = prefix,
            name_val = field.long_name.lower()
        )
        outfile.write(name_const)
        outfile.write("\n")

    def _generate_bitfield_accessors(self, reg, field, outfile):
        preserved_mask = self._get_preserved_mask(reg)

        if field.access in ["rw", "rw1c", "rw1cs", "ro", "ros"]:
            # Check bit enabled from register 
            accessor = "{indent}inline auto {func}() noexcept\n"
            accessor += "{indent}{{ return is_bit_set(get(), from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.is_bit_set_function,
                argtype = "value_type",
                arg = reg.name.lower(),
            )
            outfile.write(accessor)

            # Check bit enabled from an integer value
            accessor = "{indent}inline auto {func}(const {argtype} &{arg}) noexcept\n"
            accessor += "{indent}{{ return is_bit_set({arg}, from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.is_bit_set_function,
                argtype = "value_type",
                arg = reg.name.lower(),
            )
            outfile.write(accessor)

            # Check bit disabled from register 
            accessor = "{indent}inline auto {func}() noexcept\n"
            accessor += "{indent}{{ return !is_bit_set(get(), from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.is_bit_cleared_function,
                argtype = "value_type",
                arg = reg.name.lower(),
            )
            outfile.write(accessor)

            # Check bit disabled from an integer value
            accessor = "{indent}inline auto {func}(const {argtype} &{arg}) noexcept\n"
            accessor += "{indent}{{ return !is_bit_set({arg}, from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.is_bit_cleared_function,
                argtype = "value_type",
                arg = reg.name.lower(),
            )
            outfile.write(accessor)

        if field.access in ["rw", "rw1c", "rw1cs", "wo"]:
            # Enable the bit in the register 
            accessor = "{indent}inline void {func}() noexcept\n"
            accessor += "{indent}{{ set(set_bit(get(), from)); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.bit_set_function,
                argtype = "value_type",
                arg = reg.name.lower(),
                regsize = reg.size
            )
            outfile.write(accessor)

            # Enable the bit in an integer value
            accessor = "{indent}inline void {func}({argtype} &{arg}) noexcept\n"
            accessor += "{indent}{{ {arg} = set_bit({arg}, from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.bit_set_function,
                argtype = "value_type",
                arg = reg.name.lower(),
            )
            outfile.write(accessor)

        if field.access in ["rw", "wo"]:
            # Disable the bit in the register 
            accessor = "{indent}inline void {func}() noexcept\n"
            accessor += "{indent}{{ set(clear_bit(get(), from)); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.bit_clear_function,
                argtype = "value_type",
                arg = reg.name.lower(),
                regsize = reg.size
            )
            outfile.write(accessor)

            # Disable the bit in an integer value
            accessor = "{indent}inline void {func}({argtype} &{arg}) noexcept\n"
            accessor += "{indent}{{ {arg} = clear_bit({arg}, from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.bit_clear_function,
                argtype = "value_type",
                arg = reg.name.lower(),
            )
            outfile.write(accessor)

        if field.access in ["rw", "rw1c", "rw1cs", "ro", "ros"]:
            # Dump function
            accessor = "{indent}inline void dump(int level, const value_type &{arg}, std::string *msg = nullptr)\n".format(
                indent = self._indent_string(),
                arg = reg.name.lower()
            )
            accessor += "{indent}{{ bfdebug_subbool(level, name, is_enabled({arg}), msg); }}\n".format(
                indent = self._indent_string(),
                arg = reg.name.lower()
            )
            outfile.write(accessor)

    def _generate_field_accessors(self, reg, field, outfile):
        is_readable = False
        is_writeable = False
        if field.access in ["rw", "rw1c", "rw1cs", "ro", "ros"]:
            is_readable = True
        if field.access in ["rw", "rw1c", "rw1cs", "wo"]:
            is_writeable = True

        if is_readable:
            # Get the field value from the register
            accessor = "{indent}inline auto {func}() noexcept\n"
            accessor += "{indent}{{ return get_bits(read_iommu_{size}(offset), mask) >> from; }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.register_field_read_function,
                size = reg.size
            )
            outfile.write(accessor)

            # Get the field value from an integer value
            accessor = "{indent}inline auto {func}(const {argtype} &{arg}) noexcept\n"
            accessor += "{indent}{{ return get_bits({arg}, mask) >> from; }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.register_field_read_function,
                argtype = "value_type",
                arg = reg.name.lower()
            )
            outfile.write(accessor)

        if is_writeable:
            # Set the field's value in an integer value
            accessor = "{indent}inline void {func}({valtype} val) noexcept\n"
            accessor += "{indent}{{ set(set_bits(read_iommu_{size}(offset), mask, val << from)); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.register_field_write_function,
                valtype = "uint64_t",
                size = reg.size
            )
            outfile.write(accessor)

            # Set the field's value in an integer value
            accessor = "{indent}inline void {func}({argtype} &{arg}, {valtype} val) noexcept\n"
            accessor += "{indent}{{ {arg} = set_bits({arg}, mask, val << from); }}\n\n"
            accessor = accessor.format(
                indent = self._indent_string(),
                func = config.register_field_write_function,
                argtype = "value_type",
                valtype = "uint64_t",
                arg = reg.name.lower()
            )
            outfile.write(accessor)

        # Dump function
        if is_readable:
            accessor = "{indent}inline void dump(int level, const value_type &{arg}, std::string *msg = nullptr)\n".format(
                indent = self._indent_string(),
                arg = reg.name.lower()
            )
            accessor += "{indent}{{ bfdebug_subnhex(level, name, get({arg}), msg); }}\n".format(
                indent = self._indent_string(),
                arg = reg.name.lower()
            )
            outfile.write(accessor)

    def _increase_indent(self):
        self._current_indent_level += 1

    def _decrease_indent(self):
        if self._current_indent_level <= 0:
            raise ShoulderGeneratorException("Indent level cannot be negative")
        self._current_indent_level -= 1

    def _indent_string(self):
        indent_str = ""
        for level in range(0, self._current_indent_level):
            indent_str += "\t"
        return indent_str
