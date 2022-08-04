#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_write_cr2(uint64_t value)
{
    int file_desc;
    int status;
    struct write_cr2_operands write_cr2_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return;
    }

    write_cr2_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_WRITE_CR2, &write_cr2_ops)) {
        printf("[libpal] write_cr2 ioctl failed\n");
        return;
    }
}
