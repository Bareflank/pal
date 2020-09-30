enable_language(ASM_MASM)

add_library(pal_x64_64bit_none_ms64)

target_sources(pal_x64_64bit_none_ms64 PRIVATE 
    cpuid.asm
    rdmsr.asm
    read_cr0.asm
    read_cr2.asm
    read_cr3.asm
    read_cr4.asm
    read_cr8.asm
    vmread.asm
    vmwrite.asm
    write_cr0.asm
    write_cr2.asm
    write_cr3.asm
    write_cr4.asm
    write_cr8.asm
    wrmsr.asm
    xgetbv.asm
    xsetbv.asm
)
