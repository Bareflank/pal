enable_language(ASM-ATT)

add_library(pal_armv8_aarch64_none_aapcs64)
target_include_directories(pal_armv8_aarch64_none_aapcs64 PRIVATE
    ${CMAKE_SOURCE_DIR}/devpal/include
)

target_sources(pal_armv8_aarch64_none_aapcs64 PRIVATE
    sys.s
    sysl.s
)
