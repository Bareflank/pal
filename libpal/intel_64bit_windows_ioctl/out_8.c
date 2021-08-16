#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

void pal_execute_out_8(uint32_t address, uint8_t value)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct out_8_operands out_8_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return;
    }

    out_8_ops.in.address = address;
    out_8_ops.in.value = value;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_OUT_8,
        &out_8_ops, sizeof(struct out_8_operands), &out_8_ops, sizeof(struct out_8_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return;
    }

    CloseHandle(device_handle);
}
