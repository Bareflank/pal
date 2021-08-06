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

option(
    PAL_C
    "Enable pal for the C language"
    ON
)

option(
    PAL_C++11
    "Enable pal for the C++11 language"
    ON
)

option(
    PAL_ENABLE_PRINTERS
    "Enable pretty-print functions in generated APIs"
    ON
)

option(
    PAL_ARMV8A_AARCH32_AAPCS_GNU
    "Enable pal for ARMv8a (aarch32) from the AAPCS ABI to GNU inline assemler"
    OFF
)

option(
    PAL_ARMV8A_AARCH64_AAPCS64_GNU
    "Enable pal for ARMv8a (aarch64) from the AAPCS64 ABI to GNU inline assemler"
    OFF
)

option(
    PAL_INTEL_64BIT_SYSTEMV_GNUINLINE
    "Enable pal for Intel (64-bit) from the SystemV ABI to GNU inline Assemler"
    OFF
)

option(
    PAL_INTEL_64BIT_SYSTEMV_NASM
    "Enable pal for Intel (64-bit) from the systemv ABI to a Nasm assembler library"
    OFF
)

option(
    PAL_INTEL_64BIT_MS64_MASM
    "Enable pal for Intel (64-bit) from the MS64 ABI to a Microsoft Assembler (MASM) library"
    OFF
)

option(
    PAL_INTEL_64BIT_LINUX_IOCTL
    "Enable pal for Intel (64-bit) from a Linux application to a Linux driver via an IOCTL"
    OFF
)

option(
    PAL_ACPI
    "Enable pal for ACPI tables"
    OFF
)

option(
    PAL_PCIE
    "Enable pal for PCIe devices"
    OFF
)

option(
    PAL_TEST
    "Enable the project's tests"
    OFF
)

option(
    PAL_EXAMPLE
    "Enable the project's examples"
    OFF
)

option(
    PAL_QUIET_CMAKE
    "Enable to supress build and code-generator output from CMake"
    OFF
)

option(
    PAL_DRIVER
    "Enable pal driver for the current host system"
    OFF
)

pal_add_config(
    CONFIG_NAME PAL_STDINT_HEADER
    CONFIG_TYPE STRING
    DEFAULT_VAL ""
    DESCRIPTION "If specified, will be used as the path to #include for C/C++ dependencies from stdint.h"
)

if(PAL_DRIVER AND ${CMAKE_HOST_SYSTEM_NAME} STREQUAL Linux)
    execute_process(
        COMMAND uname -r
        OUTPUT_VARIABLE KERNEL_RELEASE
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )

    find_path(PAL_LINUX_HEADERS_DIR_DEFAULT_VALUE
        include/linux/user.h
        PATHS /lib/modules/${KERNEL_RELEASE}/build
    )

    pal_add_config(
        CONFIG_NAME PAL_LINUX_HEADERS_DIR
        CONFIG_TYPE STRING
        DEFAULT_VAL ${PAL_LINUX_HEADERS_DIR_DEFAULT_VALUE}
        DESCRIPTION "Directory for linux kernel headers to be used for building the devpal driver"
    )

    unset(PAL_LINUX_HEADERS_DIR_DEFAULT_VALUE CACHE)
endif()
