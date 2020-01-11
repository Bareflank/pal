cmake_minimum_required(VERSION 3.12)
project(pal NONE)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

include(${CMAKE_CURRENT_LIST_DIR}/cmake/colors.cmake)
include(${CMAKE_CURRENT_LIST_DIR}/cmake/config/default.cmake)
include(${PAL_SOURCE_CMAKE_DIR}/macros/print_banner.cmake)
include(${PAL_SOURCE_CMAKE_DIR}/macros/print_usage.cmake)

set(PYTHONPATH ${CMAKE_CURRENT_LIST_DIR})

file(GLOB_RECURSE PAL_SRC_FILES "pal/*.py" "data/*.yml")
set(PAL_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/pal_output.stamp)

add_custom_command(
    COMMAND PYTHONPATH=${PYTHONPATH} ${Python3_EXECUTABLE} -m pal
        -o ${CMAKE_BINARY_DIR}/pal
        --arch=${ARCH}
        --language=${LANGUAGE}
        --access_mechanism=${ACCESS_MECHANISM}
        --print_mechanism=${PRINT_MECHANISM}
        --file_format=${FILE_FORMAT}
        --generator=${GENERATOR}
        --register_read_function=${REGISTER_READ_FUNCTION}
        --register_write_function=${REGISTER_WRITE_FUNCTION}
        --field_read_function=${FIELD_READ_FUNCTION}
        --field_write_function=${FIELD_WRITE_FUNCTION}
        --bit_set_function=${BIT_SET_FUNCTION}
        --bit_is_set_function=${BIT_IS_SET_FUNCTION}
        --bit_clear_function=${BIT_CLEAR_FUNCTION}
        --bit_is_clear_function=${BIT_IS_CLEAR_FUNCTION}
        --print_function=${PRINT_FUNCTION}
    COMMAND cmake -E touch ${PAL_OUTPUT_STAMP}
    OUTPUT ${PAL_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
    COMMENT "Generating PAL outputs"
)

add_custom_target(generate ALL DEPENDS ${PAL_OUTPUT_STAMP})

set(CMAKE_INSTALL_MESSAGE NEVER)
install(
    DIRECTORY ${CMAKE_BINARY_DIR}/pal
    DESTINATION ${CMAKE_INSTALL_PREFIX}/include
)

print_banner()
print_usage()
