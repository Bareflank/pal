use std::process::Command;

fn main() {
    generate_language_bindings();
    link_libpal();
    println!("cargo:rerun-if-changed=build.rs");
}

fn generate_language_bindings() {
    let cmake_build_dir = "./build";
    std::fs::create_dir_all(cmake_build_dir)
        .expect("Failed to create cmake build directory");

    configure_cmake(cmake_build_dir);
    run_cmake(cmake_build_dir);
}

fn link_libpal() {
    if cfg!(feature = "armv8a-aarch64-none-aapcs64") {
        println!(r"cargo:rustc-link-search=./build/libpal/armv8a-aarch64-none-aapcs64/");
        println!("cargo:rustc-link-lib=static=pal_armv8a_aarch64_none_aapcs64");
    }

    if cfg!(feature = "armv8a-aarch64-linux-devpal") {
        println!(r"cargo:rustc-link-search=./build/libpal/armv8a-aarch64-linux-devpal/");
        println!("cargo:rustc-link-lib=static=pal_armv8a_aarch64_linux_devpal");
    }

    if cfg!(feature = "x64-64bit-linux-devpal") {
        println!(r"cargo:rustc-link-search=./build/libpal/x64-64bit-linux-devpal/");
        println!("cargo:rustc-link-lib=static=pal_x64_64bit_linux_devpal");
    }

    if cfg!(feature = "x64-64bit-none-ms64") {
        println!(r"cargo:rustc-link-search=./build/libpal/x64-64bit-none-ms64/");
        println!("cargo:rustc-link-lib=static=pal_x64_64bit_none_ms64");
    }

    if cfg!(feature = "x64-64bit-none-systemv") {
        println!(r"cargo:rustc-link-search=./build/libpal/x64-64bit-none-systemv/");
        println!("cargo:rustc-link-lib=static=pal_x64_64bit_none_systemv");
    }
}

fn configure_cmake(cmake_build_dir: &str) {
    let mut args = vec![
        "-B",
        cmake_build_dir,
        "-S",
        ".",
        "-DPAL_TARGET_LANGUAGE=rust",
        "-DPAL_PRINT_MECHANISM=rust_println"
    ];

    if cfg!(feature = "intel_64bit") {
        args.push("-DPAL_TARGET_EXECUTION_STATE=intel_64bit");
    }

    if cfg!(feature = "armv8a_aarch64") {
        args.push("-DPAL_TARGET_EXECUTION_STATE=armv8a_aarch64");
    }

    if cfg!(feature = "armv8a_aarch32") {
        args.push("-DPAL_TARGET_EXECUTION_STATE=armv8a_aarch32");
    }

    if cfg!(feature = "armv8a-aarch64-none-aapcs64") {
        args.push("-DPAL_LIBPAL_ABI=armv8a-aarch64-none-aapcs64");
    }

    if cfg!(feature = "armv8a-aarch64-linux-devpal") {
        args.push("-DPAL_LIBPAL_ABI=armv8a-aarch64-linux-devpal");
    }

    if cfg!(feature = "x64-64bit-linux-devpal") {
        args.push("-DPAL_LIBPAL_ABI=x64-64bit-linux-devpal");
    }

    if cfg!(feature = "x64-64bit-none-ms64") {
        args.push("-DPAL_LIBPAL_ABI=x64-64bit-none-ms64");
    }

    if cfg!(feature = "x64-64bit-none-systemv") {
        args.push("-DPAL_LIBPAL_ABI=x64-64bit-none-systemv");
    }

    let output = Command::new("cmake")
            .args(args)
            .output()
            .expect("cmake configure command failed");

    let output_text = String::from_utf8(output.stdout).unwrap();
    println!("{}", output_text);
}

fn run_cmake(cmake_build_dir: &str) {
    let output = Command::new("cmake")
            .arg("--build")
            .arg(cmake_build_dir)
            .output()
            .expect("cmake build command failed");
    let output_text = String::from_utf8(output.stdout).unwrap();
    println!("{}", output_text);
}
