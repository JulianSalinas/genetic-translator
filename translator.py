#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------------------------------

import re
import random
import itertools as it
from util import *
from tables import *


# ----------------------------------------------------------------------------------------------------------------------

# Retorna una secuencia random de ADN según el largo especificado
def random_sec_dna(size):
    bases = list(complement_table.keys())
    return ''.join([random.choice(bases) for i in range(size + 1)])


# ----------------------------------------------------------------------------------------------------------------------

# Proceso de transcripcion del ADN, primero complementa y luego sustituye 'T' por 'U'
def dna_to_rna(string):
    return complement_dna(string).replace('T', 'U')


# ----------------------------------------------------------------------------------------------------------------------

# Funcion para convertir de una cadena de ADN en aminoacidos
# amin_format:  0. Formato de 3 letras
#               1. Nombre completo
#               N. Formato de 1 letra

def dna_to_amins(dna_string, amin_format=2):
    codons = re.findall('...', dna_string.upper())
    amins = [codon_to_amin_tab[codon] for codon in codons]
    if 0 <= amin_format < 2:
        amins = [amin_format_tab[amin][amin_format] for amin in amins]
    return amins


# ----------------------------------------------------------------------------------------------------------------------

# Funcion para convertir de una cadena de aminoacidos a todas las combinaciones de ADN
# Se debe indicar el formato de entrada de los aminoacidos, que es el mismo usando en la funcion anterior

def amins_to_dna(amins_string, amin_format=2):
    amins = reformat_aminoacids(re.findall("\w+", amins_string), amin_format)
    combinations = amin_to_codon_tab[amins[0]]
    for i in range(1, len(amins)):
        codons = amin_to_codon_tab[amins[i]]
        combinations = [x + y for x, y in it.product(combinations, codons)]
    return combinations


# ----------------------------------------------------------------------------------------------------------------------

# Cambia los aminoacidos a formato de una letra para poder procesarlos con la funcion anterior
# Se debe indicar el formato de entrada de los aminoacidos, que es el mismo usando en la funcion anterior

def reformat_aminoacids(amins_list, amin_format=2):
    slc_amins = []
    if 0 <= amin_format < 2:
        for amin in amins_list:
            for key, value in amin_format_tab.items():
                if amin == value[amin_format]:
                    slc_amins.append(key)
    return amins_list if len(slc_amins) == 0 else slc_amins

# ----------------------------------------------------------------------------------------------------------------------
