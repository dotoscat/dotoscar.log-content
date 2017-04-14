Title: standalone executables with cx_Freeze
Date: 2017-04-14
Category: Python
Tags: python, development
Authors: Oscar Triano 'dotoscat'
Slug: en
Lang: en

cx_Freeze is a set of utilities that help us build a Python executable.
This is ideal for distribute Python applications for end users, specially
Windows users, without worrying about whether they have installed a Python environment or not.

cx_Freeze installation is simple

    :::shell
    pip install cx_Freeze

cx_Freeze will gave us [up to three ways](http://cx-freeze.readthedocs.io/en/latest/overview.html) to use the tools, being one of them
a command program. The other one is an utility script *cxfreeze-quickstart* that creates
a *setup.py* based on *distutils*.

## Our hello world program

Let's create a simple "hello world" program.
We want an additional and optional parameter to replace "world"

    :::python
    #!/usr/bin/env python

    import sys

    who = 'world'

    if len(sys.argv) > 1:
        who = sys.argv[1]

    print('hello {}'.format(who))

Save it as *hello.py*.

Let's test it

    :::shell
    > ./hello.py
    hello world
    > ./hello.py me
    hello me

This is looking good. This program could be any useful program (or game) we
want to distribute and be used effortless by our users in Windows.

`cxfreeze hello.py`

This will create an *main.exe* on *dist* folder (it will created for us).

    :::shell
    > cd dist
    > hello
    hello world

Compress *dist* folder, rename it as you wish (*hello-world* for example) and we are done.

*dist* folder size is around 10 MB, and compressed with zip around 5 MB. Of course, this is much for a simple hello world program. The idea is to distribute
more complex but small programs or just whole Python applications with cx_Freeze.
