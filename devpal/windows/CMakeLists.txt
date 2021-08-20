message(STATUS "Building Windows Driver")

set(VS_SOLUTION_FILE ${CMAKE_CURRENT_LIST_DIR}/visual_studio/devpal.sln)
set(VS_PROJECT_FILE ${CMAKE_CURRENT_LIST_DIR}/visual_studio/devpal.vcxproj)
set(VS_CONFIGURATION "Release")
set(VS_PLATFORM "x64")
set(VS_OUTPUT_DIR ${CMAKE_CURRENT_LIST_DIR}/visual_studio/${VS_PLATFORM}/${VS_CONFIGURATION})
set(DRIVER_BIN ${VS_OUTPUT_DIR}/devpal/devpal.sys)
set(MSBUILD_CMD msbuild ${VS_SOLUTION_FILE} /p:Configuration=${VS_CONFIGURATION} /p:Platform=${VS_PLATFORM})

# configure_file(${CMAKE_CURRENT_LIST_DIR}/visual_studio/devpal.vcxproj.in ${CMAKE_CURRENT_LIST_DIR}/visual_studio/devpal.vcxproj)

add_custom_command(
    OUTPUT ${DRIVER_BIN}
    COMMAND ${MSBUILD_CMD}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS ${VS_SOLUTION_FILE} ${VS_PROJECT_FILE}
    VERBATIM
)

add_custom_target(devpal ALL DEPENDS ${DRIVER_BIN})