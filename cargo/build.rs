use std::process::Command;
use std::env;

fn main() {
    generate_language_bindings();
    build_libpal();
    link_libpal();
    println!("cargo:rerun-if-changed=build.rs");
}

fn generate_language_bindings() {
    let out_dir  = env::var_os("OUT_DIR").unwrap();

    let mut args = vec![
        "-o",
        out_dir.to_str().unwrap(),
        "--language=rust",
        "--print_mechanism=rust_println"
    ];

    if cfg!(feature = "armv8a_aarch64_linux_ioctl") {
        args.push("--execution_state=armv8a_aarch64");
        args.push("--access_mechanism=libpal");
    }

    if cfg!(feature = "intel_64bit_systemv_nasm") || cfg!(feature = "intel_64bit_linux_ioctl") {
        args.push("--execution_state=intel_64bit");
        args.push("--access_mechanism=libpal");
    }

    // TODO: Add support for print functions in a no_std environment
    if cfg!(not(feature = "enable_printers")) {
        args.push("--enable_printers=off");
    }

    let status = Command::new("./pal.py")
            .args(args)
            .status()
            .expect("failed to spawn pal.py");

    assert!(status.success());
}

fn build_libpal() {
    let cmake_build_dir   = env::var_os("OUT_DIR").unwrap();

    configure_cmake(cmake_build_dir.to_str().unwrap());
    run_cmake(cmake_build_dir.to_str().unwrap());
}


fn link_libpal() {
    let out_dir  = env::var_os("OUT_DIR").unwrap();

    if cfg!(feature = "armv8a_aarch64_linux_ioctl") {
        println!(r"cargo:rustc-link-search={}/libpal/armv8a_aarch64_linux_ioctl/", out_dir.to_str().unwrap());
        println!("cargo:rustc-link-lib=static=pal_armv8a_aarch64_linux_ioctl");
    }

    if cfg!(feature = "intel_64bit_linux_ioctl") {
        println!(r"cargo:rustc-link-search={}/libpal/intel_64bit_linux_ioctl/", out_dir.to_str().unwrap());
        println!("cargo:rustc-link-lib=static=pal_intel_64bit_linux_ioctl");
    }

    if cfg!(feature = "intel_64bit_systemv_nasm") {
        println!(r"cargo:rustc-link-search={}/libpal/intel_64bit_systemv_nasm/", out_dir.to_str().unwrap());
        println!("cargo:rustc-link-lib=static=pal_intel_64bit_systemv_nasm");
    }
}

fn configure_cmake(cmake_build_dir: &str) {
    let mut args = vec![
        "-B",
        cmake_build_dir,
        "-S",
        ".",
        "-DPAL_C=OFF",
        "-DPAL_C++11=OFF"
    ];

    if cfg!(feature = "armv8a_aarch64_linux_ioctl") {
        args.push("-DPAL_ARMV8A_AARCH64_LINUX_IOCTL=ON");
    }

    if cfg!(feature = "intel_64bit_linux_ioctl") {
        args.push("-DPAL_INTEL_64BIT_LINUX_IOCTL=ON");
    }

    if cfg!(feature = "intel_64bit_systemv_nasm") {
        args.push("-DPAL_INTEL_64BIT_SYSTEMV_NASM=ON");
    }

    let status = Command::new("cmake")
            .args(args)
            .status()
            .expect("failed to spawn cmake configure");

    assert!(status.success());
}

fn run_cmake(cmake_build_dir: &str) {
    let status = Command::new("cmake")
            .arg("--build")
            .arg(cmake_build_dir)
            .status()
            .expect("failed to spawn cmake build");

    assert!(status.success());
}
