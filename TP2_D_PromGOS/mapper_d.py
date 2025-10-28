#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (d): Promedio del Grado de Servicio (GoS) por operador móvil.
"""

import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue  # Omitir encabezado

    campos = line.strip().split(',')
    if len(campos) < 8:
        continue

    operador = campos[4].strip()  # columna 5
    gos = campos[7].strip()       # columna 8  ← AJUSTE AQUÍ

    try:
        gos_val = float(gos)
        print(f"{operador}\t{gos_val}")
    except ValueError:
        continue

