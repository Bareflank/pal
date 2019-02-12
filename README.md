# Shoulder for ARM

The Shoulder for ARM project aims to bridge the gap between software developers
and the ARM Architecture Reference Manual while programming bare-metal
applications for the ARMv8-A architecture. Using ARM's
[machine parsable CPU specifications](https://developer.arm.com/products/architecture/cpu-architecture/a-profile/exploration-tools),
Shoulder generates a register-access intrinsics API for C and C++ as a
header file to be included in your own bare-metal ARM software or firmware
project.

Shoulder for ARM is currently in a work-in-progress state, and is mostly
being used as a support tool for porting the
[Bareflank Hypervisor](https://github.com/Bareflank/hypervisor) project to ARM.
Instructions and examples on how to use Shoulder for your own projects will
be added as the project matures for other use cases.
