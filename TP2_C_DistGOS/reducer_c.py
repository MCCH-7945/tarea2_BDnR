#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reducer (c): Calcula la distribución porcentual del Grado de Servicio (GoS)
para cada operador móvil.
Entrada esperada (ya ordenada):
operador,gos    1
"""

import sys

cuenta = {}      # Conteo por (operador, gos)
totales = {}     # Total de registros por operador

for line in sys.stdin:
    try:
        key, val = line.strip().split('\t')
        operador, gos = key.split(',')
        val = int(val)
    except ValueError:
        continue

    cuenta[(operador, gos)] = cuenta.get((operador, gos), 0) + val
    totales[operador] = totales.get(operador, 0) + val 
    print(f"DEBUG: {line.strip()}", file=sys.stderr)

for (operador, gos), c in cuenta.items():
    total = totales.get(operador, 0)
    pct = (c / total) * 100 if total > 0 else 0
    print(f"{operador},{gos}\t{pct:.2f}%")

