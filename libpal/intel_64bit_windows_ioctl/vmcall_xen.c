#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

uint64_t pal_execute_vmcall_xen(uint64_t rax, uint64_t rdi, uint64_t rsi, uint64_t rdx, uint64_t r10, uint64_t r8, uint64_t r9)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct vmcall_xen_operands vmcall_xen_ops = { 0 };

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFFFFFFFFFF;
    }

    vmcall_xen_ops.in.rax = rax;
    vmcall_xen_ops.in.rdi = rdi;
    vmcall_xen_ops.in.rsi = rsi;
    vmcall_xen_ops.in.rdx = rdx;
    vmcall_xen_ops.in.r10 = r10;
    vmcall_xen_ops.in.r8 = r8;
    vmcall_xen_ops.in.r9 = r9;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_VMCALL_XEN,
        &vmcall_xen_ops, sizeof(struct vmcall_xen_operands), &vmcall_xen_ops, sizeof(struct vmcall_xen_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return 0xFFFFFFFFFFFFFFFF;
    }

    CloseHandle(device_handle);

    return vmcall_xen_ops.out.rax;
}
