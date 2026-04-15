"""
2a.
no connections

code:
void setup(){
    pinMode(13,OUTPUT);
}

void loop(){
    digitalWrite(13,HIGH);
    delay(1000);
    digitalWrite(13,LOW);
    delay(1000);
}

2b.
pin 13 --> resistor ---> anode ---> cathode ---> gnd

code:
void setup(){
    pinMode(13,OUTPUT);
}

void loop(){
    digitalWrite(13,HIGH);
    delay(1000);
    digitalWrite(13,LOW);
    delay(1000);
}

2c.
pin 9~ --> resistor -->anode -->cathode --> gnd

int led_pin = 9
void setup(){
    pinMode(led_pin,OUTPUT);
}

void loop(){
    for (int i = 0; i<255; i++){
        analogWrite(led_pin,i);
        delay(5);
    }
    for (int i = 255; i>0; i++){
        analogWrite(led_pin,i);
        delay(5);
    }
}

2d.
Pin 9~ → Resistor → LED (Anode / long leg)
LED (Cathode / short leg) → GND

Left pin  → 5V
Middle pin → A0
Right pin → GND

code:
int led_pin = 9;
int pot_pin = A0;
int output;
int led_value;

void setup(){
    pinMode(led_pin,OUTPUT);
}

void loop(){
    output = analogRead(pot_pin);
    led_value = map(output,0,1023,0,255);
    analogWrite(led_pin,led_value);
}
"""

"""
----------------------------------------------------------------------------------------------------------------------
"""

"""
3.LED with push down
regular led connection
5v --> button--->pin2-->resistor--->gnd

code:
const int led_pin = 13;
const int button_pin = 2;
int button_state = 0;

void setup(){
  pinMode(led_pin,OUTPUT);
  pinMode(button_pin,INPUT);
}

void loop(){
  if (digitalRead(button_pin) == HIGH){
    	digitalWrite(led_pin, HIGH);
  }
  else{
    	digitalWrite(led_pin, LOW);
  }
}
"""

"------------------------------------------------------------------------------------------------------------------------------"

"""
4.a
5v --> LDR ----->A0---->Resistor----->gnd

code:
int ldrpin = A0;

void setup(){
    Serial.begin(9600);

}

void loop(){
    int value = analogRead(ldrpin);
    Serial.println(value);
    delay(500);
}

4b.
5v-->LDR-->A0-->resistor-->gnd
regular led connection

int led_pin = 13;
int ldr_pin = A0;

void setup(){
    Serial.begin(9600);
    pinMode(led_pin,OUTPUT);
}

void loop(){
    int value = analogRead(ldr_pin);

    if (value < 100){//threshold
        digitalWrite(led_pin,HIGH);
    }
    else{
        digitalWrite(led_pin,LOW);
    }
}
"""

"--------------------------------------------------------------------------------------------------------------------"

"""
5a. IR --> LED
IR SENSOR:
VCC --> 5v
out --> pin2
GND --> GND

regular led connection

code:
int ledpin = 13;
int irpin = 2;

void setup(){
    pinMode(ledpin,OUTPUT);
    pinMode(irpin,INPUT);
}

void loop(){
    int status = digitalRead(irpin);

    if (status == LOW){//object detected
        digitalWrite(ledpin,HIGH);
    }
    else{
        digitalWrite(ledpin,LOW);
    }
}

5b IR ----> Buzzer

IR:
vcc --> 5v
out --> pin 2
gnd --> gnd

buzzer:
pin 8 -->positive(long leg)---->negative(short leg)-->gnd

code:
int irpin = 2;
int buzzerpin = 8;

void setup(){
    pinMode(irpin,INPUT);
    pinMode(buzzerpin,OUTPUT);
}

void loop(){
    int status = digitalRead(irpin);

    if (status == LOW){//object detected
        tone(buzzerpin,500);
    }
    else{
        noTone(buzzerpin);
    }
}

6a. Servo motor
red --> 5v
brown --> grnd
yellow --> pin 3

code:
#include <Servo.h>

Servo myServo;
int servoPin = 3;

void setup(){
    myServo.attach(servoPin);
}

void loop(){
    for (int pos = 0; pos<=180; pos++){
        myServo.write(pos);
        delay(15);
    }
    for (int pos = 180; pos>=0; pos--){
        myServo.write(pos);
        delay(15);
    }
}

6B.

circuit

Arduino ---> L293D
pin 10 --> pin 2(IN1)
pin 11 --> pin 7(IN2)

L293D --> DC Motor
pin 3 --> terminal 1
pin 6 --> terminal 2

positive connections
L293D enable pin 1 and normal pin 16 common connection ---> 5v(VCC) in Arduino
L293D pin 8 ---> external battery's posotive terminal(VSS)

Ground connections
(L293D pin 4, pin 5), (external battery source's ground/negative terminal) ---> common connection to Arduino's grnd


IN1 IN2   output
0    0     stop
1    0     clockwise
0    1     anti-clockwise
1    1     stop

code:

int IN1 = 10;
int IN2 = 11;

void setup(){
    pinMode(IN1,OUTPUT);
    pinMode(IN2,OUTPUT);
}

void loop(){
    //clockwise
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    delay(2000);

    //stop
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,LOW);
    delay(2000);

    //anti-clockwise
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,HIGH);
    delay(2000);

    //stop
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,LOW);
    delay(2000);

6C. with a push button thats it
5v --> button ---> pin 2---->resistor-----> gnd

rest everything do the same as before, just add the buttons to the 5v and gnd's already existing common connections

code:
int IN1 = 10;
int IN2 = 11;
int buttonpin = 2;

void setup(){
    pinMode(IN1,OUTPUT);
    pinMode(IN2,OUTPUT);
    pinMode(buttonpin,INPUT);
}

void loop(){
    int value = digitalRead(buttonpin);

    if (value == HIGH){
        //clockwise
        digitalWrite(IN1,HIGH);
        digitalWrite(IN2,LOW);
    }
    else{
        //anti-clockwise
        digitalWrite(IN1,LOW);
        digitalWrite(IN2,HIGH);
    }
}

"""

"----------------------------------------------------------------------------------------------------------------"

"""
7a.Ultrasonic sensor
HC-SR04 sensor --> arduino
vcc --> 5v
GND --> GND
trig --> pin 3
echo --> pin 2

LED COnnection regular but use analog pin
pin 9~ --> resistor -->LED(anode) --->LED(cathode) --->GND

common connections to gnd

code:
#define trigPin 3
#define echoPin 2
int ledPin = 9;

void setup(){
    pinMode(trigPin,OUTPUT);
    pinMode(ledPin,OUTPUT);
    pinMode(echoPin,INPUT);
}

void loop(){
    digitalWrite(trigPin,LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin,HIGH);
    delayMicroseconds(10);

    digitalWrite(trigPin,LOW);

    long duration = pulseIn(echoPin,HIGH);
    int distance = duration * 0.034 / 2;
    distance = constrain(distance, 0, 100);
    int brightness = map(distance,0,100,255,0);

    analogWrite(ledPin,brightness);
}

7b.
🔹 7b) Distance → Gate Control
🔸 Version 1: LED as Gate
🔌 Connections

HC-SR04 → same as above

Gate (LED)

Pin 8 → 220Ω → LED → GND
💻 Code
#define trigPin 3
#define echoPin 2

int gatePin = 8;

void setup(){
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(gatePin, OUTPUT);
}

void loop(){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH);
    int distance = duration * 0.034 / 2;

    if(distance < 20){
        digitalWrite(gatePin, HIGH); // open
    }
    else{
        digitalWrite(gatePin, LOW);  // close
    }
}
🔸 Version 2: Servo Gate (Realistic)
🔌 Connections

HC-SR04 → same as above

Servo

Red → 5V
Brown → GND
Yellow → Pin 9
💻 Code
#include <Servo.h>

#define trigPin 3
#define echoPin 2

Servo gateServo;

void setup(){
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    gateServo.attach(9);
}

void loop(){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH);
    int distance = duration * 0.034 / 2;

    if(distance < 20){
        gateServo.write(90); // open
    }
    else{
        gateServo.write(0);  // close
    }
}




"""


"------------------------------------------------------------------------------------------------------------------------"

"""
14.
14.a
HC-05 --> arduino
vcc --> 5v
gnd ---> gnd
TX ---> RX(pin 0 of arduino)
RX --> TX(pin 1 of arduino)

**important note: remove TX and RX wires while uploading the code, reconnect them after uploading

code:
int ledpin = 13;

void setup(){
    pinMode(ledpin,OUTPUT);
    Serial.begin(9600);
}

void loop(){
    if (Serial.available()){
        char command = Serial.read();

        if (command == '1'){
            digitalWrite(ledpin,HIGH);
        }
        else if(command == '0'){
            digitalWrite(ledpin,LOW);
        }
    }
}

14.b
HC-05 --> Arduino
vcc -->5v
gnd --> gnd
TX --> RX(pin 0 of arduino)
RX --> TX(pin 1 of arduino)

**important note: remove TX and RX wires while uploading code, connectthem back after uploading

DHT11 sensor
vcc --> 5v
gnd --> gnd
data --> pin 2

code:

#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);

void setup(){
    Serial.begin(9600);
    dht.begin();
}

void loop(){
    float temp = dht.readTemperature();
    float humidity = dht.readHumidity();

    if (isnan(temp) || isnan(humidity)){
        Serial.println("Sensor is not working");
    }
    else{
        Serial.println(temp);
        Serial.println(humidity);
    }
}
"""


"__________________________________________________________________________________________________________________________"




"""
8.Raspberry Pi
8a. led
circuit
GPIO4 ---> resistor ---> anode ---> cathode ----> gnd

code:
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

while True:
    GPIO.output(4,True)
    time.sleep(1)
    GPIO.output(4,False)
    time.sleep(1)

8b. led with toggle(button basically)
connections
GPIO4 --->resistor --->anode ---->cathode --> gnd

GPIO17 -----> button ----->gnd

code:
import RPi.GPIO as GPIO
import time

LED = 4
BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

LED_STATE = False
while True:
    if GPIO.input(BUTTON) == 1:
        LED_STATE = not LED_STATE
        GPIO.output(LED,LED_STATE)
        time.sleep(0.3)
"""

"------------------------------------------------------------------------------------------------------------------------"

"""
9.
DHT11 ---> Raspberry pi
VCC --> 3.3v(pin1)
gnd ---> gnd(pin 6)
data --> GPIO4

terminal
sudo apt update
sudo apt install -y python3-venv or python3-full python3-venv libgpiod2

python3 -m venv venv
source venv/bin/activate

inside venv
pip install adafruit-circuitpython-dht

code:
import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D4)

while True:
    try:
        print(dht.temperature)
        print(dht.humidity)
    except RunTimeError as e:
        print("ERROR:",e)
    time.sleep(2)

sudo venv/bin/python file.py
"""


"------------------------------------------------------------------------------------------------------------------"

"""
10.
EXP 10 — NodeMCU LED BLINK

AIM:
Blink built-in / external LED using NodeMCU (ESP8266)

CONNECTION:
D4 → Resistor → LED (+)
LED (-) → GND

SETUP (Arduino IDE):
1. File → Preferences
   Add:
   https://arduino.esp8266.com/stable/package_esp8266com_index.json

2. Tools → Board Manager → Install esp8266

3. Tools → Board → NodeMCU 1.0 (ESP-12E)

4. Tools → Port → Select COM port

CODE:
void setup() {
  pinMode(D4, OUTPUT);
}

void loop() {
  digitalWrite(D4, HIGH);
  delay(1000);

  digitalWrite(D4, LOW);
  delay(1000);
}

EXECUTION:
Click Upload → wait for “Done uploading”

OUTPUT:
LED blinks ON and OFF every 1 second

KEY POINTS:
- NodeMCU uses Arduino (C/C++)
- Code is uploaded (not run like Raspberry Pi)
- D4 is GPIO pin
- HIGH = ON, LOW = OFF
"""

"------------------------------------------------------------------------------------------------------------------------"

"""
go to the folder where mosquitto is downloaded in terminal

>mosquitto -v

then in new terminal
create two python files subscriber.py and publisher.py

publisher.py
import paho.mqtt.client as mqtt
import time

broker = "localhost"
port = 1883

client = mqtt.Client()

client.connect(broker,port)

topic = "home/room1/light"

try:
    state = "OFF"

    while True:
        client.publish(topic,state)
        print("Published: ",state)

        state = "ON" if state == "OFF" else "OFF"
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()

    
subscriber.py
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883

def on_message(client, userdata, msg):
    print("Topic: ",msg.topic)
    print("Messge: ",msg.payload.decode())

client = mqtt.Client()

client.on_message = on_message

client.connect(broker,port)

topic = "home/room1/light"
client.subscribe(topic)

client.loop_forever()

first run publisher and then subscriber

"""

"-----------------------------------------------------------------------------------------------------------------------"

"""
COAP with raspberry pi

server.py

import asyncio
from aiocoap import Context,Message,CONTENT
import aiocoap.resource as resource
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

class SwitchResource(resource.Resource):
    async def render_get(self,request):
        if GPIO.input(17) == 1:
            return Message(payload=b"ON", code=CONTENT)
        else:
            return Message(payload=b"OFF", code=CONTENT)
        
async def main():
    root = resource.Site()
    root.add_resource(['Switch'],SwitchResource())

    await Context.create_server_context(
        root,
        bind=("localhost",5683)
    )

    print("COAP Server running at coap://localhost:5683/Switch")

    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())

    
client.py
import asyncio
from aiocoap import Context,Message,GET

async def main():
    protocol = await Context.create_client_context()

    request = Message(
        code=GET,
        uri = "coap://localhost:5683/switch"
    )

    try:
        while True:
            response = await protocol.request(request).response

            print(response.payload.decode())

            await asyncio.sleep(2)
    finally:
        await protocol.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
"""

"---------------------------------------------------------------------------------------------------------------------"

"""Fire Fucking Base

#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>

// WiFi (your hotspot)
#define WIFI_SSID "vivo Y100A"
#define WIFI_PASS "password"

// Firebase
#define FIREBASE_HOST "iot-lab-finals-default-rtdb.firebaseio.com"
#define FIREBASE_APIKEY "AIzaSyAhayZBNOLD5YEr5MaPfNCep5DDSiMwEiI"
#define AUTH_EMAIL "sudharshan2370007@ssn.edu.in"
#define AUTH_PASS "2J7sbZsZe@"

// Firebase objects
FirebaseData firebaseData;
FirebaseConfig config;
FirebaseAuth auth;

void setup() {
  Serial.begin(115200);

  pinMode(D0, OUTPUT);

  // Connect to WiFi
  Serial.print("Connecting to WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("\nWiFi Connected");

  // Firebase setup
  config.host = FIREBASE_HOST;
  config.api_key = FIREBASE_APIKEY;

  auth.user.email = AUTH_EMAIL;
  auth.user.password = AUTH_PASS;

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  Serial.println("Connected to Firebase");

  // Initialize value
  Firebase.setBool(firebaseData, "/ledStatus", false);
}

void loop() {

  if (Firebase.getBool(firebaseData, "/ledStatus")) {

    if (firebaseData.dataType() == "boolean") {

      bool led = firebaseData.boolData();

      digitalWrite(D0, led ? HIGH : LOW);

      Serial.print("LED: ");
      Serial.println(led ? "ON" : "OFF");
    }
  }

  delay(1000);
}

"""