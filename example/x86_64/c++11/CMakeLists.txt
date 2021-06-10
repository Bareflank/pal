add_executable(basic_usage basic_usage.cpp)
target_link_libraries(basic_usage pal libpal)

add_executable(hypercall hypercall.cpp)
target_link_libraries(hypercall pal libpal)
