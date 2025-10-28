#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (h): Calcula la pérdida de paquetes promedio (packet loss) por operador móvil.
Emite pares clave-valor en el formato:
operador    perdida
"""

import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue  # Omitir encabezado si existe

    campos = line.strip().split(',')
    if len(campos) < 10:
        continue  # Evitar líneas incompletas

    operador = campos[4].strip()     # columna 5 → operador
    perdida = campos[-1].strip()     # última columna → pérdida de paquetes

    # Limpieza del valor: eliminar símbolo '%' y espacios
    perdida = perdida.replace('%', '').strip()

    # Evitar valores vacíos
    if perdida == '':
        continue

    try:
        loss = float(perdida)
        print(f"{operador}\t{loss}")
    except ValueError:
        continue

