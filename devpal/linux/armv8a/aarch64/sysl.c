#include <linux/uaccess.h>
#include "devpal_abi_armv8a_aarch64.h"
#include <linux/printk.h>
#include "pal/aarch64/sysl_inline.h"

long handle_devpal_ioctl_sysl(struct sysl_operands * user_ops)
{
    //Init of variables/operands 
    uint8_t op1 = 0;
    uint8_t crn = 0;
    uint8_t crm = 0;
    uint8_t op2 = 0;
    uint64_t value = 0;
    struct sysl_operands kern_ops = {0};

    if (copy_from_user(&kern_ops, user_ops, sizeof(struct sysl_operands)))
        return -1;

    op0 = kern_ops.in.op0;
    op1 = kern_ops.in.op1;
    crn = kern_ops.in.crn;
    crm = kern_ops.in.crm;
    op2 = kern_ops.in.op2;

    //The switch vector the sys/sysl instruction encodin, the last 5 bits are not used for our purposes
    switch_vector |= (op0 & 0x3) << 19;
    switch_vector |= (op1 & 0x7) << 16;
    switch_vector |= (crn & 0xF) << 12;
    switch_vector |= (crm & 0xF) << 8;
    switch_vector |= (op2 & 0x7) << 5;

    //printk(KERN_INFO "operands: %x, %x, %x, %x, %x\n", op0, op1, crn, crm, op2);
    //printk(KERN_INFO "vector hex: %x", switch_vector);

    switch (switch_vector)
    {
    case 0x181020:
        value = pal_get_actlr_el1_inline();
        break;
    case 0x1c1020:
        value = pal_get_actlr_el2_inline();
        break;
    case 0x1e1020:
        value = pal_get_actlr_el3_inline();
        break;
    case 0x185100:
        value = pal_get_afsr0_el1_inline();
        break;
    case 0x1c5100:
        value = pal_get_afsr0_el2_inline();
        break;
    case 0x1e5100:
        value = pal_get_afsr0_el3_inline();
        break;
    case 0x185120:
        value = pal_get_afsr1_el1_inline();
        break;
    case 0x1c5120:
        value = pal_get_afsr1_el2_inline();
        break;
    case 0x1e5120:
        value = pal_get_afsr1_el3_inline();
        break;
    case 0x1900e0:
        value = pal_get_aidr_el1_inline();
        break;
    case 0x18a300:
        value = pal_get_amair_el1_inline();
        break;
    case 0x1ca300:
        value = pal_get_amair_el2_inline();
        break;
    case 0x1ea300:
        value = pal_get_amair_el3_inline();
        break;
    case 0x1bd220:
        value = pal_get_amcfgr_el0_inline();
        break;
    case 0x1bd240:
        value = pal_get_amcgcr_el0_inline();
        break;
    case 0x1bd280:
        value = pal_get_amcntenclr0_el0_inline();
        break;
    case 0x1bd300:
        value = pal_get_amcntenclr1_el0_inline();
        break;
    case 0x1bd2a0:
        value = pal_get_amcntenset0_el0_inline();
        break;
    case 0x1bd320:
        value = pal_get_amcntenset1_el0_inline();
        break;
    case 0x1bd200:
        value = pal_get_amcr_el0_inline();
        break;
    case 0x1bd400:
        value = pal_get_amevcntr00_el0_inline();
        break;
    case 0x1bd540:
        value = pal_get_amevcntr010_el0_inline();
        break;
    case 0x1bd560:
        value = pal_get_amevcntr011_el0_inline();
        break;
    case 0x1bd580:
        value = pal_get_amevcntr012_el0_inline();
        break;
    case 0x1bd5a0:
        value = pal_get_amevcntr013_el0_inline();
        break;
    case 0x1bd5c0:
        value = pal_get_amevcntr014_el0_inline();
        break;
    case 0x1bd5e0:
        value = pal_get_amevcntr015_el0_inline();
        break;
    case 0x1bd420:
        value = pal_get_amevcntr01_el0_inline();
        break;
    case 0x1bd440:
        value = pal_get_amevcntr02_el0_inline();
        break;
    case 0x1bd460:
        value = pal_get_amevcntr03_el0_inline();
        break;
    case 0x1bd480:
        value = pal_get_amevcntr04_el0_inline();
        break;
    case 0x1bd4a0:
        value = pal_get_amevcntr05_el0_inline();
        break;
    case 0x1bd4c0:
        value = pal_get_amevcntr06_el0_inline();
        break;
    case 0x1bd4e0:
        value = pal_get_amevcntr07_el0_inline();
        break;
    case 0x1bd500:
        value = pal_get_amevcntr08_el0_inline();
        break;
    case 0x1bd520:
        value = pal_get_amevcntr09_el0_inline();
        break;
    case 0x1bdc00:
        value = pal_get_amevcntr10_el0_inline();
        break;
    case 0x1bdd40:
        value = pal_get_amevcntr110_el0_inline();
        break;
    case 0x1bdd60:
        value = pal_get_amevcntr111_el0_inline();
        break;
    case 0x1bdd80:
        value = pal_get_amevcntr112_el0_inline();
        break;
    case 0x1bdda0:
        value = pal_get_amevcntr113_el0_inline();
        break;
    case 0x1bddc0:
        value = pal_get_amevcntr114_el0_inline();
        break;
    case 0x1bdde0:
        value = pal_get_amevcntr115_el0_inline();
        break;
    case 0x1bdc20:
        value = pal_get_amevcntr11_el0_inline();
        break;
    case 0x1bdc40:
        value = pal_get_amevcntr12_el0_inline();
        break;
    case 0x1bdc60:
        value = pal_get_amevcntr13_el0_inline();
        break;
    case 0x1bdc80:
        value = pal_get_amevcntr14_el0_inline();
        break;
    case 0x1bdca0:
        value = pal_get_amevcntr15_el0_inline();
        break;
    case 0x1bdcc0:
        value = pal_get_amevcntr16_el0_inline();
        break;
    case 0x1bdce0:
        value = pal_get_amevcntr17_el0_inline();
        break;
    case 0x1bdd00:
        value = pal_get_amevcntr18_el0_inline();
        break;
    case 0x1bdd20:
        value = pal_get_amevcntr19_el0_inline();
        break;
    case 0x1bd600:
        value = pal_get_amevtyper00_el0_inline();
        break;
    case 0x1bd740:
        value = pal_get_amevtyper010_el0_inline();
        break;
    case 0x1bd760:
        value = pal_get_amevtyper011_el0_inline();
        break;
    case 0x1bd780:
        value = pal_get_amevtyper012_el0_inline();
        break;
    case 0x1bd7a0:
        value = pal_get_amevtyper013_el0_inline();
        break;
    case 0x1bd7c0:
        value = pal_get_amevtyper014_el0_inline();
        break;
    case 0x1bd7e0:
        value = pal_get_amevtyper015_el0_inline();
        break;
    case 0x1bd620:
        value = pal_get_amevtyper01_el0_inline();
        break;
    case 0x1bd640:
        value = pal_get_amevtyper02_el0_inline();
        break;
    case 0x1bd660:
        value = pal_get_amevtyper03_el0_inline();
        break;
    case 0x1bd680:
        value = pal_get_amevtyper04_el0_inline();
        break;
    case 0x1bd6a0:
        value = pal_get_amevtyper05_el0_inline();
        break;
    case 0x1bd6c0:
        value = pal_get_amevtyper06_el0_inline();
        break;
    case 0x1bd6e0:
        value = pal_get_amevtyper07_el0_inline();
        break;
    case 0x1bd700:
        value = pal_get_amevtyper08_el0_inline();
        break;
    case 0x1bd720:
        value = pal_get_amevtyper09_el0_inline();
        break;
    case 0x1bde00:
        value = pal_get_amevtyper10_el0_inline();
        break;
    case 0x1bdf40:
        value = pal_get_amevtyper110_el0_inline();
        break;
    case 0x1bdf60:
        value = pal_get_amevtyper111_el0_inline();
        break;
    case 0x1bdf80:
        value = pal_get_amevtyper112_el0_inline();
        break;
    case 0x1bdfa0:
        value = pal_get_amevtyper113_el0_inline();
        break;
    case 0x1bdfc0:
        value = pal_get_amevtyper114_el0_inline();
        break;
    case 0x1bdfe0:
        value = pal_get_amevtyper115_el0_inline();
        break;
    case 0x1bde20:
        value = pal_get_amevtyper11_el0_inline();
        break;
    case 0x1bde40:
        value = pal_get_amevtyper12_el0_inline();
        break;
    case 0x1bde60:
        value = pal_get_amevtyper13_el0_inline();
        break;
    case 0x1bde80:
        value = pal_get_amevtyper14_el0_inline();
        break;
    case 0x1bdea0:
        value = pal_get_amevtyper15_el0_inline();
        break;
    case 0x1bdec0:
        value = pal_get_amevtyper16_el0_inline();
        break;
    case 0x1bdee0:
        value = pal_get_amevtyper17_el0_inline();
        break;
    case 0x1bdf00:
        value = pal_get_amevtyper18_el0_inline();
        break;
    case 0x1bdf20:
        value = pal_get_amevtyper19_el0_inline();
        break;
    case 0x1bd260:
        value = pal_get_amuserenr_el0_inline();
        break;
    case 0x182220:
        value = pal_get_apdakeyhi_el1_inline();
        break;
    case 0x182200:
        value = pal_get_apdakeylo_el1_inline();
        break;
    case 0x182260:
        value = pal_get_apdbkeyhi_el1_inline();
        break;
    case 0x182240:
        value = pal_get_apdbkeylo_el1_inline();
        break;
    case 0x182320:
        value = pal_get_apgakeyhi_el1_inline();
        break;
    case 0x182300:
        value = pal_get_apgakeylo_el1_inline();
        break;
    case 0x182120:
        value = pal_get_apiakeyhi_el1_inline();
        break;
    case 0x182100:
        value = pal_get_apiakeylo_el1_inline();
        break;
    case 0x182160:
        value = pal_get_apibkeyhi_el1_inline();
        break;
    case 0x182140:
        value = pal_get_apibkeylo_el1_inline();
        break;
    case 0x190040:
        value = pal_get_ccsidr2_el1_inline();
        break;
    case 0x190000:
        value = pal_get_ccsidr_el1_inline();
        break;
    case 0x190020:
        value = pal_get_clidr_el1_inline();
        break;
    case 0x1be000:
        value = pal_get_cntfrq_el0_inline();
        break;
    case 0x1ce100:
        value = pal_get_cnthctl_el2_inline();
        break;
    case 0x1ce220:
        value = pal_get_cnthp_ctl_el2_inline();
        break;
    case 0x1ce240:
        value = pal_get_cnthp_cval_el2_inline();
        break;
    case 0x1ce200:
        value = pal_get_cnthp_tval_el2_inline();
        break;
    case 0x1ce520:
        value = pal_get_cnthps_ctl_el2_inline();
        break;
    case 0x1ce540:
        value = pal_get_cnthps_cval_el2_inline();
        break;
    case 0x1ce500:
        value = pal_get_cnthps_tval_el2_inline();
        break;
    case 0x1ce320:
        value = pal_get_cnthv_ctl_el2_inline();
        break;
    case 0x1ce340:
        value = pal_get_cnthv_cval_el2_inline();
        break;
    case 0x1ce300:
        value = pal_get_cnthv_tval_el2_inline();
        break;
    case 0x1ce420:
        value = pal_get_cnthvs_ctl_el2_inline();
        break;
    case 0x1ce440:
        value = pal_get_cnthvs_cval_el2_inline();
        break;
    case 0x1ce400:
        value = pal_get_cnthvs_tval_el2_inline();
        break;
    case 0x18e100:
        value = pal_get_cntkctl_el1_inline();
        break;
    case 0x1be220:
        value = pal_get_cntp_ctl_el0_inline();
        break;
    case 0x1be240:
        value = pal_get_cntp_cval_el0_inline();
        break;
    case 0x1be200:
        value = pal_get_cntp_tval_el0_inline();
        break;
    case 0x1be020:
        value = pal_get_cntpct_el0_inline();
        break;
    case 0x1fe220:
        value = pal_get_cntps_ctl_el1_inline();
        break;
    case 0x1fe240:
        value = pal_get_cntps_cval_el1_inline();
        break;
    case 0x1fe200:
        value = pal_get_cntps_tval_el1_inline();
        break;
    case 0x1be320:
        value = pal_get_cntv_ctl_el0_inline();
        break;
    case 0x1be340:
        value = pal_get_cntv_cval_el0_inline();
        break;
    case 0x1be300:
        value = pal_get_cntv_tval_el0_inline();
        break;
    case 0x1be040:
        value = pal_get_cntvct_el0_inline();
        break;
    case 0x1ce060:
        value = pal_get_cntvoff_el2_inline();
        break;
    case 0x18d020:
        value = pal_get_contextidr_el1_inline();
        break;
    case 0x1cd020:
        value = pal_get_contextidr_el2_inline();
        break;
    case 0x181040:
        value = pal_get_cpacr_el1_inline();
        break;
    case 0x1c1140:
        value = pal_get_cptr_el2_inline();
        break;
    case 0x1e1140:
        value = pal_get_cptr_el3_inline();
        break;
    case 0x1a0000:
        value = pal_get_csselr_el1_inline();
        break;
    case 0x1b0020:
        value = pal_get_ctr_el0_inline();
        break;
    case 0x184240:
        value = pal_get_currentel_inline();
        break;
    case 0x1c3000:
        value = pal_get_dacr32_el2_inline();
        break;
    case 0x1b4220:
        value = pal_get_daif_inline();
        break;
    case 0x107ec0:
        value = pal_get_dbgauthstatus_el1_inline();
        break;
    case 0x1000a0:
        value = pal_get_dbgbcr0_el1_inline();
        break;
    case 0x100aa0:
        value = pal_get_dbgbcr10_el1_inline();
        break;
    case 0x100ba0:
        value = pal_get_dbgbcr11_el1_inline();
        break;
    case 0x100ca0:
        value = pal_get_dbgbcr12_el1_inline();
        break;
    case 0x100da0:
        value = pal_get_dbgbcr13_el1_inline();
        break;
    case 0x100ea0:
        value = pal_get_dbgbcr14_el1_inline();
        break;
    case 0x100fa0:
        value = pal_get_dbgbcr15_el1_inline();
        break;
    case 0x1001a0:
        value = pal_get_dbgbcr1_el1_inline();
        break;
    case 0x1002a0:
        value = pal_get_dbgbcr2_el1_inline();
        break;
    case 0x1003a0:
        value = pal_get_dbgbcr3_el1_inline();
        break;
    case 0x1004a0:
        value = pal_get_dbgbcr4_el1_inline();
        break;
    case 0x1005a0:
        value = pal_get_dbgbcr5_el1_inline();
        break;
    case 0x1006a0:
        value = pal_get_dbgbcr6_el1_inline();
        break;
    case 0x1007a0:
        value = pal_get_dbgbcr7_el1_inline();
        break;
    case 0x1008a0:
        value = pal_get_dbgbcr8_el1_inline();
        break;
    case 0x1009a0:
        value = pal_get_dbgbcr9_el1_inline();
        break;
    case 0x100080:
        value = pal_get_dbgbvr0_el1_inline();
        break;
    case 0x100a80:
        value = pal_get_dbgbvr10_el1_inline();
        break;
    case 0x100b80:
        value = pal_get_dbgbvr11_el1_inline();
        break;
    case 0x100c80:
        value = pal_get_dbgbvr12_el1_inline();
        break;
    case 0x100d80:
        value = pal_get_dbgbvr13_el1_inline();
        break;
    case 0x100e80:
        value = pal_get_dbgbvr14_el1_inline();
        break;
    case 0x100f80:
        value = pal_get_dbgbvr15_el1_inline();
        break;
    case 0x100180:
        value = pal_get_dbgbvr1_el1_inline();
        break;
    case 0x100280:
        value = pal_get_dbgbvr2_el1_inline();
        break;
    case 0x100380:
        value = pal_get_dbgbvr3_el1_inline();
        break;
    case 0x100480:
        value = pal_get_dbgbvr4_el1_inline();
        break;
    case 0x100580:
        value = pal_get_dbgbvr5_el1_inline();
        break;
    case 0x100680:
        value = pal_get_dbgbvr6_el1_inline();
        break;
    case 0x100780:
        value = pal_get_dbgbvr7_el1_inline();
        break;
    case 0x100880:
        value = pal_get_dbgbvr8_el1_inline();
        break;
    case 0x100980:
        value = pal_get_dbgbvr9_el1_inline();
        break;
    case 0x1079c0:
        value = pal_get_dbgclaimclr_el1_inline();
        break;
    case 0x1078c0:
        value = pal_get_dbgclaimset_el1_inline();
        break;
    case 0x130400:
        value = pal_get_dbgdtr_el0_inline();
        break;
    case 0x130500:
        value = pal_get_dbgdtrrx_el0_inline();
        break;
    case 0x101480:
        value = pal_get_dbgprcr_el1_inline();
        break;
    case 0x140700:
        value = pal_get_dbgvcr32_el2_inline();
        break;
    case 0x1000e0:
        value = pal_get_dbgwcr0_el1_inline();
        break;
    case 0x100ae0:
        value = pal_get_dbgwcr10_el1_inline();
        break;
    case 0x100be0:
        value = pal_get_dbgwcr11_el1_inline();
        break;
    case 0x100ce0:
        value = pal_get_dbgwcr12_el1_inline();
        break;
    case 0x100de0:
        value = pal_get_dbgwcr13_el1_inline();
        break;
    case 0x100ee0:
        value = pal_get_dbgwcr14_el1_inline();
        break;
    case 0x100fe0:
        value = pal_get_dbgwcr15_el1_inline();
        break;
    case 0x1001e0:
        value = pal_get_dbgwcr1_el1_inline();
        break;
    case 0x1002e0:
        value = pal_get_dbgwcr2_el1_inline();
        break;
    case 0x1003e0:
        value = pal_get_dbgwcr3_el1_inline();
        break;
    case 0x1004e0:
        value = pal_get_dbgwcr4_el1_inline();
        break;
    case 0x1005e0:
        value = pal_get_dbgwcr5_el1_inline();
        break;
    case 0x1006e0:
        value = pal_get_dbgwcr6_el1_inline();
        break;
    case 0x1007e0:
        value = pal_get_dbgwcr7_el1_inline();
        break;
    case 0x1008e0:
        value = pal_get_dbgwcr8_el1_inline();
        break;
    case 0x1009e0:
        value = pal_get_dbgwcr9_el1_inline();
        break;
    case 0x1000c0:
        value = pal_get_dbgwvr0_el1_inline();
        break;
    case 0x100ac0:
        value = pal_get_dbgwvr10_el1_inline();
        break;
    case 0x100bc0:
        value = pal_get_dbgwvr11_el1_inline();
        break;
    case 0x100cc0:
        value = pal_get_dbgwvr12_el1_inline();
        break;
    case 0x100dc0:
        value = pal_get_dbgwvr13_el1_inline();
        break;
    case 0x100ec0:
        value = pal_get_dbgwvr14_el1_inline();
        break;
    case 0x100fc0:
        value = pal_get_dbgwvr15_el1_inline();
        break;
    case 0x1001c0:
        value = pal_get_dbgwvr1_el1_inline();
        break;
    case 0x1002c0:
        value = pal_get_dbgwvr2_el1_inline();
        break;
    case 0x1003c0:
        value = pal_get_dbgwvr3_el1_inline();
        break;
    case 0x1004c0:
        value = pal_get_dbgwvr4_el1_inline();
        break;
    case 0x1005c0:
        value = pal_get_dbgwvr5_el1_inline();
        break;
    case 0x1006c0:
        value = pal_get_dbgwvr6_el1_inline();
        break;
    case 0x1007c0:
        value = pal_get_dbgwvr7_el1_inline();
        break;
    case 0x1008c0:
        value = pal_get_dbgwvr8_el1_inline();
        break;
    case 0x1009c0:
        value = pal_get_dbgwvr9_el1_inline();
        break;
    case 0x1b00e0:
        value = pal_get_dczid_el0_inline();
        break;
    case 0x18c120:
        value = pal_get_disr_el1_inline();
        break;
    case 0x1b42a0:
        value = pal_get_dit_inline();
        break;
    case 0x1b4520:
        value = pal_get_dlr_el0_inline();
        break;
    case 0x1b4500:
        value = pal_get_dspsr_el0_inline();
        break;
    case 0x184020:
        value = pal_get_elr_el1_inline();
        break;
    case 0x1c4020:
        value = pal_get_elr_el2_inline();
        break;
    case 0x1e4020:
        value = pal_get_elr_el3_inline();
        break;
    case 0x185300:
        value = pal_get_erridr_el1_inline();
        break;
    case 0x185320:
        value = pal_get_errselr_el1_inline();
        break;
    case 0x185460:
        value = pal_get_erxaddr_el1_inline();
        break;
    case 0x185420:
        value = pal_get_erxctlr_el1_inline();
        break;
    case 0x185400:
        value = pal_get_erxfr_el1_inline();
        break;
    case 0x185500:
        value = pal_get_erxmisc0_el1_inline();
        break;
    case 0x185520:
        value = pal_get_erxmisc1_el1_inline();
        break;
    case 0x185540:
        value = pal_get_erxmisc2_el1_inline();
        break;
    case 0x185560:
        value = pal_get_erxmisc3_el1_inline();
        break;
    case 0x1854c0:
        value = pal_get_erxpfgcdn_el1_inline();
        break;
    case 0x1854a0:
        value = pal_get_erxpfgctl_el1_inline();
        break;
    case 0x185480:
        value = pal_get_erxpfgf_el1_inline();
        break;
    case 0x185440:
        value = pal_get_erxstatus_el1_inline();
        break;
    case 0x185200:
        value = pal_get_esr_el1_inline();
        break;
    case 0x1c5200:
        value = pal_get_esr_el2_inline();
        break;
    case 0x1e5200:
        value = pal_get_esr_el3_inline();
        break;
    case 0x186000:
        value = pal_get_far_el1_inline();
        break;
    case 0x1c6000:
        value = pal_get_far_el2_inline();
        break;
    case 0x1e6000:
        value = pal_get_far_el3_inline();
        break;
    case 0x1b4400:
        value = pal_get_fpcr_inline();
        break;
    case 0x1c5300:
        value = pal_get_fpexc32_el2_inline();
        break;
    case 0x1b4420:
        value = pal_get_fpsr_inline();
        break;
    case 0x1810c0:
        value = pal_get_gcr_el1_inline();
        break;
    case 0x1c11e0:
        value = pal_get_hacr_el2_inline();
        break;
    case 0x1c1100:
        value = pal_get_hcr_el2_inline();
        break;
    case 0x1c6080:
        value = pal_get_hpfar_el2_inline();
        break;
    case 0x1c1160:
        value = pal_get_hstr_el2_inline();
        break;
    case 0x18c880:
        value = pal_get_icc_ap0r0_el1_inline();
        break;
    case 0x18c8a0:
        value = pal_get_icc_ap0r1_el1_inline();
        break;
    case 0x18c8c0:
        value = pal_get_icc_ap0r2_el1_inline();
        break;
    case 0x18c8e0:
        value = pal_get_icc_ap0r3_el1_inline();
        break;
    case 0x18c900:
        value = pal_get_icc_ap1r0_el1_inline();
        break;
    case 0x18c920:
        value = pal_get_icc_ap1r1_el1_inline();
        break;
    case 0x18c940:
        value = pal_get_icc_ap1r2_el1_inline();
        break;
    case 0x18c960:
        value = pal_get_icc_ap1r3_el1_inline();
        break;
    case 0x18c860:
        value = pal_get_icc_bpr0_el1_inline();
        break;
    case 0x18cc60:
        value = pal_get_icc_bpr1_el1_inline();
        break;
    case 0x18cc80:
        value = pal_get_icc_ctlr_el1_inline();
        break;
    case 0x1ecc80:
        value = pal_get_icc_ctlr_el3_inline();
        break;
    case 0x18c840:
        value = pal_get_icc_hppir0_el1_inline();
        break;
    case 0x18cc40:
        value = pal_get_icc_hppir1_el1_inline();
        break;
    case 0x18c800:
        value = pal_get_icc_iar0_el1_inline();
        break;
    case 0x18cc00:
        value = pal_get_icc_iar1_el1_inline();
        break;
    case 0x18ccc0:
        value = pal_get_icc_igrpen0_el1_inline();
        break;
    case 0x18cce0:
        value = pal_get_icc_igrpen1_el1_inline();
        break;
    case 0x1ecce0:
        value = pal_get_icc_igrpen1_el3_inline();
        break;
    case 0x184600:
        value = pal_get_icc_pmr_el1_inline();
        break;
    case 0x18cb60:
        value = pal_get_icc_rpr_el1_inline();
        break;
    case 0x18cca0:
        value = pal_get_icc_sre_el1_inline();
        break;
    case 0x1cc9a0:
        value = pal_get_icc_sre_el2_inline();
        break;
    case 0x1ecca0:
        value = pal_get_icc_sre_el3_inline();
        break;
    case 0x1cc800:
        value = pal_get_ich_ap0r0_el2_inline();
        break;
    case 0x1cc820:
        value = pal_get_ich_ap0r1_el2_inline();
        break;
    case 0x1cc840:
        value = pal_get_ich_ap0r2_el2_inline();
        break;
    case 0x1cc860:
        value = pal_get_ich_ap0r3_el2_inline();
        break;
    case 0x1cc900:
        value = pal_get_ich_ap1r0_el2_inline();
        break;
    case 0x1cc920:
        value = pal_get_ich_ap1r1_el2_inline();
        break;
    case 0x1cc940:
        value = pal_get_ich_ap1r2_el2_inline();
        break;
    case 0x1cc960:
        value = pal_get_ich_ap1r3_el2_inline();
        break;
    case 0x1ccb60:
        value = pal_get_ich_eisr_el2_inline();
        break;
    case 0x1ccba0:
        value = pal_get_ich_elrsr_el2_inline();
        break;
    case 0x1ccb00:
        value = pal_get_ich_hcr_el2_inline();
        break;
    case 0x1ccc00:
        value = pal_get_ich_lr0_el2_inline();
        break;
    case 0x1ccd40:
        value = pal_get_ich_lr10_el2_inline();
        break;
    case 0x1ccd60:
        value = pal_get_ich_lr11_el2_inline();
        break;
    case 0x1ccd80:
        value = pal_get_ich_lr12_el2_inline();
        break;
    case 0x1ccda0:
        value = pal_get_ich_lr13_el2_inline();
        break;
    case 0x1ccdc0:
        value = pal_get_ich_lr14_el2_inline();
        break;
    case 0x1ccde0:
        value = pal_get_ich_lr15_el2_inline();
        break;
    case 0x1ccc20:
        value = pal_get_ich_lr1_el2_inline();
        break;
    case 0x1ccc40:
        value = pal_get_ich_lr2_el2_inline();
        break;
    case 0x1ccc60:
        value = pal_get_ich_lr3_el2_inline();
        break;
    case 0x1ccc80:
        value = pal_get_ich_lr4_el2_inline();
        break;
    case 0x1ccca0:
        value = pal_get_ich_lr5_el2_inline();
        break;
    case 0x1cccc0:
        value = pal_get_ich_lr6_el2_inline();
        break;
    case 0x1ccce0:
        value = pal_get_ich_lr7_el2_inline();
        break;
    case 0x1ccd00:
        value = pal_get_ich_lr8_el2_inline();
        break;
    case 0x1ccd20:
        value = pal_get_ich_lr9_el2_inline();
        break;
    case 0x1ccb40:
        value = pal_get_ich_misr_el2_inline();
        break;
    case 0x1ccbe0:
        value = pal_get_ich_vmcr_el2_inline();
        break;
    case 0x1ccb20:
        value = pal_get_ich_vtr_el2_inline();
        break;
    case 0x180580:
        value = pal_get_id_aa64afr0_el1_inline();
        break;
    case 0x1805a0:
        value = pal_get_id_aa64afr1_el1_inline();
        break;
    case 0x180500:
        value = pal_get_id_aa64dfr0_el1_inline();
        break;
    case 0x180520:
        value = pal_get_id_aa64dfr1_el1_inline();
        break;
    case 0x180600:
        value = pal_get_id_aa64isar0_el1_inline();
        break;
    case 0x180620:
        value = pal_get_id_aa64isar1_el1_inline();
        break;
    case 0x180700:
        value = pal_get_id_aa64mmfr0_el1_inline();
        break;
    case 0x180720:
        value = pal_get_id_aa64mmfr1_el1_inline();
        break;
    case 0x180740:
        value = pal_get_id_aa64mmfr2_el1_inline();
        break;
    case 0x180400:
        value = pal_get_id_aa64pfr0_el1_inline();
        break;
    case 0x180420:
        value = pal_get_id_aa64pfr1_el1_inline();
        break;
    case 0x180480:
        value = pal_get_id_aa64zfr0_el1_inline();
        break;
    case 0x180160:
        value = pal_get_id_afr0_el1_inline();
        break;
    case 0x180140:
        value = pal_get_id_dfr0_el1_inline();
        break;
    case 0x180200:
        value = pal_get_id_isar0_el1_inline();
        break;
    case 0x180220:
        value = pal_get_id_isar1_el1_inline();
        break;
    case 0x180240:
        value = pal_get_id_isar2_el1_inline();
        break;
    case 0x180260:
        value = pal_get_id_isar3_el1_inline();
        break;
    case 0x180280:
        value = pal_get_id_isar4_el1_inline();
        break;
    case 0x1802a0:
        value = pal_get_id_isar5_el1_inline();
        break;
    case 0x1802e0:
        value = pal_get_id_isar6_el1_inline();
        break;
    case 0x180180:
        value = pal_get_id_mmfr0_el1_inline();
        break;
    case 0x1801a0:
        value = pal_get_id_mmfr1_el1_inline();
        break;
    case 0x1801c0:
        value = pal_get_id_mmfr2_el1_inline();
        break;
    case 0x1801e0:
        value = pal_get_id_mmfr3_el1_inline();
        break;
    case 0x1802c0:
        value = pal_get_id_mmfr4_el1_inline();
        break;
    case 0x180100:
        value = pal_get_id_pfr0_el1_inline();
        break;
    case 0x180120:
        value = pal_get_id_pfr1_el1_inline();
        break;
    case 0x180380:
        value = pal_get_id_pfr2_el1_inline();
        break;
    case 0x1c5020:
        value = pal_get_ifsr32_el2_inline();
        break;
    case 0x18c100:
        value = pal_get_isr_el1_inline();
        break;
    case 0x18a460:
        value = pal_get_lorc_el1_inline();
        break;
    case 0x18a420:
        value = pal_get_lorea_el1_inline();
        break;
    case 0x18a4e0:
        value = pal_get_lorid_el1_inline();
        break;
    case 0x18a440:
        value = pal_get_lorn_el1_inline();
        break;
    case 0x18a400:
        value = pal_get_lorsa_el1_inline();
        break;
    case 0x18a200:
        value = pal_get_mair_el1_inline();
        break;
    case 0x1ca200:
        value = pal_get_mair_el2_inline();
        break;
    case 0x1ea200:
        value = pal_get_mair_el3_inline();
        break;
    case 0x100200:
        value = pal_get_mdccint_el1_inline();
        break;
    case 0x130100:
        value = pal_get_mdccsr_el0_inline();
        break;
    case 0x1c1120:
        value = pal_get_mdcr_el2_inline();
        break;
    case 0x1e1320:
        value = pal_get_mdcr_el3_inline();
        break;
    case 0x101000:
        value = pal_get_mdrar_el1_inline();
        break;
    case 0x100240:
        value = pal_get_mdscr_el1_inline();
        break;
    case 0x180000:
        value = pal_get_midr_el1_inline();
        break;
    case 0x18a520:
        value = pal_get_mpam0_el1_inline();
        break;
    case 0x18a500:
        value = pal_get_mpam1_el1_inline();
        break;
    case 0x1ca500:
        value = pal_get_mpam2_el2_inline();
        break;
    case 0x1ea500:
        value = pal_get_mpam3_el3_inline();
        break;
    case 0x1ca400:
        value = pal_get_mpamhcr_el2_inline();
        break;
    case 0x18a480:
        value = pal_get_mpamidr_el1_inline();
        break;
    case 0x1ca600:
        value = pal_get_mpamvpm0_el2_inline();
        break;
    case 0x1ca620:
        value = pal_get_mpamvpm1_el2_inline();
        break;
    case 0x1ca640:
        value = pal_get_mpamvpm2_el2_inline();
        break;
    case 0x1ca660:
        value = pal_get_mpamvpm3_el2_inline();
        break;
    case 0x1ca680:
        value = pal_get_mpamvpm4_el2_inline();
        break;
    case 0x1ca6a0:
        value = pal_get_mpamvpm5_el2_inline();
        break;
    case 0x1ca6c0:
        value = pal_get_mpamvpm6_el2_inline();
        break;
    case 0x1ca6e0:
        value = pal_get_mpamvpm7_el2_inline();
        break;
    case 0x1ca420:
        value = pal_get_mpamvpmv_el2_inline();
        break;
    case 0x1800a0:
        value = pal_get_mpidr_el1_inline();
        break;
    case 0x180300:
        value = pal_get_mvfr0_el1_inline();
        break;
    case 0x180320:
        value = pal_get_mvfr1_el1_inline();
        break;
    case 0x180340:
        value = pal_get_mvfr2_el1_inline();
        break;
    case 0x1b4200:
        value = pal_get_nzcv_inline();
        break;
    case 0x101380:
        value = pal_get_osdlr_el1_inline();
        break;
    case 0x100040:
        value = pal_get_osdtrrx_el1_inline();
        break;
    case 0x100340:
        value = pal_get_osdtrtx_el1_inline();
        break;
    case 0x100640:
        value = pal_get_oseccr_el1_inline();
        break;
    case 0x101180:
        value = pal_get_oslsr_el1_inline();
        break;
    case 0x184260:
        value = pal_get_pan_inline();
        break;
    case 0x187400:
        value = pal_get_par_el1_inline();
        break;
    case 0x189ae0:
        value = pal_get_pmbidr_el1_inline();
        break;
    case 0x189a00:
        value = pal_get_pmblimitr_el1_inline();
        break;
    case 0x189a20:
        value = pal_get_pmbptr_el1_inline();
        break;
    case 0x189a60:
        value = pal_get_pmbsr_el1_inline();
        break;
    case 0x1befe0:
        value = pal_get_pmccfiltr_el0_inline();
        break;
    case 0x1b9d00:
        value = pal_get_pmccntr_el0_inline();
        break;
    case 0x1b9cc0:
        value = pal_get_pmceid0_el0_inline();
        break;
    case 0x1b9ce0:
        value = pal_get_pmceid1_el0_inline();
        break;
    case 0x1b9c40:
        value = pal_get_pmcntenclr_el0_inline();
        break;
    case 0x1b9c20:
        value = pal_get_pmcntenset_el0_inline();
        break;
    case 0x1b9c00:
        value = pal_get_pmcr_el0_inline();
        break;
    case 0x1be800:
        value = pal_get_pmevcntr0_el0_inline();
        break;
    case 0x1be940:
        value = pal_get_pmevcntr10_el0_inline();
        break;
    case 0x1be960:
        value = pal_get_pmevcntr11_el0_inline();
        break;
    case 0x1be980:
        value = pal_get_pmevcntr12_el0_inline();
        break;
    case 0x1be9a0:
        value = pal_get_pmevcntr13_el0_inline();
        break;
    case 0x1be9c0:
        value = pal_get_pmevcntr14_el0_inline();
        break;
    case 0x1be9e0:
        value = pal_get_pmevcntr15_el0_inline();
        break;
    case 0x1bea00:
        value = pal_get_pmevcntr16_el0_inline();
        break;
    case 0x1bea20:
        value = pal_get_pmevcntr17_el0_inline();
        break;
    case 0x1bea40:
        value = pal_get_pmevcntr18_el0_inline();
        break;
    case 0x1bea60:
        value = pal_get_pmevcntr19_el0_inline();
        break;
    case 0x1be820:
        value = pal_get_pmevcntr1_el0_inline();
        break;
    case 0x1bea80:
        value = pal_get_pmevcntr20_el0_inline();
        break;
    case 0x1beaa0:
        value = pal_get_pmevcntr21_el0_inline();
        break;
    case 0x1beac0:
        value = pal_get_pmevcntr22_el0_inline();
        break;
    case 0x1beae0:
        value = pal_get_pmevcntr23_el0_inline();
        break;
    case 0x1beb00:
        value = pal_get_pmevcntr24_el0_inline();
        break;
    case 0x1beb20:
        value = pal_get_pmevcntr25_el0_inline();
        break;
    case 0x1beb40:
        value = pal_get_pmevcntr26_el0_inline();
        break;
    case 0x1beb60:
        value = pal_get_pmevcntr27_el0_inline();
        break;
    case 0x1beb80:
        value = pal_get_pmevcntr28_el0_inline();
        break;
    case 0x1beba0:
        value = pal_get_pmevcntr29_el0_inline();
        break;
    case 0x1be840:
        value = pal_get_pmevcntr2_el0_inline();
        break;
    case 0x1bebc0:
        value = pal_get_pmevcntr30_el0_inline();
        break;
    case 0x1be860:
        value = pal_get_pmevcntr3_el0_inline();
        break;
    case 0x1be880:
        value = pal_get_pmevcntr4_el0_inline();
        break;
    case 0x1be8a0:
        value = pal_get_pmevcntr5_el0_inline();
        break;
    case 0x1be8c0:
        value = pal_get_pmevcntr6_el0_inline();
        break;
    case 0x1be8e0:
        value = pal_get_pmevcntr7_el0_inline();
        break;
    case 0x1be900:
        value = pal_get_pmevcntr8_el0_inline();
        break;
    case 0x1be920:
        value = pal_get_pmevcntr9_el0_inline();
        break;
    case 0x1bec00:
        value = pal_get_pmevtyper0_el0_inline();
        break;
    case 0x1bed40:
        value = pal_get_pmevtyper10_el0_inline();
        break;
    case 0x1bed60:
        value = pal_get_pmevtyper11_el0_inline();
        break;
    case 0x1bed80:
        value = pal_get_pmevtyper12_el0_inline();
        break;
    case 0x1beda0:
        value = pal_get_pmevtyper13_el0_inline();
        break;
    case 0x1bedc0:
        value = pal_get_pmevtyper14_el0_inline();
        break;
    case 0x1bede0:
        value = pal_get_pmevtyper15_el0_inline();
        break;
    case 0x1bee00:
        value = pal_get_pmevtyper16_el0_inline();
        break;
    case 0x1bee20:
        value = pal_get_pmevtyper17_el0_inline();
        break;
    case 0x1bee40:
        value = pal_get_pmevtyper18_el0_inline();
        break;
    case 0x1bee60:
        value = pal_get_pmevtyper19_el0_inline();
        break;
    case 0x1bec20:
        value = pal_get_pmevtyper1_el0_inline();
        break;
    case 0x1bee80:
        value = pal_get_pmevtyper20_el0_inline();
        break;
    case 0x1beea0:
        value = pal_get_pmevtyper21_el0_inline();
        break;
    case 0x1beec0:
        value = pal_get_pmevtyper22_el0_inline();
        break;
    case 0x1beee0:
        value = pal_get_pmevtyper23_el0_inline();
        break;
    case 0x1bef00:
        value = pal_get_pmevtyper24_el0_inline();
        break;
    case 0x1bef20:
        value = pal_get_pmevtyper25_el0_inline();
        break;
    case 0x1bef40:
        value = pal_get_pmevtyper26_el0_inline();
        break;
    case 0x1bef60:
        value = pal_get_pmevtyper27_el0_inline();
        break;
    case 0x1bef80:
        value = pal_get_pmevtyper28_el0_inline();
        break;
    case 0x1befa0:
        value = pal_get_pmevtyper29_el0_inline();
        break;
    case 0x1bec40:
        value = pal_get_pmevtyper2_el0_inline();
        break;
    case 0x1befc0:
        value = pal_get_pmevtyper30_el0_inline();
        break;
    case 0x1bec60:
        value = pal_get_pmevtyper3_el0_inline();
        break;
    case 0x1bec80:
        value = pal_get_pmevtyper4_el0_inline();
        break;
    case 0x1beca0:
        value = pal_get_pmevtyper5_el0_inline();
        break;
    case 0x1becc0:
        value = pal_get_pmevtyper6_el0_inline();
        break;
    case 0x1bece0:
        value = pal_get_pmevtyper7_el0_inline();
        break;
    case 0x1bed00:
        value = pal_get_pmevtyper8_el0_inline();
        break;
    case 0x1bed20:
        value = pal_get_pmevtyper9_el0_inline();
        break;
    case 0x189e40:
        value = pal_get_pmintenclr_el1_inline();
        break;
    case 0x189e20:
        value = pal_get_pmintenset_el1_inline();
        break;
    case 0x189ec0:
        value = pal_get_pmmir_el1_inline();
        break;
    case 0x1b9c60:
        value = pal_get_pmovsclr_el0_inline();
        break;
    case 0x1b9e60:
        value = pal_get_pmovsset_el0_inline();
        break;
    case 0x189900:
        value = pal_get_pmscr_el1_inline();
        break;
    case 0x1c9900:
        value = pal_get_pmscr_el2_inline();
        break;
    case 0x1b9ca0:
        value = pal_get_pmselr_el0_inline();
        break;
    case 0x1899a0:
        value = pal_get_pmsevfr_el1_inline();
        break;
    case 0x189980:
        value = pal_get_pmsfcr_el1_inline();
        break;
    case 0x189940:
        value = pal_get_pmsicr_el1_inline();
        break;
    case 0x1899e0:
        value = pal_get_pmsidr_el1_inline();
        break;
    case 0x189960:
        value = pal_get_pmsirr_el1_inline();
        break;
    case 0x1899c0:
        value = pal_get_pmslatfr_el1_inline();
        break;
    case 0x1b9e00:
        value = pal_get_pmuserenr_el0_inline();
        break;
    case 0x1b9d40:
        value = pal_get_pmxevcntr_el0_inline();
        break;
    case 0x1b9d20:
        value = pal_get_pmxevtyper_el0_inline();
        break;
    case 0x1800c0:
        value = pal_get_revidr_el1_inline();
        break;
    case 0x1810a0:
        value = pal_get_rgsr_el1_inline();
        break;
    case 0x18c040:
        value = pal_get_rmr_el1_inline();
        break;
    case 0x1cc040:
        value = pal_get_rmr_el2_inline();
        break;
    case 0x1ec040:
        value = pal_get_rmr_el3_inline();
        break;
    case 0x1b2400:
        value = pal_get_rndr_inline();
        break;
    case 0x1b2420:
        value = pal_get_rndrrs_inline();
        break;
    case 0x18c020:
        value = pal_get_rvbar_el1_inline();
        break;
    case 0x1cc020:
        value = pal_get_rvbar_el2_inline();
        break;
    case 0x1ec020:
        value = pal_get_rvbar_el3_inline();
        break;
    case 0x1e1100:
        value = pal_get_scr_el3_inline();
        break;
    case 0x181000:
        value = pal_get_sctlr_el1_inline();
        break;
    case 0x1c1000:
        value = pal_get_sctlr_el2_inline();
        break;
    case 0x1e1000:
        value = pal_get_sctlr_el3_inline();
        break;
    case 0x1bd0e0:
        value = pal_get_scxtnum_el0_inline();
        break;
    case 0x18d0e0:
        value = pal_get_scxtnum_el1_inline();
        break;
    case 0x1cd0e0:
        value = pal_get_scxtnum_el2_inline();
        break;
    case 0x1ed0e0:
        value = pal_get_scxtnum_el3_inline();
        break;
    case 0x1c1320:
        value = pal_get_sder32_el2_inline();
        break;
    case 0x1e1120:
        value = pal_get_sder32_el3_inline();
        break;
    case 0x184100:
        value = pal_get_sp_el0_inline();
        break;
    case 0x1c4100:
        value = pal_get_sp_el1_inline();
        break;
    case 0x1e4100:
        value = pal_get_sp_el2_inline();
        break;
    case 0x184200:
        value = pal_get_spsel_inline();
        break;
    case 0x1c4320:
        value = pal_get_spsr_abt_inline();
        break;
    case 0x184000:
        value = pal_get_spsr_el1_inline();
        break;
    case 0x1c4000:
        value = pal_get_spsr_el2_inline();
        break;
    case 0x1e4000:
        value = pal_get_spsr_el3_inline();
        break;
    case 0x1c4360:
        value = pal_get_spsr_fiq_inline();
        break;
    case 0x1c4300:
        value = pal_get_spsr_irq_inline();
        break;
    case 0x1c4340:
        value = pal_get_spsr_und_inline();
        break;
    case 0x1b42c0:
        value = pal_get_ssbs_inline();
        break;
    case 0x1b42e0:
        value = pal_get_tco_inline();
        break;
    case 0x182040:
        value = pal_get_tcr_el1_inline();
        break;
    case 0x1c2040:
        value = pal_get_tcr_el2_inline();
        break;
    case 0x1e2040:
        value = pal_get_tcr_el3_inline();
        break;
    case 0x186500:
        value = pal_get_tfsr_el1_inline();
        break;
    case 0x1c6500:
        value = pal_get_tfsr_el2_inline();
        break;
    case 0x1e6500:
        value = pal_get_tfsr_el3_inline();
        break;
    case 0x186620:
        value = pal_get_tfsre0_el1_inline();
        break;
    case 0x1bd040:
        value = pal_get_tpidr_el0_inline();
        break;
    case 0x18d080:
        value = pal_get_tpidr_el1_inline();
        break;
    case 0x1cd040:
        value = pal_get_tpidr_el2_inline();
        break;
    case 0x1ed040:
        value = pal_get_tpidr_el3_inline();
        break;
    case 0x1bd060:
        value = pal_get_tpidrro_el0_inline();
        break;
    case 0x181220:
        value = pal_get_trfcr_el1_inline();
        break;
    case 0x1c1220:
        value = pal_get_trfcr_el2_inline();
        break;
    case 0x182000:
        value = pal_get_ttbr0_el1_inline();
        break;
    case 0x1c2000:
        value = pal_get_ttbr0_el2_inline();
        break;
    case 0x1e2000:
        value = pal_get_ttbr0_el3_inline();
        break;
    case 0x182020:
        value = pal_get_ttbr1_el1_inline();
        break;
    case 0x1c2020:
        value = pal_get_ttbr1_el2_inline();
        break;
    case 0x184280:
        value = pal_get_uao_inline();
        break;
    case 0x18c000:
        value = pal_get_vbar_el1_inline();
        break;
    case 0x1cc000:
        value = pal_get_vbar_el2_inline();
        break;
    case 0x1ec000:
        value = pal_get_vbar_el3_inline();
        break;
    case 0x1cc120:
        value = pal_get_vdisr_el2_inline();
        break;
    case 0x1c00a0:
        value = pal_get_vmpidr_el2_inline();
        break;
    case 0x1c2200:
        value = pal_get_vncr_el2_inline();
        break;
    case 0x1c0000:
        value = pal_get_vpidr_el2_inline();
        break;
    case 0x1c5260:
        value = pal_get_vsesr_el2_inline();
        break;
    case 0x1c2640:
        value = pal_get_vstcr_el2_inline();
        break;
    case 0x1c2600:
        value = pal_get_vsttbr_el2_inline();
        break;
    case 0x1c2140:
        value = pal_get_vtcr_el2_inline();
        break;
    case 0x1c2100:
        value = pal_get_vttbr_el2_inline();
        break;
    case 0x181200:
        value = pal_get_zcr_el1_inline();
        break;
    case 0x1c1200:
        value = pal_get_zcr_el2_inline();
        break;
    case 0x1e1200:
        value = pal_get_zcr_el3_inline();
        break;
    default:
        printk(KERN_INFO "Defualt case!");
        return -EINVAL;
    }
    
    kern_ops.out.value = value;
    if (copy_to_user(user_ops, &kern_ops, sizeof(struct sysl_operands)))
        return -1;

    return 0;
}
