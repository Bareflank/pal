#include <windows.h>
#include <initguid.h>
#include <SetupAPI.h>

DEFINE_GUID(GUID_DEVPAL_DEVINTERFACE, 0x6da124e8, 0x2b25, 0xefd8, 0x45, 0xc3, 0xab, 0xe6, 0xf0, 0xd2, 0x79, 0x90);

HANDLE get_devpal_handle(void)
{
    BOOL ret;
    HANDLE info;
    DWORD const flags = DIGCF_DEVICEINTERFACE | DIGCF_PRESENT;
    SP_INTERFACE_DEVICE_DETAIL_DATA* dev_data;
    SP_DEVINFO_DATA dev_info;
    dev_info.cbSize = sizeof(SP_DEVINFO_DATA);
    DWORD size;
    HANDLE device_handle;

    SP_INTERFACE_DEVICE_DATA if_info;
    if_info.cbSize = sizeof(SP_INTERFACE_DEVICE_DATA);

    info = SetupDiGetClassDevsW(&GUID_DEVPAL_DEVINTERFACE, NULL, NULL, flags);
    if (INVALID_HANDLE_VALUE == info) {
        printf("SetupDiGetClassDevs failed\n");
        return INVALID_HANDLE_VALUE;
    }

    ret = SetupDiEnumDeviceInfo(info, 0, &dev_info);
    if (ret == FALSE) {
        printf("SetupDiEnumDeviceInfo failed: %d\n", GetLastError());
        return INVALID_HANDLE_VALUE;
    }

    ret = SetupDiEnumDeviceInterfaces(info, &dev_info, &GUID_DEVPAL_DEVINTERFACE, 0, &if_info);
    if (ret == FALSE) {
        printf("SetupDiEnumDeviceInterfaces failed\n");
        return INVALID_HANDLE_VALUE;
    }

    ret = SetupDiGetDeviceInterfaceDetailA(info, &if_info, NULL, 0, &size, NULL);
    if (ret == TRUE) {
        printf("SetupDiGetDeviceInterfaceDetailA failed\n");
        return INVALID_HANDLE_VALUE;
    }

    if (GetLastError() != ERROR_INSUFFICIENT_BUFFER) {
        printf("SetupDiGetDeviceInterfaceDetailA failed\n");
        return INVALID_HANDLE_VALUE;
    }

    dev_data = (SP_INTERFACE_DEVICE_DETAIL_DATA*)(malloc(size));
    if (NULL == dev_data) {
        printf("malloc failed in ioctl\n");
        return INVALID_HANDLE_VALUE;
    }

    dev_data->cbSize = sizeof(SP_INTERFACE_DEVICE_DETAIL_DATA);

    ret = SetupDiGetDeviceInterfaceDetail(info, &if_info, dev_data, size, NULL, NULL);
    if (ret == FALSE) {
        printf("SetupDiGetDeviceInterfaceDetail failed: error %d\n", GetLastError());
        return INVALID_HANDLE_VALUE;
    }

    device_handle = CreateFile(
        dev_data->DevicePath,
        GENERIC_READ | GENERIC_WRITE,
        0,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    if (NULL == device_handle) {
        printf("ioctl CreateFile failed\n");
        return INVALID_HANDLE_VALUE;
    }

    return device_handle;
}
