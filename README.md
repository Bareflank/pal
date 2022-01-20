![PAL](https://github.com/Bareflank/pal/raw/gh-pages/PAL-logo.png)

The Bareflank PAL (**P**rocessor/**P**eripheral **A**bstraction **L**ayer) project
provides developers and researchers of systems (operating systems,
hypervisors, platform firmware) with a software API for manipulating low-level
system state (instructions and registers) within a CPU. The project also provides
APIs for register-level interfaces (memory-mapped, I/O mapped) for peripheral
devices and system data structures.

The PAL project consists of:

* A [database](data) (yaml files) that describes facts (normally documented by .pdf
manuals) about how a CPU (e.g. Intel, AMD, ARMv8), peripheral (e.g. PCIe device)
or data structure (e.g. ACPI table) is structured and accessed.
* [Code generators](pal) (C, C++, Rust) that create a library of accessor functions
(a software API) for manipulating the information described by the database.
* [Support libraries](libpal) and [shims](devpal) (e.g. drivers) that enable generated accessor
functions to integrate and run in numerous execution contexts (e.g. inline
assembly code, or forwarded from an application to a driver via an IOCTL)
* Build system interfaces that provide integration with a variety of compilers,
languages, and toolchains
* [Examples](example) that demonstrate how to use PAL's generated APIs in each supported
programming language

The PAL project enables a variety of different use cases:

* Control (read/write/execute) and view (print) the contents of hardware devices in a bare-metal software project
* Research, audit, test, or control privileged system state from an unprivileged application (much like [Chipsec](https://github.com/chipsec/chipsec) or [RWEverything](http://rweverything.com/))
* Build test harnesses, mock devices, or hardware emulators

## A Brief Example

To demonstrate what PAL is all about, let's implement a small program
that uses PALs generated APIs for the Intel platform in 3 different languages
(C, C++, Rust).  The program defines a single function that performs the
following tasks: 

* Read the value of the IA32_FEATURE_CONTROL MSR by name
* Read the value of the IA32_TSC MSR using its address, and the x86 RDMSR instruction
* Enable paging by setting the PG bit (bit 31) in control register CR0
* Print the value of CPUID leaf 0x1, output register EAX

### C

```c
#include "pal/msr/ia32_feature_control.h"
#include "pal/msr/ia32_tsc.h"
#include "pal/control_register/cr0.h"
#include "pal/cpuid/leaf_01_eax.h"

void pal_example(void)
{
    uint64_t msr1 = pal_get_ia32_feature_control();
    uint64_t msr2 = pal_execute_rdmsr(PAL_IA32_TSC_ADDRESS);
    pal_enable_cr0_pg();
    pal_print_leaf_01_eax();
}
```

### C++

```c++
#include "pal/msr/ia32_feature_control.h"
#include "pal/msr/ia32_tsc.h"
#include "pal/control_register/cr0.h"
#include "pal/cpuid/leaf_01_eax.h"

void pal_example(void)
{
    auto msr1 = pal::ia32_feature_control::get();
    auto msr2 = pal::execute_rdmsr(pal::ia32_tsc::ADDRESS);
    pal::cr0::pg::enable();
    pal::leaf_01_eax::print();
}
```

### Rust

```rust
use pal;

pub fn pal_example() {
    let msr1 = pal::msr::ia32_feature_control::get();
    let msr2 = pal::instruction::execute_rdmsr(pal::msr::ia32_tsc::ADDRESS);
    pal::control_register::cr0::pg::enable();
    pal::cpuid::leaf_01_eax::print();
}
```

For more examples that show how to use PAL with different CPU architectures and peripheral devices, check out the project's [example](example) and [test](test) directories.

## Dependencies

Build-time dependencies will vary depending on your host system, target language, build system, and compiler toolchain. The following provides a good starting point for using most of PAL's features:

### Ubuntu

For running the code generator:
```
sudo apt-get install python3 python3-pip
pip3 install lxml dataclasses colorama pyyaml
```

For building support libraries and shims:
```
sudo apt-get install cmake cmake-curses-gui build-essential linux-headers-$(uname -r)
```

### Windows

TODO

## Building and Integrating

There are numerous build interfaces to configure, generate, and build PAL APIs for use with your project. Depending on the needs of your target language, compiler toolchain and execution environment, you may need to use one or more of the following build interfaces.

### CMake (C/C++)

CMake provides the easiest way to integrate all of PAL's features with C and C++ projects. The CMake build interface works by specifying a configuration input that describes what PAL should generate code for (fomatted as `-DPAL_<ARCHITECTURE>_<EXCECUTION_STATE>_<SOURCE_ENVIRONMENT>_<TARGET_ENVIRONMENT>=ON`). Cmake then runs the code generator and builds any necessary support libraries and shims for that configuration. Example (run from the project's top directory):

```
mkdir build && cd build
cmake .. -DPAL_INTEL_64BIT_SYSTEMV_GNUINLINE=ON
make
```

To explore all available configuration opions for the CMake build interface, run the following from your CMake build directory:
```
ccmake .
```

### Cargo (Rust, experimental)

Cargo provides the easiest way to integrate all of PAL's features with Rust projects. The Cargo build interface works by specifying a crate feature that describes what PAL should generate code for (fomatted as `<architecture>_<execution_state>_<source_environment>_<target_environment`). Cargo then runs the PAL code generator and builds any necessary support libraries and shims for that configuration. Example (place this into your project's Cargo.toml):
```toml
[dependencies.pal]
git = "ssh://git@ssh.github.com/bareflank/pal.git"
features = ["intel_64bit_linux_ioctl"]
```

To explore all available configuration opions for the Cargo build interface, see the `[features]` section of PAL's [Cargo.toml](Cargo.toml) file

### Code Generator

If you want to generate code from the project's database that does not require any support libraries (e.g. C/C++ code with inline assembly), you can run the code generator directly. Example:

```
./pal/pal.py --language=c --execution_state=intel_64bit --access_mechanism=gnu_inline
```

To explore all available configuration opions for the code generator:

```
./pal/pal/py --help
```

## Project status and scope

TODO: Need to make a grid/table that shows support for many different arch/language/runtime scenarios:

## Is the project missing something you need?

Contributions, enhancements and feature requests to the project are welcome. In addition to the backlog in project's issue tracker, the project will always be seeking support for:

* Additional database entries. Is the project missing a defintion for something you need? Help us add it!
* Database auditing. Did you find a mistake in a database entry? Help us fix it!
* Database maintenance. Do you work for an orginization that designs or publishes the information described in our database? Get in touch to help us maintain the data over time!
