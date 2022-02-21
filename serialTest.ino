void setup() {
  Serial.begin(9600);
}

String test = "";
void loop() {
  if( Serial.available() ){
    test = Serial.readStringUntil('\n');
    Serial.println("return:"+test);
  }
  delay(10);
}
