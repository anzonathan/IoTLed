//IOT LED 

//Led 
int led = 13;

//Python Value from Host PC
int input;

void setup() {
  //Serial Monitor to display Logs
  Serial.begin(115200);
  Serial.setTimeout(1); //yet to know what this does

  //Declaring the led as an output
  pinMode(led,OUTPUT);


}

void loop() {
  //Listening for host serial
  while (!Serial.available());

  //Convert serial reading to integer: Try Serial.Read
  input = Serial.readString().toInt();
  //input = Serial.read();


  if (input == 1){
    digitalWrite(led, HIGH);
    Serial.println("On");
  }

  else if (input == 0){
    digitalWrite(led, LOW);
    Serial.println("Off");
  }

  else {Serial.println("Invalid");}


  

}
