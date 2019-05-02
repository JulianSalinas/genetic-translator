#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ----------------------------------------------------------------------------------------------------------------------

# Obtiene el contenido de un archivo de texto, si el archivo no existe, el contenido retornado sera ''

def get_file_content(file_path="default.in"):

    content = ''
    try:
        file = open(file_path)
        content = file.read()
        file.close()
    except IOError:
        print("El arhivo " + file_path + " no existe o no se ha podido leer")
    return content


# ----------------------------------------------------------------------------------------------------------------------

# Escribe texto en un archivo.
# Si no especficar el nombre/ruta el archivo se crea en la misma carpeta que este archivo con el nombre default.out

def write_file(content, file_path='default.out'):

    try:
        file = open(file_path, "w+")
        file.write(content)
        file.close()
    except IOError:
        print("Error al escribir el archivo " + file_path)

# ----------------------------------------------------------------------------------------------------------------------

