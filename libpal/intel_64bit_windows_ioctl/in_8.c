#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

uint8_t pal_execute_in_8(uint32_t address)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct in_8_operands in_8_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return 0xFF;
    }

    in_8_ops.in.address = address;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_IN_8,
        &in_8_ops, sizeof(struct in_8_operands), &in_8_ops, sizeof(struct in_8_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return 0xFF;
    }

    CloseHandle(device_handle);

    return in_8_ops.out.value;
}
