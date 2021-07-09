function(pal_run_generator)
    set(options)
    set(oneVal TARGET_NAME INPUT_DIR OUTPUT_DIR EXECUTION_STATE LANGUAGE ACCESS_MECHANISM)
    set(multiVal)
    cmake_parse_arguments(ARG "${options}" "${oneVal}" "${multiVal}" ${ARGN})

    if(NOT ARG_TARGET_NAME)
        message(FATAL_ERROR "Must specify TARGET_NAME argument to pal_run_generator cmake function")
    endif()

    if(NOT ARG_OUTPUT_DIR)
        message(FATAL_ERROR "Must specify OUTPUT_DIR argument to pal_run_generator cmake function")
    endif()

    file(GLOB_RECURSE DEPEND_SRC_FILES CONFIGURE_DEPENDS "pal/*.py" "data/*.yml")
    set(TARGET_OUTPUT_STAMP ${ARG_OUTPUT_DIR}/${ARG_TARGET_NAME}_output.stamp)

    set(GENERATE_CMD ${Python3_EXECUTABLE} ${CMAKE_CURRENT_LIST_DIR}/pal.py)

    if(ARG_INPUT_DIR)
        list(APPEND GENERATE_CMD -i ${ARG_INPUT_DIR})
    endif()

    if(ARG_OUTPUT_DIR)
        list(APPEND GENERATE_CMD -o ${ARG_OUTPUT_DIR})
    endif()

    if(ARG_EXECUTION_STATE)
        list(APPEND GENERATE_CMD --execution_state=${ARG_EXECUTION_STATE})
    endif()

    if(ARG_LANGUAGE)
        list(APPEND GENERATE_CMD --language=${ARG_LANGUAGE})
    endif()

    if(ARG_ACCESS_MECHANISM)
        list(APPEND GENERATE_CMD --access_mechanism=${ARG_ACCESS_MECHANISM})
    endif()

    if(NOT PAL_ENABLE_PRINTERS)
        list(APPEND GENERATE_CMD --enable_printers=false --print_mechanism=none)
    endif()

    if(${CMAKE_HOST_SYSTEM_NAME} STREQUAL "Windows")
        list(APPEND GENERATE_CMD --file_format=windows)
    endif()

    if(PAL_QUIET_CMAKE)
        list(APPEND GENERATE_CMD --log_level="error")
    endif()

    add_custom_command(
        COMMAND ${GENERATE_CMD}
        COMMAND cmake -E touch ${TARGET_OUTPUT_STAMP}
        OUTPUT ${TARGET_OUTPUT_STAMP}
        DEPENDS ${DEPEND_SRC_FILES}
        COMMENT "Generating ${ARG_TARGET_NAME} outputs"
    )

    add_custom_target(run_generator_${ARG_TARGET_NAME} ALL DEPENDS ${TARGET_OUTPUT_STAMP})

    add_library(${ARG_TARGET_NAME} INTERFACE)
    target_include_directories(${ARG_TARGET_NAME} INTERFACE ${ARG_OUTPUT_DIR}/include)
    add_dependencies(${ARG_TARGET_NAME} run_generator_${ARG_TARGET_NAME})
endfunction(pal_run_generator)
