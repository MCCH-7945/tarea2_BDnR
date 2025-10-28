#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (f): Calcula el jitter promedio por operador móvil.
Emite pares clave-valor en el formato:
operador    jitter
"""

import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue  # Omitir encabezado

    campos = line.strip().split(',')
    if len(campos) < 10:
        continue

    operador = campos[4].strip()   # columna del operador móvil
    jitter = campos[9].strip()     # columna del jitter (ajustar si cambia el orden)

    try:
        jitter_val = float(jitter)
        print(f"{operador}\t{jitter_val}")
    except ValueError:
        continue

