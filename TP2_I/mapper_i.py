#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (i): Calcula la latencia promedio por operador móvil.
Emite pares clave-valor en el formato:
operador    latencia
"""

import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue  # Omitir encabezado si existe

    campos = line.strip().split(',')
    if len(campos) < 10:
        continue  # Evitar líneas incompletas

    operador = campos[4].strip()     # columna 5 → operador
    latencia = campos[8].strip()     # columna 9 → latencia (ajusta si necesario)

    # Limpieza del valor: eliminar "ms", "%", espacios
    latencia = latencia.lower().replace('ms', '').replace('%', '').strip()

    # Evitar valores vacíos
    if latencia == '':
        continue

    try:
        delay = float(latencia.replace(',', '.'))
        print(f"{operador}\t{delay}")
    except ValueError:
        continue

