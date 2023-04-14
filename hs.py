#!/usr/bin/env python3

import subprocess

output = subprocess.check_output(["python3", "prepare_new_deployment.py"]).decode().split("\n")

for line in output:
  parts = line.split("=")

  for j in range(6):
    if j == 0:
      env = parts[j]
    elif j == 1:
      context = parts[j]
    elif j == 2:
      model = parts[j]
    elif j == 3:
      version = parts[j]
    elif j == 4:
      sysuid = parts[j]
    elif j == 5:
      testingtime = parts[j]

  print("Env:", env)
  print("Deployment Context:", context)
  print("Model Names:", model)
  print("Model Versions:", version)
  print("SystemUIDs:", sysuid)
  print("TestingTime:", testingtime)
