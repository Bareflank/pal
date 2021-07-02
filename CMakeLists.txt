cmake_minimum_required(VERSION 3.12)
project(pal)

if(PAL_C)
    enable_language(C)
endif()

if(PAL_C++11)
    enable_language(CXX)
endif()

find_package(Python3 COMPONENTS Interpreter REQUIRED)

include(${CMAKE_CURRENT_LIST_DIR}/cmake/init_project.cmake)

set(PYTHONPATH ${CMAKE_CURRENT_LIST_DIR})

if(PAL_ARMV8A_AARCH32_AAPCS_GNU)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_armv8a_aarch32_aapcs_gnuasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_armv8a_aarch32_aapcs_gnuasm
            LANGUAGE c
            EXECUTION_STATE armv8a_aarch32
            ACCESS_MECHANISM gas_aarch32
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_armv8a_aarch32_aapcs_gnuasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_armv8a_aarch32_aapcs_gnuasm
            LANGUAGE c++11
            EXECUTION_STATE armv8a_aarch32
            ACCESS_MECHANISM gas_aarch32
        )
    endif()
endif()

if(PAL_ARMV8A_AARCH64_AAPCS64_GNU)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_armv8a_aarch64_aapcs64_gnuasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_armv8a_aarch64_aapcs64_gnuasm
            LANGUAGE c
            EXECUTION_STATE armv8a_aarch64
            ACCESS_MECHANISM gas_aarch64
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_armv8a_aarch64_aapcs64_gnuasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_armv8a_aarch64_aapcs64_gnuasm
            LANGUAGE c++11
            EXECUTION_STATE armv8a_aarch64
            ACCESS_MECHANISM gas_aarch64
        )
    endif()
endif()

if(PAL_INTEL_64BIT_SYSTEMV_GNUATT)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_systemv_gnuatt
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_intel_64bit_systemv_gnuatt
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM gas_att
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_systemv_gnuatt
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_intel_64bit_systemv_gnuatt
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM gas_att
        )
    endif()
endif()

if(PAL_INTEL_64BIT_SYSTEMV_GNUINTEL)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_systemv_gnuintel
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_intel_64bit_systemv_gnuintel
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM gas_intel
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_systemv_gnuintel
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_intel_64bit_systemv_gnuintel
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM gas_intel
        )
    endif()
endif()

if(PAL_INTEL_64BIT_SYSTEMV_NASM)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_systemv_nasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_intel_64bit_systemv_nasm
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_systemv_nasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_intel_64bit_systemv_nasm
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/intel_64bit_systemv_nasm)
endif()

if(PAL_INTEL_64BIT_MS64_MASM)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_ms64_masm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_intel_64bit_ms64_masm
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_ms64_masm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_intel_64bit_ms64_masm
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/intel_64bit_ms64_masm)
endif()

if(PAL_INTEL_64BIT_LINUX_IOCTL)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c_intel_64bit_linux_ioctl
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11_intel_64bit_linux_ioctl
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/intel_64bit_linux_ioctl)

    if(PAL_DRIVER)
        add_subdirectory(devpal/linux)
    endif()
endif()

# if(PAL_ACPI)
#     if(PAL_C)
#         pal_run_generator(
#             TARGET_NAME c_acpi
#             INPUT_DIR ${CMAKE_SOURCE_DIR}/data/acpi
#             OUTPUT_DIR ${CMAKE_BINARY_DIR}/acpi
#             LANGUAGE c
#         )
#     endif()
#
#     if(PAL_C++11)
#         pal_run_generator(
#             TARGET_NAME c++11_acpi
#             INPUT_DIR ${CMAKE_SOURCE_DIR}/data/acpi
#             OUTPUT_DIR ${CMAKE_BINARY_DIR}/acpi
#             LANGUAGE c++11
#         )
#     endif()
# endif()

add_library(pal INTERFACE)
# add_dependencies(pal pal_generate)
# target_include_directories(pal INTERFACE ${CMAKE_BINARY_DIR})
# target_link_libraries(pal INTERFACE libpal)

set(CMAKE_INSTALL_MESSAGE NEVER)
install(
    DIRECTORY ${CMAKE_BINARY_DIR}
    DESTINATION ${CMAKE_INSTALL_PREFIX}/include
)

if(PAL_TEST)
    add_subdirectory(test)
endif()

if(PAL_EXAMPLE)
    add_subdirectory(example)
endif()

if(NOT PAL_QUIET_CMAKE)
    pal_print_banner()
    pal_print_usage()
endif()
