from pal.writer.abstract_writer import AbstractWriter

from pal.writer.register.c.register_writer import CRegisterWriter
from pal.writer.register.cxx11.register_writer import Cxx11RegisterWriter
from pal.writer.register.yaml import YamlRegisterWriter
from pal.writer.register.none import NoneRegisterWriter

from pal.writer.access_mechanism.gas_x86_64_intel_syntax import \
    GasX86_64IntelSyntaxAccessMechanismWriter
from pal.writer.access_mechanism.gas_x86_64_att_syntax import \
    GasX86_64AttSyntaxAccessMechanismWriter
from pal.writer.access_mechanism.gas_aarch64 import \
    GasAarch64AccessMechanismWriter
from pal.writer.access_mechanism.gas_aarch32 import \
    GasAarch32AccessMechanismWriter
from pal.writer.access_mechanism.libpal import \
    LibpalAccessMechanismWriter
from pal.writer.access_mechanism.cxx_test import \
    CxxTestAccessMechanismWriter
from pal.writer.access_mechanism.c_test import \
    CTestAccessMechanismWriter
from pal.writer.access_mechanism.yaml import \
    YamlAccessMechanismWriter
from pal.writer.access_mechanism.none import \
    NoneAccessMechanismWriter

from pal.writer.print_mechanism.printf_utf8 import PrintfUtf8PrintMechanismWriter
from pal.writer.print_mechanism.none import NonePrintMechanismWriter

from pal.writer.file_format.unix import UnixFileFormatWriter
from pal.writer.file_format.windows import WindowsFileFormatWriter
from pal.writer.file_format.yaml import YamlFileFormatWriter
from pal.writer.file_format.none import NoneFileFormatWriter

from pal.writer.comment.c_multiline import CMultilineCommentWriter
from pal.writer.comment.yaml import YamlCommentWriter
from pal.writer.comment.none import NoneCommentWriter

from pal.writer.instruction.libpal_c import LibpalCInstructionWriter
from pal.writer.instruction.libpal_cxx11 import LibpalCxx11InstructionWriter
from pal.writer.instruction.none import NoneInstructionWriter

language_options = [
    "c",
    "c++11",
    "yaml",
    "none",
]

access_mechanism_options = [
    "gas_intel",
    "gas_att",
    "gas_aarch64",
    "gas_aarch32",
    "libpal",
    "test",
    "yaml",
    "none",
]

print_mechanism_options = {
    "printf_utf8": PrintfUtf8PrintMechanismWriter,
    "none": NonePrintMechanismWriter,
}

file_format_options = {
    "unix": UnixFileFormatWriter,
    "windows": WindowsFileFormatWriter,
    "yaml": YamlFileFormatWriter,
    "none": NoneFileFormatWriter,
}


def get_access_mechanism_writer(config):
    if config.execution_state == "intel_64bit" and config.access_mechanism == "gas_intel":
        return GasX86_64IntelSyntaxAccessMechanismWriter
    elif config.execution_state == "intel_64bit" and config.access_mechanism == "gas_att":
        return GasX86_64AttSyntaxAccessMechanismWriter
    elif config.execution_state == "armv8a_aarch64" and config.access_mechanism == "gas_aarch64":
        return GasAarch64AccessMechanismWriter
    elif config.execution_state == "armv8a_aarch32" and config.access_mechanism == "gas_aarch32":
        return GasAarch32AccessMechanismWriter
    elif config.access_mechanism == "test" and language == "c++11":
        return CxxTestAccessMechanismWriter
    elif config.access_mechanism == "test" and language == "c":
        return CTestAccessMechanismWriter
    elif config.access_mechanism == "yaml":
        return YamlAccessMechanismWriter
    elif config.access_mechanism == "libpal":
        return LibpalAccessMechanismWriter
    else:
        return NoneAccessMechanismWriter


def get_register_writer(config):
    if config.language == "c":
        return CRegisterWriter
    elif config.language == "c++11":
        return Cxx11RegisterWriter
    elif config.language == "yaml":
        return YamlRegisterWriter
    else:
        return NoneRegisterWriter


def get_instruction_writer(config):
    if config.language == "c":
        return LibpalCInstructionWriter
    elif config.language == "c++11":
        return LibpalCxx11InstructionWriter
    else:
        return NoneInstructionWriter


def get_comment_writer(config):
    if config.language == "c" or config.language == "c++11":
        return CMultilineCommentWriter
    elif config.language == "yaml":
        return YamlCommentWriter
    else:
        return NoneCommentWriter


def make_writer(config):

    if config.language not in language_options:
        raise Exception("invalid language option: " + str(language))

    if config.access_mechanism not in access_mechanism_options:
        raise Exception("invalid access mechanism option: " + str(access_mechanism))

    if config.print_mechanism not in print_mechanism_options:
        raise Exception("invalid print_mechanism option: " +
                        str(print_mechanism))

    if config.file_format not in file_format_options:
        raise Exception("invalid file_format option: " + str(file_format))

    access_mechanism_writer = get_access_mechanism_writer(config)
    register_writer = get_register_writer(config)
    instruction_writer = get_instruction_writer(config)
    comment_writer = get_comment_writer(config)

    class Writer(
            AbstractWriter,
            register_writer,
            instruction_writer,
            access_mechanism_writer,
            print_mechanism_options[config.print_mechanism],
            file_format_options[config.file_format],
            comment_writer
          ):
        pass

    return Writer()
