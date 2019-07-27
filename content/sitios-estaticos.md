Title: Generadores de sitios web estaticos
Category: Desarrollo web
Tags: herramientas
Date: 2019-7-20

Hoy en día para crear un sitio o un blog tiras de wordpress, drupal u otro CMS donde requieres al menos
de un servidor web con soporte con un lenguaje de programación como PHP y una base de datos SQL como MySQL o PostreSQL. Algunos de ellos tienen la función de caché: almacenan el contenido ya renderizado para evitar el proceso de nuevo en un futuro; Pues con un generador de sitios web estáticos **no te hace falta nada más que un servidor web**.

### No hace falta base de datos

Por lo general, no. *El contenido lo haces y lo guardas en un lenguaje de formato o marcado como markdown, incluso en HTML o XML, en donde quieras*. Lo importante es que el generador sepa dónde está el contenido para poder hacer el sitio de forma apropiada.

### Contenido dinámico en un sitio web estático

Si necesitas mostrar contenido dinamico tiene que ser con **ayuda de JavaScript**, hoy en día JavaScript es capaz de [hacer muchas cosas al lado del cliente](https://developer.mozilla.org/en-US/docs/Web/API), puedes por ejemplo implementar un [servicio de comentarios](https://disqus.com/) para cada uno de tus posts. Incluso puedes *implementar los servicios que quieras en la misma máquina* donde está tu sitio web estático ([separación de intereses](https://es.wikipedia.org/wiki/Separaci%C3%B3n_de_intereses)). Pero *lo esencial de un sitio web no depende de JavaScript*, o no debería mostrar contenido a través de JavaScript **salvo que tu intención sea hacer una aplicación web**.

### ¿Quieres probar?

Uso [pelican](https://blog.getpelican.com/), escrito en Python, pero hay [más generadores de sitios estaticos](https://www.staticgen.com/about) que *pueden estar en tu lenguaje de programación preferido*.
