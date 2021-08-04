add_library(pal_armv8_aarch64_linux_devpal)
target_include_directories(pal_armv8_aarch64_linux_devpal PRIVATE
    ${PAL_SOURCE_ROOT_DIR}/devpal/include
)

target_sources(pal_armv8_aarch64_linux_devpal PRIVATE
    sys.c
    sysl.c
)
