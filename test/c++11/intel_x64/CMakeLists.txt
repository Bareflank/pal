cmake_minimum_required(VERSION 3.12)
project(c++11-x86_64-linux-gnu-gcc CXX)

set(SOURCES
    cr3.cpp
    xcr0.cpp
    ia32_feature_control.cpp
    leaf_01.cpp
    leaf_04.cpp
    leaf_0D.cpp
    eptp.cpp
    guest_interrupt_status.cpp
    # facs.cpp
    main.cpp
)

# -----------------------------------------------------------------------------
# Generate and compile using Intel assembler syntax
# -----------------------------------------------------------------------------
set(INTEL_SYNTAX_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/intel_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/intel_asm/pal
        --arch=intel_x64
        --language=c++11
        --access_mechanism=gas_intel
        --print_mechanism=printf_utf8
        --file_format=unix
        --generator=c++_header
        --acpi=ON
    COMMAND cmake -E touch ${INTEL_SYNTAX_OUTPUT_STAMP}
    OUTPUT ${INTEL_SYNTAX_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
)
add_custom_target(test_generate_x86_64_intel_asm ALL DEPENDS ${INTEL_SYNTAX_OUTPUT_STAMP})

add_executable(test_compile_x86_64_intel_asm
    ${SOURCES}
)

target_include_directories(test_compile_x86_64_intel_asm
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}/intel_asm
)

target_compile_options(test_compile_x86_64_intel_asm
    PRIVATE
        -masm=intel
)

install(TARGETS test_compile_x86_64_intel_asm DESTINATION bin)
add_dependencies(test_compile_x86_64_intel_asm test_generate_x86_64_intel_asm)

# -----------------------------------------------------------------------------
# Generate and compile using AT&T assembler syntax
# -----------------------------------------------------------------------------
set(ATT_SYNTAX_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/att_output.stamp)
add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/att_asm/pal
        --arch=intel_x64
        --language=c++11
        --access_mechanism=gas_att
        --print_mechanism=printf_utf8
        --file_format=unix
        --generator=c++_header
        --acpi=ON
    COMMAND cmake -E touch ${ATT_SYNTAX_OUTPUT_STAMP}
    OUTPUT ${ATT_SYNTAX_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
)
add_custom_target(test_generate_x86_64_att_asm ALL DEPENDS ${ATT_SYNTAX_OUTPUT_STAMP})

add_executable(test_compile_x86_64_att_asm
    ${SOURCES}
)

target_include_directories(test_compile_x86_64_att_asm
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}/att_asm
)

target_compile_options(test_compile_x86_64_att_asm
    PRIVATE
        -masm=att
)

install(TARGETS test_compile_x86_64_att_asm DESTINATION bin)
add_dependencies(test_compile_x86_64_att_asm test_generate_x86_64_att_asm)
