add_library(pal_amd_64bit_systemv_gnuinline INTERFACE)

target_include_directories(pal_amd_64bit_systemv_gnuinline INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}
    ${CMAKE_CURRENT_LIST_DIR}/include/pal/instruction
)

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include/pal/instruction)
target_sources(pal_amd_64bit_systemv_gnuinline PRIVATE
    ${SRC_DIR}/cpuid_inline.h
)

add_custom_target(pal_amd_64bit_systemv_gnuinline_install_headers)

if(PAL_C)
    add_custom_command(
        TARGET pal_amd_64bit_systemv_gnuinline_install_headers
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_CURRENT_LIST_DIR}/include
            ${CMAKE_BINARY_DIR}/c/amd_64bit_systemv_gnuinline/include
    )
endif()

if(PAL_C++11)
    add_custom_command(
        TARGET pal_amd_64bit_systemv_gnuinline_install_headers
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_CURRENT_LIST_DIR}/include
            ${CMAKE_BINARY_DIR}/c++11/amd_64bit_systemv_gnuinline/include
    )
endif()

add_dependencies(pal_amd_64bit_systemv_gnuinline pal_amd_64bit_systemv_gnuinline_install_headers)
