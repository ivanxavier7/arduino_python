py -m venv virtualEnv
source virtualEnv/Scripts/activate
Cntrl + Shift + P -> Python: Select Interpreter -> virtualEnv Interpreter


Requirements:
pyserial
vpython


Docs:
https://www.arduino.cc/reference/tr/


VSCode

Extensions:
* Arduino
* Arduino-Snippets
* C/C++
* VS Code Arduino API
* Python
* Python Extension Pack
* Python Path
* Python Snippets

Bottom bar:
AVR ISP
Arduino UNO
COM3

New Window:
1. Cntrl + k
2. o

arduino.json:
{
    "port": "COM3",
    "board": "arduino:avr:uno",
    "programmer": "avrisp",
    "sketch": "Arduino\\Arduino.ino",
    "output": "build"
}

Circuits:

2_Voltemeter/Arduino/Arduino.ino:
https://www.circuits-diy.com/how-to-use-a-potentiometer-arduino-tutorial/


Needed:
Gyroscope
Accelerometer
Relays ( Not sure )


https://www.youtube.com/watch?v=KMhbV1p3MWk


Optimize:
https://docs.arduino.cc/retired/hacking/software/PortManipulation/
https://www.youtube.com/playlist?list=PLKL6KBeCnI3X7cb1sznYuyScUesOxS-kL
https://www.youtube.com/watch?v=6q1yEb_ukw8


Use registers like assembly to save memory and be more efficient.