---
title: Clases y visibilidad entre objetos – POO
author: Javinator9889
date: 2018-09-16T18:41:09+00:00
url: /poo-classes-visibility/
amp_status:
  - disabled
categories:
  - Java
  - POO
tags:
  - clases
  - enumerados
  - java
  - poo
  - private
  - public

ShowTOC: false

---
En la [sección anterior][1] vimos una pequeña introducción a la _Programación Orientada a Objetos_, en la que explicábamos este concepto así como sus ventajas. Hoy continuamos con las **clases y la visibilidad entre objetos**.

<!--more-->

## Requisitos para este tema

  * Noción básica de programación y tipos de datos, así como _tipos abstractos de datos_.
  * Haber leído la sección anterior.

  1. **[Introducción][1]**
  2. [_**Clases y visibilidad**_][2]
  3. **Herencia**
  4. **Clases abstractas e interfaces**
  5. **Polimorfismo**
  6. **Clases internas y excepciones**
  7. **Clases genéricas**
  8. **Colecciones**
  9. **Entrada/salida**

## Visibilidad entre objetos

Dependiendo de cada lenguaje de programación, la visibilidad de los objetos se declara de distintas maneras, usando palabras reservadas o definiendo algún prefijo en el nombre de la variable.

En **Java**, usaremos las palabras reservadas `public, private, protected:`

  * `public` define una visibilidad **pública**, es decir, puede ser accedido desde cualquier parte de la aplicación.
  * `private` es exactamente lo contrario de `public`, y solo puede ser accedido desde la propia clase que lo contiene.
  * `protected` es bastante permisivo, teniendo visibilidad dentro del mismo paquete, fuera de éste o para aquellas clases que heredan.
  * Finalmente, si no hay declarada ninguna visibilidad, el objeto tendrá **visibilidad de paquete**, es decir, solo se podrá acceder a él desde la propia clase o desde el paquete que lo contiene.

Por el [principio de encapsulación][3], y a no ser que se vayan a usar para otra cosa, **todos los atributos de una clase** tienen que ser `private`, de manera que solo se pueda acceder a ellos mediante métodos provistos por la propia clase para ello.

{{< lazyimage src="images/Java_logo.png" width=300 >}}

## Clases

Una clase es un nivel de abstracción bastante elevado dentro del paradigma de la POO, ya que sirve principalmente para **encapsular atributos y métodos**.

Como tiene un nivel de abstracción bastante elevado, usaremos las clases para englobar siempre **objetos, atributos y métodos** que tienen _algo en común_. En el ejemplo anterior, podríamos tener una clase **"Hospital"** que englobaría las **Habitaciones, Pacientes y Doctores**, además de tener los datos propios del hospital.

Una clase siempre se definirá de la misma manera, añadiendo o quitando _keywords_ (**palabras reservadas**) de la misma declaración:

```java
(public) class NombreDeClase {[...]}
```

*(el atributo `public` va entre paréntesis porque podría ser suprimido, dependiendo de nuestras necesidades)*.

Con esto ya tendríamos definida nuestra clase. 

**AVISO:** en _Java_, el **nombre del fichero** tiene que coincidir con el **nombre de la clase**. Así, si el fichero se llama **Hospital.java**, la clase principal tendrá que ser:
```java
public class Hospital
```

Cada clase tiene lo que se conoce como **constructor**: es un método especial que, para invocarlo, se usa la _keyword_ "_new_" delante de éste. Un constructor nos permite **crear una instancia de la clase** que vamos a utilizar, y así poder acceder a aquellos atributos y métodos no estáticos de la misma.

Por ejemplo, supongamos que nuestra clase `Hospital` tiene un método llamado `metodo1` y, en un momento dado, lo queremos usar. Para ello, crearemos una instancia de nuestra clase y ya podremos acceder a dicho método:

```java
Hospital instanciaDelHospital = new Hospital() // Constructor de la clase
instanciaDelHospital.metodo1() // Ya podemos usar los métodos de la clase
```

De otra manera, si no hiciéramos lo anterior, no podríamos acceder a los métodos de la clase `Hospital` a no ser que fueran estáticos. ¿Qué quiere decir que sean **métodos o atributos estáticos**? Esta caracterización implica que _podemos acceder a ellos_ sin necesidad de crear una instancia de una clase. Esto es útil para aplicar, por ejemplo, el patrón de diseño [Singleton][4], obtener datos que nunca varían, etc. Para que un objeto dentro de una clase sea estático, ha de ir precedido por la _keyword_: `static`. Así, podríamos definir:

```java
public class EjemploStatic {
    public static final int ID = 1234; // final implica que el valor NUNCA cambia<br />
    public static void metodoEstatico() {
        System.out.println("Soy un método estático");
    }
}
/*----------------------------------------------------------------*/
int id = EjemploStatic.ID; // Acceso al valor ID desde fuera de la clase, sin necesidad de crear una instancia de la misma con "new"
EjemploStatic.metodoEstatico(); // Escribirá en la consola "Soy un método estático"`
```

Dentro de una clase, tenemos también la _keyword_ `this`, la cual tiene un comportamiento que resutalrá muy útil a la hora de programar. `this` se usa para referenciar aquellos **métodos y objetos** propios de la clase no estáticos, así como la propia clase. Es decir, cuando estamos usando `this` nos estamos refiriendo a **la totalidad de la clase, como si estuviera instanciada**. Por ejemplo:

{{< gist Javinator9889 b475e4a5ab349d19a8d6475616ce5ac2 "ThisClass.java" >}}

Finalmente, dentro de una clase podemos tener lo que se conoce como **sobrecarga de métodos**: por ejemplo, cuando queremos crear nuestro objeto **Hospital**, es posible que todavía no sepamos el **id** del hospital, o las habitaciones que **tenemos libres u ocupadas**. Por ello mismo, _Java_ nos permite declarar un método con el mismo nombre pero distintos atributos, para poder adaptar nuestras necesidades. Así, tendremos (directamente los constructores):

```java
public Hospital() {}; // Constructor por defecto
public Hospital(int id) {...} // Haremos algo con el "id"
public Hospital(int id, Rooms[] habitaciones) {...} // Haremos algo con "id" y "habitaciones"
/*---------------------------------------------------------*/
Hospital h1 = new Hospital(); // Primer constructor
Hospital h2 = new Hospital(1); // Segundo constructor
Hospital h3 = new Hospital(1, habitaciones); // Tercer constructor. "habitaciones" suponemos que lo hemos creado previamente
```

Ya para acabar, por el **principio de encapsulación**, todos los atributos de una clase han de ser **privados**, de manera que el acceso a ellos se tenga que hacer mediante los métodos que proporciona la clase o, en su defecto, _usando el constructor_. Dichos métodos tienen una nomenclatura particular, y se conocen como métodos _get_ y _set_ (**obtener,** **establecer**)**.** De esta forma, nuestra clase **Hospital** quedaría:

{{< gist Javinator9889 b475e4a5ab349d19a8d6475616ce5ac2 "Hospital.java" >}}

Y esto sería lo principal relacionado con las clases. A continuación, veremos un tipo especial de clase (conocido como _enumerados_) y estudiaremos sus ventajas.

### Enumerados

Un **enumerado** es un _tipo especial de clase_ que nos permite definir de una única vez varias clases con nombres distintos pero atributos y métodos comunes.

Para declarar que una clase es del tipo **enumerado**, añadiremos en la cabecera la _keyword_ `enum`:

```java
public enum Enumerado
```

Los distintos tipos de enumerado que podemos tener se declaran como si fueran un _array_, es decir, uno tras otro separados con una **coma**, excepto el último que llevará un **punto y coma**. Al igual que el resto de clases, `enum` nos permite hacer lo que queramos con la única excepción de que **el constructor es siempre privado**. El truco está en que, al declarar los tipos de enumerado como hemos mencionado anteriormente, de forma implícita estamos _creando instancias de nuestro enumerado_. Además, al declarar los tipos de enumerado podremos usar el **constructor que más nos convenga**. Así, para acceder a los atributos y métodos del enumerado, será tan sencillo como referenciarlo directamente, como si hubiéramos puesto el valor `static` delante.

Además, un enumerado provee unos ciertos métodos de la clase muy útiles para según qué queramos hacer:

  * `public static NombreEnumerado[] values();` &#8211; devuelve un _array_ con todos los **enumerados existentes** dentro de la clase.
  * `public int ordinal();` &#8211; devuelve la posición de un enumerado ya instanciado **dentro del orden** en el que lo hayamos definido (la posición en el array).
  * `public String name();` &#8211; devuelve el **nombre del enumerado** como una variable tipo `String`.
  * `public static NombreEnumerado valueOf(String name);` &#8211; devuelve el objeto **enumerado** a partir del nombre del mismo.

De esta forma, ejemplificando:

{{< gist Javinator9889 b475e4a5ab349d19a8d6475616ce5ac2 "Enumeration.java" >}}

Y bueno, esto sería todo en cuanto a **clases y visibilidad de objetos se refiere**. En el siguiente post trataremos el tema de la **herencia**, un factor muy importante que dará paso al **polimorfismo**, una de las grandes ventajas de _Java_.

##### Si tienes alguna duda, escríbeme en los comentarios &#8211; te contestaré lo antes posible 😊

 [1]: https://blog.javinator9889.com/poo-introduction
 [2]: https://blog.javinator9889.com/poo-classes-visibility
 [3]: https://www.tutorialspoint.com/java/java_encapsulation.htm
 [4]: https://es.wikipedia.org/wiki/Singleton