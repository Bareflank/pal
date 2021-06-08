cmake_minimum_required(VERSION 3.12)
project(pal C CXX)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

include(${CMAKE_CURRENT_LIST_DIR}/cmake/init_project.cmake)

set(PYTHONPATH ${CMAKE_CURRENT_LIST_DIR})

file(GLOB_RECURSE PAL_SRC_FILES "pal/*.py" "data/*.yml")
set(PAL_OUTPUT_STAMP ${CMAKE_CURRENT_BINARY_DIR}/pal_output.stamp)

if(PAL_QUIET_CMAKE)
    set(PAL_LOG_LEVEL "error")
else()
    set(PAL_LOG_LEVEL "info")
endif()

add_custom_command(
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_LIST_DIR}/pal.py
        -o ${PAL_OUTPUT_DIR}/pal
        --execution_state=${PAL_TARGET_EXECUTION_STATE}
        --language=${PAL_TARGET_LANGUAGE}
        --access_mechanism=${PAL_ACCESS_MECHANISM}
        --print_mechanism=${PAL_PRINT_MECHANISM}
        --file_format=${PAL_FILE_FORMAT}
        --acpi=${PAL_ENABLE_ACPI}
        --log_level=${PAL_LOG_LEVEL}
    COMMAND cmake -E touch ${PAL_OUTPUT_STAMP}
    OUTPUT ${PAL_OUTPUT_STAMP}
    DEPENDS ${PAL_SRC_FILES}
    COMMENT "Generating PAL outputs"
)

add_custom_target(pal_generate ALL DEPENDS ${PAL_OUTPUT_STAMP})

if(${PAL_ACCESS_MECHANISM} STREQUAL libpal)
    add_subdirectory(libpal)
endif()

if(${PAL_ENABLE_DEVPAL})
    add_subdirectory(devpal)
endif()

add_library(pal INTERFACE)
add_dependencies(pal pal_generate)
target_include_directories(pal INTERFACE ${PAL_OUTPUT_DIR})
target_link_libraries(pal INTERFACE libpal)

set(CMAKE_INSTALL_MESSAGE NEVER)
install(
    DIRECTORY ${PAL_OUTPUT_DIR}/pal
    DESTINATION ${CMAKE_INSTALL_PREFIX}/include
)

if(PAL_ENABLE_TEST)
    add_subdirectory(test)
endif()

if(PAL_ENABLE_EXAMPLE)
    add_subdirectory(example)
endif()

if(NOT PAL_QUIET_CMAKE)
    pal_print_banner()
    pal_print_usage()
endif()
