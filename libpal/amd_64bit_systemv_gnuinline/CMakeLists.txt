add_library(pal_amd_64bit_systemv_gnuinline)

set_target_properties(pal_amd_64bit_systemv_gnuinline PROPERTIES LINKER_LANGUAGE C)

target_include_directories(pal_amd_64bit_systemv_gnuinline PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
    ${CMAKE_CURRENT_LIST_DIR}/include/pal/instruction
)

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include/pal/instruction)
target_sources(pal_amd_64bit_systemv_gnuinline PRIVATE
    ${SRC_DIR}/cpuid_inline.h
)

if(PAL_C)
    add_custom_command(
        TARGET pal_amd_64bit_systemv_gnuinline
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_CURRENT_LIST_DIR}/include
            ${CMAKE_BINARY_DIR}/c/amd_64bit_systemv_gnuinline/include
    )
endif()

if(PAL_C++11)
    add_custom_command(
        TARGET pal_amd_64bit_systemv_gnuinline
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_CURRENT_LIST_DIR}/include
            ${CMAKE_BINARY_DIR}/c++11/amd_64bit_systemv_gnuinline/include
    )
endif()
