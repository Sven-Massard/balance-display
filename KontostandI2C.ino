/*
  I2C Pinouts

  SDA -> A4
  SCL -> A5
*/

//Import the library required
#include <Wire.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

#define SLAVE_ADDRESS 0x04

boolean receiving = false;
String out = "";
int state = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  lcd.begin(16, 2);
  Wire.onReceive(empfangen);
}

void loop() {
  delay(100);
}

void empfangen(int anzahl) {
  int c = 0;
  receiving = true;
  while (0 < Wire.available()) {
    c = Wire.read();
    if (c == 10) {
      receiving = false;
      output();
      out = "";
    }
    else {
      out += (char)c;
    }
  }



}

void output() {
  Serial.println(out);
  lcd.clear();
  lcd.print("Kontostand:");
  lcd.setCursor(0, 1);
  lcd.print(out + "Euro");
}

