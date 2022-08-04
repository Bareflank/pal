#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_rdtsc(void)
{
    int file_desc;
    int status;
    struct rdtsc_operands rdtsc_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    if(ioctl(file_desc, DEVPAL_EXECUTE_RDTSC, &rdtsc_ops)) {
        printf("[libpal] rdtsc ioctl failed\n");
        return -1;
    }

    return rdtsc_ops.out.value;
}
