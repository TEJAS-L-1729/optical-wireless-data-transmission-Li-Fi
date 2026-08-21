#define led 6
#define period 1
char* text="Hey, this is a Visual light communication (VLC) project!";
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
  delay(5000);
}

void send_byte(char my_byte)
{
  //transmittes the binary code for each character in the text using PWM
  digitalWrite(led, LOW);
  delay(period);
  for(int i=0;i<8;i++)
  {
    //LED emmits light only when the bit reads one
    digitalWrite(led, (my_byte & (0x01<<i))!=0);
    Serial.println(my_byte & (0x01<<i));
    delay(period);
  }
  digitalWrite(led, HIGH);
  delay(period);
}