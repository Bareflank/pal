function(pal_find_python_module module)
    execute_process(
        COMMAND ${Python3_EXECUTABLE} -c "import ${module}"
        RESULT_VARIABLE PY_EXIT_STATUS
        OUTPUT_QUIET
        ERROR_QUIET
    )
    if (NOT ${PY_EXIT_STATUS} EQUAL 0)
        message(
            SEND_ERROR
            "The ${Yellow} ${module} ${ColorReset} Python3 package is ${BoldRed} not found! ${ColorReset}"
        )
	set(PYTHON_MODULES_MISSING TRUE PARENT_SCOPE)
    endif()
endfunction(pal_find_python_module)
