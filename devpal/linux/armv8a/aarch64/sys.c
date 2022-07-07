#include <linux/uaccess.h>
#include "devpal_abi_armv8a_aarch64.h"
#include "pal/aarch64/sys_inline.h"

long handle_devpal_ioctl_sys(struct sys_operands * user_ops)
{
    uint8_t op0 = 0;
    uint8_t op1 = 0;
    uint8_t crn = 0;
    uint8_t crm = 0;
    uint8_t op2 = 0;
    uint64_t value = 0;
    uint32_t switch_vector = 0;
    struct sys_operands kern_ops = {0};

    if (copy_from_user(&kern_ops, user_ops, sizeof(struct sys_operands)))
        return -1;

    op0 = kern_ops.in.op0;
    op1 = kern_ops.in.op1;
    crn = kern_ops.in.crn;
    crm = kern_ops.in.crm;
    op2 = kern_ops.in.op2;
    value = kern_ops.in.value;

    // The switch vector the sys/sysl instruction encodin, the last 5 bits are not used for our purposes
    switch_vector |= (op0 & 0x3) << 19;
    switch_vector |= (op1 & 0x7) << 16;
    switch_vector |= (crn & 0xF) << 12;
    switch_vector |= (crm & 0xF) << 8;
    switch_vector |= (op2 & 0x7) << 5;

    //printk("Vector: val= %x", switch_vector);

    switch (switch_vector)
    {
    case 0x181020:
        pal_set_actlr_el1_inline(value);
        break;
    case 0x1c1020:
        pal_set_actlr_el2_inline(value);
        break;
    case 0x1e1020:
        pal_set_actlr_el3_inline(value);
        break;
    case 0x185100:
        pal_set_afsr0_el1_inline(value);
        break;
    case 0x1c5100:
        pal_set_afsr0_el2_inline(value);
        break;
    case 0x1e5100:
        pal_set_afsr0_el3_inline(value);
        break;
    case 0x185120:
        pal_set_afsr1_el1_inline(value);
        break;
    case 0x1c5120:
        pal_set_afsr1_el2_inline(value);
        break;
    case 0x1e5120:
        pal_set_afsr1_el3_inline(value);
        break;
    case 0x1900e0:
        pal_set_aidr_el1_inline(value);
        break;
    case 0x18a300:
        pal_set_amair_el1_inline(value);
        break;
    case 0x1ca300:
        pal_set_amair_el2_inline(value);
        break;
    case 0x1ea300:
        pal_set_amair_el3_inline(value);
        break;
    case 0x1bd220:
        pal_set_amcfgr_el0_inline(value);
        break;
    case 0x1bd240:
        pal_set_amcgcr_el0_inline(value);
        break;
    case 0x1bd280:
        pal_set_amcntenclr0_el0_inline(value);
        break;
    case 0x1bd300:
        pal_set_amcntenclr1_el0_inline(value);
        break;
    case 0x1bd2a0:
        pal_set_amcntenset0_el0_inline(value);
        break;
    case 0x1bd320:
        pal_set_amcntenset1_el0_inline(value);
        break;
    case 0x1bd200:
        pal_set_amcr_el0_inline(value);
        break;
    case 0x1bd400:
        pal_set_amevcntr00_el0_inline(value);
        break;
    case 0x1bd540:
        pal_set_amevcntr010_el0_inline(value);
        break;
    case 0x1bd560:
        pal_set_amevcntr011_el0_inline(value);
        break;
    case 0x1bd580:
        pal_set_amevcntr012_el0_inline(value);
        break;
    case 0x1bd5a0:
        pal_set_amevcntr013_el0_inline(value);
        break;
    case 0x1bd5c0:
        pal_set_amevcntr014_el0_inline(value);
        break;
    case 0x1bd5e0:
        pal_set_amevcntr015_el0_inline(value);
        break;
    case 0x1bd420:
        pal_set_amevcntr01_el0_inline(value);
        break;
    case 0x1bd440:
        pal_set_amevcntr02_el0_inline(value);
        break;
    case 0x1bd460:
        pal_set_amevcntr03_el0_inline(value);
        break;
    case 0x1bd480:
        pal_set_amevcntr04_el0_inline(value);
        break;
    case 0x1bd4a0:
        pal_set_amevcntr05_el0_inline(value);
        break;
    case 0x1bd4c0:
        pal_set_amevcntr06_el0_inline(value);
        break;
    case 0x1bd4e0:
        pal_set_amevcntr07_el0_inline(value);
        break;
    case 0x1bd500:
        pal_set_amevcntr08_el0_inline(value);
        break;
    case 0x1bd520:
        pal_set_amevcntr09_el0_inline(value);
        break;
    case 0x1bdc00:
        pal_set_amevcntr10_el0_inline(value);
        break;
    case 0x1bdd40:
        pal_set_amevcntr110_el0_inline(value);
        break;
    case 0x1bdd60:
        pal_set_amevcntr111_el0_inline(value);
        break;
    case 0x1bdd80:
        pal_set_amevcntr112_el0_inline(value);
        break;
    case 0x1bdda0:
        pal_set_amevcntr113_el0_inline(value);
        break;
    case 0x1bddc0:
        pal_set_amevcntr114_el0_inline(value);
        break;
    case 0x1bdde0:
        pal_set_amevcntr115_el0_inline(value);
        break;
    case 0x1bdc20:
        pal_set_amevcntr11_el0_inline(value);
        break;
    case 0x1bdc40:
        pal_set_amevcntr12_el0_inline(value);
        break;
    case 0x1bdc60:
        pal_set_amevcntr13_el0_inline(value);
        break;
    case 0x1bdc80:
        pal_set_amevcntr14_el0_inline(value);
        break;
    case 0x1bdca0:
        pal_set_amevcntr15_el0_inline(value);
        break;
    case 0x1bdcc0:
        pal_set_amevcntr16_el0_inline(value);
        break;
    case 0x1bdce0:
        pal_set_amevcntr17_el0_inline(value);
        break;
    case 0x1bdd00:
        pal_set_amevcntr18_el0_inline(value);
        break;
    case 0x1bdd20:
        pal_set_amevcntr19_el0_inline(value);
        break;
    case 0x1bd600:
        pal_set_amevtyper00_el0_inline(value);
        break;
    case 0x1bd740:
        pal_set_amevtyper010_el0_inline(value);
        break;
    case 0x1bd760:
        pal_set_amevtyper011_el0_inline(value);
        break;
    case 0x1bd780:
        pal_set_amevtyper012_el0_inline(value);
        break;
    case 0x1bd7a0:
        pal_set_amevtyper013_el0_inline(value);
        break;
    case 0x1bd7c0:
        pal_set_amevtyper014_el0_inline(value);
        break;
    case 0x1bd7e0:
        pal_set_amevtyper015_el0_inline(value);
        break;
    case 0x1bd620:
        pal_set_amevtyper01_el0_inline(value);
        break;
    case 0x1bd640:
        pal_set_amevtyper02_el0_inline(value);
        break;
    case 0x1bd660:
        pal_set_amevtyper03_el0_inline(value);
        break;
    case 0x1bd680:
        pal_set_amevtyper04_el0_inline(value);
        break;
    case 0x1bd6a0:
        pal_set_amevtyper05_el0_inline(value);
        break;
    case 0x1bd6c0:
        pal_set_amevtyper06_el0_inline(value);
        break;
    case 0x1bd6e0:
        pal_set_amevtyper07_el0_inline(value);
        break;
    case 0x1bd700:
        pal_set_amevtyper08_el0_inline(value);
        break;
    case 0x1bd720:
        pal_set_amevtyper09_el0_inline(value);
        break;
    case 0x1bde00:
        pal_set_amevtyper10_el0_inline(value);
        break;
    case 0x1bdf40:
        pal_set_amevtyper110_el0_inline(value);
        break;
    case 0x1bdf60:
        pal_set_amevtyper111_el0_inline(value);
        break;
    case 0x1bdf80:
        pal_set_amevtyper112_el0_inline(value);
        break;
    case 0x1bdfa0:
        pal_set_amevtyper113_el0_inline(value);
        break;
    case 0x1bdfc0:
        pal_set_amevtyper114_el0_inline(value);
        break;
    case 0x1bdfe0:
        pal_set_amevtyper115_el0_inline(value);
        break;
    case 0x1bde20:
        pal_set_amevtyper11_el0_inline(value);
        break;
    case 0x1bde40:
        pal_set_amevtyper12_el0_inline(value);
        break;
    case 0x1bde60:
        pal_set_amevtyper13_el0_inline(value);
        break;
    case 0x1bde80:
        pal_set_amevtyper14_el0_inline(value);
        break;
    case 0x1bdea0:
        pal_set_amevtyper15_el0_inline(value);
        break;
    case 0x1bdec0:
        pal_set_amevtyper16_el0_inline(value);
        break;
    case 0x1bdee0:
        pal_set_amevtyper17_el0_inline(value);
        break;
    case 0x1bdf00:
        pal_set_amevtyper18_el0_inline(value);
        break;
    case 0x1bdf20:
        pal_set_amevtyper19_el0_inline(value);
        break;
    case 0x1bd260:
        pal_set_amuserenr_el0_inline(value);
        break;
    case 0x182220:
        pal_set_apdakeyhi_el1_inline(value);
        break;
    case 0x182200:
        pal_set_apdakeylo_el1_inline(value);
        break;
    case 0x182260:
        pal_set_apdbkeyhi_el1_inline(value);
        break;
    case 0x182240:
        pal_set_apdbkeylo_el1_inline(value);
        break;
    case 0x182320:
        pal_set_apgakeyhi_el1_inline(value);
        break;
    case 0x182300:
        pal_set_apgakeylo_el1_inline(value);
        break;
    case 0x182120:
        pal_set_apiakeyhi_el1_inline(value);
        break;
    case 0x182100:
        pal_set_apiakeylo_el1_inline(value);
        break;
    case 0x182160:
        pal_set_apibkeyhi_el1_inline(value);
        break;
    case 0x182140:
        pal_set_apibkeylo_el1_inline(value);
        break;
    case 0x190040:
        pal_set_ccsidr2_el1_inline(value);
        break;
    case 0x190000:
        pal_set_ccsidr_el1_inline(value);
        break;
    case 0x190020:
        pal_set_clidr_el1_inline(value);
        break;
    case 0x1be000:
        pal_set_cntfrq_el0_inline(value);
        break;
    case 0x1ce100:
        pal_set_cnthctl_el2_inline(value);
        break;
    case 0x1ce220:
        pal_set_cnthp_ctl_el2_inline(value);
        break;
    case 0x1ce240:
        pal_set_cnthp_cval_el2_inline(value);
        break;
    case 0x1ce200:
        pal_set_cnthp_tval_el2_inline(value);
        break;
    case 0x1ce520:
        pal_set_cnthps_ctl_el2_inline(value);
        break;
    case 0x1ce540:
        pal_set_cnthps_cval_el2_inline(value);
        break;
    case 0x1ce500:
        pal_set_cnthps_tval_el2_inline(value);
        break;
    case 0x1ce320:
        pal_set_cnthv_ctl_el2_inline(value);
        break;
    case 0x1ce340:
        pal_set_cnthv_cval_el2_inline(value);
        break;
    case 0x1ce300:
        pal_set_cnthv_tval_el2_inline(value);
        break;
    case 0x1ce420:
        pal_set_cnthvs_ctl_el2_inline(value);
        break;
    case 0x1ce440:
        pal_set_cnthvs_cval_el2_inline(value);
        break;
    case 0x1ce400:
        pal_set_cnthvs_tval_el2_inline(value);
        break;
    case 0x18e100:
        pal_set_cntkctl_el1_inline(value);
        break;
    case 0x1be220:
        pal_set_cntp_ctl_el0_inline(value);
        break;
    case 0x1be240:
        pal_set_cntp_cval_el0_inline(value);
        break;
    case 0x1be200:
        pal_set_cntp_tval_el0_inline(value);
        break;
    case 0x1be020:
        pal_set_cntpct_el0_inline(value);
        break;
    case 0x1fe220:
        pal_set_cntps_ctl_el1_inline(value);
        break;
    case 0x1fe240:
        pal_set_cntps_cval_el1_inline(value);
        break;
    case 0x1fe200:
        pal_set_cntps_tval_el1_inline(value);
        break;
    case 0x1be320:
        pal_set_cntv_ctl_el0_inline(value);
        break;
    case 0x1be340:
        pal_set_cntv_cval_el0_inline(value);
        break;
    case 0x1be300:
        pal_set_cntv_tval_el0_inline(value);
        break;
    case 0x1be040:
        pal_set_cntvct_el0_inline(value);
        break;
    case 0x1ce060:
        pal_set_cntvoff_el2_inline(value);
        break;
    case 0x18d020:
        pal_set_contextidr_el1_inline(value);
        break;
    case 0x1cd020:
        pal_set_contextidr_el2_inline(value);
        break;
    case 0x181040:
        pal_set_cpacr_el1_inline(value);
        break;
    case 0x1c1140:
        pal_set_cptr_el2_inline(value);
        break;
    case 0x1e1140:
        pal_set_cptr_el3_inline(value);
        break;
    case 0x1a0000:
        pal_set_csselr_el1_inline(value);
        break;
    case 0x1b0020:
        pal_set_ctr_el0_inline(value);
        break;
    case 0x184240:
        pal_set_currentel_inline(value);
        break;
    case 0x1c3000:
        pal_set_dacr32_el2_inline(value);
        break;
    case 0x1b4220:
        pal_set_daif_inline(value);
        break;
    case 0x107ec0:
        pal_set_dbgauthstatus_el1_inline(value);
        break;
    case 0x1000a0:
        pal_set_dbgbcr0_el1_inline(value);
        break;
    case 0x100aa0:
        pal_set_dbgbcr10_el1_inline(value);
        break;
    case 0x100ba0:
        pal_set_dbgbcr11_el1_inline(value);
        break;
    case 0x100ca0:
        pal_set_dbgbcr12_el1_inline(value);
        break;
    case 0x100da0:
        pal_set_dbgbcr13_el1_inline(value);
        break;
    case 0x100ea0:
        pal_set_dbgbcr14_el1_inline(value);
        break;
    case 0x100fa0:
        pal_set_dbgbcr15_el1_inline(value);
        break;
    case 0x1001a0:
        pal_set_dbgbcr1_el1_inline(value);
        break;
    case 0x1002a0:
        pal_set_dbgbcr2_el1_inline(value);
        break;
    case 0x1003a0:
        pal_set_dbgbcr3_el1_inline(value);
        break;
    case 0x1004a0:
        pal_set_dbgbcr4_el1_inline(value);
        break;
    case 0x1005a0:
        pal_set_dbgbcr5_el1_inline(value);
        break;
    case 0x1006a0:
        pal_set_dbgbcr6_el1_inline(value);
        break;
    case 0x1007a0:
        pal_set_dbgbcr7_el1_inline(value);
        break;
    case 0x1008a0:
        pal_set_dbgbcr8_el1_inline(value);
        break;
    case 0x1009a0:
        pal_set_dbgbcr9_el1_inline(value);
        break;
    case 0x100080:
        pal_set_dbgbvr0_el1_inline(value);
        break;
    case 0x100a80:
        pal_set_dbgbvr10_el1_inline(value);
        break;
    case 0x100b80:
        pal_set_dbgbvr11_el1_inline(value);
        break;
    case 0x100c80:
        pal_set_dbgbvr12_el1_inline(value);
        break;
    case 0x100d80:
        pal_set_dbgbvr13_el1_inline(value);
        break;
    case 0x100e80:
        pal_set_dbgbvr14_el1_inline(value);
        break;
    case 0x100f80:
        pal_set_dbgbvr15_el1_inline(value);
        break;
    case 0x100180:
        pal_set_dbgbvr1_el1_inline(value);
        break;
    case 0x100280:
        pal_set_dbgbvr2_el1_inline(value);
        break;
    case 0x100380:
        pal_set_dbgbvr3_el1_inline(value);
        break;
    case 0x100480:
        pal_set_dbgbvr4_el1_inline(value);
        break;
    case 0x100580:
        pal_set_dbgbvr5_el1_inline(value);
        break;
    case 0x100680:
        pal_set_dbgbvr6_el1_inline(value);
        break;
    case 0x100780:
        pal_set_dbgbvr7_el1_inline(value);
        break;
    case 0x100880:
        pal_set_dbgbvr8_el1_inline(value);
        break;
    case 0x100980:
        pal_set_dbgbvr9_el1_inline(value);
        break;
    case 0x1079c0:
        pal_set_dbgclaimclr_el1_inline(value);
        break;
    case 0x1078c0:
        pal_set_dbgclaimset_el1_inline(value);
        break;
    case 0x130400:
        pal_set_dbgdtr_el0_inline(value);
        break;
    case 0x130500:
        pal_set_dbgdtrrx_el0_inline(value);
        break;
    case 0x101480:
        pal_set_dbgprcr_el1_inline(value);
        break;
    case 0x140700:
        pal_set_dbgvcr32_el2_inline(value);
        break;
    case 0x1000e0:
        pal_set_dbgwcr0_el1_inline(value);
        break;
    case 0x100ae0:
        pal_set_dbgwcr10_el1_inline(value);
        break;
    case 0x100be0:
        pal_set_dbgwcr11_el1_inline(value);
        break;
    case 0x100ce0:
        pal_set_dbgwcr12_el1_inline(value);
        break;
    case 0x100de0:
        pal_set_dbgwcr13_el1_inline(value);
        break;
    case 0x100ee0:
        pal_set_dbgwcr14_el1_inline(value);
        break;
    case 0x100fe0:
        pal_set_dbgwcr15_el1_inline(value);
        break;
    case 0x1001e0:
        pal_set_dbgwcr1_el1_inline(value);
        break;
    case 0x1002e0:
        pal_set_dbgwcr2_el1_inline(value);
        break;
    case 0x1003e0:
        pal_set_dbgwcr3_el1_inline(value);
        break;
    case 0x1004e0:
        pal_set_dbgwcr4_el1_inline(value);
        break;
    case 0x1005e0:
        pal_set_dbgwcr5_el1_inline(value);
        break;
    case 0x1006e0:
        pal_set_dbgwcr6_el1_inline(value);
        break;
    case 0x1007e0:
        pal_set_dbgwcr7_el1_inline(value);
        break;
    case 0x1008e0:
        pal_set_dbgwcr8_el1_inline(value);
        break;
    case 0x1009e0:
        pal_set_dbgwcr9_el1_inline(value);
        break;
    case 0x1000c0:
        pal_set_dbgwvr0_el1_inline(value);
        break;
    case 0x100ac0:
        pal_set_dbgwvr10_el1_inline(value);
        break;
    case 0x100bc0:
        pal_set_dbgwvr11_el1_inline(value);
        break;
    case 0x100cc0:
        pal_set_dbgwvr12_el1_inline(value);
        break;
    case 0x100dc0:
        pal_set_dbgwvr13_el1_inline(value);
        break;
    case 0x100ec0:
        pal_set_dbgwvr14_el1_inline(value);
        break;
    case 0x100fc0:
        pal_set_dbgwvr15_el1_inline(value);
        break;
    case 0x1001c0:
        pal_set_dbgwvr1_el1_inline(value);
        break;
    case 0x1002c0:
        pal_set_dbgwvr2_el1_inline(value);
        break;
    case 0x1003c0:
        pal_set_dbgwvr3_el1_inline(value);
        break;
    case 0x1004c0:
        pal_set_dbgwvr4_el1_inline(value);
        break;
    case 0x1005c0:
        pal_set_dbgwvr5_el1_inline(value);
        break;
    case 0x1006c0:
        pal_set_dbgwvr6_el1_inline(value);
        break;
    case 0x1007c0:
        pal_set_dbgwvr7_el1_inline(value);
        break;
    case 0x1008c0:
        pal_set_dbgwvr8_el1_inline(value);
        break;
    case 0x1009c0:
        pal_set_dbgwvr9_el1_inline(value);
        break;
    case 0x1b00e0:
        pal_set_dczid_el0_inline(value);
        break;
    case 0x18c120:
        pal_set_disr_el1_inline(value);
        break;
    case 0x1b42a0:
        pal_set_dit_inline(value);
        break;
    case 0x1b4520:
        pal_set_dlr_el0_inline(value);
        break;
    case 0x1b4500:
        pal_set_dspsr_el0_inline(value);
        break;
    case 0x184020:
        pal_set_elr_el1_inline(value);
        break;
    case 0x1c4020:
        pal_set_elr_el2_inline(value);
        break;
    case 0x1e4020:
        pal_set_elr_el3_inline(value);
        break;
    case 0x185300:
        pal_set_erridr_el1_inline(value);
        break;
    case 0x185320:
        pal_set_errselr_el1_inline(value);
        break;
    case 0x185460:
        pal_set_erxaddr_el1_inline(value);
        break;
    case 0x185420:
        pal_set_erxctlr_el1_inline(value);
        break;
    case 0x185400:
        pal_set_erxfr_el1_inline(value);
        break;
    case 0x185500:
        pal_set_erxmisc0_el1_inline(value);
        break;
    case 0x185520:
        pal_set_erxmisc1_el1_inline(value);
        break;
    case 0x185540:
        pal_set_erxmisc2_el1_inline(value);
        break;
    case 0x185560:
        pal_set_erxmisc3_el1_inline(value);
        break;
    case 0x1854c0:
        pal_set_erxpfgcdn_el1_inline(value);
        break;
    case 0x1854a0:
        pal_set_erxpfgctl_el1_inline(value);
        break;
    case 0x185480:
        pal_set_erxpfgf_el1_inline(value);
        break;
    case 0x185440:
        pal_set_erxstatus_el1_inline(value);
        break;
    case 0x185200:
        pal_set_esr_el1_inline(value);
        break;
    case 0x1c5200:
        pal_set_esr_el2_inline(value);
        break;
    case 0x1e5200:
        pal_set_esr_el3_inline(value);
        break;
    case 0x186000:
        pal_set_far_el1_inline(value);
        break;
    case 0x1c6000:
        pal_set_far_el2_inline(value);
        break;
    case 0x1e6000:
        pal_set_far_el3_inline(value);
        break;
    case 0x1b4400:
        pal_set_fpcr_inline(value);
        break;
    case 0x1c5300:
        pal_set_fpexc32_el2_inline(value);
        break;
    case 0x1b4420:
        pal_set_fpsr_inline(value);
        break;
    case 0x1810c0:
        pal_set_gcr_el1_inline(value);
        break;
    case 0x1c11e0:
        pal_set_hacr_el2_inline(value);
        break;
    case 0x1c1100:
        pal_set_hcr_el2_inline(value);
        break;
    case 0x1c6080:
        pal_set_hpfar_el2_inline(value);
        break;
    case 0x1c1160:
        pal_set_hstr_el2_inline(value);
        break;
    case 0x18c880:
        pal_set_icc_ap0r0_el1_inline(value);
        break;
    case 0x18c8a0:
        pal_set_icc_ap0r1_el1_inline(value);
        break;
    case 0x18c8c0:
        pal_set_icc_ap0r2_el1_inline(value);
        break;
    case 0x18c8e0:
        pal_set_icc_ap0r3_el1_inline(value);
        break;
    case 0x18c900:
        pal_set_icc_ap1r0_el1_inline(value);
        break;
    case 0x18c920:
        pal_set_icc_ap1r1_el1_inline(value);
        break;
    case 0x18c940:
        pal_set_icc_ap1r2_el1_inline(value);
        break;
    case 0x18c960:
        pal_set_icc_ap1r3_el1_inline(value);
        break;
    case 0x18cbc0:
        pal_set_icc_asgi1r_el1_inline(value);
        break;
    case 0x18c860:
        pal_set_icc_bpr0_el1_inline(value);
        break;
    case 0x18cc60:
        pal_set_icc_bpr1_el1_inline(value);
        break;
    case 0x18cc80:
        pal_set_icc_ctlr_el1_inline(value);
        break;
    case 0x1ecc80:
        pal_set_icc_ctlr_el3_inline(value);
        break;
    case 0x18cb20:
        pal_set_icc_dir_el1_inline(value);
        break;
    case 0x18c820:
        pal_set_icc_eoir0_el1_inline(value);
        break;
    case 0x18cc20:
        pal_set_icc_eoir1_el1_inline(value);
        break;
    case 0x18c840:
        pal_set_icc_hppir0_el1_inline(value);
        break;
    case 0x18cc40:
        pal_set_icc_hppir1_el1_inline(value);
        break;
    case 0x18c800:
        pal_set_icc_iar0_el1_inline(value);
        break;
    case 0x18cc00:
        pal_set_icc_iar1_el1_inline(value);
        break;
    case 0x18ccc0:
        pal_set_icc_igrpen0_el1_inline(value);
        break;
    case 0x18cce0:
        pal_set_icc_igrpen1_el1_inline(value);
        break;
    case 0x1ecce0:
        pal_set_icc_igrpen1_el3_inline(value);
        break;
    case 0x184600:
        pal_set_icc_pmr_el1_inline(value);
        break;
    case 0x18cb60:
        pal_set_icc_rpr_el1_inline(value);
        break;
    case 0x18cbe0:
        pal_set_icc_sgi0r_el1_inline(value);
        break;
    case 0x18cba0:
        pal_set_icc_sgi1r_el1_inline(value);
        break;
    case 0x18cca0:
        pal_set_icc_sre_el1_inline(value);
        break;
    case 0x1cc9a0:
        pal_set_icc_sre_el2_inline(value);
        break;
    case 0x1ecca0:
        pal_set_icc_sre_el3_inline(value);
        break;
    case 0x1cc800:
        pal_set_ich_ap0r0_el2_inline(value);
        break;
    case 0x1cc820:
        pal_set_ich_ap0r1_el2_inline(value);
        break;
    case 0x1cc840:
        pal_set_ich_ap0r2_el2_inline(value);
        break;
    case 0x1cc860:
        pal_set_ich_ap0r3_el2_inline(value);
        break;
    case 0x1cc900:
        pal_set_ich_ap1r0_el2_inline(value);
        break;
    case 0x1cc920:
        pal_set_ich_ap1r1_el2_inline(value);
        break;
    case 0x1cc940:
        pal_set_ich_ap1r2_el2_inline(value);
        break;
    case 0x1cc960:
        pal_set_ich_ap1r3_el2_inline(value);
        break;
    case 0x1ccb60:
        pal_set_ich_eisr_el2_inline(value);
        break;
    case 0x1ccba0:
        pal_set_ich_elrsr_el2_inline(value);
        break;
    case 0x1ccb00:
        pal_set_ich_hcr_el2_inline(value);
        break;
    case 0x1ccc00:
        pal_set_ich_lr0_el2_inline(value);
        break;
    case 0x1ccd40:
        pal_set_ich_lr10_el2_inline(value);
        break;
    case 0x1ccd60:
        pal_set_ich_lr11_el2_inline(value);
        break;
    case 0x1ccd80:
        pal_set_ich_lr12_el2_inline(value);
        break;
    case 0x1ccda0:
        pal_set_ich_lr13_el2_inline(value);
        break;
    case 0x1ccdc0:
        pal_set_ich_lr14_el2_inline(value);
        break;
    case 0x1ccde0:
        pal_set_ich_lr15_el2_inline(value);
        break;
    case 0x1ccc20:
        pal_set_ich_lr1_el2_inline(value);
        break;
    case 0x1ccc40:
        pal_set_ich_lr2_el2_inline(value);
        break;
    case 0x1ccc60:
        pal_set_ich_lr3_el2_inline(value);
        break;
    case 0x1ccc80:
        pal_set_ich_lr4_el2_inline(value);
        break;
    case 0x1ccca0:
        pal_set_ich_lr5_el2_inline(value);
        break;
    case 0x1cccc0:
        pal_set_ich_lr6_el2_inline(value);
        break;
    case 0x1ccce0:
        pal_set_ich_lr7_el2_inline(value);
        break;
    case 0x1ccd00:
        pal_set_ich_lr8_el2_inline(value);
        break;
    case 0x1ccd20:
        pal_set_ich_lr9_el2_inline(value);
        break;
    case 0x1ccb40:
        pal_set_ich_misr_el2_inline(value);
        break;
    case 0x1ccbe0:
        pal_set_ich_vmcr_el2_inline(value);
        break;
    case 0x1ccb20:
        pal_set_ich_vtr_el2_inline(value);
        break;
    case 0x180580:
        pal_set_id_aa64afr0_el1_inline(value);
        break;
    case 0x1805a0:
        pal_set_id_aa64afr1_el1_inline(value);
        break;
    case 0x180500:
        pal_set_id_aa64dfr0_el1_inline(value);
        break;
    case 0x180520:
        pal_set_id_aa64dfr1_el1_inline(value);
        break;
    case 0x180600:
        pal_set_id_aa64isar0_el1_inline(value);
        break;
    case 0x180620:
        pal_set_id_aa64isar1_el1_inline(value);
        break;
    case 0x180700:
        pal_set_id_aa64mmfr0_el1_inline(value);
        break;
    case 0x180720:
        pal_set_id_aa64mmfr1_el1_inline(value);
        break;
    case 0x180740:
        pal_set_id_aa64mmfr2_el1_inline(value);
        break;
    case 0x180400:
        pal_set_id_aa64pfr0_el1_inline(value);
        break;
    case 0x180420:
        pal_set_id_aa64pfr1_el1_inline(value);
        break;
    case 0x180480:
        pal_set_id_aa64zfr0_el1_inline(value);
        break;
    case 0x180160:
        pal_set_id_afr0_el1_inline(value);
        break;
    case 0x180140:
        pal_set_id_dfr0_el1_inline(value);
        break;
    case 0x180200:
        pal_set_id_isar0_el1_inline(value);
        break;
    case 0x180220:
        pal_set_id_isar1_el1_inline(value);
        break;
    case 0x180240:
        pal_set_id_isar2_el1_inline(value);
        break;
    case 0x180260:
        pal_set_id_isar3_el1_inline(value);
        break;
    case 0x180280:
        pal_set_id_isar4_el1_inline(value);
        break;
    case 0x1802a0:
        pal_set_id_isar5_el1_inline(value);
        break;
    case 0x1802e0:
        pal_set_id_isar6_el1_inline(value);
        break;
    case 0x180180:
        pal_set_id_mmfr0_el1_inline(value);
        break;
    case 0x1801a0:
        pal_set_id_mmfr1_el1_inline(value);
        break;
    case 0x1801c0:
        pal_set_id_mmfr2_el1_inline(value);
        break;
    case 0x1801e0:
        pal_set_id_mmfr3_el1_inline(value);
        break;
    case 0x1802c0:
        pal_set_id_mmfr4_el1_inline(value);
        break;
    case 0x180100:
        pal_set_id_pfr0_el1_inline(value);
        break;
    case 0x180120:
        pal_set_id_pfr1_el1_inline(value);
        break;
    case 0x180380:
        pal_set_id_pfr2_el1_inline(value);
        break;
    case 0x1c5020:
        pal_set_ifsr32_el2_inline(value);
        break;
    case 0x18c100:
        pal_set_isr_el1_inline(value);
        break;
    case 0x18a460:
        pal_set_lorc_el1_inline(value);
        break;
    case 0x18a420:
        pal_set_lorea_el1_inline(value);
        break;
    case 0x18a4e0:
        pal_set_lorid_el1_inline(value);
        break;
    case 0x18a440:
        pal_set_lorn_el1_inline(value);
        break;
    case 0x18a400:
        pal_set_lorsa_el1_inline(value);
        break;
    case 0x18a200:
        pal_set_mair_el1_inline(value);
        break;
    case 0x1ca200:
        pal_set_mair_el2_inline(value);
        break;
    case 0x1ea200:
        pal_set_mair_el3_inline(value);
        break;
    case 0x100200:
        pal_set_mdccint_el1_inline(value);
        break;
    case 0x130100:
        pal_set_mdccsr_el0_inline(value);
        break;
    case 0x1c1120:
        pal_set_mdcr_el2_inline(value);
        break;
    case 0x1e1320:
        pal_set_mdcr_el3_inline(value);
        break;
    case 0x101000:
        pal_set_mdrar_el1_inline(value);
        break;
    case 0x100240:
        pal_set_mdscr_el1_inline(value);
        break;
    case 0x180000:
        pal_set_midr_el1_inline(value);
        break;
    case 0x18a520:
        pal_set_mpam0_el1_inline(value);
        break;
    case 0x18a500:
        pal_set_mpam1_el1_inline(value);
        break;
    case 0x1ca500:
        pal_set_mpam2_el2_inline(value);
        break;
    case 0x1ea500:
        pal_set_mpam3_el3_inline(value);
        break;
    case 0x1ca400:
        pal_set_mpamhcr_el2_inline(value);
        break;
    case 0x18a480:
        pal_set_mpamidr_el1_inline(value);
        break;
    case 0x1ca600:
        pal_set_mpamvpm0_el2_inline(value);
        break;
    case 0x1ca620:
        pal_set_mpamvpm1_el2_inline(value);
        break;
    case 0x1ca640:
        pal_set_mpamvpm2_el2_inline(value);
        break;
    case 0x1ca660:
        pal_set_mpamvpm3_el2_inline(value);
        break;
    case 0x1ca680:
        pal_set_mpamvpm4_el2_inline(value);
        break;
    case 0x1ca6a0:
        pal_set_mpamvpm5_el2_inline(value);
        break;
    case 0x1ca6c0:
        pal_set_mpamvpm6_el2_inline(value);
        break;
    case 0x1ca6e0:
        pal_set_mpamvpm7_el2_inline(value);
        break;
    case 0x1ca420:
        pal_set_mpamvpmv_el2_inline(value);
        break;
    case 0x1800a0:
        pal_set_mpidr_el1_inline(value);
        break;
    case 0x180300:
        pal_set_mvfr0_el1_inline(value);
        break;
    case 0x180320:
        pal_set_mvfr1_el1_inline(value);
        break;
    case 0x180340:
        pal_set_mvfr2_el1_inline(value);
        break;
    case 0x1b4200:
        pal_set_nzcv_inline(value);
        break;
    case 0x101380:
        pal_set_osdlr_el1_inline(value);
        break;
    case 0x100040:
        pal_set_osdtrrx_el1_inline(value);
        break;
    case 0x100340:
        pal_set_osdtrtx_el1_inline(value);
        break;
    case 0x100640:
        pal_set_oseccr_el1_inline(value);
        break;
    case 0x101080:
        pal_set_oslar_el1_inline(value);
        break;
    case 0x101180:
        pal_set_oslsr_el1_inline(value);
        break;
    case 0x184260:
        pal_set_pan_inline(value);
        break;
    case 0x187400:
        pal_set_par_el1_inline(value);
        break;
    case 0x189ae0:
        pal_set_pmbidr_el1_inline(value);
        break;
    case 0x189a00:
        pal_set_pmblimitr_el1_inline(value);
        break;
    case 0x189a20:
        pal_set_pmbptr_el1_inline(value);
        break;
    case 0x189a60:
        pal_set_pmbsr_el1_inline(value);
        break;
    case 0x1befe0:
        pal_set_pmccfiltr_el0_inline(value);
        break;
    case 0x1b9d00:
        pal_set_pmccntr_el0_inline(value);
        break;
    case 0x1b9cc0:
        pal_set_pmceid0_el0_inline(value);
        break;
    case 0x1b9ce0:
        pal_set_pmceid1_el0_inline(value);
        break;
    case 0x1b9c40:
        pal_set_pmcntenclr_el0_inline(value);
        break;
    case 0x1b9c20:
        pal_set_pmcntenset_el0_inline(value);
        break;
    case 0x1b9c00:
        pal_set_pmcr_el0_inline(value);
        break;
    case 0x1be800:
        pal_set_pmevcntr0_el0_inline(value);
        break;
    case 0x1be940:
        pal_set_pmevcntr10_el0_inline(value);
        break;
    case 0x1be960:
        pal_set_pmevcntr11_el0_inline(value);
        break;
    case 0x1be980:
        pal_set_pmevcntr12_el0_inline(value);
        break;
    case 0x1be9a0:
        pal_set_pmevcntr13_el0_inline(value);
        break;
    case 0x1be9c0:
        pal_set_pmevcntr14_el0_inline(value);
        break;
    case 0x1be9e0:
        pal_set_pmevcntr15_el0_inline(value);
        break;
    case 0x1bea00:
        pal_set_pmevcntr16_el0_inline(value);
        break;
    case 0x1bea20:
        pal_set_pmevcntr17_el0_inline(value);
        break;
    case 0x1bea40:
        pal_set_pmevcntr18_el0_inline(value);
        break;
    case 0x1bea60:
        pal_set_pmevcntr19_el0_inline(value);
        break;
    case 0x1be820:
        pal_set_pmevcntr1_el0_inline(value);
        break;
    case 0x1bea80:
        pal_set_pmevcntr20_el0_inline(value);
        break;
    case 0x1beaa0:
        pal_set_pmevcntr21_el0_inline(value);
        break;
    case 0x1beac0:
        pal_set_pmevcntr22_el0_inline(value);
        break;
    case 0x1beae0:
        pal_set_pmevcntr23_el0_inline(value);
        break;
    case 0x1beb00:
        pal_set_pmevcntr24_el0_inline(value);
        break;
    case 0x1beb20:
        pal_set_pmevcntr25_el0_inline(value);
        break;
    case 0x1beb40:
        pal_set_pmevcntr26_el0_inline(value);
        break;
    case 0x1beb60:
        pal_set_pmevcntr27_el0_inline(value);
        break;
    case 0x1beb80:
        pal_set_pmevcntr28_el0_inline(value);
        break;
    case 0x1beba0:
        pal_set_pmevcntr29_el0_inline(value);
        break;
    case 0x1be840:
        pal_set_pmevcntr2_el0_inline(value);
        break;
    case 0x1bebc0:
        pal_set_pmevcntr30_el0_inline(value);
        break;
    case 0x1be860:
        pal_set_pmevcntr3_el0_inline(value);
        break;
    case 0x1be880:
        pal_set_pmevcntr4_el0_inline(value);
        break;
    case 0x1be8a0:
        pal_set_pmevcntr5_el0_inline(value);
        break;
    case 0x1be8c0:
        pal_set_pmevcntr6_el0_inline(value);
        break;
    case 0x1be8e0:
        pal_set_pmevcntr7_el0_inline(value);
        break;
    case 0x1be900:
        pal_set_pmevcntr8_el0_inline(value);
        break;
    case 0x1be920:
        pal_set_pmevcntr9_el0_inline(value);
        break;
    case 0x1bec00:
        pal_set_pmevtyper0_el0_inline(value);
        break;
    case 0x1bed40:
        pal_set_pmevtyper10_el0_inline(value);
        break;
    case 0x1bed60:
        pal_set_pmevtyper11_el0_inline(value);
        break;
    case 0x1bed80:
        pal_set_pmevtyper12_el0_inline(value);
        break;
    case 0x1beda0:
        pal_set_pmevtyper13_el0_inline(value);
        break;
    case 0x1bedc0:
        pal_set_pmevtyper14_el0_inline(value);
        break;
    case 0x1bede0:
        pal_set_pmevtyper15_el0_inline(value);
        break;
    case 0x1bee00:
        pal_set_pmevtyper16_el0_inline(value);
        break;
    case 0x1bee20:
        pal_set_pmevtyper17_el0_inline(value);
        break;
    case 0x1bee40:
        pal_set_pmevtyper18_el0_inline(value);
        break;
    case 0x1bee60:
        pal_set_pmevtyper19_el0_inline(value);
        break;
    case 0x1bec20:
        pal_set_pmevtyper1_el0_inline(value);
        break;
    case 0x1bee80:
        pal_set_pmevtyper20_el0_inline(value);
        break;
    case 0x1beea0:
        pal_set_pmevtyper21_el0_inline(value);
        break;
    case 0x1beec0:
        pal_set_pmevtyper22_el0_inline(value);
        break;
    case 0x1beee0:
        pal_set_pmevtyper23_el0_inline(value);
        break;
    case 0x1bef00:
        pal_set_pmevtyper24_el0_inline(value);
        break;
    case 0x1bef20:
        pal_set_pmevtyper25_el0_inline(value);
        break;
    case 0x1bef40:
        pal_set_pmevtyper26_el0_inline(value);
        break;
    case 0x1bef60:
        pal_set_pmevtyper27_el0_inline(value);
        break;
    case 0x1bef80:
        pal_set_pmevtyper28_el0_inline(value);
        break;
    case 0x1befa0:
        pal_set_pmevtyper29_el0_inline(value);
        break;
    case 0x1bec40:
        pal_set_pmevtyper2_el0_inline(value);
        break;
    case 0x1befc0:
        pal_set_pmevtyper30_el0_inline(value);
        break;
    case 0x1bec60:
        pal_set_pmevtyper3_el0_inline(value);
        break;
    case 0x1bec80:
        pal_set_pmevtyper4_el0_inline(value);
        break;
    case 0x1beca0:
        pal_set_pmevtyper5_el0_inline(value);
        break;
    case 0x1becc0:
        pal_set_pmevtyper6_el0_inline(value);
        break;
    case 0x1bece0:
        pal_set_pmevtyper7_el0_inline(value);
        break;
    case 0x1bed00:
        pal_set_pmevtyper8_el0_inline(value);
        break;
    case 0x1bed20:
        pal_set_pmevtyper9_el0_inline(value);
        break;
    case 0x189e40:
        pal_set_pmintenclr_el1_inline(value);
        break;
    case 0x189e20:
        pal_set_pmintenset_el1_inline(value);
        break;
    case 0x189ec0:
        pal_set_pmmir_el1_inline(value);
        break;
    case 0x1b9c60:
        pal_set_pmovsclr_el0_inline(value);
        break;
    case 0x1b9e60:
        pal_set_pmovsset_el0_inline(value);
        break;
    case 0x189900:
        pal_set_pmscr_el1_inline(value);
        break;
    case 0x1c9900:
        pal_set_pmscr_el2_inline(value);
        break;
    case 0x1b9ca0:
        pal_set_pmselr_el0_inline(value);
        break;
    case 0x1899a0:
        pal_set_pmsevfr_el1_inline(value);
        break;
    case 0x189980:
        pal_set_pmsfcr_el1_inline(value);
        break;
    case 0x189940:
        pal_set_pmsicr_el1_inline(value);
        break;
    case 0x1899e0:
        pal_set_pmsidr_el1_inline(value);
        break;
    case 0x189960:
        pal_set_pmsirr_el1_inline(value);
        break;
    case 0x1899c0:
        pal_set_pmslatfr_el1_inline(value);
        break;
    case 0x1b9c80:
        pal_set_pmswinc_el0_inline(value);
        break;
    case 0x1b9e00:
        pal_set_pmuserenr_el0_inline(value);
        break;
    case 0x1b9d40:
        pal_set_pmxevcntr_el0_inline(value);
        break;
    case 0x1b9d20:
        pal_set_pmxevtyper_el0_inline(value);
        break;
    case 0x1800c0:
        pal_set_revidr_el1_inline(value);
        break;
    case 0x1810a0:
        pal_set_rgsr_el1_inline(value);
        break;
    case 0x18c040:
        pal_set_rmr_el1_inline(value);
        break;
    case 0x1cc040:
        pal_set_rmr_el2_inline(value);
        break;
    case 0x1ec040:
        pal_set_rmr_el3_inline(value);
        break;
    case 0x1b2400:
        pal_set_rndr_inline(value);
        break;
    case 0x1b2420:
        pal_set_rndrrs_inline(value);
        break;
    case 0x18c020:
        pal_set_rvbar_el1_inline(value);
        break;
    case 0x1cc020:
        pal_set_rvbar_el2_inline(value);
        break;
    case 0x1ec020:
        pal_set_rvbar_el3_inline(value);
        break;
    case 0x1e1100:
        pal_set_scr_el3_inline(value);
        break;
    case 0x181000:
        pal_set_sctlr_el1_inline(value);
        break;
    case 0x1c1000:
        pal_set_sctlr_el2_inline(value);
        break;
    case 0x1e1000:
        pal_set_sctlr_el3_inline(value);
        break;
    case 0x1bd0e0:
        pal_set_scxtnum_el0_inline(value);
        break;
    case 0x18d0e0:
        pal_set_scxtnum_el1_inline(value);
        break;
    case 0x1cd0e0:
        pal_set_scxtnum_el2_inline(value);
        break;
    case 0x1ed0e0:
        pal_set_scxtnum_el3_inline(value);
        break;
    case 0x1c1320:
        pal_set_sder32_el2_inline(value);
        break;
    case 0x1e1120:
        pal_set_sder32_el3_inline(value);
        break;
    case 0x184100:
        pal_set_sp_el0_inline(value);
        break;
    case 0x1c4100:
        pal_set_sp_el1_inline(value);
        break;
    case 0x1e4100:
        pal_set_sp_el2_inline(value);
        break;
    case 0x184200:
        pal_set_spsel_inline(value);
        break;
    case 0x1c4320:
        pal_set_spsr_abt_inline(value);
        break;
    case 0x184000:
        pal_set_spsr_el1_inline(value);
        break;
    case 0x1c4000:
        pal_set_spsr_el2_inline(value);
        break;
    case 0x1e4000:
        pal_set_spsr_el3_inline(value);
        break;
    case 0x1c4360:
        pal_set_spsr_fiq_inline(value);
        break;
    case 0x1c4300:
        pal_set_spsr_irq_inline(value);
        break;
    case 0x1c4340:
        pal_set_spsr_und_inline(value);
        break;
    case 0x1b42c0:
        pal_set_ssbs_inline(value);
        break;
    case 0x1b42e0:
        pal_set_tco_inline(value);
        break;
    case 0x182040:
        pal_set_tcr_el1_inline(value);
        break;
    case 0x1c2040:
        pal_set_tcr_el2_inline(value);
        break;
    case 0x1e2040:
        pal_set_tcr_el3_inline(value);
        break;
    case 0x186500:
        pal_set_tfsr_el1_inline(value);
        break;
    case 0x1c6500:
        pal_set_tfsr_el2_inline(value);
        break;
    case 0x1e6500:
        pal_set_tfsr_el3_inline(value);
        break;
    case 0x186620:
        pal_set_tfsre0_el1_inline(value);
        break;
    case 0x1bd040:
        pal_set_tpidr_el0_inline(value);
        break;
    case 0x18d080:
        pal_set_tpidr_el1_inline(value);
        break;
    case 0x1cd040:
        pal_set_tpidr_el2_inline(value);
        break;
    case 0x1ed040:
        pal_set_tpidr_el3_inline(value);
        break;
    case 0x1bd060:
        pal_set_tpidrro_el0_inline(value);
        break;
    case 0x181220:
        pal_set_trfcr_el1_inline(value);
        break;
    case 0x1c1220:
        pal_set_trfcr_el2_inline(value);
        break;
    case 0x182000:
        pal_set_ttbr0_el1_inline(value);
        break;
    case 0x1c2000:
        pal_set_ttbr0_el2_inline(value);
        break;
    case 0x1e2000:
        pal_set_ttbr0_el3_inline(value);
        break;
    case 0x182020:
        pal_set_ttbr1_el1_inline(value);
        break;
    case 0x1c2020:
        pal_set_ttbr1_el2_inline(value);
        break;
    case 0x184280:
        pal_set_uao_inline(value);
        break;
    case 0x18c000:
        pal_set_vbar_el1_inline(value);
        break;
    case 0x1cc000:
        pal_set_vbar_el2_inline(value);
        break;
    case 0x1ec000:
        pal_set_vbar_el3_inline(value);
        break;
    case 0x1cc120:
        pal_set_vdisr_el2_inline(value);
        break;
    case 0x1c2200:
        pal_set_vncr_el2_inline(value);
        break;
    case 0x1c5260:
        pal_set_vsesr_el2_inline(value);
        break;
    case 0x1c2640:
        pal_set_vstcr_el2_inline(value);
        break;
    case 0x1c2600:
        pal_set_vsttbr_el2_inline(value);
        break;
    case 0x1c2140:
        pal_set_vtcr_el2_inline(value);
        break;
    case 0x1c2100:
        pal_set_vttbr_el2_inline(value);
        break;
    case 0x181200:
        pal_set_zcr_el1_inline(value);
        break;
    case 0x1c1200:
        pal_set_zcr_el2_inline(value);
        break;
    case 0x1e1200:
        pal_set_zcr_el3_inline(value);
        break;
    default:
        printk(KERN_INFO "Defualt case!");
        return -EINVAL;
        break;
    }


    return 0;
}
