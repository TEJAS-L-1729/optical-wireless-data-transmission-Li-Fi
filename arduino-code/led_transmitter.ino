#define led A0
#define period 100
char* text="//RVCE//";
int len=strlen(text);

void setup()
{
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(250000);
}

void loop()
{
  // put your main code here, to run repeatedly:
  for(int i=0;i<len;i++)
  {
    send_byte(text[i]);
  }
  delay(1000);
}

void send_byte(char my_byte)
{
  delay(period);
  digitalWrite(led, LOW);
  for(int i=0;i<8;i++)
  {
    digitalWrite(led, (my_byte & (0x01<<i))!=0);
    Serial.println(my_byte & (0x01<<i));
    delay(period);
  }
  digitalWrite(led, HIGH);
  delay(period);
}