#include <SPI.h>
#include <MFRC522.h>


constexpr uint8_t RST_PIN = 9;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = 10;     // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance

float sal1 = 0.0;
float sal2 = 0.0;
float sal3 = 0.0;
float sal4 = 0.0;
float sal5 = 0.0;
float sal6 = 0.0;

char c = ' ';

String valor = " ";
int valfin = 0;
String vala = " ";
byte val;

void setup() {
 
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,INPUT);
  pinMode(8,OUTPUT);
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
  
}

void loop() {
  //Serial.print('s');
  if(Serial.available()>0){
    c = Serial.read();
    switch(c)
    {
    case '1':
      Escribir();
      break;
    case '2':
      Leer();
      break;
    case '3':
    /*
      digitalWrite(8,HIGH);
      delay(1000);
      digitalWrite(8,LOW);
    */
      
      sal1 = sal1 + valfin;
      //sal1 = sal1 - 5;
      if(sal1<=0){
        digitalWrite(2,LOW);
        //sal1 = 0;
      }else{
        digitalWrite(2,HIGH);
      }
      //Serial.print(sal1);
      break;
    case '4':
      sal2 = sal2 + valfin;
      break;
    case '5':
      sal3 = sal3 + valfin;
      break;
    case '6':
      digitalWrite(8,HIGH);
      delay(1000);
      digitalWrite(8,LOW);
      sal4 = sal4 + valfin;
      break;
    case '7':
      sal5 = sal5 + valfin;
      break;
    case '8':
      sal6 = sal6 + valfin;
      break;
    case '9':
      Serial.print(sal1);
      break;
    case '0':
      Serial.print(sal2);
      break;
    case '$':
      Serial.print(sal3);
      break;
    case '%':
      Serial.print(sal4);
      break;
    case '&':
      //sal5 = sal5 - 100.34;
      Serial.print(sal5);
      break;
    case '/':
      Serial.print(sal6);
      break;
    }
  }
  /*
  if(digitalRead(2) == 1){
    sal1 = sal1 - 0.19;
    if(sal1<=0){
      //salida rele
      sal1 = 0;
    }
  }
  if(digitalRead(3) == 1){
    sal2 = sal2 - 0.19;
    if(sal2<=0){
      //salida rele
      sal2 = 0;
    }
  }
  if(digitalRead(4) == 1){
    sal3 = sal3 - 0.19;
    if(sal3<=0){
      //salida rele
      sal3 = 0;
    }
  }
  if(digitalRead(5) == 1){
    sal4 = sal4 - 0.19;
    if(sal4<=0){
      //salida rele
      sal4 = 0;
    }
  }
  if(digitalRead(6) == 1){
    sal5 = sal5 - 0.19;
    if(sal5<=0){
      //salida rele
      sal5 = 0;
    }
  }
  */
  if(digitalRead(7) == HIGH){
    sal1 = sal1 -1;
    while(digitalRead(7)==HIGH){
      delay(100);
    }
    if(sal1<=0){
      digitalWrite(2,LOW);
      sal1 = 0;
    }
    
  }
}
void Escribir()
{
  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  // Look for new cards
  while ( ! mfrc522.PICC_IsNewCardPresent()) {
    //return;
  }

  // Select one of the cards
  while ( ! mfrc522.PICC_ReadCardSerial()) {
    //return;
  }

  byte buffer[34];
  byte block;
  MFRC522::StatusCode status;
  byte len;
  

  while(!Serial.available()){}
  len = Serial.readBytesUntil('#', (char *) buffer, 30) ; // read family name from serial
  for (byte i = len; i < 30; i++) buffer[i] = ' ';     // pad with spaces

  block = 1;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    //Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  
  // Write block
  status = mfrc522.MIFARE_Write(block, buffer, 16);
  if (status != MFRC522::STATUS_OK) {
    //Serial.print(F("Recarga falló: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  //Serial.println(" ");
  mfrc522.PICC_HaltA(); // Halt PICC
  mfrc522.PCD_StopCrypto1();  // Stop encryption on PCD
  
}
void Leer()
{
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  //some variables we need
  byte block;
  byte len;
  MFRC522::StatusCode status;

  //-------------------------------------------

  // Look for new cards
  while ( ! mfrc522.PICC_IsNewCardPresent()) {
    //return;
  }

  // Select one of the cards
  while ( ! mfrc522.PICC_ReadCardSerial()) {
    //return;
  }


  len = 18;


  byte buffer2[18];
  block = 1;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, 1, &key, &(mfrc522.uid)); //line 834
  if (status != MFRC522::STATUS_OK) {
    //Serial.print("Authentication failed: ");
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  status = mfrc522.MIFARE_Read(block, buffer2, &len);
  if (status != MFRC522::STATUS_OK) {
    //Serial.print("Reading failed: ");
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  //PRINT LAST NAME
  for (uint8_t i = 0; i < 16; i++) {
    Serial.write(buffer2[i]);
    valor = valor + (char)buffer2[i];
  }
  valfin = valor.toInt();
  valor = "";

  //----------------------------------------

  //Serial.println("\n**End Reading**\n");
  //valfin = valfin - 3000;
  //Serial.print(valfin);
  delay(1000); //change value if you want to read cards faster

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
}
