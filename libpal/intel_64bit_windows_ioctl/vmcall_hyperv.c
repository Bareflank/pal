#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

uint64_t pal_execute_vmcall_hyperv(uint64_t rcx, uint64_t rdx)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct vmcall_hyperv_operands vmcall_hyperv_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFFFFFFFFFF;
    }

    vmcall_hyperv_ops.in.rcx = rcx;
    vmcall_hyperv_ops.in.rdx = rdx;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_VMCALL_HYPERV,
        &vmcall_hyperv_ops, sizeof(struct vmcall_hyperv_operands), &vmcall_hyperv_ops, sizeof(struct vmcall_hyperv_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFFFFFFFFFF;
    }

    CloseHandle(device_handle);

    return vmcall_hyperv_ops.out.r8;
}
