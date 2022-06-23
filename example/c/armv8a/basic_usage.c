// TODO: Import generated PAL headers here

#include <stdio.h>
#include <pal/aarch64/sctlr_el1.h>

int main(void)
{
    printf("NOTE: Don't forget to load the devpal driver before running the example!\n");

    uint64_t val =  pal_get_sctlr_el1();
    pal_print_sctlr_el1_from_value(printf, val);
    printf("SCTLR_EL1 hex: %lx\n", val);

    // Change a specific bit in sctlr_el1
    /*
    uint64_t tmp = 0x8;
    val ^= tmp;
    printf("After xor: %lx\n", val);
    pal_set_sctlr_el1(val);

    val = pal_get_sctlr_el1();
    printf("SCTLR_EL1 hex: %lx\n", val);
    pal_print_sctlr_el1_from_value(printf, val);
    */
}
