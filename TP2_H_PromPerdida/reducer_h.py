#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (h): Calcula la pérdida de paquetes promedio por operador móvil.
Entrada esperada:
operador    perdida
"""

import sys

suma = {}
conteo = {}

for line in sys.stdin:
    try:
        operador, loss = line.strip().split('\t')
        loss = float(loss)
    except ValueError:
        continue

    suma[operador] = suma.get(operador, 0.0) + loss
    conteo[operador] = conteo.get(operador, 0) + 1

for operador in sorted(suma.keys()):
    promedio = suma[operador] / conteo[operador]
    print(f"{operador}\t{promedio:.2f}")

