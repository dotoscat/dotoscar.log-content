date=2020-7-13
title=Entrada por teclado en Go
category=programacion
---

# Entrada por teclado en Go

A veces un programa de terminal necesita interacción con el usuario, y el mecanismo tradicional de entrada es con un teclado. En algunos lenguajes esto es trivial. Python, por ejemplo, ofrece input(), que admite además
una cadena como parámetro para mostrar un mensaje antes de la entrada

    respuesta = input("¿Quieres continuar? ")

Escribes tu respuesta, presionas intro, y ya el programa se encarga de procesar esa respuesta
como volvértela a pedir si no es la respuesta esperada o continuar acorde a lo que quieres hacer.

en otros lenguajes no es tan trivial, y este es el caso de Go.

En go la entrada del sistema, en la terminal normalmente es el teclado, está en *os.Stdin*, por lo que lo puedes tratar como si un descriptor de fichero se tratara.

Esta es la implementación del *input* en Go

<script src="https://gist.github.com/dotoscat/21f0892f680fdccf485cb685247ed634.js"></script>

## Ejemplo de uso

    func main() {
        fmt.Println("Escribe: ")
        reader := bufio.NewReader(os.Stdin)
        cadena, err := reader.ReadString('\n')
        if err != nil {
            log.Fatalln(err)
        }
        fmt.Println(cadena)
        entrada, err := input("¿Estás seguro de continuar? ")
        fmt.Println(entrada, err)
    }

Esta es una forma cómoda de recibir la entrada para el usuario.
