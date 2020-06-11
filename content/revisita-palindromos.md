title: Revisita a los palindromos
category: Programación
date: 2019-9-8
script: es-palindromo.js

Hace tiempo hice de práctica con haskell una función que determinaba si una palabra era palíndroma o no.
La implementación que hice era bastante sencilla para lo que me pedía el ejercicio

    esPalindromo xs
    | xs == [] = False
    | odd (length xs) = False --es impar?
    | otherwise = 
        drop mitad xs == reverse (take mitad xs) 
        where
            mitad = div (length xs) 2

Hace uso de funciones ya definidas en el lenguaje, y tiene un fallo enorme: Dice que la palabra no es palíndroma si su longitud es impar.
Por cosas de prácticas [hice un curso de khan academy sobre algoritmos](https://es.khanacademy.org/computing/computer-science/algorithms) y ahí aprendí de forma apropiada como hacer la función en condiciones.
Por definición un algoritmo es un conjunto de pasos para realizar una tarea, no hace falta matemáticas bastante avanzadas para hacer esto (pero pueden formar parte si haces un algoritmo que impliquen simulaciones físicas, por ejemplo).

Para saber si una palabra es palíndroma:

1. ¿La cadena está vacía o sólo tiene una letra? *Hemos terminado*, la palabra **es palídroma**.
2. Nos fijamos si la primera y última letra de palabra coinciden.
3. Si no coinciden *hemos terminado*, la palabra **no es palíndroma**, de lo contrario continúa.
4. Se coge una subcadena a partir de quitar la primera y última letra de la palabra, y le aplicamos los pasos a partir del punto 1.

El punto 1. es lo que se conoce como el *caso base* y ahí es donde termina la función (ya sea recursiva o no) afirmando que la palabra es palíndroma. (Un ejemplo básico es la palabra "a", que se lee igual de derecha a izquierda).

Pues con esto se redefine la función de estar forma

<pre>
esPalindromo2 xs
    | length xs  2 = True
    | head xs == last xs = esPalindromo2 (subcadena xs)
    | otherwise = False
        where subcadena xs = tail (init xs)
</pre>

Se prueba

<pre>
*Main> esPalindromo2 ""
True
*Main> esPalindromo2 "a"
True
*Main> esPalindromo2 "abba"
True
*Main> esPalindromo2 "girafarig"
True
*Main> esPalindromo2 "girafariga"
False
*Main> esPalindromo2 "gi"        
False
*Main> esPalindromo2 "asa"
True
</pre>

Pues esto está listo

## BONO: Saber si una palabra es palíndroma en JavaScript

<input id="palabra" type="text" min="0" max="64" /> <span id="esnoes">es</span> palíndroma.

[El código fuente en JavaScript]({attach}theme/js/es-palindromo.js)
