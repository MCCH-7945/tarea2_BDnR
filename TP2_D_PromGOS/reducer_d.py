#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (d): Calcula el promedio del Grado de Servicio (GoS) para cada operador móvil.
Entrada esperada:
operador    gos
"""

import sys

suma = {}
conteo = {}

for line in sys.stdin:
    try:
        operador, gos = line.strip().split('\t')
        gos = float(gos)
    except ValueError:
        continue

    suma[operador] = suma.get(operador, 0.0) + gos
    conteo[operador] = conteo.get(operador, 0) + 1

for operador in suma:
    promedio = suma[operador] / conteo[operador]
    print(f"{operador}\t{promedio:.2f}")

