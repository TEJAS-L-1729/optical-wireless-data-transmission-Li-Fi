#include <stdio.h>
#define ldr A0
#define threshold 50
#define period 1

bool previous_state;
bool current_state;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop()
{
  current_state=get_ldr();
  if(!current_state && previous_state)
  {
    print_byte(get_byte());
  }
  previous_state=current_state;
}

bool get_ldr()
{
  //to check if the laser is on or off
  int voltage = analogRead(ldr);
  return voltage>threshold? true: false;
}

char get_byte()
{
  //to extract binary code sent by the laser
  char ret = 0;
  delay(period * 1.5);
  for(int i=0;i<8;i++)
  {
    ret=ret|(get_ldr() << i);
    delay(period);
  }
  return ret;
}

void print_byte(char my_byte)
{
  //extracts the character specific to the ascii binary code received and prints it
  char buff[2];
  sprintf(buff, "%c", my_byte);
  Serial.print(buff);
}