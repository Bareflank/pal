#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

void pal_execute_out_32(uint32_t address, uint32_t value)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct out_32_operands out_32_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return;
    }

    out_32_ops.in.address = address;
    out_32_ops.in.value = value;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_OUT_32,
        &out_32_ops, sizeof(struct out_32_operands), &out_32_ops, sizeof(struct out_32_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return;
    }

    CloseHandle(device_handle);
}
