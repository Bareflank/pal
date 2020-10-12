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

# ------------------------------------------------------------------------------
# Configs
# ------------------------------------------------------------------------------

include(${PAL_SOURCE_CMAKE_DIR}/macros/pal_add_config.cmake)

pal_add_config(
    CONFIG_NAME PAL_TARGET_EXECUTION_STATE
    CONFIG_TYPE STRING
    DEFAULT_VAL intel_64bit
    DESCRIPTION "The target architecture + execution state"
    OPTIONS armv8a_aarch64 armv8a_aarch32 intel_64bit
)

pal_add_config(
    CONFIG_NAME PAL_TARGET_LANGUAGE
    CONFIG_TYPE STRING
    DEFAULT_VAL c++11
    DESCRIPTION "The target programming language"
    OPTIONS c c++11 yaml none
)

pal_add_config(
    CONFIG_NAME PAL_ACCESS_MECHANISM
    CONFIG_TYPE STRING
    DEFAULT_VAL gas_att
    DESCRIPTION "The target access mechanism type"
    OPTIONS gas_att gas_intel gas_aarch64 gas_aarch32 libpal test yaml none
)

pal_add_config(
    CONFIG_NAME PAL_PRINT_MECHANISM
    CONFIG_TYPE STRING
    DEFAULT_VAL printf_utf8
    DESCRIPTION "The target function printing style"
    OPTIONS printf_utf8 none
)

pal_add_config(
    CONFIG_NAME PAL_FILE_FORMAT
    CONFIG_TYPE STRING
    DEFAULT_VAL unix
    DESCRIPTION "The target file format"
    OPTIONS unix windows yaml none
)

pal_add_config(
    CONFIG_NAME PAL_ENABLE_TEST
    CONFIG_TYPE BOOL
    DEFAULT_VAL OFF
    DESCRIPTION "Set to ON to enable the project's tests"
)

pal_add_config(
    CONFIG_NAME PAL_OUTPUT_DIR
    CONFIG_TYPE STRING
    DEFAULT_VAL ${CMAKE_BINARY_DIR}/pal/include
    DESCRIPTION "Directory for PAL to generated output"
)

pal_add_config(
    CONFIG_NAME PAL_QUIET_CMAKE
    CONFIG_TYPE BOOL
    DEFAULT_VAL OFF
    DESCRIPTION "Set to ON to supress build output from CMake"
)

pal_add_config(
    CONFIG_NAME PAL_ENABLE_ACPI
    CONFIG_TYPE BOOL
    DEFAULT_VAL OFF
    DESCRIPTION "EXPERIMENTAL: Set to ON to include ACPI in the generated PAL output"
)
