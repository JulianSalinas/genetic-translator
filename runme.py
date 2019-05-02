#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------------------------------

import sys
import time
import gettext
from translator import *
from in_out import *


# ----------------------------------------------------------------------------------------------------------------------

# Traduce lo que se muestra en la opcion de ayuda al espanhol

def my_gettext(s):

    current_dict = {
        'usage: ': 'Modo de uso ',
        'optional arguments': 'Argumentos opcionales',
        'show this help message and exit': 'Mostrar esta ayuda y salir',
        'positional arguments': 'Argumentos posicionales',
        'the following arguments are required: %s': 'Los siguientes argumentos son requeridos: %s',
        'show program''s version number and exit': 'Mostrar la versión del programa y salir',
        'expected one argument': 'Se espera un argumento',
        'expected at least one argument': 'Se espera al menos un argumento'
    }
    if s in current_dict:
        return current_dict[s]
    return s

gettext.gettext = my_gettext

# ----------------------------------------------------------------------------------------------------------------------

# Mensajes que se mostran al ejecutar la ayuda (-h)

mod_help = \
    "Modo 1: Traductor de ADN a aminoácidos\n" \
    "Modo 2: Traductor de aminoácidos a ADN\n"

file_help = \
    "Nombre del archivo a traducir\n"

out_help = \
    "Nombre del archivo de salida\n"

string_help = \
    "Cadena que desea traducir\n"

format_help = \
    "Formato de entrada/salida de los aminoácidos" \
    "0. Formato de 3 letras" \
    "1. Nombre completo" \
    "N. Formato de 1 letra"

# ----------------------------------------------------------------------------------------------------------------------

# Interpreta los argumentos que son pasados por medio de la linea de comandos

import argparse


def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "-modo", help=mod_help, type=int, required=True)
    parser.add_argument("-f", "-formato", help=format_help, type=int, required=True)
    parser.add_argument("-a", "-archivo", help=file_help, type=str)
    parser.add_argument("-c", "-cadena", help=string_help, type=str)
    parser.add_argument("-s", "-salida", help=out_help, type=str)
    return parser


# ----------------------------------------------------------------------------------------------------------------------

def parse_args():
    cmdparser = init_argparse()
    try:
        arguments = cmdparser.parse_args()
    except IOError as msg:
        cmdparser.error(str(msg))
        sys.exit(-1)
    return arguments

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    print("\nTraductor genético versión 0.1.2")
    print("Hora de ejecución: " + time.strftime("%H:%M:%S"))

    args = parse_args()

    mod = args.m
    amin_format = args.f

    if not args.a and not args.c:
        print("Debe especificar una cadena o un nombre de archivo")
        sys.exit(-1)

    text = None

    if args.c:
        text = args.c

    elif args.a:
        text = get_file_content(args.a)
        if not text:
            sys.exit(-1)

    print("Entrada: " + text)

    out = None

    if mod == 1:

        text = text.upper()

        if not is_dna(text):
            print("Cadena inválida")
            sys.exit(-1)

        out = dna_to_amins(text, amin_format)

    elif mod == 2:
        out = amins_to_dna(text, amin_format)

    if args.s:
        write_file(out, args.s)
    else:
        print("Salida: " + ' '.join(out) + "\n")

# ----------------------------------------------------------------------------------------------------------------------
