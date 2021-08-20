#include <ntddk.h>
#include <wdf.h>
#include "devpal_abi_x64.h"

UINT32 pal_execute_in_32(UINT16 address);

void handle_devpal_ioctl_in_32(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength
)
{
    NTSTATUS status;
    struct in_32_operands* operands_in;
    struct in_32_operands* operands_out;
    size_t in_buffer_size = 0;
    size_t out_buffer_size = 0;

    status = WdfRequestRetrieveInputBuffer(Request, InputBufferLength, &operands_in, &in_buffer_size);
    if (!NT_SUCCESS(status) || in_buffer_size < sizeof(struct in_32_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    status = WdfRequestRetrieveOutputBuffer(Request, OutputBufferLength, &operands_out, &out_buffer_size);
    if (!NT_SUCCESS(status) || out_buffer_size < sizeof(struct in_32_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    WdfRequestSetInformation(Request, out_buffer_size);
    RtlSecureZeroMemory(operands_out, out_buffer_size);
    RtlCopyMemory(operands_out, operands_in, sizeof(struct in_32_operands));

    operands_out->out.value = pal_execute_in_32(operands_in->in.address);

    WdfRequestComplete(Request, STATUS_SUCCESS);
}
