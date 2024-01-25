const int buttonPin = 2;
const int ledPin = 12;

int buttonState = 0;
int lastButtonState = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH && lastButtonState == LOW) {
    digitalWrite(ledPin, !digitalRead(ledPin)); 
  }

  lastButtonState = buttonState;

  if (digitalRead(buttonPin) == HIGH) {
    Serial.println("BUTTON_PRESSED");
    delay(500);  
  }
}
