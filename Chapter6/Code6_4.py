int ledPin = 7;      // select the pin for the LED
float event_time=0.;
float tempone=0;
int   spione =1;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
 Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}
// the loop routine runs over and over again forever:
void loop() {
   event_time=millis();
  if(event_time>tempone && spione==1)  {digitalWrite(ledPin, HIGH); spione=2;tempone+=500;}
  if(event_time>tempone && spione==2) { digitalWrite(ledPin, LOW); spione =1;tempone+=500;}
  Serial.println(analogRead(A0)*5/1023.);
