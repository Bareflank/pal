if(${CMAKE_GENERATOR} MATCHES "Visual Studio")
    enable_language(ASM_MASM)

    add_library(libpal 
	    cpuid_x64.asm
	    rdmsr_x64.asm
    )
    set_target_properties(libpal PROPERTIES OUTPUT_NAME pal)
    target_include_directories(libpal PUBLIC ${CMAKE_CURRENT_LIST_DIR})
endif()
