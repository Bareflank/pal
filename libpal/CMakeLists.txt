add_library(libpal INTERFACE)

if(${CMAKE_GENERATOR} MATCHES "Visual Studio")
    add_subdirectory(x64-64bit-none-ms64)
    target_link_libraries(libpal INTERFACE pal_x64_64bit_none_ms64)
else()
    add_subdirectory(x64-64bit-none-systemv)
    target_link_libraries(libpal INTERFACE pal_x64_64bit_none_systemv)
endif()
