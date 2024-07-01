#include <Servo.h>

// Set output pins
const int TriggerPin = 11;
const int EchoPin = 12;
const int motorSignalPin = 9;

// Starting location
const int startAngle = 90;

// Rotation limits
const int minimumAngle = 6;
const int maximumAngle = 175;

// Speed control (delay between angle changes in milliseconds)
const int angleChangeDelay = 50;  // Increase this value to slow down the servo

// Library class instance
Servo motor;

void setup(void) 
{
    pinMode(TriggerPin, OUTPUT);
    pinMode(EchoPin, INPUT);
    motor.attach(motorSignalPin);
    Serial.begin(115200);
}

void loop(void)
{
    static int currentAngle = startAngle;
    static int motorRotateAmount = 1; // Change in angle per cycle

    // Move motor
    motor.write(currentAngle);
    delay(angleChangeDelay); // Adjusted delay to slow down servo

    // Calculate the distance from the sensor and output the angle and distance via serial
    SerialOutput(currentAngle, CalculateDistance());

    // Update motor location
    currentAngle += motorRotateAmount;

    // If the motor has reached the limits, change direction
    if (currentAngle <= minimumAngle || currentAngle >= maximumAngle) 
    {
        motorRotateAmount = -motorRotateAmount;
    }
}

int CalculateDistance(void)
{
    // Trigger the ultrasonic sensor and measure the duration of the echo
    digitalWrite(TriggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(TriggerPin, LOW);
    long duration = pulseIn(EchoPin, HIGH);

    // Convert duration to distance (in cm)
    float distance = duration * 0.017F;
    return int(distance);
}

void SerialOutput(const int angle, const int distance)
{
    // Output angle and distance via serial
    Serial.println(String(angle) + "," + String(distance));
}