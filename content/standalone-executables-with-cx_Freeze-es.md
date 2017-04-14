Title: standalone executables with cx_Freeze
Date: 2017-04-14
Category: Python
Tags: python, development
Authors: Oscar Triano 'dotoscat'
Slug: intro-cxFreeze
Lang: es

cx_Freeze es un conjunto de utilidades que nos ayuda a construir un ejecutable de Python.
Esto es idea para distribuir aplicaciones de Python para usuarios finales, especialmente usuarios de Windows, sin preocuparse que tengan instalado un entorno de Python.

La instalación de cx_Freeze es simple

    :::shell
    pip install cx_Freeze

cx_Freeze nos dará hasta [tres formas](http://cx-freeze.readthedocs.io/en/latest/overview.html) de usar las herramientas, siendo una de ellas un programa para la consola. El otro es un asistente *cxfreeze-quickstart* que crea un *setup.py* basado en *distutils*.

## Nuestro programa hello world

Vamos a crear un programa "hello world".
Queremos un parámetro adicional y opcional para reemplazar "mundo".

    :::python
    #!/usr/bin/env python

    import sys

    who = 'world'

    if len(sys.argv) > 1:
        who = sys.argv[1]

    print('hello {}'.format(who))

Guardarlo como *hello.py*.

Vamos a probarlo

    :::shell
    > ./hello.py
    hello world
    > ./hello.py me
    hello me

Esto se ve bien. Este programa podría cualquier programa útil (o juego) que queremos distribuir y ser usado sin esfuerzo por nuestro usuarios en Windows.

`cxfreeze hello.py`

Esto creará un *hello.exe* en la carpeta *dist* (será creada por nosotros).

    :::shell
    > cd dist
    > hello
    hello world

Comprime la carpeta *dist*, renómbrala como quieras (*hello-world* por ejemplo) y hemos acabado.

El tamaño de la carpeta *dist* es sobre 10 MB, y comprimido con zip sobre 5 MB. Por supuesto, esto es mucho para un simple hola mundo. La idea es distribuir programas más complejos pero más pequeños o solamente toda una aplicación en Python con cx_Freeze.
