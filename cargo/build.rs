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

    if cfg!(feature = "intel_64bit_systemv_nasm") || cfg!(feature = "intel_64bit_linux_ioctl") {
        args.push("--execution_state=intel_64bit");
        args.push("--access_mechanism=libpal");
    }

    // TODO: Add support for print functions in a no_std environment
    if cfg!(feature = "intel_64bit_systemv_nasm") {
        args.push("--enable_printers=off");
    }

    let output = Command::new("./pal.py")
            .args(args)
            .output()
            .expect("failed to spawn pal.py");

    assert!(output.status.success());

    let output_text = String::from_utf8(output.stdout).unwrap();
    println!("{}", output_text);
}

fn build_libpal() {
    let cmake_build_dir   = env::var_os("OUT_DIR").unwrap();

    configure_cmake(cmake_build_dir.to_str().unwrap());
    run_cmake(cmake_build_dir.to_str().unwrap());
}


fn link_libpal() {
    let out_dir  = env::var_os("OUT_DIR").unwrap();

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

    if cfg!(feature = "intel_64bit_linux_ioctl") {
        args.push("-DPAL_INTEL_64BIT_LINUX_IOCTL=ON");
    }

    if cfg!(feature = "intel_64bit_systemv_nasm") {
        args.push("-DPAL_INTEL_64BIT_SYSTEMV_NASM=ON");
    }

    let output = Command::new("cmake")
            .args(args)
            .output()
            .expect("failed to spawn cmake configure");

    assert!(output.status.success());

    let output_text = String::from_utf8(output.stdout).unwrap();
    println!("{}", output_text);
}

fn run_cmake(cmake_build_dir: &str) {
    let output = Command::new("cmake")
            .arg("--build")
            .arg(cmake_build_dir)
            .output()
            .expect("failed to spawn cmake build");

    assert!(output.status.success());

    let output_text = String::from_utf8(output.stdout).unwrap();
    println!("{}", output_text);
}
