const int LED= 6;//Digital pin that the LED is connected
#include <LiquidCrystal.h>

int rs=7;
int en=8;
int d4=9;
int d5=10;
int d6=11;
int d7=12;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

void setup(){
lcd.begin(16,2);

Serial.begin(9600);
pinMode(6, OUTPUT);

}

void loop() {
lcd.setCursor(0,0);
int sensorReading= analogRead(A0); //reads the sensor value

Serial.println (sensorReading); //prints out the sensor reading
lcd.print("Moisture level");
lcd.setCursor(0,1);
lcd.print(sensorReading);
if (sensorReading > 800){//if reading is above 800, LED blinks on and off
digitalWrite(6,HIGH); //turns the LED on
delay(1000); //waits for a second
digitalWrite(6,LOW); //turns the LED off
delay(1000); //waits for a second
}
}
