enable_language(ASM_NASM)

add_library(pal_intel_64bit_systemv_nasm)

target_compile_options(pal_intel_64bit_systemv_nasm PRIVATE
    "-f elf64"
)

target_sources(pal_intel_64bit_systemv_nasm PRIVATE
    bsf.asm
    bsr.asm
    clflush.asm
    cpuid.asm
    in_16.asm
    in_32.asm
    in_8.asm
    invd.asm
    invept.asm
    invept_checked.asm
    invvpid.asm
    invvpid_checked.asm
    lfence.asm
    lgdt.asm
    lidt.asm
    mfence.asm
    out_16.asm
    out_32.asm
    out_8.asm
    pause.asm
    popcnt.asm
    rdmsr.asm
    rdtsc.asm
    rdtscp.asm
    read_cr0.asm
    read_cr2.asm
    read_cr3.asm
    read_cr4.asm
    read_cr8.asm
    read_cs.asm
    read_dr7.asm
    read_ds.asm
    read_es.asm
    read_fs.asm
    read_gs.asm
    read_ldtr.asm
    read_mem16.asm
    read_mem32.asm
    read_mem64.asm
    read_mem8.asm
    read_rflags.asm
    read_ss.asm
    read_tr.asm
    sfence.asm
    sgdt.asm
    sidt.asm
    vmcall.asm
    vmcall_hyperv.asm
    vmcall_kvm.asm
    vmcall_xen.asm
    vmclear.asm
    vmclear_checked.asm
    vmptrld.asm
    vmptrld_checked.asm
    vmptrst.asm
    vmptrst_checked.asm
    vmread.asm
    vmread_checked.asm
    vmread.asm
    vmread_checked.asm
    vmwrite.asm
    vmwrite_checked.asm
    vmxoff.asm
    vmxoff_checked.asm
    vmxoff.asm
    vmxoff_checked.asm
    vmxon.asm
    vmxon_checked.asm
    wbinvd.asm
    write_cr3.asm
    write_cr4.asm
    write_cr8.asm
    write_cs.asm
    write_dr7.asm
    write_ds.asm
    write_es.asm
    write_fs.asm
    write_gs.asm
    write_ldtr.asm
    write_mem16.asm
    write_mem32.asm
    write_mem64.asm
    write_mem8.asm
    write_rflags.asm
    write_ss.asm
    write_tr.asm
    wrmsr.asm
    xgetbv.asm
    xsetbv.asm
)
