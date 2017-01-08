Title: Square root of a number with Newton's method
Date: 2017-01-08
Category: Python
Tags: maths, playing
Slug: sqrt-newton
Lang: es
Authors: Oscar Triano 'dotoscat'

Vamos hacer nuestra propia version de la raíz cuadrada usando el [método de Newton](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Newton)

Vamos a usar dos formas: Una es procedural, el otro es funcional

##Procedural

    #!python
    def sqrt_newton(x):
	    z = 1.0
	    last_z = None
	    while True:
            z = z - ((z*z - x)/(2.0*z))
		    if last_z is not None and last_z - z < 0.001:
			     return z
		    last_z = z

Seguro que  esta es una forma directa de resolver un problema. Verás el número 0.001.
Este número es una forma de asegurar que el programa devolverá z si z está mas o menos cerca de 0.
Como nota: En la programación procedural hay estado, y si hay estados entonces hay datos mutables.

    :::python
    sqrt_newton_rec(9.0)
    3.000000001396984

##Funcional

    #!python
    def sqrt_newton_rec(x, z=1.0, last_z=None):
    	if z == 1.0: return sqrt_newton_rec(x, z - ((z*z - x)/(2.0*z)), None)
    	if last_z is not None and last_z - z < 0.001:
    		return z
    	return sqrt_newton_rec(x, z - ((z*z - x)/(2.0*z)), z)

Desde aquí las cosas son un poco complicadas. No hay bucles. Solamante llamadas recursivas. Y no hay estados, solamente pasamos los resultados a la siguiente llamada de la función.
¿Viste la línea 2? Si esa línea la función recursiva es equivalente a esta función 

    #!python
    def sqrt_newton(x):
	z = 1.0
	last_z = None
	while True:
        z = z - ((z*z - x)/(2.0*z))
	    last_z = z
	    if last_z is not None and last_z - z < 0.001:
		    return z

last_z = z es asignado después de la asignación a z, dando resultados equivocados.

¿Cómo empezamos esto? Un ejemplo

    :::python
    sqrt_newton_rec(9.0)
    3.000000001396984

##Comparaciones

Ahora las Comparaciones, ¿cuál es rápido? Python tiene algunos modulos para medir el tiempo de ejecución
Vamos a usar el módulo timeit. Este módulo es para trozos de código.

99*99 is 9801, y la raíz cuadrada de 9801 es 99

    :::python
    import timeit

    timeit.repeat('sqrt_newton_rec(99*99)', globals=globals())
    [5.687824495602399, 5.532753252373368, 5.615399405985954]

    timeit.repeat('sqrt_newton(99*99)', globals=globals())
    [4.547379188610648, 4.452797279736842, 4.643888148973929]

El tiempo para la función recursiva es de unos 5.6 segundos, y para la función procedural sobre 4.5 segundos.
La función recursiva es 1.2 más lenta que la otra función.

Y eso es todo, por el momento :)
