#include <Wire.h>
#include "Adafruit_MCP9808.h"
#include <SoftwareSerial.h>

SoftwareSerial myserial(2, 3);  //RX,TX

Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();

int LEDPIN = 13;
int ss_temp;

void clear1()
{
  while (myserial.available() > 0)
    myserial.read();
}

int hex(char *hex)
{
  byte n = (int)strtol(hex, NULL, 16);
  return n;
}

byte chk;

byte addChk(byte n)
{
  chk += n;
  return n;
}

// For heating
void m1(byte pwm){
  clear1();
  chk = 0;
  myserial.write(hex("2A")); // startCode
  myserial.write(hex("0D"));
  myserial.write(pwm);
  myserial.write(pwm);
  myserial.write(hex("23")); //endCode
}

// For cooling
void m2(byte pwm){
  clear1();
  chk = 0;
  myserial.write(hex("2A")); // startCode
  myserial.write(hex("07"));
  myserial.write(pwm);
  myserial.write(pwm);
  myserial.write(hex("23")); //endCode  
}

void stopp(){
  clear1();
  chk = 0;
  myserial.write(hex("2A")); // startCode
  myserial.write(hex("05"));
  myserial.write(hex("FF"));
  myserial.write(hex("FF"));
  myserial.write(hex("23")); //endCode  
}
 
void setup() 
{
    pinMode(LEDPIN, OUTPUT);
 
    Serial.begin(9600);     // communication with the host computer
    while (!Serial);
 
    myserial.begin(9600);  

    if (!tempsensor.begin(0x18)) {
      Serial.println("Couldn't find MCP9808! Check your connections and verify the address is correct.");
      while (1);
    }
      
    Serial.println("Found MCP9808!");
  
    tempsensor.setResolution(3); // sets the resolution mode of reading, the modes are defined in the table bellow:
    // Mode Resolution SampleTime
    //  0    0.5°C       30 ms
    //  1    0.25°C      65 ms
    //  2    0.125°C     130 ms
    //  3    0.0625°C    250 ms

    
 
//    Serial.println("");
//    Serial.println("Remember to to set Both NL & CR in the serial monitor.");
    Serial.println("Ready");
    Serial.println("");   

    // Get current temperature
    tempsensor.wake();
    float c = tempsensor.readTempC();
    Serial.print("Initial Temp: "); 
    Serial.print(c, 4); Serial.print("*C\t\n");
    ss_temp = (int)c;
  
    delay(250);
    tempsensor.shutdown_wake(1);
    Serial.println("");
    delay(200);

//    while(1){
//      for (int i=0;i<255;i++){ 
//        m1(i);  
//        delay(10);  
//      }
//      for (int i=255;i>=0;i--){
//         m1(i);
//         delay(10);
//      }
//        
//    }

//    while(1){
//      m1();
//      delay(1000);
//      m2();
//      delay(1000);
//      stopp();
//      delay(1000);
//    }
}

//*?~~#

int max_temp = 44; // max human body temp
int min_temp = 13; // min human body temp
int temp = 0;
int power = 5;

void loop() 
{
  if (power > 255){
    while(1);
  }

  Serial.print("Starting at Power level ");
  Serial.print(power);
  Serial.println();

  long int start = millis();  
  while (millis() - start < 600000){
    
    m1(power);  

    // record temp
    tempsensor.wake();
    float temp = tempsensor.readTempC();
    Serial.print("Temp: "); 
    Serial.print(temp, 4); Serial.print("*C\t\n");
  
    delay(250);
    tempsensor.shutdown_wake(1);
    Serial.println("");
    delay(200);
    
    
  }

  power += 5;
}
