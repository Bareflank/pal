#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

uint32_t pal_execute_in_32(uint32_t address)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct in_32_operands in_32_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFF;
    }

    in_32_ops.in.address = address;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_IN_32,
        &in_32_ops, sizeof(struct in_32_operands), &in_32_ops, sizeof(struct in_32_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFF;
    }

    CloseHandle(device_handle);

    return in_32_ops.out.value;
}
