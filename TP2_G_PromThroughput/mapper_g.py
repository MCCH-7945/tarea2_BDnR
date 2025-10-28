#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (g): Calcula el throughput promedio por operador móvil.
Emite pares clave-valor en el formato:
operador    throughput
"""

import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue  # Omitir encabezado si existe

    campos = line.strip().split(',')
    if len(campos) < 10:
        continue  # Evitar líneas incompletas

    operador = campos[4].strip()     # columna 5 → operador
    throughput = campos[9].strip()   # columna 10 → throughput

    # Limpieza: eliminar unidades o símbolos, como "kbps" o "%"
    throughput = throughput.lower().replace('kbps', '').replace('%', '').strip()

    # Evitar valores vacíos
    if throughput == '':
        continue

    try:
        tput = float(throughput.replace(',', '.'))
        print(f"{operador}\t{tput}")
    except ValueError:
        continue

