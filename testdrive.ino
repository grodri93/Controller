int left_motor = 3;
int right_motor = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(left_motor, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  int i = 1;

   char data = ' ';
    if(Serial.available()) {
      data = Serial.read();
      Serial.println(data); 
    }
  if( data == 'X') {  
  digitalWrite(left_motor, HIGH);
  delay(1);
  digitalWrite(left_motor, LOW);
  delay(i);
  }



}
