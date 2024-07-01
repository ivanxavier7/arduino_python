* Mode 0 - HC-SR04 (Default)
    Emulates other sensor
* Mode 1 - Automatic Serial Data
    Calculates distance itself
* Mode 2 - Serial Data
* Mode 3 - Automatic Trigger
    Needs 200k Resistor, Signal every 200ms and needs manual calculation
* Mode 4 - Automatic Trigger Low-power
    Needs 360k Resistor, Signal every 200ms and needs manual calculation
* Mode 5 - (Needs 470k Resistor)
    1.5meters switch, boolean


Serial Data:
    4bytes

    1. Byte x00 - Header
        Always FF
    2. Byte x01 - High signal distance
    3. Byte x02 - Low signal distance
    4. Byte x03 - Checksum
        Bottom eight bits from Sum(x00 + x01 +x03) - For validation