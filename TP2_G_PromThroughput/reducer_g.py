#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (g): Calcula el throughput promedio por operador móvil.
Entrada esperada:
operador    throughput
"""

import sys

suma = {}
conteo = {}

for line in sys.stdin:
    try:
        operador, tput = line.strip().split('\t')
        tput = float(tput)
    except ValueError:
        continue

    suma[operador] = suma.get(operador, 0.0) + tput
    conteo[operador] = conteo.get(operador, 0) + 1

for operador in sorted(suma.keys()):
    promedio = suma[operador] / conteo[operador]
    print(f"{operador}\t{promedio:.2f}")

