


#define LEFT_PIN_A 6
#define LEFT_PIN_B 9
#define LEFT_ENCODER 2

#define RIGHT_PIN_A 10
#define RIGHT_PIN_B 11
#define RIGHT_ENCODER 3

#define BUZZER 5

String incomingByte;    // for incoming serial data

int song_notes[] = {76, 78, 78,  80,78,80,78,76,78, 76, 78, 83,  81, 80, 78,  76,   73, 69, 71};
int song_time[] = {333,333,333,1666,66,66,66,66,66, 333,333,1666,333,333, 50, 616, 1333, 1666,999};

int num = 19;


unsigned long int left = 0, right = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode(LEFT_PIN_A, OUTPUT);
  pinMode(LEFT_PIN_B, OUTPUT);
  pinMode(RIGHT_PIN_A, OUTPUT);
  pinMode(RIGHT_PIN_B, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  pinMode(LEFT_ENCODER, INPUT_PULLUP);
  pinMode(RIGHT_ENCODER, INPUT_PULLUP); 
  
  Serial.begin(115200);
  Serial.setTimeout(10);
  
  attachInterrupt(digitalPinToInterrupt(LEFT_ENCODER), left_encoder, FALLING);
  attachInterrupt(digitalPinToInterrupt(RIGHT_ENCODER), right_encoder, FALLING);
//
//  TCCR1B = TCCR1B & B11111000 | B00000001;
//  TCCR2B = TCCR2B & B11111000 | B00000001;
//  TCCR0B = TCCR0B & B11111000 | B00000001;

}

void loop() {
  // put your main code here, to run repeatedly:
//playSong();
  if (Serial.available() > 0) {
  
    // read the incoming byte:
    incomingByte = Serial.readString();
  
    // say what you got:
//    Serial.print(incomingByte);
    executeInput(incomingByte);
    Serial.flush();
  }
}

void moveMotor(float spee, int pinA, int pinB){

  if (spee < 0){
    analogWrite(pinA, (int)(-spee*255));
    digitalWrite(pinB, LOW);
    
  }
  else if (spee > 0){
    digitalWrite(pinA, LOW);
    analogWrite(pinB, (int)(spee*255));
    
  }else{
    digitalWrite(pinA, HIGH);
    digitalWrite(pinB, HIGH);
  } 
}


void executeInput(String input){

  long val;

  if (input.startsWith("ML")){
    val = strip(input);
    Serial.println((float)(val - 512)/512);
    moveMotor((float)(val - 512)/512,LEFT_PIN_A, LEFT_PIN_B);
  }
  else if(input.startsWith("MR")){
    val = strip(input);
    Serial.println((float)(val - 512)/512);
    moveMotor((float)(val - 512)/512,RIGHT_PIN_A, RIGHT_PIN_B);
  }

  writeEncoderData();
  
}

long strip(String input){
  long out;
  input.remove(0,2);
  out = input.toInt();
  return out;
}


void left_encoder(){
  left++;
}

void right_encoder(){
  right++;
}

void writeEncoderData(){
  Serial.println("EL" + String(left));
  Serial.println("ER" + String(right));
  left = 0;
  right = 0;
}




void playSong(){
  for(int i = 0; i < num; i++){
    playNote(song_notes[i], song_time[i]);
  }
}


void playNote(int note, int len){

  float a = ((float)(note - 69)) / 12.0;

  tone(BUZZER,pow(2,a)*440.0);
  delay(len);
  noTone(BUZZER);
  delay(2);
}
