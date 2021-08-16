#include <windows.h>
#include <winioctl.h>
#include <initguid.h>
#include <stdio.h>
#include <devpal_abi.h>

HANDLE get_devpal_handle(void);

typedef struct pal_cpuid_return_values {
    UINT32 eax;
    UINT32 ebx;
    UINT32 ecx;
    UINT32 edx;
} pal_cpuid_return_values;

struct pal_cpuid_return_values pal_execute_cpuid(uint32_t leaf, uint32_t subleaf)
{
    HANDLE device_handle;
    BOOL ioctl_success;
    DWORD ioctl_bytes_out;
    struct cpuid_operands cpuid_ops = { 0 };
    struct pal_cpuid_return_values outputs = {.eax=0xFFFFFFFF, .ebx=0xFFFFFFFF, .ecx=0xFFFFFFFF, .edx=0xFFFFFFFF};

    device_handle = get_devpal_handle();
    if (INVALID_HANDLE_VALUE == device_handle) {
        printf("Failed to open handle to the devpal device, error: %d\n", GetLastError());
        return outputs;
    }

    cpuid_ops.in.leaf = leaf;
    cpuid_ops.in.subleaf = subleaf;

    ioctl_success = DeviceIoControl(device_handle, DEVPAL_EXECUTE_CPUID,
        &cpuid_ops, sizeof(struct cpuid_operands), &cpuid_ops, sizeof(struct cpuid_operands),
        &ioctl_bytes_out, NULL);

    if (!ioctl_success) {
        printf("Failed to execute ioctl to devpal device, error: %d\n", GetLastError());
        return outputs;
    }

    CloseHandle(device_handle);

    outputs.eax = cpuid_ops.out.eax;
    outputs.ebx = cpuid_ops.out.ebx;
    outputs.ecx = cpuid_ops.out.ecx;
    outputs.edx = cpuid_ops.out.edx;

    return outputs;
}
