add_library(pal_intel_64bit_systemv_gnuinline)

set_target_properties(pal_intel_64bit_systemv_gnuinline PROPERTIES LINKER_LANGUAGE C)

target_include_directories(pal_intel_64bit_systemv_gnuinline PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
)

target_sources(pal_intel_64bit_systemv_gnuinline PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include/pal/instruction/cpuid_inline.h
    ${CMAKE_CURRENT_SOURCE_DIR}/include/pal/instruction/rdmsr_inline.h
)

add_custom_command(
    TARGET pal_intel_64bit_systemv_gnuinline
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_CURRENT_LIST_DIR}/include
        ${CMAKE_CURRENT_BINARY_DIR}/include
)
