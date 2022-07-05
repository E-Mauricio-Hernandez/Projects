#include <SPI.h>
#include <MFRC522.h>


constexpr uint8_t RST_PIN = 8;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = 53;     // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance


//####APARTAMENTOS SALIDAS RELES######
int apt1 = 2;
int apt2 = 3;
int apt3 = 4;
int apt4 = 5;
int apt5 = 6;
int apt6 = 7;  //este ya no
//#########APARTAMENTOS ENTRADAS#######
int pin1 = 22; 
int pin2 = 24; 
int pin3 = 26; 
int pin4 = 28; 
int pin5 = 30;
int pin6 = 32;  //este ya no perros
//########convertir#########
int conv1 = 0;
int conv2 = 0;
int conv3 = 0;
int conv4 = 0;
int conv5 = 0;
int conv6 = 0;
//#######variables convertidas a pulsos##########
unsigned long pulsos1 = 0;
unsigned long pulsos2 = 0;
unsigned long pulsos3 = 0;
unsigned long pulsos4 = 0;
unsigned long pulsos5 = 0;
unsigned long pulsos6 = 0;
//#######FLANCOS SUBIDA APARTAMENTOS##########
bool dato1 = LOW;
bool datoAnterior1 = LOW;

bool dato2 = LOW;
bool datoAnterior2 = LOW;

bool dato3 = LOW;
bool datoAnterior3 = LOW;

bool dato4 = LOW;
bool datoAnterior4 = LOW;

bool dato5 = LOW;
bool datoAnterior5 = LOW;

bool dato6 = LOW;
bool datoAnterior6 = LOW;

//#########variables en kw###########
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
 Serial.begin(9600);
 //############PINES SALIDAS################
  pinMode(apt1, OUTPUT); 
  pinMode(apt2, OUTPUT); 
  pinMode(apt3, OUTPUT); 
  pinMode(apt4, OUTPUT); 
  pinMode(apt5, OUTPUT); 
  pinMode(apt6, OUTPUT);
  //############PINES ENTRADAS##############
  pinMode(pin1, INPUT);
  pinMode(pin2, INPUT);
  pinMode(pin3, INPUT);
  pinMode(pin4, INPUT);
  pinMode(pin5, INPUT);
  pinMode(pin6, INPUT);


  
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
      conv1 = 1;
      sal1 = sal1 + valfin;
      if(sal1<=0){
        digitalWrite(apt1,LOW);
      }else{
        digitalWrite(apt1,HIGH);
      }

      break;
      
    case '4':
      conv2 = 1;
      sal2 = sal2 + valfin;
      if(sal2<=0){
        digitalWrite(apt2,HIGH);
        //sal1 = 0;
      }else{
        digitalWrite(apt2,LOW);
      }
      break;
    case '5':
      conv3 = 1;  
      sal3 = sal3 + valfin;
     
      if(sal3<=0){
        digitalWrite(apt3,LOW);
      }else{
        digitalWrite(apt3,HIGH);
      }
      break;
    case '6':
      conv4 = 1;
      sal4 = sal4 + valfin;
  
      if(sal4<=0){
        digitalWrite(apt4,LOW);

      }else{
        digitalWrite(apt4,HIGH);
      }
      break;
    case '7':
      conv5 = 1;
      sal5 = sal5 + valfin;
      if(sal5<=0){
        digitalWrite(apt5,LOW);

      }else{
        digitalWrite(apt5,HIGH);
      }

      break;
    case '8':
      conv6 = 1;
      sal6 = sal6 + valfin;
      if(sal6<=0){
        digitalWrite(apt6,LOW);
      }else{
        digitalWrite(apt6,HIGH);
      }
      break;
    case '9':
      Serial.print(pulsos1);
      break;
    case '0':
      Serial.print(pulsos2);
      break;
    case '$':
      Serial.print(pulsos3);
      break;
    case '%':
      Serial.print(pulsos4);
      break;
    case '&':
      Serial.print(pulsos5);
      break;
    case '/':
      Serial.print(pulsos6);
      break;
    }
  }
if (conv1 == 1) {
  pulsos1 = pulsos1 + (sal1*3200);
  conv1 = 0;
  sal1 =0;
  }

if (conv2 == 1) {
  pulsos2 = pulsos2 + (sal2*3200);
  pulsos2 = 11;
  conv2 = 0;
  sal2 = 0;
  }
if (conv3 == 1) {
  pulsos3 = pulsos3 + (sal3*3200);
  conv3 = 0;
  sal3 = 0;
  }
if (conv4 ==1) {
  pulsos4 = pulsos4 + (sal4*3200);
  conv1 = 0;
  sal4 = 0;
  }
if (conv5 == 1) {
  pulsos5 = pulsos5 + (sal5*3200);
  conv5 = 0;
  sal5 = 0;
  }
if (conv6 == 1) {
  pulsos6 = pulsos6 + (sal6*3200);
  conv6 = 0;
  sal6 = 0;
  }
//########LECTURA PINES######
dato1 = digitalRead(pin1);
dato2 = digitalRead(pin2);
dato3 = digitalRead(pin3);
dato4 = digitalRead(pin4);
dato5 = digitalRead(pin5);
dato6 = digitalRead(pin6);

if(dato1 == HIGH && datoAnterior1 == LOW && pulsos1 >0) {
  pulsos1 = pulsos1 - 1;
  }  
 datoAnterior1 = dato1;

if(dato2 == HIGH && datoAnterior2 == LOW && pulsos2 >0) {
  pulsos2 = pulsos2 - 1;
  }  
 datoAnterior2 = dato2;
 
if(dato3 == HIGH && datoAnterior3 == LOW && pulsos3 >0) {
  pulsos3 = pulsos3 - 1;
  }  
 datoAnterior3 = dato3;
 
if(dato4 == HIGH && datoAnterior4 == LOW && pulsos4 >0) {
  pulsos4 = pulsos4 - 1;
  }  
 datoAnterior4 = dato4;
 
if(dato5 == HIGH && datoAnterior5 == LOW && pulsos5 >0) {
  pulsos5 = pulsos5 - 1;
  }  
 datoAnterior5 = dato5;
 
if(dato6 == HIGH && datoAnterior6 == LOW && pulsos6 >0) {
  pulsos6 = pulsos6 - 1;
  }  
 datoAnterior6 = dato6;

//#########pregunta saldo#########
if (pulsos1 > 0){
  digitalWrite(apt1, HIGH);
  } 
else{
  digitalWrite(apt1, LOW);
  }
if (pulsos2 >0){
  digitalWrite(apt2, HIGH);
  } 
else{
  digitalWrite(apt2, LOW);
  }  
if (pulsos3 >0){
  digitalWrite(apt3, HIGH);
  } 
else{
  digitalWrite(apt3, LOW);
  }
if (pulsos4 >0){
  digitalWrite(apt4, HIGH);
  } 
else{
  digitalWrite(apt4, LOW);
  } 
if (pulsos5 >0){
  digitalWrite(apt5, HIGH);
  } 
else{
  digitalWrite(apt5, LOW);
  }
if (pulsos6>0){
  digitalWrite(apt6, HIGH);
  } 
else{
  digitalWrite(apt6, LOW);
  
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
