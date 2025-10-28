#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (f): Calcula el jitter promedio por operador móvil.
Entrada esperada:
operador    jitter
"""

import sys

suma = {}
conteo = {}

for line in sys.stdin:
    try:
        operador, jitter = line.strip().split('\t')
        jitter = float(jitter)
    except ValueError:
        continue

    suma[operador] = suma.get(operador, 0.0) + jitter
    conteo[operador] = conteo.get(operador, 0) + 1

for operador in suma:
    promedio = suma[operador] / conteo[operador]
    print(f"{operador}\t{promedio:.2f}")


