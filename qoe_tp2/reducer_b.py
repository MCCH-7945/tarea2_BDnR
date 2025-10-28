#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (b): Calcula el porcentaje de cada tipo de dispositivo dentro de cada operador.
Entrada esperada (ya ordenada):
operador,dispositivo    1
"""

import sys

cuenta = {}      # Conteo por (operador, dispositivo)
totales = {}     # Totales por operador

for line in sys.stdin:
    try:
        key, val = line.strip().split('\t')
        operador, disp = key.split(',')
        val = int(val)
    except ValueError:
        continue

    cuenta[(operador, disp)] = cuenta.get((operador, disp), 0) + val
    totales[operador] = totales.get(operador, 0) + val

for (operador, disp), c in cuenta.items():
    total = totales.get(operador, 0)
    pct = (c / total) * 100 if total > 0 else 0
    print(f"{operador},{disp}\t{pct:.2f}%")




