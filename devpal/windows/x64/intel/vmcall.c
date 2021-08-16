#include <ntddk.h>
#include <wdf.h>
#include "pal/instruction/vmcall.h"

void handle_devpal_ioctl_vmcall(
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength
)
{
    UNREFERENCED_PARAMETER(OutputBufferLength);
    UNREFERENCED_PARAMETER(InputBufferLength);

    pal_execute_vmcall();
    WdfRequestComplete(Request, STATUS_SUCCESS);
}
