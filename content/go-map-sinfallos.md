title: Golang sin fallos en los map
date: 2019-8-11

Mientras estaba haciendo el tour para aprender Golang me encontré con un ejercicio para practicar
map. Tenía que completar una función *WordCount* para que pasara las pruebas.

Mi primera solución a este problema, que funcionó, fué este.

    func WordCount(s string) map[string]int {
        var words map[string]int = make(map[string]int)
        for _, word := range strings.Fields(s) {
            _, ok := words[word]
            if ok {
                words[word] += 1
            }else{
                words[word] = 1
            }
        }
        return words
    }

Todo bien, hasta que me dí cuenta de un detalle: Si la clave no estaba en *words*, que es el mapa
al devolver, su valor retornaría 0. Como me gusta mejorar las cosas en lo posible hice otra
solución que funciona igual con menos líneas.

    func WordCount(s string) map[string]int {
        var words map[string]int = make(map[string]int)
        for _, word := range strings.Fields(s) {
            words[word] += 1
        }
        return words
    }

<code>words[word] += 1</code> sería lo mismo que <code>words[word] = words[word] + 1</code>

Continúo con el tour.
