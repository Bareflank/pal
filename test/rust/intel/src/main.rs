#![cfg_attr(not(feature = "std"),
    no_std,
    feature(lang_items, start),
)]

mod cpuid;
mod cr3;
mod eptp;
mod guest_interrupt_status;
mod ia32_feature_control;
mod leaf_01;
mod leaf_04;
mod leaf_0d;
mod rdmsr;
mod read_cr3;
mod write_cr3;
mod xcr0;

fn main() {

    cr3::test_cr3_compile();
    cpuid::test_cpuid_compile();
    eptp::test_eptp_compile();
    guest_interrupt_status::test_guest_interrupt_status_compile();
    ia32_feature_control::test_ia32_feature_control_compile();
    rdmsr::test_rdmsr_compile();
    leaf_01::test_leaf_01_compile();
    leaf_04::test_leaf_04_compile();
    leaf_0d::test_leaf_0d_compile();
    read_cr3::test_read_cr3_compile();
    write_cr3::test_write_cr3_compile();
    xcr0::test_xcr0_compile();
}

#[cfg(not(feature = "std"))]
#[start]
fn start(_argc: isize, _argv: *const *const u8) -> isize {
    main();
    0
}

#[cfg(not(feature = "std"))]
#[no_mangle]
fn __libc_csu_init() {}

#[cfg(not(feature = "std"))]
#[no_mangle]
fn __libc_csu_fini() {}

#[cfg(not(feature = "std"))]
#[no_mangle]
fn __libc_start_main() {}

#[cfg(not(feature = "std"))]
#[lang = "eh_personality"]
extern "C" fn eh_personality() {}

#[cfg(not(feature = "std"))]
#[panic_handler]
fn panic(_panic: &core::panic::PanicInfo<'_>) -> ! {
    loop {}
}
