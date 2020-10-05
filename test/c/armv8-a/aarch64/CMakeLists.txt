cmake_minimum_required(VERSION 3.12)
project(c-aarch64-linux-gnu-gcc C)

set(PROJECT_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/pal_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/pal
        --arch=armv8-a
        --language=c
        --access_mechanism=gas_aarch64
        --print_mechanism=printf_utf8
        --file_format=unix
        --generator=c_header
    COMMAND cmake -E touch ${PROJECT_OUTPUT_STAMP}
    OUTPUT ${PROJECT_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
    COMMENT "Generating PAL outputs"
)

add_custom_target(test_generate_aarch64 ALL DEPENDS ${PROJECT_OUTPUT_STAMP})

add_executable(test_compile_aarch64
    spsr_el2.c
    gich_vmcr.c
    main.c
)

target_include_directories(test_compile_aarch64
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}
)

install(TARGETS test_compile_aarch64 DESTINATION bin)
add_dependencies(test_compile_aarch64 test_generate_aarch64)
