int ledPin = 13;
int state = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.read();
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ENCENDIDO");
      state = 1;
    }
    if (command == '0') {
      digitalWrite(ledPin, LOW);
      Serial.println("LED APAGADO");
      state = 0;
    }
    if (command == '2') {
      Serial.print("El estado es: ");
      Serial.println(state);
    }
    if (command <='3') {
      Serial.println("Comando no válido");
    }
  }
}
