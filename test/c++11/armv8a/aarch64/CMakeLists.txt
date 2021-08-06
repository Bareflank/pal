cmake_minimum_required(VERSION 3.12)
project(c++11-aarch64-linux-gnu-gcc CXX)

set(PROJECT_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/pal_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}
        --execution_state=armv8a_aarch64
        --language=c++11
        --access_mechanism=gnu_inline
        --print_mechanism=printf_utf8
        --file_format=unix
    COMMAND cmake -E touch ${PROJECT_OUTPUT_STAMP}
    OUTPUT ${PROJECT_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
    COMMENT "Generating PAL outputs"
)

add_custom_target(test_generate_aarch64 ALL DEPENDS ${PROJECT_OUTPUT_STAMP})

add_executable(test_compile_aarch64
    spsr_el2.cpp
    # gich_vmcr.cpp
    main.cpp
)

target_include_directories(test_compile_aarch64
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}/include
)

install(TARGETS test_compile_aarch64 DESTINATION bin)
add_dependencies(test_compile_aarch64 test_generate_aarch64)
