#include "devpal_abi_armv8a_aarch64.h"

inline struct hvc_operands pal_execute_hvc_inline(struct hvc_operands * kern_ops)
{
    // Note teh strange X0 W0 case here per ARM manual
    uint64_t X0 = (*kern_ops).in.W0;
    uint64_t X1 = (*kern_ops).in.X1;
    uint64_t X2 = (*kern_ops).in.X2;
    uint64_t X3 = (*kern_ops).in.X3;
    uint64_t X4 = (*kern_ops).in.X4;
    uint64_t X5 = (*kern_ops).in.X5;
    uint64_t X6 = (*kern_ops).in.X6;
    uint64_t X7 = (*kern_ops).in.X7;
    uint64_t X8 = (*kern_ops).in.X8;
    uint64_t X9 = (*kern_ops).in.X9;
    uint64_t X10 = (*kern_ops).in.X10;
    uint64_t X11 = (*kern_ops).in.X11;
    uint64_t X12 = (*kern_ops).in.X12;
    uint64_t X13 = (*kern_ops).in.X13;
    uint64_t X14 = (*kern_ops).in.X14;

    __asm__ volatile(
        "ldr w0, %0\n"
        "ldr x1, %1\n"
        "ldr x2, %2\n"
        "ldr x3, %3\n"
        "ldr x4, %4\n"
        "ldr x5, %5\n"
        "ldr x6, %6\n"
        "ldr x7, %7\n"
        "ldr x8, %8\n"
        "ldr x9, %9\n"
        "ldr x10, %10\n"
        "ldr x11, %11\n"
        "ldr x12, %12\n"
        "ldr x13, %13\n"
        "ldr x14, %14\n"
        "hvc #0\n"
        "str x0, %0\n"
        "str x1, %1\n"
        "str x2, %2\n"
        "str x3, %3\n"
        "str x4, %4\n"
        "str x5, %5\n"
        "str x6, %6\n"
        "str x7, %7\n"
        "str x8, %8\n"
        "str x9, %9\n"
        "str x10, %10\n"
        "str x11, %11\n"
        "str x12, %12\n"
        "str x13, %13\n"
        "str x14, %14\n"
        : "+m"(X0),
          "+m"(X1),
          "+m"(X2),
          "+m"(X3),
          "+m"(X4),
          "+m"(X5),
          "+m"(X6),
          "+m"(X7),
          "+m"(X8),
          "+m"(X9),
          "+m"(X10),
          "+m"(X11),
          "+m"(X12),
          "+m"(X13),
          "+m"(X14)
        :
        : "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7",
          "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17");

    (*kern_ops).out.X0 = X0;
    (*kern_ops).out.X1 = X1;
    (*kern_ops).out.X2 = X2;
    (*kern_ops).out.X3 = X3;
    (*kern_ops).out.X4 = X4;
    (*kern_ops).out.X5 = X5;
    (*kern_ops).out.X6 = X6;
    (*kern_ops).out.X7 = X7;
    (*kern_ops).out.X8 = X8;
    (*kern_ops).out.X9 = X9;
    (*kern_ops).out.X10 = X10;
    (*kern_ops).out.X11 = X11;
    (*kern_ops).out.X12 = X12;
    (*kern_ops).out.X13 = X13;
    (*kern_ops).out.X14 = X14;

    return (*kern_ops);
}