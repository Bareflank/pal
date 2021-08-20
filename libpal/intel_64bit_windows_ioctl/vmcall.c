#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

void pal_execute_vmcall(void)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return;
    }

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_VMCALL,
        NULL, 0, NULL, 0,
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return;
    }

    CloseHandle(device_handle);
}