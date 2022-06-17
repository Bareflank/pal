if(${CMAKE_HOST_SYSTEM_PROCESSOR} STREQUAL x86_64)
    add_subdirectory(intel)
endif()

if(${CMAKE_HOST_SYSTEM_PROCESSOR} STREQUAL aarch64)
    add_subdirectory(armv8a)
endif()
