Title: Function decorators @
Date: 2017-03-19
Category: Python
Tags: Programming, decorators
Slug: function-decorators
Lang: en
Status: draft

Function decorators @
=====================

Function decorators are mainly used to extend functions without inheritance.

Python functions are first-class objects. You can pass a function as argument to a function, even return a function. Also a function can be defined inside another function!

Here a simple example. We want to create a function which will add "Hello " to any string that is returned from the function that is passed as parameter.

    :::python

    def hello(func):
        def wrapped():
            return "Hello " + func()
        return hello_inner

    def input_name():
        return input("Your name: ")

    input_name_wrapped = hello(input_name)

    print(input_name_wrapped())
    Your name: Me
    Hello Me

Yes, basically are closures (like JavaScript). But this is not all. What if we replace *input_name_wrapped* by *input_name*?

    :::python

    input_name = hello(input_name)

    print(input_name())
    Your name: Me
    Hello Me

Well, I think things are getting interesting. The same function name input_name is used for the the same wrapped input_name and we want to do this some times with others functions as well.

There is a shortcut? Yes, function decorators.

    :::python

    @hello
    def input_name():
        return input("Your name: ")

Simple like that. It's just sintactic sugar. This code does the same that all before, in just fewer lines.

There is a problem with our function decorator hello: the wrapped function arguments are restricted to the same number that the function decorated. We can't decorate a function like random_input(list) because has 1 parameter and we defined our wrapped function with none parameters.

Let's solve this.

    :::python
    def hello(func):
        def wrapped(*args, **kargs):
            return "Hello " + func(*args, **kargs)
        return wrapped

We pass variable argument list to functions. *args is a list of values and **kargs is a dictionary of values associated with keys.

Now we can do things like this

    :::python

    @hello
    def input_name()
        return input("Name ")

    @hello
    def random_name(names, times=1)
        """
        'names' is an iterable of strings
        """
        from random import choice
        if times < 1: return ''
        chosen_ones = ''
        for i in range(times):
            chosen_ones += choice(names) + ', '
        return chosen_ones.rstrip(', ')

    print(input_name())
    Your name: Pedro
    Hello Pedro

    print(random_name(("José", "Clara", "Pedro", "Ana")))
    Hello Pedro
    print(random_name(("José", "Clara", "Pedro", "Ana")))
    print(random_name(("José", "Clara", "Pedro", "Ana"), 7))
    Hello Pedro, Pedro, Clara, Clara, Ana, José, Ana
    print(random_name(("José", "Clara", "Pedro", "Ana"), times=4))
    Hello Ana, Ana, José, Pedro

You can chain decorators

    :::python
    def paragraph(func)
        def wrapped(*args, **kargs):
            return '<p>' + func(*args, **kargs) +' </p>'

    @paragraph
    @hello
    def get_from_file(filename):
        """
        We do operations with a file and we return a name

        file = open(filename)
        for l in file:
            if l.startswith("user: "):
                name = l.split(':')[1].strip()
        file.close()

        But this is a 'black box' :)

        """
        name = "Mimikyu"
        return name



## Summary

A fuction decorator is a function that takes a function and returns a wrapped function that uses the passed function.

## There is more

We have decorators use parameters than are not functions, methods that are decorators, even class decorators. Python [has a module with tools for high-order functions](https://docs.python.org/3.5/library/functools.html).
