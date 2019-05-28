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

import os

class Configuration():
    """ A single user-definable configuration variable """
    def __init__(self, name, default_value):
        self.name = name
        self.default_value = default_value
        self.value = default_value
        self.description = "Description N/A"
        self.options = []

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

class ShoulderConfig:
    """ Ecapsulates all user-definable Configurations for Shoulder """
    def __init__(self):
        self._configurations = {}

    def __str__(self):
        string = ""
        for key, value in sorted(self._configurations.items()):
            string += str(value) + "\n"
        return string

    def __getitem__(self, key):
        return self._configurations[key].value

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
# from shoulder.config import config
#
# value = config.my_config
# value2 = config["my_config_2"]
# config["my_config"] = "a new value"
# config.my_config = "another new value"

config  = ShoulderConfig()

# -----------------------------------------------------------------------------
# Logging options
# -----------------------------------------------------------------------------

c = Configuration("log_level", "info")
c.description = "Log-level visibility for Shoulder logger messages"
c.options = ["debug", "info", "warn", "error"]
config.add_configuration(c)

c = Configuration("log_with_color", True)
c.description = "Use colored output for Shoulder logger messages"
config.add_configuration(c)

# -----------------------------------------------------------------------------
# Function generation options
# -----------------------------------------------------------------------------

c = Configuration("encoded_functions", False)
c.description = "Use 32bit encoded instruction values instead of traditional mnemonic accesses"
config.add_configuration(c)

c = Configuration("register_read_function", "get")
c.description = "Name of generated functions for reading registers"
config.add_configuration(c)

c = Configuration("register_write_function", "set")
c.description = "Name of generated functions for writing registers"
config.add_configuration(c)

c = Configuration("register_field_read_function", "get")
c.description = "Name of generated functions for reading register fields"
config.add_configuration(c)

c = Configuration("register_field_write_function", "set")
c.description = "Name of generated functions for writing register fields"
config.add_configuration(c)

c = Configuration("bit_set_function", "enable")
c.description = "Name of generated functions for setting a bit to the value 1"
config.add_configuration(c)

c = Configuration("bit_clear_function", "disable")
c.description = "Name of generated functions for setting a bit to the value 0"
config.add_configuration(c)

c = Configuration("is_bit_set_function", "is_enabled")
c.description = "Name of generated functions for checking if a bit is set to 1"
config.add_configuration(c)

c = Configuration("is_bit_cleared_function", "is_disabled")
c.description = "Name of generated functions for checking if a bit is set to 0"
config.add_configuration(c)

# -----------------------------------------------------------------------------
# C++ options
# -----------------------------------------------------------------------------

c = Configuration("cxx_namespace", "shoulder::aarch64")
c.description = "Top namespace to place generated c++ functions into"
config.add_configuration(c)

# -----------------------------------------------------------------------------
# C options
# -----------------------------------------------------------------------------

c = Configuration("c_prefix", "")
c.description = "Prefix to place in front of generated C functions"
config.add_configuration(c)

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

_package_dir = os.path.dirname(os.path.realpath(__file__))
c = Configuration("shoulder_package_dir", str(_package_dir))
c.description = "Path the shoulder python package directory"
config.add_configuration(c)

_project_dir = os.path.abspath(os.path.join(_package_dir, ".."))
c = Configuration("shoulder_project_dir", str(_project_dir))
c.description = "Path the top directory of the shoulder project"
config.add_configuration(c)

_scripts_dir = os.path.join(_project_dir, "scripts")
c = Configuration("shoulder_scripts_dir", _scripts_dir)
c.description = "Path the shoulder project scripts directory"
config.add_configuration(c)

_include_dir = os.path.join(_project_dir, "include")
c = Configuration("shoulder_include_dir", _include_dir)
c.description = "Path the shoulder header include directory"
config.add_configuration(c)

_test_dir = os.path.join(_project_dir, "test")
c = Configuration("shoulder_test_dir", _test_dir)
c.description = "Path the shoulder test directory"
config.add_configuration(c)

_xml_register_dir = os.path.abspath(os.path.join(_project_dir, "../ARMv85A-SysReg-00bet9/SysReg_v85A_xml-00bet9"))
c = Configuration("xml_register_dir", _xml_register_dir)
c.description = "Path to XML register specficiation directory"
config.add_configuration(c)

_output_dir = os.path.join(_project_dir, "output")
c = Configuration("shoulder_output_dir", _output_dir)
c.description = "Path the shoulder output directory"
config.add_configuration(c)

c = Configuration("license_template_path", os.path.join(_scripts_dir, "license.txt"))
c.description = "Path to license template for generated files"
config.add_configuration(c)
