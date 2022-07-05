int i=0;
void setup() {
delay(1000);
Serial.begin(9600);

}
 
void loop() {
i=i+1;
Serial.println(i);
delay(500);                     
}

