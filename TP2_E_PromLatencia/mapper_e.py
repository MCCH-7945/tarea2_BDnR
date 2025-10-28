#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (e): Calcula la latencia promedio por operador móvil.
Emite pares clave-valor en el formato:
operador    latencia
"""

import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue  # Omitir encabezado

    campos = line.strip().split(',')
    if len(campos) < 9:
        continue

    operador = campos[4].strip()   # columna del operador
    latencia = campos[8].strip()   # columna de latencia (ajustar según CSV)

    try:
        lat = float(latencia)
        print(f"{operador}\t{lat}")
    except ValueError:
        continue

