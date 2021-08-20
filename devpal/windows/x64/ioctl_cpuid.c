#include <ntddk.h>
#include <wdf.h>
#include "devpal_abi_x64.h"

typedef struct pal_cpuid_return_values {
	UINT32 eax;
	UINT32 ebx;
	UINT32 ecx;
	UINT32 edx;
} pal_cpuid_return_values;

pal_cpuid_return_values pal_execute_cpuid(UINT32 leaf, UINT32 subleaf);

void handle_devpal_ioctl_cpuid(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength
)
{
    NTSTATUS status;
    struct cpuid_operands* operands_in;
    struct cpuid_operands* operands_out;
    size_t in_buffer_size = 0;
    size_t out_buffer_size = 0;
    pal_cpuid_return_values values;

    status = WdfRequestRetrieveInputBuffer(Request, InputBufferLength, &operands_in, &in_buffer_size);
    if (!NT_SUCCESS(status) || in_buffer_size < sizeof(struct cpuid_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    status = WdfRequestRetrieveOutputBuffer(Request, OutputBufferLength, &operands_out, &out_buffer_size);
    if (!NT_SUCCESS(status) || out_buffer_size < sizeof(struct cpuid_operands)) {
        WdfRequestComplete(Request, STATUS_ACCESS_DENIED);
        return;
    }

    WdfRequestSetInformation(Request, out_buffer_size);
    RtlSecureZeroMemory(operands_out, out_buffer_size);
    RtlCopyMemory(operands_out, operands_in, sizeof(struct cpuid_operands));

    values = pal_execute_cpuid(operands_in->in.leaf, operands_in->in.subleaf);

    operands_out->out.eax = values.eax;
    operands_out->out.ebx = values.ebx;
    operands_out->out.ecx = values.ecx;
    operands_out->out.edx = values.edx;

    WdfRequestComplete(Request, STATUS_SUCCESS);
}
