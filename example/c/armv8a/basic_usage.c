// TODO: Import generated PAL headers here

#include <stdio.h>
#include <pal/aarch64/sctlr_el1.h>

int main(void)
{
    printf("NOTE: Don't forget to load the devpal driver before running the example!\n");

    uint64_t val =  pal_get_sctlr_el1();
    pal_print_sctlr_el1_from_value(printf, val);
    printf("SCTLR_EL1 decimal:: %ld\n", val);
    printf("SCTLR_EL1 hex:: %lx\n", val);
}
