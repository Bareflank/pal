#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_wrmsr_checked(uint32_t address, uint64_t value, uint64_t * error_out)
{
    int file_desc;
    int status;
    struct wrmsr_operands wrmsr_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        if(error_out) *error_out = -1;
        return;
    }

    wrmsr_ops.in.address = address;
    wrmsr_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_WRMSR, &wrmsr_ops)) {
        printf("[libpal] wrmsr ioctl failed\n");
        if(error_out) *error_out = -1;
        return;
    }
}

void pal_execute_wrmsr(uint32_t address, uint64_t value)
{ pal_execute_wrmsr_checked(address, value, NULL); }
