from pal.generator.c_header_generator import CHeaderGenerator
from pal.generator.cxx_header_generator import CxxHeaderGenerator
from pal.generator.rust_generator import RustGenerator
from pal.generator.yaml_data_generator import YamlDataGenerator


def make_generators(config, writer):
    generators = []

    if config.language == "c++11":
        generators.append(CxxHeaderGenerator(writer))

    if config.language == "c":
        generators.append(CHeaderGenerator(writer))

    if config.language == "rust":
        generators.append(RustGenerator(writer))

    if config.language == "yaml":
        generators.append(YamlDataGenerator(writer))

    return generators
