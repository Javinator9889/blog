---
title: Herencia – POO
author: Javinator9889
type: post
date: -001-11-30T00:00:00+00:00
draft: true
url: /?p=138
categories:
  - Java
  - POO

---
Continuando lo que vimos en la [sección anterior,][1] continuamos con una de las propiedades más potentes de la Programación Orientada a Objetos: la herencia.

Este concepto añade mucha fuerza y capacidad a los lenguajes de programación, permitiéndonos reutilizar código para generar nuevos métodos, clases y atributos.

<!--more-->

## Requisitos para este tema

  * Haber leído y comprendido las lecciones anteriores

## Índice

  1. [**Introducción**][2]
  2. [**Clases y **<b style="font-size: 1rem;">visibilidad</b>][1]
  3. [**_Herencia_**][3]
  4. **Clases abstractas e interfaces**
  5. **Polimorfismo**
  6. **Clases internas y excepciones**
  7. **Clases genéricas**
  8. **Colecciones**
  9. **Entrada/salida**

<img loading="lazy" class="alignnone size-medium wp-image-142" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/09/inheritance-300x144.gif" alt="" width="300" height="144" /> 

## ¿Qué es la herencia?

En la lección anterior vimos toda la potencia que nos daban las clases, así como su uso e implementación. Nos permitían encapsular objetos, métodos y atributos, declarar distintas visibilidades y poder trabajar con aquellos objetos que contiene en su interior.

Una de las frases más repetidas (y con razón) es:

> Si algo ya funciona, no lo hagas de nuevo, sino que utiliza lo que ya habían creado.

Y es que ésto es lo que nos permite la herencia: **reutilizar código.**

Por ejemplo, en la imagen anterior, vemos una especie de jerarquía: en la cima está la visión más abstracta, más global, **un animal**. En el siguiente nivel, encontramos ya una caracterización dentro de los animales como pueden ser sus tipos: **omnívoros, herbívoros y carnívoros**. Y, finalmente, dentro de cada tipo de animal encontramos especies: **conejos, leones, hienas, el ser humano**, &#8230;

Al final todos tienen algo en común y es el _ser animales_. Pero también tienen el mismo número de _extremidades_, _pelo_ en el cuerpo, etc. Es decir, comparten una serie de **características comunes** a ellos. La herencia nos permite establecer todos esos atributos comunes a todos los animales de una única vez, definiendo y escribiendo únicamente la primera clase.

La herencia únicamente se produce entre clases, esto es, no podremos hacer herencia de atributos y/o de métodos.

 [1]: https://javinator9889.sytes.net/blog/poo-classes-visibility/
 [2]: https://javinator9889.sytes.net/blog/poo-introduction/
 [3]: https://javinator9889.sytes.net/blog/poo-inheritance