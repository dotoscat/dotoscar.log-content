Title: Square root of a number with Newton's method
Date: 2017-01-08
Category: Python
Tags: maths, playing
Slug: sqrt-newton
Lang: en
Authors: Oscar Triano 'dotoscat'

Let's make our version of sqrt using the [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number)

Let's use two ways: One is procedural, the other one is functional

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

Sure that this is a straightforward way to solve a problem. You'll see the number the number
0.001. This number is a way to assure that the program will return z if z is more or less close to 0.
As note: In procedural programming there are states, and if there are states then there are mutable data.

    :::python
    sqrt_newton_rec(9.0)
    3.000000001396984

##Functional

    #!python
    def sqrt_newton_rec(x, z=1.0, last_z=None):
    	if z == 1.0: return sqrt_newton_rec(x, z - ((z*z - x)/(2.0*z)), None)
    	if last_z is not None and last_z - z < 0.001:
    		return z
    	return sqrt_newton_rec(x, z - ((z*z - x)/(2.0*z)), z)

From here things are a bit tricky. No loops. Only recursive calls. And no states,
only we will pass results to the next function call.
Did you see the line 2? Without this line the recursive function is equivalent to
this function

    #!python
    def sqrt_newton(x):
	    z = 1.0
	    last_z = None
	    while True:
            z = z - ((z*z - x)/(2.0*z))
	        last_z = z
	        if last_z is not None and last_z - z < 0.001:
		        return z

last_z = z is assigned after the assignation to z, giving wrong results.

How do we start this? An example

    :::python
    sqrt_newton_rec(9.0)
    3.000000001396984

##Benchmarks

Now the benchmarks, which is faster? Python has some nice profiles modules.
Let's use the module timeit. This module is for small pieces of code.

99*99 is 9801, and the square root of 9801 is 99

    :::python
    import timeit

    timeit.repeat('sqrt_newton_rec(99*99)', globals=globals())
    [5.687824495602399, 5.532753252373368, 5.615399405985954]

    timeit.repeat('sqrt_newton(99*99)', globals=globals())
    [4.547379188610648, 4.452797279736842, 4.643888148973929]

The time for the recursive fuction is around 5.6 secs, and for the procedural function
around 4.5 secs. The recusive function is 1.2 slower than the other function.

And that's all, for the moment :)
