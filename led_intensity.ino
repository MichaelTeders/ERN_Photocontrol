int blue = 10; 
int uv   = 11; 
 

int incomingByte;    
String command;  


void setup() {
  Serial.begin(9600);
  pinMode(blue, OUTPUT);
  pinMode(uv, OUTPUT);

}


void loop() {
    if(Serial.available()){
        command = Serial.readStringUntil('\n');
         
        if(command.equals("a100")){
             analogWrite(blue, 255);
             delay(1);
            analogWrite(uv, 255);           
        }
        else if(command.equals("b100")){
            analogWrite(blue, 255);
             delay(1);
            analogWrite(uv, 0); 
        }
        else if(command.equals("c100")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 255); 
        }
        else if(command.equals("d")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 0);
         }
        else if(command.equals("a50")){
            analogWrite(blue, 130);
             delay(1);
            analogWrite(uv, 130); 
         }
        else if(command.equals("b50")){
            analogWrite(blue, 130);
             delay(1);
            analogWrite(uv, 0);     
        }
        else if(command.equals("c50")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 130);     
        }        

        else if(command.equals("a25")){
            analogWrite(blue, 64);
             delay(1);
            analogWrite(uv, 64); 
         }
        else if(command.equals("b25")){
            analogWrite(blue, 64);
             delay(1);
            analogWrite(uv, 0);     
        }
        else if(command.equals("c25")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 64); }

        else if(command.equals("a75")){
            analogWrite(blue, 191);
             delay(1);
            analogWrite(uv, 191); 
         }
        else if(command.equals("b75")){
            analogWrite(blue, 191);
             delay(1);
            analogWrite(uv, 0);     
        }
        else if(command.equals("c75")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 191); }

     
        else if(command.equals("a10")){
            analogWrite(blue, 26);
             delay(1);
            analogWrite(uv, 26); 
         }
        else if(command.equals("b10")){
            analogWrite(blue, 26);
             delay(1);
            analogWrite(uv, 0);     
        }
        else if(command.equals("c10")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 26); }

         else if(command.equals("a20")){
            analogWrite(blue, 52);
             delay(1);
            analogWrite(uv, 52); 
         }
        else if(command.equals("b20")){
            analogWrite(blue, 52);
             delay(1);
            analogWrite(uv, 0);     
        }
        else if(command.equals("c20")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 52); }
          else if(command.equals("a80")){
            analogWrite(blue, 204);
             delay(1);
            analogWrite(uv, 204); 
         }
        else if(command.equals("b80")){
            analogWrite(blue, 204);
             delay(1);
            analogWrite(uv, 0);     
        }
        else if(command.equals("c80")){
            analogWrite(blue, 0);
             delay(1);
            analogWrite(uv, 204); }            
        else{
            Serial.println("Invalid command");
        }
    }
}
