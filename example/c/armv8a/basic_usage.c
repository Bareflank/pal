// TODO: Import generated PAL headers here

#include <stdio.h>
#include <pal/aarch64/sctlr_el1.h>
#include <pal/aarch64/esr_el1.h>
#include <pal/aarch64/elr_el1.h>
#include <pal/aarch64/spsr_el1.h>
#include <pal/aarch64/ttbr0_el1.h>
#include <pal/aarch64/vbar_el1.h>
#include <pal/aarch64/dbgauthstatus_el1.h>
#include <pal/aarch64/dbgbcr0_el1.h>

#include "pal/a64/smc.h"
#include "pal/a64/hvc.h"

int test_func(void) {
    printf("Hello World\n");
    return 0;
}

int main(void)
{
    printf("NOTE: Don't forget to load the devpal driver before running the example!\n");

    uint64_t val = pal_get_esr_el1();
    pal_print_esr_el1_from_value(printf, val);
    printf("esr_el1 hex: %lx\n", val);

    val =  pal_get_sctlr_el1();
    pal_print_sctlr_el1_from_value(printf, val);
    printf("SCTLR_EL1 hex: %lx\n", val);

    val = pal_get_elr_el1();
    pal_print_elr_el1_from_value(printf, val);

    val = pal_get_spsr_el1();
    pal_print_spsr_el1_fieldset_2_from_value(printf, val);

    val = pal_get_ttbr0_el1();
    pal_print_ttbr0_el1_from_value(printf, val);

    val = pal_get_vbar_el1();
    pal_print_vbar_el1_from_value(printf, val);

    val = pal_get_dbgauthstatus_el1();
    pal_print_dbgauthstatus_el1_from_value(printf, val);

    val = pal_get_dbgbcr0_el1();
    pal_print_dbgbcr0_el1_from_value(printf, val);

    // Set functions from here on DANGER ZONE. Real danger of crushing the system

    // pal_set_elr_el1(test_func);
    

    // Change contents of dbgbcr0_el1 register
    val = pal_get_dbgbcr0_el1();
    pal_print_dbgbcr0_el1_from_value(printf, val);

    uint64_t tmp = 0x6;
    //printf("After xor: %lx\n", val);
    pal_set_dbgbcr0_el1(tmp);

    val = pal_get_dbgbcr0_el1();
    printf("dbgbcr0_el1 hex: %lx\n", val);
    pal_print_dbgbcr0_el1_from_value(printf, val);

    val = pal_get_elr_el1();
    pal_print_elr_el1_from_value(printf, val);

    printf("Here func addr: %p\n", test_func);
    pal_set_elr_el1((uint64_t)test_func);

    val = pal_get_elr_el1();
    printf("elr hex: %lx\n", val);
    pal_print_elr_el1_from_value(printf, val);

    printf("=====================================\n");
    struct hvc_operands args = {0};
    args.in.W0 = 0x84000000;
    //args.in.X1 = 0xdeadbeef;
    // args.in.X2 = 0xdeadbeef;
    // args.in.X3 = 0xdeadbeef;
    args = pal_execute_hvc(&args);

    printf("Here X0: %lx\n", args.out.X0);
    printf("Here X1: %lx\n", args.out.X1);
    printf("Here X2: %lx\n", args.out.X2);
    printf("Here X3: %lx\n", args.out.X3);
    printf("Here X4: %lx\n", args.out.X4);
    printf("Here X5: %lx\n", args.out.X5);
    printf("Here X6: %lx\n", args.out.X6);
    printf("Here X7: %lx\n", args.out.X7);
    printf("Here X8: %lx\n", args.out.X8);
    printf("Here X9: %lx\n", args.out.X9);
    printf("Here X10: %lx\n", args.out.X10);
    printf("Here X11: %lx\n", args.out.X11);
    printf("Here X12: %lx\n", args.out.X12);
    printf("Here X13: %lx\n", args.out.X13);
    printf("Here X14: %lx\n", args.out.X14);
}
