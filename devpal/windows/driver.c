#include <ntddk.h>
#include <wdf.h>
#include <Initguid.h>
#include "devpal_abi.h"

DRIVER_INITIALIZE DriverEntry;
DEFINE_GUID(GUID_DEVPAL_DEVINTERFACE, 0x6da124e8, 0x2b25, 0xefd8, 0x45, 0xc3, 0xab, 0xe6, 0xf0, 0xd2, 0x79, 0x90);

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
    _In_ WDFQUEUE Queue,
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength,
    _In_ ULONG IoControlCode
)
{
    UNREFERENCED_PARAMETER(Queue);

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
