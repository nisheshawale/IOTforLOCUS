#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
//#include <ESP8266Ping.h>
#include <ArduinoJson.h>

void setup() {
 
  Serial.begin(9600);                 //Serial connection
  WiFi.begin("TP-LINK_", "--Password--");   //WiFi connection
 
  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
 
}

void loop() {

 //bool ret = Ping.ping("www.google.com");
 //Serial.println(ret);


  
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    StaticJsonBuffer<200> jsonBuffer;
  
    JsonObject& root = jsonBuffer.createObject();;
    root["room"] = "kitchen";
    root["temperature_f"] = 82.4;
    root["humidity"] = 19.2;
  
    char JSONmessageBuffer[300];
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
 
  delay(1000);  //Send a request every 30 seconds
}
