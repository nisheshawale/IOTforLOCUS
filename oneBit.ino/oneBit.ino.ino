#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
//#include <ESP8266Ping.h>
#include <ArduinoJson.h>

int i = 0;
int temp;
//String value;

void setup() {
 
  Serial.begin(9600);                 //Serial connection
  pinMode(5, INPUT); // Setup for leads off detection LO +
  pinMode(4, INPUT); // Setup for leads off detection LO -
  WiFi.begin("TP-LINK_", "ratna9841929327");   //WiFi connection
 
  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
  //value = String();
  delay(5000);
 
}

void loop() {

 //bool ret = Ping.ping("www.google.com");
 //Serial.println(ret);
  if(i < 100)
  {
      
      if((digitalRead(5) == 1)||(digitalRead(4) == 1)){
        Serial.println('!');
      }
      else{
        // send the value of analog input 0:
          temp = analogRead(A0);
      }
      //Wait for a bit to keep serial data from saturating
      Send();
      i++;
      //Serial.println(value);
      delay(1);
  }
    
}

void Send(){
    if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
      StaticJsonBuffer<200> jsonBuffer;
    
      JsonObject& root = jsonBuffer.createObject();
     // root["room"] = "kitchen";
      root["beat"] = temp;
      
      char JSONmessageBuffer[200];
      root.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
      Serial.println(JSONmessageBuffer);
    
      HTTPClient http; //Declare object of class HTTPClient
      http.begin("http://192.168.1.106:8000/testIOT/"); //Specify request destination
      http.addHeader("Content-Type", "application/json"); //Specify content-type header
     
      int httpCode = http.POST(JSONmessageBuffer); //Send the request
      String payload = http.getString(); //Get the response payload
      Serial.println(httpCode); //Print HTTP return code
      Serial.println(payload); //Print request response payload
      http.end(); //Close connection
    } else {
   
      Serial.println("Error in WiFi connection");
   
    }
}
