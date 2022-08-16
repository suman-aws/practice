
#!/bin/bash

cmd() {
            if [[ $1 == *"int"* ]]; then
              echo "INT.host"           
            fi
            if [[ $1 == *"qa"* ]]; then
              echo "QA.host"           
            fi
            if [[ $1 == *"PROD"* ]]; then
             echo "PROD.host"           
            fi
        }
cmd
