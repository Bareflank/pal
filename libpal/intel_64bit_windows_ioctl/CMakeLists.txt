add_library(pal_intel_64bit_windows_ioctl)
target_include_directories(pal_intel_64bit_windows_ioctl PRIVATE
    ${PAL_SOURCE_ROOT_DIR}/devpal/include
)

target_sources(pal_intel_64bit_windows_ioctl PRIVATE
    # bsf.c
    # bsr.c
    # clflush.c
    cpuid.c
    in_16.c
    in_32.c
    in_8.c
    # invd.c
    # invept.c
    # invept_checked.c
    # invvpid.c
    # invvpid_checked.c
    # lfence.c
    # lgdt.c
    # lidt.c
    # mfence.c
    out_16.c
    out_32.c
    out_8.c
    # pause.c
    # popcnt.c
    rdmsr.c
    # rdtsc.c
    # rdtscp.c
    # read_cr0.c
    # read_cr2.c
    # read_cr3.c
    # read_cr4.c
    # read_cr8.c
    # read_cs.c
    # read_dr7.c
    # read_ds.c
    # read_es.c
    # read_fs.c
    # read_gs.c
    # read_ldtr.c
    # read_mem16.c
    # read_mem32.c
    # read_mem64.c
    # read_mem8.c
    # read_rflags.c
    # read_ss.c
    # read_tr.c
    # sfence.c
    # sgdt.c
    # sidt.c
    vmcall.c
    vmcall_kvm.c
    vmcall_xen.c
    # vmclear.c
    # vmclear_checked.c
    # vmptrld.c
    # vmptrld_checked.c
    # vmptrst.c
    # vmptrst_checked.c
    # vmread.c
    # vmread_checked.c
    # vmread.c
    # vmread_checked.c
    # vmwrite.c
    # vmwrite_checked.c
    # vmxoff.c
    # vmxoff_checked.c
    # vmxoff.c
    # vmxoff_checked.c
    # vmxon.c
    # vmxon_checked.c
    # wbinvd.c
    # write_cr3.c
    # write_cr4.c
    # write_cr8.c
    # write_cs.c
    # write_dr7.c
    # write_ds.c
    # write_es.c
    # write_fs.c
    # write_gs.c
    # write_ldtr.c
    # write_mem16.c
    # write_mem32.c
    # write_mem64.c
    # write_mem8.c
    # write_rflags.c
    # write_ss.c
    # write_tr.c
    wrmsr.c
    # xgetbv.c
    # xsetbv.c
)
