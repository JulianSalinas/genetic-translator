#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------------------------------

import numpy as np
from tables import *


# ----------------------------------------------------------------------------------------------------------------------

# Genera un n aleatorio basado en la distribución normal, donde n pertenece al rango [-dev_std+med, +dev_std+med]
def random_normal_dist(mean=0, std=1):
    return np.random.normal(mean, std)


# ----------------------------------------------------------------------------------------------------------------------

# Genera un n aleatorio basado en la distribución de Poisson, el lambda es opcional
def random_poisson_dist(lambda_val=22):
    return np.random.poisson(lambda_val)


# ----------------------------------------------------------------------------------------------------------------------

# Genera un n aleatorio basado en la distribución lineal
def random_lineal_dist(inicio=0, fin=0):
    return np.random.randint(inicio, fin + 1)


# ----------------------------------------------------------------------------------------------------------------------

# Retorna true si la cadena solo contiene los caracteres A,C,G o T
def is_dna(string):
    string = string.upper()
    for char in string:
        if not complement_table.__contains__(char):
            return False
    return True


# ----------------------------------------------------------------------------------------------------------------------

# Retorna true si la cadena solo contiene los caracteres A,C,G o U
def is_rna(string):
    s = string.upper()
    return len(string) == s.count('A') + s.count('C') + s.count('G') + s.count('T')


# ----------------------------------------------------------------------------------------------------------------------

# Largo de una cadena
def string_lenght(string):
    return len(string)


# ----------------------------------------------------------------------------------------------------------------------

# Obtiene el elemento i de una cadena empezando desde 1
def get_string_element(string, element_i):
    return string[element_i-1]


# ----------------------------------------------------------------------------------------------------------------------

# Retorna true si 'possible_subsec' es subsecuencia del string
def is_sub_sec(possible_subsec, string):
    return all(sym in iter(string) for sym in possible_subsec)


# ----------------------------------------------------------------------------------------------------------------------

# Retorna true si 'possible_supsec' es supersecuencia del string
def is_super_sec(possible_supsec, string):
    return is_sub_sec(string, possible_supsec)


# ----------------------------------------------------------------------------------------------------------------------

# Retorna true si 'possible_substr' es substring del string
def is_sub_str(possible_substr, string):
    return not string.find(possible_substr) == -1


# ----------------------------------------------------------------------------------------------------------------------

# Retorna true si 'possible_supstr' es superstring del string
def is_sup_str(possible_supstr, string):
    return not is_sub_str(string, possible_supstr)


# ----------------------------------------------------------------------------------------------------------------------

# Retorna una subcadena de 'string' según el intervalo dado (la cadena inicia desde 1)
def get_interval(start, end, string):
    return string[start-1:end]


# ----------------------------------------------------------------------------------------------------------------------

# Retorna la unión de todas los strings pasados por parámetro
def concat_strings(*strings):
    return ''.join([string for string in strings])


# ----------------------------------------------------------------------------------------------------------------------

# Retorna el prefijo de un string hasta el indice indicado
def get_prefix(index, string):
    return string[:index]


# ----------------------------------------------------------------------------------------------------------------------

# Retorna el sufijo de un string desde el indice indicado
def get_sufix(index, string):
    return string[len(string) - index:]


# ----------------------------------------------------------------------------------------------------------------------

# True si 'possible_prefix' es prefijo de la cadena ingresada
def is_prefix(possible_prefix, string):
    return string.startswith(possible_prefix)


# ----------------------------------------------------------------------------------------------------------------------

# True si 'possible_prefix' es prefijo de la cadena ingresada
def is_suffix(possible_sufix, string):
    return string.endswith(possible_sufix)


# ----------------------------------------------------------------------------------------------------------------------

# Sustituye los carácteres de la cadena según 'complement_table' ej.(ACTG -> TGAC)
def complement_dna(string):
    complement = ''
    for c in string.upper():
        complement += complement_table[c]
    return complement


# ----------------------------------------------------------------------------------------------------------------------

# Realiza lo mismo que 'complement_dna' pero de final a inicio ej.(ACTG -> CAGT)
def inverse_complement_dna(string):
    return complement_dna(string)[::-1]


# ----------------------------------------------------------------------------------------------------------------------

# True si la cadena se lee igual al invertirla
def is_palindrome(string):
    return string == string[::-1]


# ----------------------------------------------------------------------------------------------------------------------
