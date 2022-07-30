add_library(pal_armv8a_aarch64_linux_ioctl)
target_include_directories(pal_armv8a_aarch64_linux_ioctl PRIVATE
    ${PAL_SOURCE_ROOT_DIR}/devpal/include
)

target_sources(pal_armv8a_aarch64_linux_ioctl PRIVATE
    sys.c
    sysl.c
    smc.c
    hvc.c
    read_mem16.c
    read_mem32.c
    read_mem64.c
    read_mem8.c
    write_mem16.c   
    write_mem32.c
    write_mem64.c
    write_mem8.c
)
