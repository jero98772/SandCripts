int drawudioInPin = A0;
int drawudioIn = 0;
int drawudioOut = 2;//D2

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  drawudioIn = analogRead(drawudioInPin );
  tone(drawudioOut,drawudioIn,250);
}
