inline void pal_set_actlr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_actlr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_actlr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_afsr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_afsr0_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c5_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_afsr0_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c5_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_afsr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_afsr1_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c5_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_afsr1_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c5_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_aidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_1_c0_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amair_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amair_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amair_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c10_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amcfgr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amcgcr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amcntenclr0_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c2_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amcntenclr1_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amcntenset0_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c2_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amcntenset1_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amcr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr00_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr010_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr011_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr012_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr013_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr014_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr015_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr01_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr02_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr03_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr04_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr05_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr06_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr07_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c4_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr08_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr09_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c5_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr10_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr110_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr111_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr112_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr113_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr114_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr115_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr11_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr12_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr13_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr14_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr15_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr16_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr17_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr18_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevcntr19_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c13_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper00_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper010_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper011_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper012_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper013_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper014_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper015_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper01_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper02_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper03_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper04_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper05_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper06_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper07_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c6_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper08_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper09_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c7_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper10_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper110_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper111_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper112_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper113_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper114_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper115_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper11_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper12_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_2, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper13_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_3, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper14_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_4, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper15_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_5, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper16_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_6, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper17_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c14_7, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper18_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_0, %0"
			:
			: "r"(value));
}
inline void pal_set_amevtyper19_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c15_1, %0"
			:
			: "r"(value));
}
inline void pal_set_amuserenr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c2_3, %0"
			:
			: "r"(value));
}
inline void pal_set_apdakeyhi_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_apdakeylo_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_apdbkeyhi_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c2_3, %0"
			:
			: "r"(value));
}
inline void pal_set_apdbkeylo_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_apgakeyhi_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_apgakeylo_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_apiakeyhi_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_apiakeylo_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_apibkeyhi_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c1_3, %0"
			:
			: "r"(value));
}
inline void pal_set_apibkeylo_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c1_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ccsidr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_1_c0_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ccsidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_1_c0_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_clidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_1_c0_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cntfrq_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthctl_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthp_ctl_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthp_cval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthp_tval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthps_ctl_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c5_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthps_cval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c5_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthps_tval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthv_ctl_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthv_cval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c3_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthv_tval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthvs_ctl_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthvs_cval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c4_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cnthvs_tval_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cntkctl_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c14_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cntp_ctl_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cntp_cval_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cntp_tval_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cntpct_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cntps_ctl_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_7_c14_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cntps_cval_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_7_c14_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cntps_tval_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_7_c14_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cntv_ctl_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cntv_cval_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c3_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cntv_tval_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_cntvct_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cntvoff_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c14_c0_3, %0"
			:
			: "r"(value));
}
inline void pal_set_contextidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c13_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_contextidr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c13_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_cpacr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cptr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c1_2, %0"
			:
			: "r"(value));
}
inline void pal_set_cptr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c1_2, %0"
			:
			: "r"(value));
}
inline void pal_set_csselr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_2_c0_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ctr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c0_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_currentel_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_dacr32_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c3_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_daif_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgauthstatus_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c7_c14_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c0_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr10_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c10_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr11_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c11_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr12_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr13_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c13_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr14_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c14_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr15_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c15_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c1_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c2_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c3_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr4_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c4_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr5_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c5_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr6_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c6_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr7_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c7_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr8_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c8_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbcr9_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c9_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c0_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr10_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c10_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr11_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c11_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr12_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr13_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c13_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr14_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c14_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr15_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c15_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c1_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c2_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c3_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr4_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c4_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr5_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c5_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr6_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c6_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr7_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c7_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr8_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c8_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgbvr9_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c9_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgclaimclr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c7_c9_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgclaimset_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c7_c8_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgdtr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s2_3_c0_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgdtrrx_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s2_3_c0_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgprcr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c1_c4_4, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgvcr32_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s2_4_c0_c7_0, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr10_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c10_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr11_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c11_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr12_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr13_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c13_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr14_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c14_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr15_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c15_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c1_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c2_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c3_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr4_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c4_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr5_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c5_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr6_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c6_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr7_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c7_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr8_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c8_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwcr9_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c9_7, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c0_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr10_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c10_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr11_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c11_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr12_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c12_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr13_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c13_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr14_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c14_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr15_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c15_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c1_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c2_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c3_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr4_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c4_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr5_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c5_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr6_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c6_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr7_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c7_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr8_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c8_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dbgwvr9_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c9_6, %0"
			:
			: "r"(value));
}
inline void pal_set_dczid_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c0_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_disr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_dit_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c2_5, %0"
			:
			: "r"(value));
}
inline void pal_set_dlr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c5_1, %0"
			:
			: "r"(value));
}
inline void pal_set_dspsr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_elr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_elr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_elr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c4_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_erridr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_errselr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_erxaddr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_3, %0"
			:
			: "r"(value));
}
inline void pal_set_erxctlr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_erxfr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_erxmisc0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_erxmisc1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c5_1, %0"
			:
			: "r"(value));
}
inline void pal_set_erxmisc2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c5_2, %0"
			:
			: "r"(value));
}
inline void pal_set_erxmisc3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c5_3, %0"
			:
			: "r"(value));
}
inline void pal_set_erxpfgcdn_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_6, %0"
			:
			: "r"(value));
}
inline void pal_set_erxpfgctl_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_5, %0"
			:
			: "r"(value));
}
inline void pal_set_erxpfgf_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_4, %0"
			:
			: "r"(value));
}
inline void pal_set_erxstatus_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c4_2, %0"
			:
			: "r"(value));
}
inline void pal_set_esr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c5_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_esr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c5_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_esr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c5_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_far_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c6_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_far_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c6_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_far_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c6_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_fpcr_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_fpexc32_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c5_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_fpsr_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_gcr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c0_6, %0"
			:
			: "r"(value));
}
inline void pal_set_hacr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c1_7, %0"
			:
			: "r"(value));
}
inline void pal_set_hcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_hpfar_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c6_c0_4, %0"
			:
			: "r"(value));
}
inline void pal_set_hstr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c1_3, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap0r0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_4, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap0r1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_5, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap0r2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_6, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap0r3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_7, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap1r0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c9_0, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap1r1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c9_1, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap1r2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c9_2, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ap1r3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c9_3, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_asgi1r_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c11_6, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_bpr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_3, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_bpr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_3, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ctlr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_ctlr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c12_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_dir_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c11_1, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_eoir0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_1, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_eoir1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_1, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_hppir0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_2, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_hppir1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_2, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_iar0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c8_0, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_iar1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_0, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_igrpen0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_6, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_igrpen1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_igrpen1_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c12_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_pmr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c6_0, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_rpr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c11_3, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_sgi0r_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c11_7, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_sgi1r_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c11_5, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_sre_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_sre_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c9_5, %0"
			:
			: "r"(value));
}
inline void pal_set_icc_sre_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c12_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap0r0_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c8_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap0r1_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c8_1, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap0r2_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c8_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap0r3_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c8_3, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap1r0_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c9_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap1r1_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c9_1, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap1r2_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c9_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_ap1r3_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c9_3, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_eisr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c11_3, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_elrsr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c11_5, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_hcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c11_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr0_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr10_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr11_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_3, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr12_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_4, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr13_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_5, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr14_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_6, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr15_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_7, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr1_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_1, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr2_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr3_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_3, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr4_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr5_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr6_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_6, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr7_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr8_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_lr9_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c13_1, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_misr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c11_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_vmcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c11_7, %0"
			:
			: "r"(value));
}
inline void pal_set_ich_vtr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c11_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64afr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c5_4, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64afr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c5_5, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64dfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64dfr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c5_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64isar0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c6_0, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64isar1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c6_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64mmfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c7_0, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64mmfr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c7_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64mmfr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c7_2, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64pfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64pfr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_aa64zfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c4_4, %0"
			:
			: "r"(value));
}
inline void pal_set_id_afr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_3, %0"
			:
			: "r"(value));
}
inline void pal_set_id_dfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_2, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_3, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar4_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_4, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar5_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_5, %0"
			:
			: "r"(value));
}
inline void pal_set_id_isar6_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_7, %0"
			:
			: "r"(value));
}
inline void pal_set_id_mmfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_4, %0"
			:
			: "r"(value));
}
inline void pal_set_id_mmfr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_5, %0"
			:
			: "r"(value));
}
inline void pal_set_id_mmfr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_6, %0"
			:
			: "r"(value));
}
inline void pal_set_id_mmfr3_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_7, %0"
			:
			: "r"(value));
}
inline void pal_set_id_mmfr4_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c2_6, %0"
			:
			: "r"(value));
}
inline void pal_set_id_pfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_id_pfr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_id_pfr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c3_4, %0"
			:
			: "r"(value));
}
inline void pal_set_ifsr32_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c5_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_isr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_lorc_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c4_3, %0"
			:
			: "r"(value));
}
inline void pal_set_lorea_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_lorid_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c4_7, %0"
			:
			: "r"(value));
}
inline void pal_set_lorn_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c4_2, %0"
			:
			: "r"(value));
}
inline void pal_set_lorsa_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mair_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mair_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mair_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c10_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mdccint_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mdccsr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s2_3_c0_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mdcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_mdcr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_mdrar_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c1_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mdscr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c2_2, %0"
			:
			: "r"(value));
}
inline void pal_set_midr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mpam0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c5_1, %0"
			:
			: "r"(value));
}
inline void pal_set_mpam1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mpam2_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mpam3_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c10_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamhcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c10_c4_4, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm0_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm1_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_1, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm2_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_2, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm3_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_3, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm4_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_4, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm5_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_5, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm6_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_6, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpm7_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c6_7, %0"
			:
			: "r"(value));
}
inline void pal_set_mpamvpmv_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c10_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_mpidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c0_5, %0"
			:
			: "r"(value));
}
inline void pal_set_mvfr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_mvfr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_mvfr2_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c3_2, %0"
			:
			: "r"(value));
}
inline void pal_set_nzcv_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_osdlr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c1_c3_4, %0"
			:
			: "r"(value));
}
inline void pal_set_osdtrrx_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_osdtrtx_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c3_2, %0"
			:
			: "r"(value));
}
inline void pal_set_oseccr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c0_c6_2, %0"
			:
			: "r"(value));
}
inline void pal_set_oslar_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c1_c0_4, %0"
			:
			: "r"(value));
}
inline void pal_set_oslsr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s2_0_c1_c1_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pan_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c2_3, %0"
			:
			: "r"(value));
}
inline void pal_set_par_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c7_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmbidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c10_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmblimitr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c10_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmbptr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c10_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmbsr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c10_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmccfiltr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmccntr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c13_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmceid0_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmceid1_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmcntenclr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmcntenset_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmcr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr0_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr10_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr11_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr12_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr13_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr14_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr15_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr16_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr17_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr18_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr19_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr1_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr20_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr21_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr22_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr23_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c10_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr24_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr25_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr26_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr27_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr28_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr29_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr2_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr30_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c11_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr3_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr4_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr5_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr6_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr7_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c8_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr8_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevcntr9_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c9_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper0_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper10_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper11_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper12_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper13_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper14_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper15_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper16_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper17_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper18_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper19_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper1_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper20_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper21_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper22_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper23_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c14_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper24_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper25_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper26_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper27_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper28_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper29_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper2_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper30_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c15_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper3_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper4_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper5_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper6_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper7_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c12_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper8_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmevtyper9_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c14_c13_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmintenclr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c14_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmintenset_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c14_1, %0"
			:
			: "r"(value));
}
inline void pal_set_pmmir_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c14_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmovsclr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmovsset_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c14_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmscr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmscr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c9_c9_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmselr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmsevfr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_5, %0"
			:
			: "r"(value));
}
inline void pal_set_pmsfcr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmsicr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmsidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_7, %0"
			:
			: "r"(value));
}
inline void pal_set_pmsirr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_3, %0"
			:
			: "r"(value));
}
inline void pal_set_pmslatfr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c9_c9_6, %0"
			:
			: "r"(value));
}
inline void pal_set_pmswinc_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c12_4, %0"
			:
			: "r"(value));
}
inline void pal_set_pmuserenr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c14_0, %0"
			:
			: "r"(value));
}
inline void pal_set_pmxevcntr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c13_2, %0"
			:
			: "r"(value));
}
inline void pal_set_pmxevtyper_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c9_c13_1, %0"
			:
			: "r"(value));
}
inline void pal_set_revidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c0_c0_6, %0"
			:
			: "r"(value));
}
inline void pal_set_rgsr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c0_5, %0"
			:
			: "r"(value));
}
inline void pal_set_rmr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_rmr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_rmr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c12_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_rndr_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c2_c4_0, %0"
			:
			: "r"(value));
}
inline void pal_set_rndrrs_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c2_c4_1, %0"
			:
			: "r"(value));
}
inline void pal_set_rvbar_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_rvbar_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_rvbar_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c12_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_scr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_sctlr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_sctlr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_sctlr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_scxtnum_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_scxtnum_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c13_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_scxtnum_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c13_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_scxtnum_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c13_c0_7, %0"
			:
			: "r"(value));
}
inline void pal_set_sder32_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_sder32_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_sp_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_sp_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_sp_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c4_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_spsel_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_abt_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c3_1, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c4_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_fiq_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c3_3, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_irq_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c3_0, %0"
			:
			: "r"(value));
}
inline void pal_set_spsr_und_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c4_c3_2, %0"
			:
			: "r"(value));
}
inline void pal_set_ssbs_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c2_6, %0"
			:
			: "r"(value));
}
inline void pal_set_tco_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c4_c2_7, %0"
			:
			: "r"(value));
}
inline void pal_set_tcr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_tcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_tcr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c2_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_tfsr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c6_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_tfsr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c6_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_tfsr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c6_c5_0, %0"
			:
			: "r"(value));
}
inline void pal_set_tfsre0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c6_c6_1, %0"
			:
			: "r"(value));
}
inline void pal_set_tpidr_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_tpidr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c13_c0_4, %0"
			:
			: "r"(value));
}
inline void pal_set_tpidr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c13_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_tpidr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c13_c0_2, %0"
			:
			: "r"(value));
}
inline void pal_set_tpidrro_el0_inline(uint64_t value)
{
	__asm__ volatile("msr s3_3_c13_c0_3, %0"
			:
			: "r"(value));
}
inline void pal_set_trfcr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_trfcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c2_1, %0"
			:
			: "r"(value));
}
inline void pal_set_ttbr0_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ttbr0_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ttbr0_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c2_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_ttbr1_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c2_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_ttbr1_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c0_1, %0"
			:
			: "r"(value));
}
inline void pal_set_uao_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c4_c2_4, %0"
			:
			: "r"(value));
}
inline void pal_set_vbar_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c12_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_vbar_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_vbar_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c12_c0_0, %0"
			:
			: "r"(value));
}
inline void pal_set_vdisr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c12_c1_1, %0"
			:
			: "r"(value));
}
inline void pal_set_vncr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_vsesr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c5_c2_3, %0"
			:
			: "r"(value));
}
inline void pal_set_vstcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c6_2, %0"
			:
			: "r"(value));
}
inline void pal_set_vsttbr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c6_0, %0"
			:
			: "r"(value));
}
inline void pal_set_vtcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c1_2, %0"
			:
			: "r"(value));
}
inline void pal_set_vttbr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c2_c1_0, %0"
			:
			: "r"(value));
}
inline void pal_set_zcr_el1_inline(uint64_t value)
{
	__asm__ volatile("msr s3_0_c1_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_zcr_el2_inline(uint64_t value)
{
	__asm__ volatile("msr s3_4_c1_c2_0, %0"
			:
			: "r"(value));
}
inline void pal_set_zcr_el3_inline(uint64_t value)
{
	__asm__ volatile("msr s3_6_c1_c2_0, %0"
			:
			: "r"(value));
}
