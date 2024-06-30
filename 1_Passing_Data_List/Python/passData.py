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
    dataPacket = dataPacket.split(';')                      # Split the text into a list of strings
    
    # Convert the list of strings into a list of integers
    dataPacket = [int(dataPacket[0]), int(dataPacket[1]), int(dataPacket[2])]
    
    x = dataPacket[0]                                       # Assign the first integer to x
    y = dataPacket[1]                                       # Assign the second integer to y
    z = dataPacket[2]                                       # Assign the third integer to z
    
    print("x: %d; y: %d; z: %d" % (x, y, z))               # Print the values of x, y, and z
    #print(' '.join(map(str, dataPacket)))                   # Print the list of integers