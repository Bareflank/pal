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

}
