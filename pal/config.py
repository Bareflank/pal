import os

class Configuration():
    """ A single user-definable configuration variable """
    def __init__(self, name, default_value):
        self.name = name
        self.default_value = default_value
        self.value = default_value
        self.description = "Description N/A"
        self.options = []

        if type(default_value) == bool:
            self.options = [True, False]

    def __str__(self):
        return str(self.name) + ": " + str(self.value)

    def help(self):
        print(str(self.name))
        print("\t" + str(self.description))
        print("\tValue: " + str(self.value))
        print("\tDefault Value: " + str(self.default_value))
        if self.options:
            print("\tOptions: " + str(self.options))

    def validate(self):
        if not self.name:
            msg = "Configuration has no name"
            raise AttributeError(msg)
        if not self.description:
            msg = self.name + " configuration has no description"
            raise AttributeError(msg)
        if self.options:
            if self.value not in self.options:
                msg = self.value + " is not a valid option for " + self.name
                msg += ", valid options are: " + str(self.options)
                raise AttributeError(msg)

class PalConfig:
    """ Ecapsulates all user-definable Configurations for Pal """
    def __init__(self):
        self._configurations = {}

    def __str__(self):
        string = ""
        for key, value in sorted(self._configurations.items()):
            string += str(value) + "\n"
        return string

    def __getitem__(self, key):
        if key in self._configurations:
            return self._configurations[key].value
        else:
            raise IndexError

    def __setitem__(self, key, value):
        self._configurations[key].value = value

    def __getattr__(self, name):
        try:
            config = self._configurations[name]
        except KeyError as e:
            raise AttributeError(e)

        return config.value

    def __setattr__(self, name, value):
        if name.startswith("_"):
           object.__setattr__(self, name, value)
        else:
            self._configurations[name].value = value

    def items(self):
        return self._configurations.items()

    def help(self):
        string = "Available Configurations:\n\n"
        for key, value in sorted(self._configurations.items()):
            value.help()
        return string

    def add_configuration(self, configuration):
        """ Add a new configuration """
        configuration.validate()
        self._configurations[configuration.name] = configuration

    def validate(self):
        """ Validate all defined configuration options """
        for key, value in self._configurations.items():
            value.validate()

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from pal.config import config
#
# value = config.my_config
# value2 = config["my_config_2"]
# config["my_config"] = "a new value"
# config.my_config = "another new value"

config  = PalConfig()

# -----------------------------------------------------------------------------
# General options
# -----------------------------------------------------------------------------

c = Configuration("arch", "intel_x64")
c.description = "The target architecture"
c.options = ["armv8-a", "intel_x64"]
config.add_configuration(c)

c = Configuration("language", "c++11")
c.description = "The target programming language"
c.options = ["c", "c++11", "yaml", "none"]
config.add_configuration(c)

c = Configuration("access_mechanism", "gas_att")
c.description = "The target access mechanism type"
c.options = ["gas_att", "gas_intel", "gas_aarch64", "gas_aarch32", "test",
             "libpal", "yaml", "none"]
config.add_configuration(c)

c = Configuration("print_mechanism", "printf_utf8")
c.description = "The target mechanism for printing messages"
c.options = ["printf_utf8", "none"]
config.add_configuration(c)

c = Configuration("file_format", "unix")
c.description = "The target output file format"
c.options = ["unix", "windows", "yaml", "none"]
config.add_configuration(c)

c = Configuration("generator", "c++_header")
c.description = "The target generator"
c.options = ["c_header", "c++_header", "yaml"]
config.add_configuration(c)

# -----------------------------------------------------------------------------
# Logging options
# -----------------------------------------------------------------------------

c = Configuration("log_level", "info")
c.description = "Log-level visibility for Pal logger messages"
c.options = ["debug", "info", "warn", "error"]
config.add_configuration(c)

c = Configuration("log_with_color", True)
c.description = "Use colored output for Pal logger messages"
config.add_configuration(c)

# -----------------------------------------------------------------------------
# Peripheral options
# -----------------------------------------------------------------------------

c = Configuration("acpi", False)
c.description = "EXPERIMENTAL: Set to True to generate accessors for ACPI"
config.add_configuration(c)

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

_package_dir = os.path.dirname(os.path.realpath(__file__))
_project_dir = os.path.abspath(os.path.join(_package_dir, ".."))

_data_dir = os.path.join(_project_dir, "data")
c = Configuration("pal_data_dir", _data_dir)
c.description = "Path to a pal input data directory"
config.add_configuration(c)

_output_dir = os.path.join(_project_dir, "output")
c = Configuration("pal_output_dir", _output_dir)
c.description = "Path to a pal output directory"
config.add_configuration(c)

c = Configuration("license_template_path", os.path.join(_project_dir, "LICENSE"))
c.description = "Path to license template for generated files"
config.add_configuration(c)
