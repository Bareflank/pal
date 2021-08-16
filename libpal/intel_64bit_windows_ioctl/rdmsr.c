#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

uint64_t pal_execute_rdmsr(uint32_t address)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct rdmsr_operands rdmsr_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFFFFFFFFFF;
    }

    rdmsr_ops.in.address = address;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_RDMSR,
        &rdmsr_ops, sizeof(struct rdmsr_operands), &rdmsr_ops, sizeof(struct rdmsr_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFFFFFFFFFF;
    }

    CloseHandle(device_handle);

    return rdmsr_ops.out.value;
}
