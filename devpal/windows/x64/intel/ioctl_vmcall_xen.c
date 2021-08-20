#include <ntddk.h>
#include <wdf.h>
#include "devpal_abi_x64_intel.h"

UINT64 pal_execute_vmcall_xen(UINT64 rax, UINT64 rdi, UINT64 rsi, UINT64 rdx, UINT64 r10, UINT64 r8, UINT64 r9);

void handle_devpal_ioctl_vmcall_xen(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength
)
{
    NTSTATUS status;
    struct vmcall_xen_operands* operands_in;
    struct vmcall_xen_operands* operands_out;
    size_t in_buffer_size = 0;
    size_t out_buffer_size = 0;

    status = WdfRequestRetrieveInputBuffer(Request, InputBufferLength, &operands_in, &in_buffer_size);
    if (!NT_SUCCESS(status) || in_buffer_size < sizeof(struct vmcall_xen_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    status = WdfRequestRetrieveOutputBuffer(Request, OutputBufferLength, &operands_out, &out_buffer_size);
    if (!NT_SUCCESS(status) || out_buffer_size < sizeof(struct vmcall_xen_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    WdfRequestSetInformation(Request, out_buffer_size);
    RtlSecureZeroMemory(operands_out, out_buffer_size);
    RtlCopyMemory(operands_out, operands_in, sizeof(struct vmcall_xen_operands));

    operands_out->out.rax = pal_execute_vmcall_xen(operands_in->in.rax, operands_in->in.rdi, operands_in->in.rsi, operands_in->in.rdx, operands_in->in.r10, operands_in->in.r8, operands_in->in.r9);

    WdfRequestComplete(Request, STATUS_SUCCESS);
}
