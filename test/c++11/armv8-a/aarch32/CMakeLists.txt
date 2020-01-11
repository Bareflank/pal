cmake_minimum_required(VERSION 3.12)
project(c++11-arm-linux-gnueabihf-gcc CXX)
include(${PAL_SOURCE_CMAKE_DIR}/init_subproject.cmake)

set(PROJECT_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/pal_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_INSTALL_PREFIX}/pal
        --arch=armv8-a
        --language=c++11
        --access_mechanism=gas_aarch32
        --print_mechanism=printf_utf8
        --file_format=unix
        --generator=c++_header
    COMMAND cmake -E touch ${PROJECT_OUTPUT_STAMP}
    OUTPUT ${PROJECT_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
    COMMENT "Generating PAL outputs"
)

add_custom_target(test_generate_aarch32 ALL DEPENDS ${PROJECT_OUTPUT_STAMP})

add_executable(test_compile_aarch32
    cpacr.cpp
    edeccr.cpp
    edecr.cpp
    main.cpp
)

target_include_directories(test_compile_aarch32
    PRIVATE
        ${CMAKE_INSTALL_PREFIX}
)

install(TARGETS test_compile_aarch32 DESTINATION bin)
add_dependencies(test_compile_aarch32 test_generate_aarch32)
