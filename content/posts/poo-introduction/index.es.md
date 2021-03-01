---
title: Introducción a la Programación Orientada a Objetos – POO
author: Javinator9889
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

ShowTOC: false

---
Bienvenidos a una _serie de posts_ en los que, en mayor o menor medida, intentaré introduciros a la **Programación Orientada a Objetos**. Si bien existen diversos lenguajes de [programación orientados a objetos][1], aquí nos vamos a centrar en [Java][2], debido a su sencillez, compatibilidad y alta potencia en lo que al tema se refiere. Obviamente, **todo lo visto en esta serie de _posts_** es perfectamente aplicable en cualquier otro lenguaje de programación orientado a objetos, como _Python_ o _C++_.

<!--more-->

## Requisitos para este tema

  * Nociones básicas de programación (declaración de variables, funciones, etc.).
  * Comprensión básica de la programación (funcionamiento de iteradores, condiciones, etc.).
  * Ganas de aprender 😉

## Índice

  1. **[Introducción][3]**
  2. [_**Clases y visibilidad**_][4]
  3. **Herencia**
  4. **Clases abstractas e interfaces**
  5. **Polimorfismo**
  6. **Clases internas y excepciones**
  7. **Clases genéricas**
  8. **Colecciones**
  9. **Entrada/salida**


{{< lazyimage src="images/languages.png" >}}

## ¿Qué es la Programación Orientada a Objetos?

La **Programación Orientada a Objetos** (de ahora en adelante, _POO_), es un paradigma de la programación en la que, mediante diversas técnicas que veremos a continuación, se intenta representar el mundo real usando las herramientas propias del lenguaje en cuestión.

Existen diversos mecanismos para trabajar orientado a objetos, en los que se establecen diversos niveles, yendo desde una representación bastante **abstracta** hasta una **mucho más concreta**. Por ejemplo, si pensamos en un *hospital*, contemplamos que tenemos (de mayor a menor abstracción):

  * Un **edificio**.
  * El edificio tiene un **número de habitaciones**.
  * Cada habitación **tiene un paciente** durante un tiempo, con un **doctor **asignado.
  * Cada **paciente** tiene un **nombre, DNI, número de la Seguridad Social, síntomas, edad, etc.**
  * Cada **doctor** tiene unos **estudios,** **pacientes asignados,  horas trabajadas, etc.**

Como hemos podido ver, hemos ido desde el propio **edificio** que es el hospital hasta **los distintos miembros** que lo conforman, como son _el médico y los pacientes_. Obviamente, faltan muchos más factores a contemplar, pero para entender lo que implica la abstracción es más que suficiente.

Si quisiéramos implementar en un lenguaje de programación todo lo mencionado anteriormente, tendríamos una **clase** `Hospital` la cual encapsularía las distintas `Habitaciones`, que a su vez tendría los **pacientes** con sus _nombres, DNI, números de la Seguridad Social, síntomas, etc._ y a los **doctores**, con sus _estudios, pacientes asignados, horas trabajadas, etc._ Es decir, nuevamente podemos ir de mayor a menor abstracción pero esta vez **mediante representaciones del mundo** real en un lenguaje de programación.

Todo lo mencionado anteriormente nos permite **encapsular los datos**, esto es, "guardarlos" dentro de una clase para luego poder acceder a ellos; **reutilizar lo creado**, ya que hemos definido un caso genérico de un hospital, pero no lo hemos concretizado poniéndole datos, por lo que cualquier hospital podrá adherirse a nuestra creación; ampliar y extender nuestra clase, añadiendo más parámetros como pudieran ser el número de quirófanos que tiene el hospital.

Y así podríamos seguir enumerando ventajas y posibilidades que nos da la POO, pero es mejor descubrirlas por uno mismo aprendiendo aquellos detalles y puntos delicados que tiene cada lenguaje.

En el [siguiente _post_][4] hablaremos del concepto de clases y la visibilidad entre objetos.**

 [1]: http://www.larevistainformatica.com/lenguajes-programacion-orientada-objetos.htm
 [2]: https://es.wikipedia.org/wiki/Java_(lenguaje_de_programaci%C3%B3n)
 [3]: https://blog.javinator9889.com/poo-introduction
 [4]: https://blog.javinator9889.com/poo-classes-visibility