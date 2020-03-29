# Ninja is the only supported CMake generator on Windows
if(${CMAKE_HOST_SYSTEM_NAME} STREQUAL Windows)
    message(STATUS "Using CMake Generator: Ninja")
    set(CMAKE_GENERATOR "Ninja" CACHE INTERNAL "")
endif()
