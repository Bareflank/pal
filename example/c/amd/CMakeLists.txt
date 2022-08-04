add_library(c_amd_example_dependencies INTERFACE)

if(PAL_AMD_64BIT_SYSTEMV_GNUINLINE)
    target_link_libraries(c_amd_example_dependencies INTERFACE pal_amd_64bit_systemv_gnuinline c_amd_64bit_systemv_gnuinline)
elseif(PAL_AMD_64BIT_LINUX_IOCTL)
    target_link_libraries(c_amd_example_dependencies INTERFACE pal_amd_64bit_linux_ioctl c_amd_64bit_linux_ioctl)
else()
    message(FATAL_ERROR "Must enable at least one AMD-based pal implementation to build AMD example projects")
endif()

add_executable(c_amd_basic_usage basic_usage.c)
target_link_libraries(c_amd_basic_usage c_amd_example_dependencies)
