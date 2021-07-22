if(NOT EXISTS ${PAL_LINUX_HEADERS_DIR})
    message(FATAL_ERROR "Linux kernel headers not found: ${PAL_LINUX_HEADERS_DIR}")
endif()

set(MODULE_NAME devpal)
set(MODULE_BIN ${MODULE_NAME}.ko)
set(KBUILD_CMD make -C ${PAL_LINUX_HEADERS_DIR} modules M=${CMAKE_CURRENT_BINARY_DIR} src=${CMAKE_CURRENT_SOURCE_DIR})

list(APPEND SOURCE_FILES
    driver.c
)

add_subdirectory(generic)
list(APPEND SOURCE_FILES
    generic/read_mem16.c
    generic/read_mem32.c
    generic/read_mem64.c
    generic/read_mem8.c
    generic/write_mem16.c
    generic/write_mem32.c
    generic/write_mem64.c
    generic/write_mem8.c
)

if(PAL_INTEL_64BIT_LINUX_IOCTL OR PAL_AMD_64BIT_LINUX_IOCTL)
    add_subdirectory(x64)
    list(APPEND SOURCE_FILES
        x64/cpuid.c
        x64/in_32.c
        x64/out_32.c
        x64/rdmsr.c
        x64/rdtsc.c
        x64/read_cr0.c
        x64/read_cr2.c
        x64/read_cr3.c
        x64/read_cr4.c
        x64/read_cr8.c
        x64/wrmsr.c
    )
endif()

if(PAL_ARMV8A_AARCH64_LINUX_IOCTL)
    add_subdirectory(armv8a/aarch64)
    list(APPEND SOURCE_FILES
        armv8a/aarch64/ioctl.c
        armv8a/aarch64/sys.c
        armv8a/aarch64/sysl.c
    )
endif()

if(PAL_INTEL_64BIT_LINUX_IOCTL)
    list(APPEND SOURCE_FILES
        x64/intel/ioctl.c
        x64/intel/vmcall.c
        x64/intel/vmcall_kvm.c
        x64/intel/vmcall_xen.c
    )
endif()

string (REPLACE ";" " " SOURCE_FILES_STRING "${SOURCE_FILES}")
string (REPLACE ".c" ".o" OBJECT_FILES "${SOURCE_FILES_STRING}")

set(EXTRA_CFLAGS_LIST
    "-D__kernel__"
    "-I${CMAKE_SOURCE_DIR}/devpal/include"
)
string (REPLACE ";" " " EXTRA_CFLAGS "${EXTRA_CFLAGS_LIST}")

configure_file(${CMAKE_CURRENT_LIST_DIR}/Makefile.in ${CMAKE_CURRENT_LIST_DIR}/Makefile)

add_custom_command(
    OUTPUT ${MODULE_BIN}
    COMMAND ${KBUILD_CMD}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS ${SOURCE_FILES}
    VERBATIM
)

add_custom_target(devpal ALL DEPENDS ${MODULE_BIN})

add_library(devpal_headers INTERFACE) 
target_include_directories(devpal_headers INTERFACE ${CMAKE_CURRENT_LIST_DIR})
