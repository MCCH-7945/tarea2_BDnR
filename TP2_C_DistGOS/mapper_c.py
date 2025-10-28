#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper (c): Distribución del Grado de Servicio (GoS) por operador móvil.
Versión flexible que imprime claves <operador,gos> → 1
"""

import sys

for i, line in enumerate(sys.stdin):
    # Ignorar encabezado si contiene letras
    if i == 0 and any(c.isalpha() for c in line):
        continue

    campos = line.strip().split(',')
    if len(campos) < 7:
        continue

    # Ajusta los índices después de ver tu head -1
    operador = campos[4].strip()
    gos = campos[6].strip()

    if operador and gos:
        print(f"{operador},{gos}\t1")

