# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

set(PAL_SOURCE_ROOT_DIR ${CMAKE_CURRENT_LIST_DIR}/../..
    CACHE INTERNAL
    "PAL source root directory"
)

set(PAL_SOURCE_CMAKE_DIR ${PAL_SOURCE_ROOT_DIR}/cmake
    CACHE INTERNAL
    "PAL cmake scripts directory"
)

set(PAL_SOURCE_CONFIG_DIR ${CMAKE_CURRENT_LIST_DIR}
    CACHE INTERNAL
    "PAL cmake configuration directory"
)


set(CMAKE_BUILD_TYPE "Release"
    CACHE INTERNAL
    "Defines the build type"
)

set(CMAKE_VERBOSE_MAKEFILE OFF
    CACHE INTERNAL
    "Enables verbose output"
)

# ------------------------------------------------------------------------------
# Configs
# ------------------------------------------------------------------------------

include(${PAL_SOURCE_CMAKE_DIR}/macros/add_config.cmake)

add_config(
    CONFIG_NAME ARCH
    CONFIG_TYPE STRING
    DEFAULT_VAL intel_x64
    DESCRIPTION "The target architecture"
    OPTIONS armv8-a intel_x64
)

add_config(
    CONFIG_NAME LANGUAGE
    CONFIG_TYPE STRING
    DEFAULT_VAL c++11
    DESCRIPTION "The target programming language"
    OPTIONS c++11 none
)

add_config(
    CONFIG_NAME ACCESS_MECHANISM
    CONFIG_TYPE STRING
    DEFAULT_VAL gas_att
    DESCRIPTION "The target access mechnism type"
    OPTIONS gas_att gas_intel gas_aarch64 gas_aarch32 test none
)

add_config(
    CONFIG_NAME PRINT_STYLE
    CONFIG_TYPE STRING
    DEFAULT_VAL printf_utf8
    DESCRIPTION "The target function printing style"
    OPTIONS printf_utf8 none
)

add_config(
    CONFIG_NAME FILE_FORMAT
    CONFIG_TYPE STRING
    DEFAULT_VAL unix
    DESCRIPTION "The target file format"
    OPTIONS unix windows none
)

add_config(
    CONFIG_NAME GENERATOR
    CONFIG_TYPE STRING
    DEFAULT_VAL c++_header
    DESCRIPTION "The target code generator"
    OPTIONS c++_header
)

add_config(
    CONFIG_NAME REGISTER_READ_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL get
    DESCRIPTION "Name of generated functions for reading registers"
)

add_config(
    CONFIG_NAME REGISTER_WRITE_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL set
    DESCRIPTION "Name of generated functions for writing registers"
)

add_config(
    CONFIG_NAME FIELD_READ_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL get
    DESCRIPTION "Name of generated functions for reading a register field"
)

add_config(
    CONFIG_NAME FIELD_WRITE_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL set
    DESCRIPTION "Name of generated functions for writing a register field"
)

add_config(
    CONFIG_NAME BIT_SET_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL enable
    DESCRIPTION "Name of generated functions for setting a bit to the value 1"
)

add_config(
    CONFIG_NAME BIT_CLEAR_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL disable
    DESCRIPTION "Name of generated functions for setting a bit to the value 0"
)

add_config(
    CONFIG_NAME BIT_IS_SET_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL is_enabled
    DESCRIPTION "Name of generated functions for checking if a bit is set to 1"
)

add_config(
    CONFIG_NAME BIT_IS_CLEAR_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL is_disabled
    DESCRIPTION "Name of generated functions for checking if a bit is set to 0"
)

add_config(
    CONFIG_NAME PRINT_FUNCTION
    CONFIG_TYPE STRING
    DEFAULT_VAL dump
    DESCRIPTION "Name of generated functions for printing information"
)
