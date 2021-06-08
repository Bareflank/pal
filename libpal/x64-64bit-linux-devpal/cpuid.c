#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

typedef struct pal_cpuid_return_values {
    uint32_t eax;
    uint32_t ebx;
    uint32_t ecx;
    uint32_t edx;
} pal_cpuid_return_values;

struct pal_cpuid_return_values pal_execute_cpuid(uint32_t leaf, uint32_t subleaf)
{
    int file_desc;
    int status;
    struct cpuid_operands cpuid_ops = {0};
    struct pal_cpuid_return_values values = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return values;
    }

    cpuid_ops.in.leaf = leaf;
    cpuid_ops.in.subleaf = subleaf;

    if(ioctl(file_desc, DEVPAL_EXECUTE_CPUID, &cpuid_ops)) {
        printf("[libpal] cpuid ioctl failed\n");
        return values;
    }

    values.eax = cpuid_ops.out.eax;
    values.ebx = cpuid_ops.out.ebx;
    values.ecx = cpuid_ops.out.ecx;
    values.edx = cpuid_ops.out.edx;
    return values;
}
