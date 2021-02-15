---
title: Introducción a la Programación Orientada a Objetos – POO
author: Javinator9889
type: post
date: 2018-09-16T18:40:07+00:00
url: /poo-introduction/
categories:
  - Java
  - POO
tags:
  - clases
  - java
  - poo
  - post
  - tutorial

---
Bienvenidos a una _serie de posts_ en los que, en mayor o menor medida, intentaré introduciros a la **Programación Orientada a Objetos**. Si bien existen diversos lenguajes de [programación orientados a objetos][1], aquí nos vamos a centrar en [Java][2], debido a su sencillez, compatibilidad y alta potencia en lo que al tema se refiere. Obviamente, **todo lo visto en esta serie de _posts_** es perfectamente aplicable en cualquier otro lenguaje de programación orientado a objetos, como _Python_ o _C++_.

<!--more-->

## Requisitos para este tema

  * Nociones básicas de programación (declaración de variables, funciones, etc.).
  * Comprensión básica de la programación (funcionamiento de iteradores, condiciones, etc.).
  * Ganas de aprender 😉

## Índice

<li style="list-style-type: none;">
  <ol>
    <li>
      <em><strong><a href="https://javinator9889.sytes.net/blog/poo-introduction">Introducción</a></strong></em>
    </li>
    <li>
      <a href="https://javinator9889.sytes.net/blog/poo-classes-visibility"><strong>Clases y visibilidad</strong></a>
    </li>
    <li>
      <strong>Herencia</strong>
    </li>
    <li>
      <strong>Clases abstractas e interfaces</strong>
    </li>
    <li>
      <strong>Polimorfismo</strong>
    </li>
    <li>
      <strong>Clases internas y excepciones</strong>
    </li>
    <li>
      <strong>Clases genéricas</strong>
    </li>
    <li>
      <strong>Colecciones</strong>
    </li>
    <li>
      <strong>Entrada/salida</strong>
    </li>
  </ol>
</li>

## <strong style="color: #333333; font-size: 1rem;"><strong style="font-size: 1rem;"><img loading="lazy" class="alignnone size-medium" src="https://userscontent2.emaze.com/images/e53bd040-2559-4d37-a6bc-40e8b4bd641f/b27f132b-3de5-4549-9083-4b8f376cc0dapng" width="744" height="371" /></strong></strong>

## ¿Qué es la Programación Orientada a Objetos?

La **Programación Orientada a Objetos** (de ahora en adelante, _POO_), es un paradigma de la programación en la que, mediante diversas técnicas que veremos a continuación, se intenta representar el mundo real usando las herramientas propias del lenguaje en cuestión.

Existen diversos mecanismos para trabajar <span style="font-size: 1rem;">orientado a objetos, en los que se establecen diversos niveles, yendo desde una representación bastante </span><strong style="font-size: 1rem;">abstracta </strong><span style="font-size: 1rem;">hasta una </span><strong style="font-size: 1rem;">mucho más concreta</strong><span style="font-size: 1rem;">. Por ejemplo, si pensamos en un </span><em style="font-size: 1rem;">hospital</em><span style="font-size: 1rem;">, contemplamos que tenemos (de mayor a menor abstracción):</span>

  * Un **edificio**.
  * El edificio tiene un **número de habitaciones**.
  * Cada habitación **tiene un paciente** durante un tiempo, con un **doctor **asignado.
  * Cada **paciente** tiene un **nombre, DNI, número de la Seguridad Social, síntomas, edad, etc.**
  * Cada **doctor** tiene unos **estudios,** **pacientes asignados,  horas trabajadas, etc.**

Como hemos podido ver, hemos ido desde el propio **edificio** que es el hospital hasta **los distintos miembros** que lo conforman, como son _el médico y los pacientes_. Obviamente, faltan muchos más factores a contemplar, pero para entender lo que implica la abstracción es más que suficiente.

Si quisiéramos implementar en un lenguaje de programación todo lo mencionado anteriormente, tendríamos una **clase** &#8220;Hospital&#8221; la cual encapsularía las distintas _Habitaciones_, que a su vez tendría los **pacientes** con sus _nombres, DNI, números de la Seguridad Social, síntomas, etc._ y a los **doctores**, con sus _estudios, pacientes asignados, horas trabajadas, etc._ Es decir, nuevamente podemos ir de mayor a menor abstracción pero esta vez **mediante representaciones del mundo **<strong style="font-size: 1rem;">real en un lenguaje de programación</strong><span style="font-size: 1rem;">.</span>

Todo lo mencionado anteriormente nos permite **encapsular los datos**, esto es, &#8220;guardarlos&#8221; dentro de una clase para luego poder acceder a ellos; **reutilizar lo creado**, ya que hemos definido un caso genérico de un hospital, pero no lo hemos concretizado poniéndole datos, por lo que cualquier hospital podrá adherirse a nuestra creación; **a**<strong style="font-size: 1rem;">mpliar y extender</strong> <span style="font-size: 1rem;">nuestra clase, añadiendo más parámetros como pudieran ser </span><em style="font-size: 1rem;">el número de quirófanos</em> <span style="font-size: 1rem;">que tiene el hospital.</span>

Y así podríamos seguir enumerando ventajas y posibilidades que nos da la POO, pero es mejor descubrirlas por uno mismo aprendiendo aquellos detalles y puntos delicados que tiene cada lenguaje.

En el **siguiente _post_ hablaremos del concepto de clases y la visibilidad entre objetos.**

 [1]: http://www.larevistainformatica.com/lenguajes-programacion-orientada-objetos.htm
 [2]: https://es.wikipedia.org/wiki/Java_(lenguaje_de_programaci%C3%B3n)