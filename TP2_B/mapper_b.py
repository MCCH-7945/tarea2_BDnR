#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (b): Porcentaje del tipo de dispositivo por operador móvil.
Lee el archivo regqoe100.csv y emite pares clave-valor en el formato:
operador,dispositivo    1
"""

import sys

for line in sys.stdin:
    campos = line.strip().split(',')
    if len(campos) < 10:
        continue

    operador = campos[4].strip()   # Id del operador móvil (MNO)
    disp = campos[2].strip()       # Tipo de dispositivo

    if operador.isdigit() and disp.isdigit():
        print(f"{operador},{disp}\t1")

