
#!/bin/bash

envir=$1
echo $envir

cmd() {
        if [[ $envir == *"int"* ]]; then
          echo "INT.host"           
        fi
        if [[ $envir == *"qa"* ]]; then
          echo "QA.host"           
        fi
        if [[ $envir == *"PROD"* ]]; then
         echo "PROD.host"           
        fi
      }
cmd        
