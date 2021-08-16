#include <ntddk.h>
#include <wdf.h>
#include "devpal_abi.h"

//x86-64 Generic
void handle_devpal_ioctl_cpuid(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_in_8(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_in_16(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_in_32(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_out_8(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_out_16(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_out_32(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_rdmsr(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_read_mem8(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_read_mem16(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_read_mem32(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_read_mem64(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_write_mem8(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_write_mem16(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_write_mem32(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_write_mem64(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_wrmsr(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);

// Intel Specific
void handle_devpal_ioctl_vmcall(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_vmcall_kvm(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);
void handle_devpal_ioctl_vmcall_xen(WDFREQUEST Request, size_t OutputBufferLength, size_t InputBufferLength);


VOID
devpalEvtIoDeviceControl(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength,
    _In_ ULONG IoControlCode
)
{
    switch (IoControlCode) {
    case DEVPAL_EXECUTE_CPUID: {
        handle_devpal_ioctl_cpuid(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_IN_8: {
        handle_devpal_ioctl_in_8(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_IN_16: {
        handle_devpal_ioctl_in_16(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_IN_32: {
        handle_devpal_ioctl_in_32(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_OUT_8: {
        handle_devpal_ioctl_out_8(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_OUT_16: {
        handle_devpal_ioctl_out_16(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_OUT_32: {
        handle_devpal_ioctl_out_32(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_RDMSR: {
        handle_devpal_ioctl_rdmsr(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_READ_MEM8: {
        handle_devpal_ioctl_read_mem8(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_READ_MEM16: {
        handle_devpal_ioctl_read_mem16(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_READ_MEM32: {
        handle_devpal_ioctl_read_mem32(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_READ_MEM64: {
        handle_devpal_ioctl_read_mem64(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_WRITE_MEM8: {
        handle_devpal_ioctl_write_mem8(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_WRITE_MEM16: {
        handle_devpal_ioctl_write_mem16(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_WRITE_MEM32: {
        handle_devpal_ioctl_write_mem32(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_WRITE_MEM64: {
        handle_devpal_ioctl_write_mem64(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_VMCALL: {
        handle_devpal_ioctl_vmcall(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_VMCALL_KVM: {
        handle_devpal_ioctl_vmcall_kvm(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_VMCALL_XEN: {
        handle_devpal_ioctl_vmcall_xen(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    case DEVPAL_EXECUTE_WRMSR: {
        handle_devpal_ioctl_wrmsr(Request, InputBufferLength, OutputBufferLength);
        break;
    }
    default: {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
    }
    }
}
