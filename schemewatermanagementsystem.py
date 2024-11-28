#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
#include <EEPROM.h>
void writeString(char add,String data);
String read_String(char add);

int j; int k;int l;int m;
void setup()
{
lcd.init();
lcd.backlight();
lcd.clear();
lcd.setCursor(0,0);
lcd.print("WATER MONITOR  ");
lcd.setCursor(0,1);
lcd.print("   SYSTEM");
delay(1000);
Serial.begin(9600); 
   
pinMode(A0,INPUT);
pinMode(A1,INPUT);
pinMode(A2,INPUT);

pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
digitalWrite(2,HIGH);
digitalWrite(3,HIGH);
//digitalWrite(4,LOW);
  String h = read_String(1);
  String f = read_String(2);
   j=h.toInt();
   k=f.toInt();
Serial.print(j);
Serial.print(k);

}


void loop() {


  


lcd.setCursor(0,0);
lcd.print("WATER MONITOR       ");
lcd.setCursor(0,1);
lcd.print("   SYSTEM");
delay(500);


if(j<=20)
{j++;
writeString(1, String(j));  
  digitalWrite(3,HIGH);
  digitalWrite(2,LOW);
    if(j==21)
  {
    k=1;
  writeString(2, String(k));  
    }
} 


  if(k<=20 && j>20)
{k++;
writeString(2, String(k));  
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  if(k==21)
  {j=1;
  writeString(1, String(j));  
    }
 }
lcd.clear();
lcd.setCursor(0,0);
lcd.print("STREET1 STREET2  ");
lcd.setCursor(0,1);
lcd.print(j);
lcd.setCursor(8,1);
lcd.print(k);



//  String h = read_String(11);
//  String f = read_String(12);
//   j=h.toInt();
//   k=f.toInt();
//Serial.print(j);
   delay(500);
  }

void writeString(char add,String data)
{
  int _size = data.length();
  int i;
  for(i=0;i<_size+1;i++)
  {
    EEPROM.write(add+i,data[i]);
  }
  EEPROM.write(add+_size,'\0');   //Add termination null character for String Data
}
 
 
String read_String(char add)
{
  int i;
  char data[100]; //Max 100 Bytes
  int len=0;
  unsigned char k;
  k=EEPROM.read(add);
  while(k != '\0' && len<=10)   //Read until null character
  {    
    k=EEPROM.read(add+len);
    data[len]=k;
    len++;
  }
  data[len]='\0';
  return String(data);
}