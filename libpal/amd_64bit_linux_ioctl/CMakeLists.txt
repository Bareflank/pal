add_library(pal_amd_64bit_linux_ioctl)
target_include_directories(pal_amd_64bit_linux_ioctl PRIVATE
    ${PAL_SOURCE_ROOT_DIR}/devpal/include
)

target_sources(pal_amd_64bit_linux_ioctl PRIVATE
    cpuid.c
    in_16.c
    in_32.c
    in_8.c
    out_16.c
    out_32.c
    out_8.c
    rdmsr.c
    rdtsc.c
    read_cr0.c
    read_cr2.c
    read_cr3.c
    read_cr4.c
    read_cr8.c
    read_mem16.c
    read_mem32.c
    read_mem64.c
    read_mem8.c
    write_cr0.c
    write_cr2.c
    write_cr3.c
    write_cr4.c
    write_cr8.c
    write_mem16.c
    write_mem32.c
    write_mem64.c
    write_mem8.c
    wrmsr.c
)
