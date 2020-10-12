# Add Sub Project
#
# Adds a sub-project to the build
#
# @param SOURCE_DIR path to the sub-project's top-level source directory,
#       conaining a CMakeLists.txt file
# @param BINARY_DIR path to the sub-project's top-level binary directory
# @param TOOLCHAIN path to a cmake toolchain file
# @param DEPENDS list of CMake targets this subproject depends on
#
#
function(pal_add_subproject NAME)
    set(oneVal SOURCE_DIR BINARY_DIR TOOLCHAIN INSTALL_PREFIX)
    set(multiVal DEPENDS)
    cmake_parse_arguments(ARG "" "${oneVal}" "${multiVal}" ${ARGN})

    if(ARG_SOURCE_DIR)
        set(SOURCE_DIR ${ARG_SOURCE_DIR})
    else()
        message(FATAL_ERROR "pal_add_subproject: SOURCE_DIR not provided")
    endif()

    if(ARG_BINARY_DIR)
        set(BINARY_DIR ${ARG_BINARY_DIR})
    else()
        set(BINARY_DIR ${CMAKE_BINARY_DIR})
    endif()

    if(NOT ARG_INSTALL_PREFIX)
        set(ARG_INSTALL_PREFIX ${BINARY_DIR})
    endif()

    list(APPEND CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=${ARG_INSTALL_PREFIX}
        -DCMAKE_INSTALL_MESSAGE=LAZY
        -DCMAKE_TARGET_MESSAGES=OFF
        -DCMAKE_VERBOSE_MAKEFILE=${CMAKE_VERBOSE_MAKEFILE}
        -DPython3_EXECUTABLE=${Python3_EXECUTABLE}
        -DPYTHONPATH=${PYTHONPATH}
    )

    if(ARG_TOOLCHAIN)
        list(APPEND CMAKE_ARGS -DCMAKE_TOOLCHAIN_FILE=${ARG_TOOLCHAIN})
    endif()

    ExternalProject_Add(
        ${NAME}
        PREFIX          ${BINARY_DIR}/${NAME}/
        STAMP_DIR       ${BINARY_DIR}/${NAME}/stamp
        TMP_DIR         ${BINARY_DIR}/${NAME}/tmp
        BINARY_DIR      ${BINARY_DIR}/${NAME}/build
        SOURCE_DIR      ${SOURCE_DIR}
        CMAKE_ARGS      ${CMAKE_ARGS}
        DEPENDS         ${ARG_DEPENDS}
        UPDATE_COMMAND  ${CMAKE_COMMAND} -E echo "-- checking for updates"
    )

endfunction(pal_add_subproject)
