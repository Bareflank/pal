inline uint64_t pal_get_actlr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_actlr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_actlr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_afsr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_afsr0_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c5_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_afsr0_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c5_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_afsr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_afsr1_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c5_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_afsr1_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c5_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_aidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_1_c0_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amair_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amair_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amair_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c10_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcfgr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcgcr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcntenclr0_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c2_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcntenclr1_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcntenset0_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c2_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcntenset1_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amcr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr00_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr010_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr011_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr012_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr013_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr014_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr015_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr01_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr02_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr03_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr04_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr05_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr06_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr07_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c4_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr08_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr09_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c5_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr10_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr110_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr111_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr112_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr113_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr114_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr115_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr11_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr12_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr13_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr14_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr15_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr16_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr17_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr18_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevcntr19_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c13_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper00_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper010_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper011_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper012_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper013_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper014_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper015_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper01_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper02_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper03_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper04_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper05_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper06_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper07_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c6_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper08_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper09_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c7_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper10_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper110_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper111_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper112_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper113_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper114_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper115_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper11_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper12_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper13_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper14_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper15_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper16_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper17_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c14_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper18_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amevtyper19_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c15_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_amuserenr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c2_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apdakeyhi_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apdakeylo_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apdbkeyhi_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c2_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apdbkeylo_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apgakeyhi_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apgakeylo_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apiakeyhi_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apiakeylo_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apibkeyhi_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c1_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_apibkeylo_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c1_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ccsidr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_1_c0_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ccsidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_1_c0_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_clidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_1_c0_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntfrq_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthctl_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthp_ctl_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthp_cval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthp_tval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthps_ctl_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c5_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthps_cval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c5_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthps_tval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthv_ctl_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthv_cval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c3_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthv_tval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthvs_ctl_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthvs_cval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c4_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cnthvs_tval_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntkctl_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c14_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntp_ctl_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntp_cval_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntp_tval_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntpct_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntps_ctl_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_7_c14_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntps_cval_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_7_c14_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntps_tval_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_7_c14_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntv_ctl_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntv_cval_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c3_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntv_tval_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntvct_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cntvoff_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c14_c0_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_contextidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c13_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_contextidr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c13_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cpacr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cptr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c1_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_cptr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c1_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_csselr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_2_c0_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ctr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c0_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_currentel_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dacr32_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c3_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_daif_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgauthstatus_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c7_c14_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c0_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr10_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c10_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr11_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c11_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr12_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr13_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c13_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr14_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c14_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr15_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c15_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c1_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c2_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c3_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr4_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c4_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr5_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c5_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr6_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c6_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr7_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c7_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr8_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c8_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbcr9_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c9_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c0_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr10_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c10_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr11_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c11_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr12_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c12_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr13_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c13_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr14_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c14_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr15_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c15_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c1_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c2_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c3_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr4_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c4_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr5_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c5_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr6_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c6_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr7_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c7_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr8_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c8_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgbvr9_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c9_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgclaimclr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c7_c9_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgclaimset_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c7_c8_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgdtr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_3_c0_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgdtrrx_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_3_c0_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgprcr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c1_c4_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgvcr32_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_4_c0_c7_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr10_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c10_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr11_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c11_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr12_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr13_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c13_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr14_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c14_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr15_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c15_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c1_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c2_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c3_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr4_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c4_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr5_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c5_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr6_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c6_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr7_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c7_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr8_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c8_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwcr9_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c9_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c0_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr10_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c10_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr11_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c11_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr12_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c12_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr13_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c13_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr14_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c14_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr15_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c15_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c1_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c2_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c3_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr4_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c4_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr5_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c5_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr6_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c6_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr7_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c7_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr8_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c8_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dbgwvr9_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c9_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dczid_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c0_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_disr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dit_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c2_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dlr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c5_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_dspsr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_elr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_elr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_elr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c4_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erridr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_errselr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxaddr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxctlr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxfr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxmisc0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxmisc1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c5_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxmisc2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c5_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxmisc3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c5_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxpfgcdn_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxpfgctl_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxpfgf_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_erxstatus_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c4_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_esr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c5_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_esr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c5_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_esr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c5_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_far_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c6_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_far_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c6_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_far_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c6_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_fpcr_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_fpexc32_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c5_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_fpsr_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_gcr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c0_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_hacr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c1_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_hcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_hpfar_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c6_c0_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_hstr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c1_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap0r0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap0r1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap0r2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap0r3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap1r0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c9_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap1r1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c9_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap1r2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c9_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ap1r3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c9_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_bpr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_bpr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ctlr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_ctlr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c12_c12_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_hppir0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_hppir1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_iar0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c8_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_iar1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_igrpen0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_igrpen1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_igrpen1_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c12_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_pmr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c6_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_rpr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c11_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_sre_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_sre_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c9_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_icc_sre_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c12_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap0r0_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c8_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap0r1_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c8_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap0r2_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c8_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap0r3_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c8_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap1r0_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c9_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap1r1_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c9_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap1r2_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c9_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_ap1r3_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c9_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_eisr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c11_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_elrsr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c11_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_hcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c11_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr0_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr10_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr11_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr12_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr13_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr14_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr15_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr1_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr2_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr3_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr4_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr5_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr6_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr7_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr8_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_lr9_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c13_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_misr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c11_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_vmcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c11_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ich_vtr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c11_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64afr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c5_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64afr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c5_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64dfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64dfr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c5_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64isar0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c6_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64isar1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c6_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64mmfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c7_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64mmfr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c7_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64mmfr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c7_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64pfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64pfr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_aa64zfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c4_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_afr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_dfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar4_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar5_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_isar6_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_mmfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_mmfr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_mmfr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_mmfr3_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_mmfr4_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c2_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_pfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_pfr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_id_pfr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c3_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ifsr32_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c5_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_isr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_lorc_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c4_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_lorea_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_lorid_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c4_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_lorn_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c4_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_lorsa_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mair_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mair_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mair_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c10_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mdccint_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mdccsr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_3_c0_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mdcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mdcr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mdrar_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c1_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mdscr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c2_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_midr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpam0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c5_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpam1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpam2_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpam3_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c10_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamhcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c10_c4_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm0_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm1_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm2_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm3_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm4_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm5_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm6_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpm7_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c6_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpamvpmv_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c10_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mpidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c0_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mvfr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mvfr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_mvfr2_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c3_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_nzcv_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_osdlr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c1_c3_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_osdtrrx_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_osdtrtx_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c3_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_oseccr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c0_c6_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_oslsr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s2_0_c1_c1_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pan_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c2_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_par_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c7_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmbidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c10_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmblimitr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c10_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmbptr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c10_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmbsr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c10_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmccfiltr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmccntr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c13_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmceid0_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmceid1_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmcntenclr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmcntenset_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmcr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr0_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr10_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr11_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr12_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr13_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr14_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr15_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr16_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr17_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr18_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr19_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr1_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr20_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr21_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr22_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr23_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c10_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr24_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr25_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr26_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr27_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr28_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr29_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr2_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr30_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c11_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr3_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr4_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr5_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr6_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr7_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c8_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr8_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevcntr9_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c9_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper0_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper10_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper11_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper12_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper13_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper14_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper15_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper16_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper17_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper18_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper19_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper1_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper20_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper21_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper22_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper23_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c14_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper24_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper25_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper26_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper27_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper28_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper29_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper2_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper30_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c15_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper3_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper4_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper5_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper6_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper7_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c12_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper8_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmevtyper9_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c14_c13_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmintenclr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c14_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmintenset_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c14_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmmir_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c14_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmovsclr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmovsset_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c14_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmscr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmscr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c9_c9_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmselr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c12_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmsevfr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmsfcr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmsicr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmsidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmsirr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmslatfr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c9_c9_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmuserenr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c14_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmxevcntr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c13_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_pmxevtyper_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c9_c13_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_revidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c0_c0_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rgsr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c0_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rmr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rmr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rmr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c12_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rndr_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c2_c4_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rndrrs_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c2_c4_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rvbar_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rvbar_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_rvbar_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c12_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_scr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sctlr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sctlr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sctlr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_scxtnum_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_scxtnum_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c13_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_scxtnum_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c13_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_scxtnum_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c13_c0_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sder32_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sder32_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sp_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sp_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_sp_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c4_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsel_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_abt_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c3_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c4_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_fiq_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c3_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_irq_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c3_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_spsr_und_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c4_c3_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ssbs_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c2_6"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tco_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c4_c2_7"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tcr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tcr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c2_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tfsr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c6_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tfsr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c6_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tfsr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c6_c5_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tfsre0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c6_c6_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tpidr_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tpidr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c13_c0_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tpidr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c13_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tpidr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c13_c0_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_tpidrro_el0_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_3_c13_c0_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_trfcr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_trfcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c2_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ttbr0_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ttbr0_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ttbr0_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c2_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ttbr1_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c2_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_ttbr1_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c0_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_uao_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c4_c2_4"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vbar_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c12_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vbar_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vbar_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c12_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vdisr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c12_c1_1"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vmpidr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c0_c0_5"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vncr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vpidr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c0_c0_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vsesr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c5_c2_3"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vstcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c6_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vsttbr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c6_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vtcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c1_2"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_vttbr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c2_c1_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_zcr_el1_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_0_c1_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_zcr_el2_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_4_c1_c2_0"
                     : "=r"(value));
    return value;
}
inline uint64_t pal_get_zcr_el3_inline(void)
{
    uint64_t value = 0;
    __asm__ volatile("mrs %0, s3_6_c1_c2_0"
                     : "=r"(value));
    return value;
}