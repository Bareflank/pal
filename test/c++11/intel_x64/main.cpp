#include <stddef.h>

int main(int argc, char * argv[])
{ }

extern "C"
{

void _start(void)
{ main(0, 0);}

int putchar(int c)
{ return 0;}

int __printf_chk(int flag, const char * format, ...)
{ return 0; }

int printf ( const char * format, ... )
{ return 0; }

void __stack_chk_guard(void)
{}

void __stack_chk_fail(void)
{}

void *memset(void *str, int c, size_t n)
{ return 0; }

}
