#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (e): Calcula la latencia promedio por operador móvil.
Entrada esperada:
operador    latencia
"""

import sys

suma = {}
conteo = {}

for line in sys.stdin:
    try:
        operador, lat = line.strip().split('\t')
        lat = float(lat)
    except ValueError:
        continue

    suma[operador] = suma.get(operador, 0.0) + lat
    conteo[operador] = conteo.get(operador, 0) + 1

for operador in suma:
    promedio = suma[operador] / conteo[operador]
    print(f"{operador}\t{promedio:.2f}")

