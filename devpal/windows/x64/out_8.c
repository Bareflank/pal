#include <ntddk.h>
#include <wdf.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/out_8.h"

void handle_devpal_ioctl_out_8(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength
)
{
    UNREFERENCED_PARAMETER(OutputBufferLength);

    NTSTATUS status;
    struct out_8_operands* operands_in;
    size_t in_buffer_size = 0;

    status = WdfRequestRetrieveInputBuffer(Request, InputBufferLength, &operands_in, &in_buffer_size);
    if (!NT_SUCCESS(status) || in_buffer_size < sizeof(struct out_8_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    pal_execute_out_8(operands_in->in.address, operands_in->in.value);

    WdfRequestComplete(Request, STATUS_SUCCESS);
}
