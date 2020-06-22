if(${CMAKE_GENERATOR} MATCHES "Visual Studio")
    enable_language(ASM_MASM)

    add_library(libpal cpuid_x64.asm)
    set_target_properties(libpal PROPERTIES OUTPUT_NAME pal)
endif()
