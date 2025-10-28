#!/usr/bin/python3

import sys

# Lee, desde la entrada estándar (stdin), líneas de texto relacionadas con lecturas
# de temperatura tomadas en diferentes estaciones de monitoreo.
# El archivo de entrada de ejemplo es de temperaturas tomadas en cada mes del año 2024 
# (los valores está multiplicados por 10).
# De los diferentes valores que aparecen en cada línea, sólo se utilizan
# el del mes (posiciones 20 y 21) y el de la temperatura (posiciones 88 a 91), 
# que son los valores que el programa entrega en la salida estándar (stdout).

for line in sys.stdin:
  val = line.strip()
  month, temp = val[19:21], val[87:92]
  if (temp != "+9999"):
    print(month, "\t", temp)

