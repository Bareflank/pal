#include <ntddk.h>
#include <wdf.h>
#include <Initguid.h>
#include "devpal_abi.h"

DRIVER_INITIALIZE DriverEntry;
DEFINE_GUID(GUID_DEVPAL_DEVINTERFACE, 0x6da124e8, 0x2b25, 0xefd8, 0x45, 0xc3, 0xab, 0xe6, 0xf0, 0xd2, 0x79, 0x90);

VOID
devpalEvtIoDeviceControl(
    _In_ WDFQUEUE Queue,
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength,
    _In_ ULONG IoControlCode
);

VOID
devpalEvtIoStop(
    _In_ WDFQUEUE Queue,
    _In_ WDFREQUEST Request,
    _In_ ULONG ActionFlags
)
{
    UNREFERENCED_PARAMETER(Queue);
    UNREFERENCED_PARAMETER(ActionFlags);

    WdfRequestComplete(Request, STATUS_SUCCESS);
    return;
}

NTSTATUS
devpalEvtDeviceAdd(
    _In_    WDFDRIVER       Driver,
    _Inout_ PWDFDEVICE_INIT DeviceInit
)
{
    UNREFERENCED_PARAMETER(Driver);

    NTSTATUS status;
    WDFDEVICE device;
    WDFQUEUE queue;
    WDF_IO_QUEUE_CONFIG queueConfig;

    PAGED_CODE();

    status = WdfDeviceCreate(&DeviceInit, WDF_NO_OBJECT_ATTRIBUTES, &device);
    if (!NT_SUCCESS(status)) {
        return status;
    }

    status = WdfDeviceCreateDeviceInterface(device, &GUID_DEVPAL_DEVINTERFACE, NULL);
    if (!NT_SUCCESS(status)) {
        return status;
    }

    WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE(&queueConfig, WdfIoQueueDispatchParallel);
    queueConfig.EvtIoDeviceControl = devpalEvtIoDeviceControl;
    queueConfig.EvtIoStop = devpalEvtIoStop;

    status = WdfIoQueueCreate(device, &queueConfig, WDF_NO_OBJECT_ATTRIBUTES, &queue);
    if (!NT_SUCCESS(status)) {
        return status;
    }

    return status;
}

NTSTATUS
DriverEntry(
    _In_ PDRIVER_OBJECT     DriverObject,
    _In_ PUNICODE_STRING    RegistryPath
)
{
    NTSTATUS status = STATUS_SUCCESS;
    WDF_DRIVER_CONFIG config;

    WDF_DRIVER_CONFIG_INIT(&config, devpalEvtDeviceAdd);
    status = WdfDriverCreate(DriverObject, RegistryPath, WDF_NO_OBJECT_ATTRIBUTES, &config, WDF_NO_HANDLE);

    return status;
}
