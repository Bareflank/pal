add_library(c_example_dependencies INTERFACE)

if(PAL_INTEL_64BIT_SYSTEMV_NASM)
    target_link_libraries(c_example_dependencies INTERFACE pal_intel_64bit_systemv_nasm c_intel_64bit_systemv_nasm)
elseif(PAL_INTEL_64BIT_LINUX_IOCTL)
    target_link_libraries(c_example_dependencies INTERFACE pal_intel_64bit_linux_ioctl c_intel_64bit_linux_ioctl)
elseif(PAL_INTEL_64BIT_SYSTEMV_GNUATT)
    target_link_libraries(c_example_dependencies INTERFACE pal_intel_64bit_systemv_gnuatt c_intel_64bit_systemv_gnuatt)
elseif(PAL_INTEL_64BIT_SYSTEMV_GNUINTEL)
    target_link_libraries(c_example_dependencies INTERFACE pal_intel_64bit_systemv_gnuintel c_intel_64bit_systemv_gnuintel)
elseif(PAL_INTEL_64BIT_MS64_MASM)
    target_link_libraries(c_example_dependencies INTERFACE pal_intel_64bit_ms64_masm c_intel_64bit_ms64_masm)
else()
    message(FATAL_ERROR "Must enable at least one Intel-based pal implementation to build Intel example projects")
endif()

add_executable(c_basic_usage basic_usage.c)
target_link_libraries(c_basic_usage c_example_dependencies)

add_executable(c_hypercall hypercall.c)
target_link_libraries(c_hypercall c_example_dependencies)

add_executable(c_acpi acpi.c)
target_link_libraries(c_acpi c_example_dependencies)

add_executable(c_pcie pcie.c)
target_link_libraries(c_pcie c_example_dependencies)
