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