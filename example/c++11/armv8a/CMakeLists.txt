add_library(c++_example_dependencies INTERFACE)

if(PAL_ARMV8A_AARCH64_AAPCS64_GNUINLINE)
    target_link_libraries(c++_example_dependencies INTERFACE pal_armv8a_aarch64_aapcs64_gnuinline c++11_armv8a_aarch64_aapcs64_gnuinline)
elseif(PAL_ARMV8A_AARCH64_LINUX_IOCTL)
    target_link_libraries(c++_example_dependencies INTERFACE pal_armv8a_aarch64_linux_ioctl c++11_armv8a_aarch64_linux_ioctl)
else()
    message(FATAL_ERROR "Must enable at least one ARMv8a-based pal implementation to build ARMv8a example projects")
endif()

add_executable(c++_basic_usage basic_usage.cpp)
target_link_libraries(c++_basic_usage c++_example_dependencies)
