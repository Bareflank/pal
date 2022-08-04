add_library(c++_amd_example_dependencies INTERFACE)

if(PAL_AMD_64BIT_LINUX_IOCTL)
    target_link_libraries(c++_amd_example_dependencies INTERFACE pal_amd_64bit_linux_ioctl c++11_amd_64bit_linux_ioctl)
elseif(PAL_AMD_64BIT_SYSTEMV_GNUINLINE)
    target_link_libraries(c++_amd_example_dependencies INTERFACE pal_amd_64bit_systemv_gnuinline c++11_amd_64bit_systemv_gnuinline)
else()
    message(FATAL_ERROR "Must enable at least one AMD-based pal implementation to build AMD example projects")
endif()

add_executable(c++11_amd_basic_usage basic_usage.cpp)
target_link_libraries(c++11_amd_basic_usage c++_amd_example_dependencies)
