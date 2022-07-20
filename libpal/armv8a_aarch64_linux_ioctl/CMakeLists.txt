add_library(pal_armv8a_aarch64_linux_ioctl)
target_include_directories(pal_armv8a_aarch64_linux_ioctl PRIVATE
    ${PAL_SOURCE_ROOT_DIR}/devpal/include
)

target_sources(pal_armv8a_aarch64_linux_ioctl PRIVATE
    sys.c
    sysl.c
    smc.c
)
