#!/usr/bin/python3

import sys

# Recibe como entrada, desde stdin, pares de valores (del año 2024): mes, temperatura, 
# ordenados ascendentemente por mes.
# Para cada mes, entrega la temperatura máxima en el mismo.

last_key, max_val = None, -200		#Valores iniciales.
print("Mes\tTemp. máx")

for line in sys.stdin:
  key, val = line.strip().split("\t")	#Toma un par: mes, temperatura.

  if last_key and last_key != key:	  #Si hay cambio de mes:
    print (last_key, max_val/10.0)	  #imprime el mes actual y la temp. máxima.
    last_key, max_val = key, int(val)	  #Valores iniciales del nuevo mes.
  else:
    last_key, max_val = key, max(max_val, int(val))	#Máxima temperatura al
					#comparar la anterior leída con la actual.

if last_key:
  print(last_key, max_val/10.0)		    #Último mes y temp. máx.


