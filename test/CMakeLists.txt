pal_add_compilation_test(
    c++11-aarch64-linux-gnu-gcc
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/c++11/armv8a/aarch64
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    TOOLCHAIN ${PAL_SOURCE_CMAKE_DIR}/toolchain/aarch64-linux-gnu-gcc.cmake
    INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/c++11-aarch64-linux-gnu-gcc
)

pal_add_compilation_test(
    c++11-arm-linux-gnueabihf-gcc
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/c++11/armv8a/aarch32
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    TOOLCHAIN ${PAL_SOURCE_CMAKE_DIR}/toolchain/arm-linux-gnueabihf-gcc.cmake
    INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/c++11-arm-linux-gnueabihf-gcc
)

pal_add_compilation_test(
    c++11-intel-linux-gnu-gcc
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/c++11/intel
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    TOOLCHAIN ${PAL_SOURCE_CMAKE_DIR}/toolchain/x86_64-linux-gnu-gcc.cmake
    INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/c++11-intel-linux-gnu-gcc
)

pal_add_compilation_test(
    c-aarch64-linux-gnu-gcc
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/c/armv8a/aarch64
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    TOOLCHAIN ${PAL_SOURCE_CMAKE_DIR}/toolchain/aarch64-linux-gnu-gcc.cmake
    INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/c-aarch64-linux-gnu-gcc
)

pal_add_compilation_test(
    c-aarch32-linux-gnu-gcc
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/c/armv8a/aarch32
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    TOOLCHAIN ${PAL_SOURCE_CMAKE_DIR}/toolchain/arm-linux-gnueabihf-gcc.cmake
    INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/c-aarch32-linux-gnu-gcc
)

pal_add_compilation_test(
    c-intel-linux-gnu-gcc
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/c/intel
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}
    TOOLCHAIN ${PAL_SOURCE_CMAKE_DIR}/toolchain/x86_64-linux-gnu-gcc.cmake
    INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}/c-intel-linux-gnu-gcc
)
