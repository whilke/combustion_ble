BASE_UUID_FORMAT = "0000{}-0000-1000-8000-00805f9b34fb"

DEVICE_INFO_SERVICE = 0x180A
PROBE_STATUS_SERVICE = "00000100-CAAB-3792-3D44-97AE51C1407A".lower()


STATE_COMMAND = b"\xEF\x01\x77"
DEVICE_STATUS_CHARACTERISTIC = "00000101-CAAB-3792-3D44-97AE51C1407A".lower()
UART_RX_CHARACTERISTIC = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E".lower()
UART_TX_CHARACTERISTIC = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E".lower()
SERIAL_NUMBER_CHARACTERISTIC = BASE_UUID_FORMAT.format("2a25")
FW_VERSION_CHARACTERISTIC = BASE_UUID_FORMAT.format("2a26")
HW_VERSION_CHARACTERISTIC = BASE_UUID_FORMAT.format("2a27")
MODEL_NUMBER_CHARACTERISTIC = BASE_UUID_FORMAT.format("2a24")

BT_MANUFACTURER_ID = 2503
