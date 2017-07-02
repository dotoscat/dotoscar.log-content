POO hecho bien
##############

date: 2017-07-01
category: Python
tags: python, OOP
slug: oop-done-right
authors: Oscar Triano 'dotoscat'
lang: es

Se tiene entendido que la programación orientado a objetos es para representar
objetos de un mundo. Son un conjunto de atributos, o datos, más funciones, o métodos,
que manejan todo el conjunto. Los objetos se pasan mensajes entre sí para comunicarse
que son a través de esos métodos.

En Python todo es un objeto (isinstance(3, int) es una prueba de ello), hasta las mismas
clases. Una clase es como una plantilla de cómo será construido un objeto.

Vamos a crear la típica clase de una persona. Tendrá un nombre,
tiempo de creación (nacimiento) y tiempo vivo (edad).
Una primera aproximación sería esta:

.. code-block:: python

    from time import time

    class Persona:
        def __init__(self):
            self.nombre = ""
            self.nacimiento = time()
            self.edad = 0.0
            
        def set_nombre(self, nombre):
            self.nombre = nombre
            
        def get_nombre(self):
            return self.nombre
        # Más metodos, getters y setters
    
    # Se crea un instancia y se manipula
            
    persona = Persona()
    persona.nombre = 'Oscar'
    persona.nacimiento = 1
    persona.edad = 1000
    print(persona.get_nombre())

Aquí nuestro objeto. Es válido tratar nuestro objeto como una simple estructura
de datos pero la idea es programar orientado a objetos. El acceso a los atributos
es fácil, y con los despistes cuando el código esté funcionando dará sorpresas.
Los métodos definidos, getters y setters, son redundantes.

No queremos que los atributos se manipulen así de fácil. En Python todos
los atributos son públicos y para indicar que no se deben tocar se le pone '_' delante
del nombre del atributo como convención para indicar que son privados.

Con esto quedaría ahora así

.. code-block:: python

    from time import time

    class Persona:
        def __init__(self):
            self._nombre = ""
            self._nacimiento = time()
            self._edad = 0.0
            
        def set_nombre(self, nombre):
            self._nombre = nombre
            
        def get_nombre(self):
            return self._nombre
        # Más metodos, getters y setters
    
    persona = Persona()
    persona.set_nombre('Oscar')
    persona._nacimiento = 1
    persona._edad = 1000
    print(persona.get_nombre())

NO se deben tocar los atributos si se indican, así que a partir de ahora
no se va a manipular directamente los atributos. Ahora los getters y los setters son más necesarios que nunca.
Además, los getters y los setters dan más control en la manipulación del objeto.

En una persona nos interesa saber su nombre, cambiar su nombre, su nacimiendo y la
edad que tiene. Vamos a ello. Se va a relajar en cómo se van a llamar los setters y getters.
Con esto...

.. code-block:: python

    from time import time

    class Persona:
        def __init__(self, nombre):
            self.poner_nombre(nombre)
            self._nacimiento = time()
            
        def poner_nombre(self, nombre):
            if not len(nombre): raise Exception("Pone un nombre a {}".format(self))
            self._nombre = nombre
            
        def obtener_nombre(self):
            return self._nombre
            
        def obtener_nacimiento(self):
            return self._nacimiento
            
        def obtener_edad(self):
            return time() - self._time
    
    persona = Persona("Oscar")
    print(persona.get_nombre())
