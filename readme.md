BMC
===

```
ESCUELA DE INGENIERÍA EN COMPUTACIÓN
SEDE CARTAGO
II SEMESTRE 2017
BIOLOGÍA MOLECULAR COMPUTACIONAL
PROF: ESTEBAN ARIAS MENDEZ
```

## Integrantes ##
* [Johanna Elizondo Agüero]
* [Julian Salinas Rojas]

[Johanna Elizondo Agüero]: http://git.ec.tec.ac.cr/u/joelizondo
[Julian Salinas Rojas]: http://git.ec.tec.ac.cr/u/jsalinas

## Tarea 1: Traductor genético

El programa cuenta con dos modos principales:

* _Modo 1_ : Traductor de ADN a aminoácidos Modo
* _Modo 2_: Traductor de aminoácidos a ADN

Para ver como se debe ejecutar el programa use el siguiente comando
estado dentro de la carpeta del proyecto:

```
$ python runme.py -h
```

Esto mostrará la siguiente ayuda de como debe ejecutar el programa:

```
Traductor genético versión 0.1.2
Hora de ejecución: 00:04:00

Modo de uso runme.py [-h] -m M -f F [-a A] [-c C]

Arugmentos opcionales:
  -h,   --help      Mostrar esta ayuda y salir
  -m M, -modo M     Modo 1: Traductor de ADN a aminoácidos
                    Modo 2: Traductor de aminoácidos a ADN
  -f F, -formato F  Formato de entrada/salida de los aminoácidos0. Formato de
                    3 letras1. Nombre completoN. Formato de 1 letra
  -a A, -archivo A  Nombre del archivo a traducir
  -c C, -cadena C   Cadena que desea traducir
  -s S, -salida S   Nombre del archivo de salida
```

##### Notas
* Si no se coloca el argumento para -a se debe especificar el argumento para -c
* Si no se especifica una ruta de salida -s, el resultado solo se imprimirá en la consola

##### Ejemplos del modo 1: Traducir de ADN a aminoácidos

```
$ python runme.py -m 1 -f 0 -a tests_files/test_mod_1
    Entrada: ACCGGGTTCAGTGACGTACGTACAACCGGT
    Salida: THR GLY PHE SER ASP VAL ARG THR THR GLY
```

```
$ python runme.py -m 1 -f 0 -c ACCGGGTTCAGTGACGTACGTACAACCGGT
    Entrada: ACCGGGTTCAGTGACGTACGTACAACCGGT
    Salida: THR GLY PHE SER ASP VAL ARG THR THR GLY
```

```
$ python runme.py -m 1 -f 1 -a tests_files/test_mod_1
    Entrada: ACCGGGTTCAGTGACGTACGTACAACCGGT
    Salida: THREONINE GLYCINE PHENYLALANINE SERINE ASPARTIC_ACID
            VALINE ARGININE THREONINE THREONINE GLYCINE
```

```
$ python runme.py -m 1 -f 2 -a tests_files/test_mod_1
    Entrada: ACCGGGTTCAGTGACGTACGTACAACCGGT
    Salida: T G F S D V R T T G
```

##### Ejemplos del modo 2: Traducir de aminoácidos a ADN

Recordar que la salida son todas las posibles cadenas de ADN de las que se partió para formar dichos aminoácidos

```
$ python runme.py -m 2 -f 0 -a tests_files/test_mod_2_format_0
    Entrada: THR GLY
    Salida: ACTGGT ACTGGC ACTGGA ACTGGG ACCGGT ACCGGC ACCGGA ACCGGG
            ACAGGT ACAGGC ACAGGA ACAGGG ACGGGT ACGGGC ACGGGA ACGGGG
```

```
$ python runme.py -m 2 -f 1 -a tests_files/test_mod_2_format_1
    Entrada: THREONINE GLYCINE
    Salida: ACTGGT ACTGGC ACTGGA ACTGGG ACCGGT ACCGGC ACCGGA ACCGGG
            ACAGGT ACAGGC ACAGGA ACAGGG ACGGGT ACGGGC ACGGGA ACGGGG
```

```
$ python runme.py -m 2 -f 2 -a tests_files/test_mod_2_format_2
    Entrada: T G
    Salida: ACTGGT ACTGGC ACTGGA ACTGGG ACCGGT ACCGGC ACCGGA ACCGGG
            ACAGGT ACAGGC ACAGGA ACAGGG ACGGGT ACGGGC ACGGGA ACGGGG
```
