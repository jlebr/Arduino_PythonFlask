char Comando_entrada; //Variable o comando que tecleamos
int led = 13; // pin de salida
int state = 0;

void setup() {
  Serial.begin(9600); //iniciamos el puerto serie
  pinMode(led,OUTPUT); // El pin 13 funciona como salida
  //digitalWrite(led, LOW); // Apagar el LED en el pin 13
  digitalWrite(led, state); // establecer el estado del LED en función de la variable global

}

void loop() {
  //Si el puerto serial esta disponible y hay un dato
  if (Serial.available()>0){
    delay(1000);
    // el comando de encendido es leido en el puerto serial
    Comando_entrada=Serial.read();
    delay(1000);
    //Si el comando es un 1 hace alto el pin 13 e imprime
    if(Comando_entrada=='2'){
      digitalWrite(led, HIGH);
      Serial.println("LED ENCENDIDO");
      state = 1;
    }
    if(Comando_entrada=='3'){
      digitalWrite(led, LOW);
      Serial.println("LED APAGADO");
      state = 0;
    }
    if(Comando_entrada=='4'){
      Serial.print("El valor del led es: ");
      Serial.println(state);
    }
    if(Comando_entrada>='5'){
      Serial.println("No valido");
    }
  }

}



//LINK VIDEO YOUTUBE: https://youtu.be/Mi9jFc6VjpQ?si=W5X2WPFwm2wRXZuh