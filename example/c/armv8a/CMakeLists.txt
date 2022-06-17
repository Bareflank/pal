add_library(c_example_dependencies INTERFACE)

if(PAL_ARMV8A_AARCH64_AAPCS64_GNUINLINE)
    target_link_libraries(c_example_dependencies INTERFACE pal_armv8a_aarch64_aapcs64_gnuinline c_armv8a_aarch64_aapcs64_gnuinline)
elseif(PAL_ARMV8A_AARCH64_LINUX_IOCTL)
    target_link_libraries(c_example_dependencies INTERFACE pal_armv8a_aarch64_linux_ioctl c_armv8a_aarch64_linux_ioctl)
else()
    message(FATAL_ERROR "Must enable at least one ARMv8a-based pal implementation to build ARMv8a example projects")
endif()

add_executable(c_basic_usage basic_usage.c)
target_link_libraries(c_basic_usage c_example_dependencies)
