title= Sobre mí
date= 4/7/2019
script= sobre-mi.js
---

<script>
'use strict';

window.addEventListener('load', evt => {
    const nacimiento = document.getElementById('nacimiento');
    const fechaNacimiento = nacimiento.dataset.fechanacimiento;
    const edad = Math.floor((Date.now() - new Date(fechaNacimiento)) / 1000 / 60 / 60 / 24 / 365);
    nacimiento.innerText = nacimiento.innerText.replace(/\(.*?\)/, edad);
});

</script>

## TL;DR

"Hola mundo"

## Completo

Me llamo Óscar Triano García <span id="nacimiento" data-fechanacimiento="1987">y tengo (mmmm...) años<span><noscript> (usa JavaScript para calcular mi edad. Nací el 5 de Octubre de 1987)</noscript>.

Mi interés por la informática empezó cuando quería hacer juegos desde pequeño. Con el tiempo
me he ido interesando otras áreas de la informática como el diseño y desarrollo de máquinas virtuales, los lenguajes de programación en sí, la arquitectura de computadoras... Por lo general hago diseño y el desarrollo de aplicaciones informáticas. Me puedo defender en la administración de sistemas, sobre todo bajo Linux.

Me gusta hacer las cosas lo más simple posible, con el menor número de fallos que pueda y haciendo más con menos. Suelo preferir hacer las soluciones de forma multiplataforma, por lo que la web es un enorme lienzo en el que se puede hacer y compartir muchas cosas.

Mis herramientas principales son Python, JavaScript, HTML5 y CSS3. También sé C, Lua, SQL (con MySQL, Postgre y SQLite) y PHP.

Tengo un buen nivel inglés técnico para poder leer la documentación que necesito, y escribir. Aunque mi inglés conversacional no es muy bueno lo estoy trabajando.
