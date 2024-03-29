cmake_minimum_required(VERSION 3.12)
project(pal)

if(PAL_C)
    enable_language(C)
endif()

if(PAL_C++11)
    set (CMAKE_CXX_STANDARD 11)
    enable_language(CXX)
endif()

find_package(Python3 COMPONENTS Interpreter REQUIRED)

include(${CMAKE_CURRENT_LIST_DIR}/cmake/init_project.cmake)

set(PYTHONPATH ${CMAKE_CURRENT_LIST_DIR})

# check if the environment has these python modules
pal_find_python_module(lxml)
pal_find_python_module(dataclasses)
pal_find_python_module(colorama)
pal_find_python_module(yaml)

if(PAL_ARMV8A_AARCH32_AAPCS_GNU)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_armv8a_aarch32_aapcs_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/armv8a_aarch32_aapcs_gnuinline
            LANGUAGE c
            EXECUTION_STATE armv8a_aarch32
            ACCESS_MECHANISM gnu_inline
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_armv8a_aarch32_aapcs_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/armv8a_aarch32_aapcs_gnuinline
            LANGUAGE c++11
            EXECUTION_STATE armv8a_aarch32
            ACCESS_MECHANISM gnu_inline
        )
    endif()
endif()

if(PAL_ARMV8A_AARCH64_AAPCS64_GNU)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_armv8a_aarch64_aapcs64_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/armv8a_aarch64_aapcs64_gnuinline
            LANGUAGE c
            EXECUTION_STATE armv8a_aarch64
            ACCESS_MECHANISM gnu_inline
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_armv8a_aarch64_aapcs64_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/armv8a_aarch64_aapcs64_gnuinline
            LANGUAGE c++11
            EXECUTION_STATE armv8a_aarch64
            ACCESS_MECHANISM gnu_inline
        )
    endif()
endif()

if(PAL_ARMV8A_AARCH64_LINUX_IOCTL)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_armv8a_aarch64_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/armv8a_aarch64_linux_ioctl
            LANGUAGE c
            EXECUTION_STATE armv8a_aarch64
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_armv8a_aarch64_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/armv8a_aarch64_linux_ioctl
            LANGUAGE c++11
            EXECUTION_STATE armv8a_aarch64
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/armv8a_aarch64_linux_ioctl)
endif()

if(PAL_AMD_64BIT_SYSTEMV_GNUINLINE)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_amd_64bit_systemv_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/amd_64bit_systemv_gnuinline
            LANGUAGE c
            EXECUTION_STATE amd_64bit
            ACCESS_MECHANISM gnu_inline
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_amd_64bit_systemv_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/amd_64bit_systemv_gnuinline
            LANGUAGE c++11
            EXECUTION_STATE amd_64bit
            ACCESS_MECHANISM gnu_inline
        )
    endif()

    add_subdirectory(libpal/amd_64bit_systemv_gnuinline)
    add_dependencies(c_amd_64bit_systemv_gnuinline pal_amd_64bit_systemv_gnuinline) 
endif()

if(PAL_AMD_64BIT_LINUX_IOCTL)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_amd_64bit_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/amd_64bit_linux_ioctl
            LANGUAGE c
            EXECUTION_STATE amd_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_amd_64bit_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/amd_64bit_linux_ioctl
            LANGUAGE c++11
            EXECUTION_STATE amd_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/amd_64bit_linux_ioctl)
endif()

if(PAL_INTEL_64BIT_SYSTEMV_GNUINLINE)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_systemv_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/intel_64bit_systemv_gnuinline
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM gnu_inline
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_systemv_gnuinline
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/intel_64bit_systemv_gnuinline
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM gnu_inline
        )
    endif()

    add_subdirectory(libpal/intel_64bit_systemv_gnuinline)
    add_dependencies(c_intel_64bit_systemv_gnuinline pal_intel_64bit_systemv_gnuinline) 
endif()

if(PAL_INTEL_64BIT_SYSTEMV_NASM)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_systemv_nasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/intel_64bit_systemv_nasm
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_systemv_nasm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/intel_64bit_systemv_nasm
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
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/intel_64bit_ms64_masm
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_ms64_masm
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/intel_64bit_ms64_masm
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
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/intel_64bit_linux_ioctl
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_linux_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/intel_64bit_linux_ioctl
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/intel_64bit_linux_ioctl)
endif()

if(PAL_INTEL_64BIT_WINDOWS_IOCTL)
    if(PAL_C)
        pal_run_generator(
            TARGET_NAME c_intel_64bit_windows_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c/intel_64bit_windows_ioctl
            LANGUAGE c
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    if(PAL_C++11)
        pal_run_generator(
            TARGET_NAME c++11_intel_64bit_windows_ioctl
            OUTPUT_DIR ${CMAKE_BINARY_DIR}/c++11/intel_64bit_windows_ioctl
            LANGUAGE c++11
            EXECUTION_STATE intel_64bit
            ACCESS_MECHANISM libpal
        )
    endif()

    add_subdirectory(libpal/intel_64bit_windows_ioctl)
endif()

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

if(PAL_DRIVER)
    add_subdirectory(devpal)
endif()

if(NOT PAL_QUIET_CMAKE)
    pal_print_banner()
endif()

if (NOT PAL_QUIET_CMAKE AND NOT PYTHON_MODULES_MISSING)
    pal_print_usage()
endif()
