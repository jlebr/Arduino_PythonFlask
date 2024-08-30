// Ultima version del codigo que guarda el valor del LED en la memoria interna de arduino para luego leerla o escribirla segun sea el caso
#include <EEPROM.h>

int ledPin = 12;
int AC = 10;
int relay1 = 9;
int relay2 = 8;
int relay3 = 7;
int estadoLed = 0;
int estadoFan = 0;

void setup() {
  pinMode(ledPin, OUTPUT); // Configuro ledPin como salida
  pinMode(AC, OUTPUT); // Configuro AC como salida
  pinMode(relay1, OUTPUT); // Configuro relay1 como salida
  pinMode(relay2, OUTPUT); // Configuro relay2 como salida
  pinMode(relay3, OUTPUT); // Configuro relay3 como salida
  //digitalWrite(ledpin2, HIGH);
  Serial.begin(9600);
  
  // Leer el último estado guardado en la memoria EEPROM
  estadoLed = EEPROM.read(0);
  estadoFan = EEPROM.read(1);

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
    } else if (comando == '3'){ //Cuando reciba 00 va apagar todos los relay
      digitalWrite(AC, LOW);
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, LOW);
      digitalWrite(relay3, LOW);
      Serial.println("FAN apagado");
    } else if(comando == '4'){ // Cuando reciba 4 va encender realay AC y relay1
      digitalWrite(AC, LOW);
      digitalWrite(relay2, LOW);
      digitalWrite(relay3, LOW);
      delay(10);
      digitalWrite(AC, HIGH);
      delay(10);
      digitalWrite(relay1, HIGH);
      Serial.println("FAN encedido Vel1");
    } else if(comando =='5'){// Cuando reciba 5 va encender relay AC y relay2
      digitalWrite(AC, LOW);
      digitalWrite(relay1, LOW);
      digitalWrite(relay3, LOW);
      delay(10);
      digitalWrite(AC, HIGH);
      delay(10);
      digitalWrite(relay2, HIGH);
      Serial.println("FAN encendido Vel2");
    } else if(comando =='6'){// Cuando reciba 6 va encender relay AC y relay3
      digitalWrite(AC, LOW);
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, LOW);
      delay(10);
      digitalWrite(AC, HIGH);
      delay(10);
      digitalWrite(relay3, HIGH);
      Serial.println("FAN encendido Vel3");
    }

    delay(100); // Pequeña pausa para evitar lecturas incorrectas del puerto serial
  }
}

// Realizado por Jorge Barboza