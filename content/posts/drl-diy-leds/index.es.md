---
title: '#DIY: DRL (luces diurnas) reversibles para cualquier coche'
author: Javinator9889
date: 2021-05-19
url: /drl-daylight-leds/
cover:
  image: images/cover.png
categories:
  - Tutoriales
  - DIY
tags:
  - car
  - coche
  - luces
  - LED
  - DIY
  - DRL
  - diurnas
  - machine
  - mecánica
draft: true
katex: true

---

Desde el año 2011, todos los [nuevos vehículos están obligados a llevar luces LED](https://ec.europa.eu/transport/road_safety/topics/vehicles/daytime_running_lights_es) de alta luminosidad que están encendidas **desde el contacto o arranque del motor**. La intención principal tras esta decisión es la de prevenir accidentes tanto de peatones como de otros vehículos, convirtiéndose así en un **elemento de seguridad pasiva**. Sin embargo, a lo largo del tiempo y tras una mayoritaria adopción de estas luces ya no solo es un elemento de seguridad sino también **de diseño y estética** del vehículo, otorgándole de un aire *moderno y actualizado*.

{{< lazyimage src="images/leon-headlights.jpg" caption="Luces diurnas en un Seat León III. Fuente: [Wikipedia](https://es.wikipedia.org/wiki/Luz_de_circulaci%C3%B3n_diurna)" >}}

> *Las luces diurnas ya no son solo elementos de seguridad pasiva sino además de diseño y estética del vehículo.*

Sin embargo, ¿qué sucede con todos aquellos vehículos anteriores al año 2011? ¿No tienen "derecho" a mejorar su seguridad y la del resto de usuarios de la vía? ¿No se pueden implementar estas luces? La respuesta es **sí y no**: las luces diurnas *han de estar homologadas* según el reglamento europeo y, en otro caso, deben pasar un proceso de homologación. El reglamento especifica, entre otras cosas, la **calidez de la luz** y la distancia a la que se debe colocar:

{{< lazyimage src="images/drl-diagram.jpg" caption="Colocación y separación de las luces DRL según la normativa europea. Fuente: [Hella](https://www.hella.com/techworld/uk/Technical/Automotive-lighting/Install-daytime-running-lights-740/)" width=600 >}}

Si la colocación de las luces cumple con las distancias anteriores, en principio **serán válidas** y se podrán usar perfectamente como luces diurnas. Sin embargo, según el tipo de vehículo que tengamos quizás *no se puedan cumplir los requisitos* y por tanto no sea válido.

En esta entrada de blog vamos a ver **cómo instalar unas luces DRL completamente reversibles** en *cualquier modelo de coche*.

* * * 

# 1. Pre-requisitos

Antes de realizar ninguna operación sobre nuestro vehículo es recomendable cumplir los requisitos que se muestran a continuación:
 + Tener conocimientos de mecánica y electrónica.
 + Capacidad de búsqueda y síntesis de información: se intentarán cubrir todos los puntos pero puede haber información que no se mencione aquí (o se dé por sabida).
 + "Conocer" nuestro coche: vamos a realizar operaciones que si bien no son dañinas requerirán de que sepas cómo es un motor y cómo funciona, de cara a evitar problemas.
 + No tener miedo pero sí precaución: lo que vamos a hacer es completamente reversible pero eso no implica que, si se hace mal, pueda dañar el vehículo. Se recomienda encarecidamente leer todos y cada uno de los pasos con calma, asegurarse de lo que hay que hacer.
   > *Piensa y lee mucho. Actúa una sola vez.*
 + De la tabla siguiente, tener todos los elementos que se consideran indispensables:

| # | Objeto | Necesario | Enlace |
|:-:|:-:|:-:|:-:|
| 1 | Multímetro | Opcional, pero altamente recomendado | https://s.javinator9889.com/znqgtn |
| 2 | Estación de soldadura | Opcional, pero altamente recomendado | https://s.javinator9889.com/00kQHR |
| 3 | Tubo termoretráctil | Necesario | https://s.javinator9889.com/7rSrJW |
| 4 | Terminal de empalme | Opcional - depende de conexionado a intermitentes | https://s.javinator9889.com/xhwbaw |
| 5 | Cable termoresistente | Necesario | https://s.javinator9889.com/6kD10d |
| 6 | Terminales de cobre | Necesario | https://s.javinator9889.com/KXb6qv |
| 7 | Conectores en 'T' | Necesario | https://s.javinator9889.com/a47hvq |
| 8 | *Add-A-Circuit* fusibles | Necesario - identificar el tamaño de los fusibles |  - Perfil bajo: https://s.javinator9889.com/BXRm59<br> - Perfil alto: https://s.javinator9889.com/NHMwdz |
| 9 | Pelacables automático | Opcional, pero altamente recomendado | https://s.javinator9889.com/fkLRzg |
| 10 | Decodificador/resistencia LED | Necesario | https://s.javinator9889.com/b7l74p |
| 11 | Luces DRL impermeables | Necesario | https://s.javinator9889.com/ZzyPeN |

**Materiales para realizar pruebas - opcional pero altamente recomendado:**

|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 12 | Porta pilas | Opcional | https://s.javinator9889.com/C9XJLm |
| 13 | Interruptores | Opcional | https://s.javinator9889.com/T6oqMZ |
| 14 | Placas PCB | Opcional - alternativa: protoboard (14) | https://s.javinator9889.com/uBGU63 |
| 15 | Protoboard | Opcional - alternativa: placas PCB (13) | https://s.javinator9889.com/Xtp0AE |
| 16 | Pines "de paso" de corriente | Opcional | https://s.javinator9889.com/gMjx58 |
| 17 | Pilas "AA" | Opcional | https://s.javinator9889.com/NbqA4Z |

A lo largo de la entrada se irán detallando para qué son cada uno de los elementos anteriores y su utilidad. Se deriva al lector la responsabilidad de evaluar si un elemento opcional es necesario o no.

# 2. Pasos previos
Con la intención de que todo el proceso se realice bien a la primera, vamos a preparar el entorno de trabajo. Es necesario que nos instalemos en algún sitio amplio donde estemos **cómodos**, sin **muchas molestias** y sobre todo que podamos tener una **gran movilidad** para trabajar con el coche. Es posible también alquilar un taller mecánico por horas para realizar todo el proceso, con el consiguiente coste que conlleva.

En principio, todo el proceso se podría hacer en aproximadamente **~2 horas/2h 30'** pero el hacerlo bien y con cuidado puede conllevar a que el tiempo pase a ser de **unas 5 horas**, así que mejor reservar la mañana (o el día).

## ¿Qué vamos a hacer?
Vamos a montar un sistema de luces diurnas DRL **completamente reversible** y **seguro**, aprovechando la circuitería del propio coche. La idea será colocar el nuevo circuito que alimentará y gestionará las luces como un elemento completamente independiente y aislado del resto del coche. De esta forma, conseguimos:

 1. Tener un sistema autónomo e independiente.
 2. Tener un montaje reversible, ya que *evitamos alterar el estado del vehículo*.
 3. Tener un equipo seguro: con su circuito independiente, si se produce un cortocircuito **solo** afectará a dicho circuito.
 4. Tener un sistema **actualizable**: ¿no te gustan las luces? ¿Necesitas más luminosidad? ¿Quieres usar unos LEDs homologados? Al ser un circuito reversible, en un momento dado es tan sencillo como "cambiar las bombillas".

Para realizar este proyecto y que salga bien a la primera vamos a aplicar unas pinceladas del **proceso de ingeniería**. Con esto nos aseguramos que no damos ningún paso en falso y que los problemas están, en su mayoría, solucionados antes de que sucedan. De entre todos los pasos del proceso de ingeniería, vamos a poner en práctica los siguientes:

 + Definición \*superficial\* de los requisitos que queremos satisfacer.
 + Diseño y verificación del circuito a montar.
 + Implementación paso a paso con un respaldo de pruebas.
 + Verificación final del sistema y solución de problemas.

### Definición de los requisitos
El objetivo principal es **tener un sistema de luces diurnas** DRL el cual cuente un **circuito independiente** de forma que, si se produce un cortocircuito o hay algún fallo eléctrico, el único sistema que se vea afectado sea el DRL. Por otra parte, deberá ser **completamente revertible** permitiendo su extracción sin dañar perjudicialmente al vehículo. Adicionalmente y para perseverar la integridad tanto del vehículo como del sistema este deberá ser resistente al agua, en mayor o menor medida.

El encendido y apagado del sistema deberá ser **completamente automático**, donde el conductor se limitará a usar el coche normalmente y las luces DRL se activarán/desactivarán automáticamente. Opcionalmente, el equipo se podrá integrar con la **electrónica existente del vehículo** de forma que cuando se activen los intermitentes del mismo las luces DRL reaccionarán ante dicho estímulo.

Es decir, se tienen los siguientes requisitos:

 1. Luces DRL.
 2. Instalación eléctrica independiente.
 3. Instalación eléctrica reversible.
 4. Sistema resistente al agua.
 5. Encendido y apagado automáticos.
 6. Reacción opcional frente a los intermitentes.

### Diseño y verificación del circuito a montar
Antes de realizar ninguna operación sobre el vehículo es fundamental definir una idea de qué vamos a hacer. Lo primero de todo será diseñar un circuito sobre un modelo genérico de coche que nos pueda servir de guía. Antes de diseñar el circuito hará falta tener en cuenta estas consideraciones:

 + El motor alcanza altas temperaturas, por lo que los cables deberán estar lo mejor distribuidos posibles.
 + Debido a la situación anterior, es recomendable usar la cantidad justa de cable, para evitar la exposición a las zonas de calor.
 + El circuito va a estar "al aire libre" por lo que es recomendable situarlo en zonas medianamente protegidas del motor.
 + NUNCA se deberá conectar directamente a la batería. Deberá ser un circuito independiente aislado del resto de la electrónica.
 + Los elementos que se usen deben estar debidamente aislados y protegidos de las inclemencias del tiempo.
 + Es necesario poder realizar cambios y sustituciones fácilmente una vez el sistema esté montado.

De esta forma, se tiene el siguiente esquema de cómo debe realizarse la conexión:

{{< lazyimage src="images/vehicle-sketch.png" caption="Instalación del sistema en un prototipo de vehículo." >}}

Vamos a explicar el porqué del diseño anterior. Por una parte, las luces DRL están conectadas entre sí. Esto es debido a que ambas presentan un bajo consumo y el circuito no se somete a demasiada carga con este tipo de conexionado. Además, simplifica mucho el manejo de los cables. De esta forma, la luz de la izquierda conecta sus terminales positivo (en rojo) y negativo (en negro) a los de las luces de la derecha.

Por otro lado, los terminales amarillos van conectados a una resistencia (que simboliza el decodificador LED) conectada directamente a los intermitentes del vehículo. Con esto, conseguimos que las luces reaccionen cuando accionamos los indicadores.

Finalmente, pero no menos importante, la conexión a tierra va directamente al borne de la batería (lo cual es necesario). En la implementación sin embargo veremos que hay otras opciones igualmente válidas. Para la conexión del polo positivo (12V) se utiliza un fusible que se conectará al **cuadro de fusibles** del coche y alimentará al sistema por ahí. Esto permite que el sistema se encienda y apague automáticamente, según la posición del fusible; y que esté protegido frente a cortocircuitos, ya que tiene su circuito independiente.

La intensidad máxima del fusible viene dada por el doble de la intensidad individual de cada una de las luces. En este caso, es necesario saber o bien **la potencia** de las luces DRL o bien **la intensidad máxima** que presentan. Si se conoce la intensidad individual, el valor del fusible será:

$$A_F = 2I \tag{1}$$
 
Si se conoce la potencia, hay que obtener la intensidad. Como la batería suministra 12V y la potencia es $P = V \cdot I$, entonces:

$$I = \frac{P}{V} \approx \frac{P}{12} \tag{2}$$

Por ejemplo, si cada luz DRL tiene una potencia de $2W$, la intensidad individual de cada una será:

$$I = \frac{2}{12} \approx 166~mA$$

De esta forma, el valor de la intensidad fusible usando la ecuación $\left(1\right)$ será:

$$A_F = 2 \cdot 166 = 333~mA \longrightarrow 0.3~A$$

Para este caso en particular, las luces que se usarán tienen una intensidad pico de $0.1~A$, por lo que el fusible que hay que usar deberá ser de al menos $0.2~A$. Sin embargo, fusibles de tan baja intensidad son difíciles de encontrar, por lo que usaremos el más bajo disponible - en este caso, de $3~A$.

Con todo esto establecido, el circuito final queda de la siguiente forma:

{{< lazyimage src="images/elec.png" caption="Circuito esquemático del sistema. Las luces DRL están conectadas entre sí y se alimentan desde la batería mediante un fusible de $3~A$ y se conectan a los intermitentes mediante un decodificador CANBus." >}}

#### Circuito de pruebas (opcional)
Si bien este paso es opcional, es altamente recomendado usar un circuito de pruebas para ir verificando que las conexiones se han realizado correctamente (y no comprometer la integridad de la batería del coche). El circuito que vamos a usar es muy simple:

{{< lazyimage src="images/test-graph.png" caption="Modelado del circuito de pruebas. Las dos baterías en serie proveen de $12V$." >}}

Es importante añadir el *switch* de encendido y apagado para poder probar el circuito varias veces sin gastar batería. El LED represente la luz DRL que se quiera conectar, como se muestra en el diagrama esquemático:

{{< lazyimage src="images/test-sketch.png" caption="Diagrama esquemático del circuito de pruebas." >}}

El circuito de pruebas queda de esta forma:

{{< lazyimage src="images/test-circuit.png" caption="Circuito de pruebas sobre una placa PCB." width=500 >}}

Para usarlo, basta con conectar los terminales positivo (rojo) y negativo (negro) a los pines correspondientes siguiendo el código de color o bien fijándonos en el diagrama.

## Consideraciones de seguridad
Aunque no se va a trabajar con alta tensión, la batería del vehículo tiene mucha potencia que puede variar entre $4320~W \sim 9600~W$ con intensidades de entre $400~A$ hasta $1000~A$, suficientes para resultar fatales. Por ello, aunque no es necesario es **altamente recomendable** usar un circuito de pruebas controlado para evitar exponernos a dicha corriente.

De igual manera, habrán puntos de la entrada en donde se indicará que se **debe desconectar la batería**. Aunque en apariencia pueda sonar peligroso si se toman las precauciones adecuadas no lo es, y nos dará seguridad cuando manipulemos cables o hagamos conexiones.

Finalmente, hay que tener **especial precaución** al conectar el circuito de pruebas. Si por un casual cerramos el circuito accidentalmente se sufre un alto riesgo de incendio. Asegurarse de que las conexiones de las baterías son correctas antes de encender nada (por eso, entre otros motivos, hay un interruptor).