# IoT ESP32 - Remote Control with Alexa

# Introduction
In the packages folder, you will find the different modules that make this project.
- **Alexa:** JSON of Alexa APP for custom Skill
- **esp32:** Micropython program that goes into esp32
- **lambda:** AWS Lambda Function that connects Alexa, with IoT Core Shadow Broker (MQTT)


## ESP32 
Components needed on ESP32:

- IR TX
- IR RX
- LCD Screen
- Temperature Sensor
- Humidity Sensor
- Buzzer (Pasive)

## What it does?
ESP32 connects all sensors, in the first step is possible to record Remote Control commands into the 
Memory of the ESP32. They will be used to be replicated as a smart remote control.
ESP32 will be constantly sensing the temperature and humidity.
ESP32 will be showing in an interval of time, 3 different values on the LCD Screen:

- Temperature
- Humidity
- Last command sent through MQTT (Temperature set)

ESP32 receives the command through MQTT, which is updated by Alexa with voice command.
AWS Lambda Function is used to connect Amazon Alexia with MQTT Broker AWS IoT Core.
ESP32 will send the desired command with IR.

## Latest Features
**Auto-mode** is one of the latest features.
A temperature range can be defined. By default it is set by a minimum of 24°C and maximum of 29°C.
Once the auto-mode is on, the AC will turn off when reaching the 24 °C. In the Other hand, when reached 
29°C, it will turn on again.
In a 40 m2 apartment, it took 40 minutes the first time to cool down. After the first time, it would take 
15 minutes to get from 24°C to 29°C, and 7 minutes to cool down from 29°C to 24°C.

By this, we can save energy up to 70%. The temperature won't stay all time constant, but it will be in a 
range that our body or personal comfort allows.

## Review

**Last review:** August 18th 2023
