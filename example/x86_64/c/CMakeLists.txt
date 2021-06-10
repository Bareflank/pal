add_executable(basic_usage basic_usage.c)
target_link_libraries(basic_usage pal libpal)

add_executable(hypercall hypercall.c)
target_link_libraries(hypercall pal libpal)
