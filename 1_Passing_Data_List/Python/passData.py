import time
import serial

arduinoData=serial.Serial('com3', 115200)
time.sleep(1)

while 1:
    while (arduinoData.inWaiting()==0):                     # Wait here until there is data
        pass
    
    dataPacket = arduinoString=arduinoData.readline()       # Read the line of text from the serial port
    
    dataPacket = dataPacket.decode('utf-8')                 # Decode the text from binary to text
    dataPacket = dataPacket.rstrip()                        # Remove the extra characters at the end of the text

    print(dataPacket)                                       # Print the value of voltage