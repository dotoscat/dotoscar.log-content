date=2020-10-8
title=Problema práctico en la empresa, paginación
category=programacion, webdev
---

# Problema práctico en una empresa, paginación

En una aplicación web es común hacer listados por ejemplo de clientes o de inventario, y la verdad
es bastante fácil de distribuir una aplicación web, la web es universal. La contraparte es que pueden a llegar a 
consumir mucha RAM, mas o menos dependiendo del navegador. Yo siempre he sido partidario de aprovechar la RAM pero no desperdiciarla.

El caso es que en la web de la empresa el problema que yo recuerdo que había es que cargaba todos las tarifas en una misma página tardando hasta minutos en hacerlo.
No solamente eso, sino que además los administradores tenían su ordenador todos los días encendido con el navegador abierto por lo que el [consumo de RAM se incrementaba con el tiempo](https://kb.nmsu.edu/page.php?id=82336). El otro problema con la aplicación era que si aumentaban las tarifas también aumentaban linearmente la carga de estas y además linearmente el uso de RAM.

## Solución

¿Solución? Se compraron ordenadores nuevos, con más RAM. Si bien esto solucionaba el problema temporalmente no lo hacía con la carga, y con respecto a la RAM solamente daban una patada al problema que se haría mas grande después. Las solucines que habían era comprar mas RAM u otros ordenadores con mas RAM y soluciones software como concurrencia. Sobre la concurrencia no resolvería el problema porque el problema era en el lado del cliente con respecto a la carga, no importa cuántas manos haya para pillar datos, al final estás sobrecargando el navegador con la acumulación de todos esos datos.

La solución era mucho más sencilla que todo lo de arriba, y más barato, y es usar una técnica que usan muchos frameworks web como [Django](https://github.com/django/django/blob/0a306f7da668e53af2516bfad759b52d6c650b69/django/core/paginator.py) o [Laravel](https://laravel.com/docs/8.x/pagination): paginar los datos.

Paginar consiste en pedir y mostrar una parte de todos los datos mientras mantienes referencias a esas otras partes para igualmente pedirlas y mostrarlas. Todo esto se hace desde lado del servidor para que al final el lado cliente reciba la parte ya procesada.

La web de la empresa no usaba ningún framework, nada recomendable para un proyecto grande y crítico. Así que tocaba hacer uno a mano. Se hizo de esta forma:

1. Calcular el total del número de entradas de la petición

        $total_entradas <= SELECT count(*) FROM Algo;

2. Calcular el número de páginas según el número de entradas a mostrar por página: 

        $total_paginas = $total_entradas / $entradas_por_pagina

3. Hay que tener en cuenta también el resto de la división. Se añade una página mas si el resto es distinto de cero

        if ($total_entradas % $entradas_por_pagina > 0) {
            $total_paginas++
        }

4. Ahora en la consulta según el número de página actual hay que poner los límites.

        $entradas_de_la_pagina <= SELECT NOMBRE, APELLIDOS FROM Algo LIMIT $entradas_por_pagina OFFSET $entradas_por_pagina*$pagina_actual

Finalmente con `$entradas_de_la_pagina` lo pasamos a la vista.

Contar el número de registros de una tabla a a través de un gestor de base de datos con una consulta a pesar de ser lineal es mucho mas eficiente que hacerlo con un lenguaje de programación en el servidor.

Tras implementar esta solución los administradores y los clientes de empresa dentro de lo que caben se han quedado contentos y la página no tarda minutos en cargarse. El tiempo de carga es mas o menos constante de unos segundos y el uso de RAM no se dispara.

Siempre es mejor tirar de la solución mas sencilla y barata que complicarse. Gracias por leer.
