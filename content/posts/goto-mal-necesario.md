date=2020-9-29
title=goto, un mal necesario
category=programacion
---

# GOTO, un mal necesario

*goto* es una instrucción en programación en el que saltas a una posición dentro de la ejecución del código.
Este salto puede ser tanto para atrás como hacia adelante. Funciona mas o menos así para que se entienda

    comienzo:
    if (algo) {
        goto final;
    }
    // algo
    goto comienzo:
    final:
    printf("bye");


Si uno ya tiene experiencia programando se ve que lo que hay entre *comienzo:* y *goto comienzo* se puede reemplazar por un *while*, y quizá se pueda reemplazar *goto final* por otra cosa.

goto no está en todos los lenguajes de programación, y que yo sepa solamente BASIC, C/C++, D y golang tienen esta instrucción (seguramente otros más) mas o menos como herencia portable de la instrucción de salto en ensablador *JMP*.

El caso es que muchas veces se ha utilizado esta instrucción en el mundo académico como una instrucción tabú
en el que si lo usas demuestras que eres un mal programador. Lo cierto es que hay proyectos importantes que usan *goto* como parte de su código y siempre respetando el estilo de programación estructurada. Para empezar:

* [En el proyecto del núcleo linux](https://github.com/torvalds/linux/search?q=goto)
* [CPython o la principal máquina virtual de Python](https://github.com/python/cpython/search?q=goto)
* [O en la principal implementación de Go](https://github.com/golang/go/search?p=1&q=goto)

¿Esto significa que son malos programadores? Para nada. *goto* es una herramienta mas que puede ser malusada, como
esos *if* o *for* anidados.
Basándose en el ejemplo anterior se puede hacer un bucle que cuente hasta 10 usando goto

    i := 0
    comienzo:
        i++
        fmt.Println(i)
        if i >= 10 {
            goto fin
        }
    goto comienzo
    fin:
    // algo

Y ahora usando *for*

    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }
    // fin


En el segundo ejemplo que usar *for* es mucho mas claro porque muestra la intención que es iterar mientras se cumpla la condición,
mientras que en el primero tienes que hacer un esfuerzo mental extra para saber qué se pretende hacer que este caso
es lo mismo que en el segundo.

Hay casos donde *goto* pueden ser bastante bien usado, como este:

    bool operacionCritica(cosa *uno) {
        // operaciones básicas de inicio
        bool resultado = true;
        // mas operaciones
        if (pasaAlgoMalo) {
            resultado = false;
            goto limpiar;
        }
        // mas operaciones, porque todo está bien
        limpiar:
        // operaciones de limpieza
        return resultado;
    }

o este:

    // este trozo está dentro de una función o método
    switch(tipo) {
        case FLACO:
            // operaciones en FLACO
            break;
        case CORTO:
            // operaciones en CORTO
            if (noConvence) { // si no convence a pesar de ser corto...
                goto adefault;
            }
            // mas operaciones en CORTO
            break;
        default: // hay mas tipos aparte de FLACO o CORTO
            adefault:
            // operaciones en default
            return NO;
            // el break no tiene sentido aqui si se devuelve un valor
    }
    return SI;


En estos casos las reglas con el *goto* son **no te repitas** y **mantenlo simple**. También nunca ir a hacer un salto hacia arriba, **siempre hacia abajo**.


Con todo esto intento demostrar que el *goto* bien usado es una instrucción que puede ayudar mucho en la claridad
del código. Siempre que sea posible se debe usar instrucciones de control de flujo como *if*, *for* o *switch*, que al fin y al cabo son goto glorificados para abstraer al programador de los saltos en el código.

Muchas gracias por leer.
