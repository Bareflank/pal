cmake_minimum_required(VERSION 3.12)
project(c++11-intel-linux-gnu-gcc CXX)

set(REGISTER_SOURCES
    cr3.cpp
    xcr0.cpp
    ia32_feature_control.cpp
    leaf_01.cpp
    leaf_04.cpp
    leaf_0D.cpp
    eptp.cpp
    guest_interrupt_status.cpp
    facs.cpp
    main.cpp
)

set(INSTRUCTION_SOURCES
    cpuid.cpp
    rdmsr.cpp
    read_cr3.cpp
    write_cr3.cpp
)
# -----------------------------------------------------------------------------
# Generate and compile using Intel assembler syntax
# -----------------------------------------------------------------------------
set(INTEL_SYNTAX_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/intel_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/intel_asm
        --execution_state=intel_64bit
        --language=c++11
        --access_mechanism=gas_intel
        --print_mechanism=printf_utf8
        --file_format=unix
        --acpi=ON
    COMMAND cmake -E touch ${INTEL_SYNTAX_OUTPUT_STAMP}
    OUTPUT ${INTEL_SYNTAX_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
)
add_custom_target(test_generate_intel_intel_asm ALL DEPENDS ${INTEL_SYNTAX_OUTPUT_STAMP})

add_executable(test_compile_intel_intel_asm
    ${REGISTER_SOURCES}
)

target_include_directories(test_compile_intel_intel_asm
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}/intel_asm/include
)

target_compile_options(test_compile_intel_intel_asm
    PRIVATE
        -masm=intel
        -fno-exceptions
)

install(TARGETS test_compile_intel_intel_asm DESTINATION bin)
add_dependencies(test_compile_intel_intel_asm test_generate_intel_intel_asm)

# -----------------------------------------------------------------------------
# Generate and compile using AT&T assembler syntax
# -----------------------------------------------------------------------------
set(ATT_SYNTAX_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/att_output.stamp)
add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/att_asm
        --execution_state=intel_64bit
        --language=c++11
        --access_mechanism=gas_att
        --print_mechanism=printf_utf8
        --file_format=unix
        --acpi=ON
    COMMAND cmake -E touch ${ATT_SYNTAX_OUTPUT_STAMP}
    OUTPUT ${ATT_SYNTAX_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
)
add_custom_target(test_generate_intel_att_asm ALL DEPENDS ${ATT_SYNTAX_OUTPUT_STAMP})

add_executable(test_compile_intel_att_asm
    ${REGISTER_SOURCES}
)

target_include_directories(test_compile_intel_att_asm
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}/att_asm/include
)

target_compile_options(test_compile_intel_att_asm
    PRIVATE
        -masm=att
        -fno-exceptions
)

install(TARGETS test_compile_intel_att_asm DESTINATION bin)
add_dependencies(test_compile_intel_att_asm test_generate_intel_att_asm)

# -----------------------------------------------------------------------------
# Generate and compile using libpal
# -----------------------------------------------------------------------------
set(LIBPAL_SYNTAX_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/libpal_output.stamp)
add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/libpal
        --execution_state=intel_64bit
        --language=c++11
        --access_mechanism=libpal
        --print_mechanism=printf_utf8
        --file_format=unix
        --acpi=ON
        COMMAND cmake -E touch ${LIBPAL_SYNTAX_OUTPUT_STAMP}
        OUTPUT ${LIBPAL_SYNTAX_OUTPUT_STAMP}
        DEPENDS ${REGISTER_SOURCES}
)
add_custom_target(test_generate_intel_libpal ALL DEPENDS ${LIBPAL_SYNTAX_OUTPUT_STAMP})

add_executable(test_compile_intel_libpal
    ${REGISTER_SOURCES}
    ${INSTRUCTION_SOURCES}
)

target_include_directories(test_compile_intel_libpal
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}/libpal/include
)

add_subdirectory(${PAL_SOURCE_DIR}/libpal/intel_64bit_systemv_nasm ${CMAKE_CURRENT_BINARY_DIR}/libpal/intel_64bit_systemv_nasm)
target_link_libraries(test_compile_intel_libpal pal_intel_64bit_systemv_nasm)

target_compile_options(test_compile_intel_libpal 
    PRIVATE
        -masm=att
        -fno-exceptions
)

install(TARGETS test_compile_intel_libpal DESTINATION bin)
add_dependencies(test_compile_intel_libpal test_generate_intel_libpal)
