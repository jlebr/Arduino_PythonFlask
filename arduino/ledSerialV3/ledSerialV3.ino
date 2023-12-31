// Ultima version del codigo que guarda el valor del LED en la memoria interna de arduino para luego leerla o escribirla segun sea el caso
#include <EEPROM.h>

// Utilizo el led que viene de fabrica porque no tengo leds
int ledPin = LED_BUILTIN;
int estadoLed = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  
  // Leer el último estado guardado en la memoria EEPROM
  estadoLed = EEPROM.read(0);
  
  // Encender o apagar el LED según el último estado guardado
  if (estadoLed == 1) {
    digitalWrite(ledPin, HIGH);
    Serial.println("El LED está encendido");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("El LED está apagado");
  }
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();
    
    if (comando == '1') { // si recibe 1 enciende LED y guarda valor en la EEPROM
      digitalWrite(ledPin, HIGH);
      estadoLed = 1;
      EEPROM.write(0, estadoLed); // Guardar el nuevo estado en la memoria EEPROM
      Serial.println("LED encendido");
    } else if (comando == '0') { // si recibe 0 apaga LED y guarda valor en la EEPROM
      digitalWrite(ledPin, LOW);
      estadoLed = 0;
      EEPROM.write(0, estadoLed); // Guardar el nuevo estado en la memoria EEPROM
      Serial.println("LED apagado");
    } else if (comando == '2') { // si recibe 2 va y consulta estadoLed y devuelve la respuesta acorde al estado.
      if (estadoLed == 1) {
        Serial.println("El LED está encendido");
      } else {
        Serial.println("El LED está apagado");
      }
    }
    
    delay(100); // Pequeña pausa para evitar lecturas incorrectas del puerto serial
  }
}

// Realizado por Jorge Barboza
