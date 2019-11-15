![PAL](https://github.com/Bareflank/pal/raw/gh-pages/PAL-logo.png)

Are you working on a bare-metal software project for Intel or ARM?

Are you sick of hunting through a 6000 page .pdf file to find basic facts about the contents of a system register?

Do you hate reading and writing code that ```sets |= (bitfields && like) << this;```? (and accidentally using logical AND instead of bitwise AND in the process?)

Is your software so tightly coupled to your CPU that unit testing seems impossible?

## You could use a PAL!

The Bareflank **P**rocessor **A**bstraction **L**ayer transforms facts about your CPU into a software support library. This lets you access and manipulate the low-level details of your hardware through a convinient software API. Supose you are working on a C++ project for the Intel platform, and compiling/assembling with a GNU toolchain:

0. Install Python 3 and pip install lxml

1. Generate a PAL for your project:

```
git clone https://github.com/bareflank/pal.git
./pal/pal.py --arch=intel_x64 --language=c++11 --access_mechanism=gas_att
cp -r pal/output </path/to/your/project>
```

2. Profit!

```
#include "pal/control_register/cr0.h"
#include "pal/msr/ia32_feature_control.h"
#include "pal/cpuid/leaf_01_eax.h"

void pal_test(void)
{
    pal::cr0::pg::enable();                      // <-- Enable paging in CR0
    auto msr = pal::ia32_feature_control::get(); // <-- Read the current value of an MSR
    pal::leaf_01_eax::dump();                    // <-- Print the value of a CPUID leaf
}

```

3. Reuse the code above *in userspace* for your unit tests:

```
./pal/pal.py --arch=intel_x64 --language=c++11 --access_mechanism=test
```

4. Explore other built-in configuration options:

```
./pal/pal --help
```

## Are you using CMake?

PAL has first class CMake support, just use upper-case names for all of PAL's configuration options:

```
git clone https://github.com/bareflank/pal.git
mkdir build && cd build
cmake ../pal -DARCH=armv8-a -DACCESS_MECHANISM=gas_aarch64
make
```

## Does PAL generate *everything* from the \<insert_vendor_name\> manual?
Not yet, but it does support a whole lot. Is the project missing something that you need? Help us add it! There are a few different ways you can contribute new defintions to the project:

1) Author and contribute a .yml file to the [project's data directory](data). You can copy an exisitng definition as a starting point. One .yml file == one register defintion.

2) Contribute a new [parser](pal/parser) for another existing source of information. For example, PAL can generate ARMv8-A register definitons from [ARM's offical machine readable spec](https://developer.arm.com/architectures/cpu-architecture/a-profile/exploration-tools).

3) PAL can generate the project's built in .yml files *for you*, if you can provide a way to parse an existing source of information into a [PAL model](pal/model).


## Current status and scope

This project is primarily being developed as a support library for the [Bareflank Hypervisor SDK](https://github.com/bareflank/hypervisor), but we hope that other projects will benefit as well. Scope is currently limited to:

1. System registers of a CPU.
2. Intel x86_64
3. ARMv8-A
4. C and C++

The project's future wish-list currently consists of support for:

1. Instructions of a CPU
2. Registers of peripheral devices (e.g. IOMMU, PCIe, etc)
3. Additional microarchitectures
4. Additional programming languages
