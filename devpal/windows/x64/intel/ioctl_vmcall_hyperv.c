#include <ntddk.h>
#include <wdf.h>
#include "devpal_abi_x64_intel.h"

UINT64 pal_execute_vmcall_hyperv(UINT64 rcx, UINT64 rdx);

void handle_devpal_ioctl_vmcall_hyperv(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength
)
{
    NTSTATUS status;
    struct vmcall_hyperv_operands* operands_in;
    struct vmcall_hyperv_operands* operands_out;
    size_t in_buffer_size = 0;
    size_t out_buffer_size = 0;

    status = WdfRequestRetrieveInputBuffer(Request, InputBufferLength, &operands_in, &in_buffer_size);
    if (!NT_SUCCESS(status) || in_buffer_size < sizeof(struct vmcall_hyperv_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    status = WdfRequestRetrieveOutputBuffer(Request, OutputBufferLength, &operands_out, &out_buffer_size);
    if (!NT_SUCCESS(status) || out_buffer_size < sizeof(struct vmcall_hyperv_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    WdfRequestSetInformation(Request, out_buffer_size);
    RtlSecureZeroMemory(operands_out, out_buffer_size);
    RtlCopyMemory(operands_out, operands_in, sizeof(struct vmcall_hyperv_operands));

    operands_out->out.r8 = pal_execute_vmcall_hyperv(operands_in->in.rcx, operands_in->in.rdx);

    WdfRequestComplete(Request, STATUS_SUCCESS);
}
