# TAREA 3: Diccionario de registros Modbus
# Medidor ultrasónico TUF-2000M

modbus_tuf = {
    "0x01": {
        "unit": "m3/h",
        "multiplier": 0.1,
        "modbus_type": "Holding"
    },
    "0x03": {
        "unit": "m/s",
        "multiplier": 0.01,
        "modbus_type": "Input"
    },
    "0x09": {
        "unit": "m3",
        "multiplier": 1.0,
        "modbus_type": "Holding"
    }
}
