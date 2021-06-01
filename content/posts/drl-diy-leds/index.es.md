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
| 5 | Cable termorresistente | Necesario | https://s.javinator9889.com/6kD10d |
| 6 | Terminales de cobre | Necesario | https://s.javinator9889.com/KXb6qv |
| 7 | Conectores en 'T' | Necesario | https://s.javinator9889.com/a47hvq |
| 8 | *Add-A-Circuit* fusibles | Necesario - identificar el tamaño de los fusibles |  - Perfil bajo: https://s.javinator9889.com/BXRm59<br> - Perfil alto: https://s.javinator9889.com/NHMwdz |
| 9 | Bridas de plástico | Recomendable | https://s.javinator9889.com/vycCso |
| 10 | Pelacables automático | Opcional, pero altamente recomendado | https://s.javinator9889.com/fkLRzg |
| 11 | Decodificador/resistencia LED | Necesario | https://s.javinator9889.com/b7l74p |
| 12 | Luces DRL impermeables | Necesario | https://s.javinator9889.com/ZzyPeN |

**Materiales para realizar pruebas - opcional pero altamente recomendado:**

|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 13 | Porta pilas | Opcional | https://s.javinator9889.com/C9XJLm |
| 14 | Interruptores | Opcional | https://s.javinator9889.com/T6oqMZ |
| 15 | Placas PCB | Opcional - alternativa: protoboard (14) | https://s.javinator9889.com/uBGU63 |
| 16 | Protoboard | Opcional - alternativa: placas PCB (13) | https://s.javinator9889.com/Xtp0AE |
| 17 | Pines "de paso" de corriente | Opcional | https://s.javinator9889.com/gMjx58 |
| 18 | Pilas "AA" | Opcional | https://s.javinator9889.com/NbqA4Z |

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

# 3. Implantación paso a paso del sistema DRL
*Se sugiere leer detenidamente cada paso antes de realizar ninguna acción. Es recomendable estar seguro de lo que se ha de hacer*

## 3.1. Preparación de los cables
El primer paso consistirá en preparar los cables. En el dispositivo que venga es muy probable que dichos cables tengan una parte expuesta de cobre muy pequeña lo cual dificulta directamente el poder manipularlos. Como los queremos conectar a un cable preparado para el calor y más resistente, necesitamos pelarlos hasta que tengan un tamaño adecuado.

{{< lazyimage src="images/cables-short.jpg" caption="Vista inicial de los cables. La parte expuesta de cobre es muy pequeña, por lo que hace falta quitar exceso de plástico envolvente." >}}

Para ello, usando el [**pelacables**](https://s.javinator9889.com/fkLRzg) sugerido aumentamos significativamente la parte expuesta de cobre:

{{< lazyimage src="images/cutting-cables.jpg" caption=" " >}}

A continuación recubrimos los cables con [**tres cubiertas protectoras**](https://s.javinator9889.com/7rSrJW) de plástico aislante, ya que después no podremos añadirlo:

{{< lazyimage src="images/cable-wrapper.jpg" caption="Plástico aislante termoretráctil alrededor de los cables. Por cada polo (negativo y positivo) usaremos un plástico aislante para asegurarnos de que no se suelta la conexión. Con el plástico grande mantenemos las dos conexiones juntas y organizadas." >}}

Del [**hilo de cobre resistente a altas temperaturas**](https://s.javinator9889.com/6kD10d) cortamos una sección *suficientemente larga* para cubrir toda la conexión del vehículo. Para ello es necesario irse al motor del coche y medir aproximadamente cuánto cable necesitamos para que vaya desde el frontal del parachoques hasta el cuadro de fusibles, localizado al lado del volante del conductor. Para este caso en particular, usar unos **2.5 m** de cable será suficiente.

Realizamos un empalme rápido **enrollando los cables entre sí**. Es importante respetar el *código de color* (rojo positivo; negro a tierra) para después saber de un vistazo qué cables estamos manejando:

{{< lazyimage src="images/joining-cables.jpg" caption="Empalme de los cables atándolos entre sí. De momento, el conector amarillo (de los intermitentes) se queda al aire, sin conectar." >}}

Y para asegurarnos una conectividad duradera y segura, aplicamos con [**la estación de soldadura**](https://s.javinator9889.com/00kQHR) una gota de estaño sobre la unión:

{{< lazyimage src="images/soldering-cables.jpg" caption="Unión definitiva de los cables soldándolos con estaño." >}}

Si bien es cierto que el paso anterior **no es necesario**, realizar la soldadura de los cables nos asegurará una correcta y continua conductividad y reforzará la unión de los cables.

Finalmente, movemos los **plásticos termoretráctiles** hasta cubrir los cables y, aplicando calor con un *mechero* o una *pistola de calor*, se cierran sobre la soldadura. Esto hay que hacerlo **plástico a plástico**, no es recomendable aplicar calor sobre los tres a la vez para que se cierren. El resultado final queda así:

{{< lazyimage src="images/heating-cables.jpg" caption="Unión de los cables con el plástico aislante por encima. Esto añade resistencia a la humedad, al agua y evita que se suelte la soldadura." >}}

Destacar que el **cable amarillo** debe quedarse fuera de la unión en todo momento, lo usaremos más adelante. Finalmente, pero no menos importante, deberemos comprobar que la luz DRL se enciende correctamente y funciona. En otro caso, la soldadura que hemos realizado es **incorrecta** y habrá que deshacerlo y repetir el proceso. 

> *Nota: comprobar de antemano que las luces funcionan para no estar buscando una aguja en un pajar.*

{{< youtube id="BTQ-iHfVyUQ" title="Primera prueba tras realizar el empalme de los DRL" >}}

Si ya tenemos realizado este primer paso **debemos repetir el mismo proceso** pero con la otra luz DRL. En este caso, como se va a unir a la luz que acabamos de preparar, la longitud del cable deberá ser mucho más pequeña (unos 50~60 cm serán suficientes).

## 3.2. Identificación del sitio de colocación de los DRL
Aunque este paso pueda parecer simple, es fundamental para asegurarnos tanto **una correcta visibilidad** como un **correcto funcionamiento** de las luces. Evidentemente, se han de situar en el parachoques delantero pero hay distintos sitios válidos:

{{< lazyimage src="images/frontal.png" caption="Ubicaciones válidas en la parrilla frontal del vehículo." >}}

 1. En la rejilla de ventilación inferior (en azul) los DRL se pueden colocar fácilmente y el sitio es flexible, lo que permite una mejor manipulación. Sin embargo, el acceso a la zona desde el motor es complejo y puede resultar tedioso.
 2. Encima de las luces antinieblas (en rojo) es un **muy buen sitio** para situar los DRL que otorga una gran visibilidad. Sin embargo, es necesario *agujerear* el parachoques para poder pasar los cables hacia el motor.
 3. El DRL situado en frente de las luces (en amarillo) es otra ubicación **con alta visibilidad** pero presenta dos pegas: es necesario agujerear o bien el parachoques o bien las luces para poder pasar los cables y puede **reducir la visibilidad**.
 4. En la rejilla de ventilación superior (en violeta) los DRL otorgan muy buena visibilidad y el acceso es sencillo. Sin embargo, el lugar no es flexible y es muy complejo cumplir con las regulaciones europeas en lo referente a la **distancia que debe separar las luces**.

En este caso nos vamos a decantar por la opción primera por varios motivos:
 + Ofrece un fácil acceso desde el exterior.
 + Es un plástico blando que difícilmente se va a romper por presión o por ejercer fuerza.
 + Con la distancia adecuada cumple el reglamento europeo de luces DRL.
 + En la cavidad interior hay espacio suficiente para poner cables y añadir conexiones.

A la zona se puede acceder desde arriba, donde está el propio motor y el radiador:

{{< lazyimage src="images/rack-access.jpg" caption=" " >}}

y en su interior presenta un gran hueco donde se pueden situar cables e incluso aprovechar los ya existentes para unirlos y que se mantengan fijos (para evitar movimientos durante la marcha):

{{< lazyimage src="images/rack-space.jpg" caption=" " >}}

## 3.3. Preparación de la unión con los intermitentes (opcional)
Si queremos que las luces DRL reaccionen ante la activación de los intermitentes hace falta unir al [cable de cobre termorresistente](https://s.javinator9889.com/6kD10d) los pines amarillos que hemos dejado antes sueltos. Al igual que en la vez anterior, primero añadimos un [plástico termoretráctil](https://s.javinator9889.com/7rSrJW) (de color amarillo preferiblemente) alrededor de la conexión:

{{< lazyimage src="images/signal-cable.jpg" caption="Tubo termoretráctil sobre el cable termorresistente. Para la posterior conexión con los intermitentes, es recomendable usar entre 50~60 cm. de cable." >}}

Al igual que antes, empalmamos los cables atándolos entre sí y aplicamos una gota de estaño para soldarlos y asegurarnos una gran conectividad:

{{< lazyimage src="images/signal-soldered.jpg" caption=" " >}}

Cerramos la unión con el plástico termoretráctil aplicando calor con un mechero y, fundamental, verificamos el correcto funcionamiento tanto de la luz como del indicador de intermitentes (para encender los intermitentes basta con conectar la señal (amarillo) al positivo de 12V):

{{< youtube id="GCQIZ3nZIz8" title="Prueba de los DRL con el conexionado a intermitentes realizado." >}}

Finalmente volvemos a repetir todo el proceso con la otra luz que queda pendiente.

## 3.4. Colocación de las luces DRL en el vehículo
Una vez hemos realizado las conexiones ya podemos pasar a **situar las luces DRL** en el vehículo. Como queremos que el sistema sea *completamente reversible* utilizaremos [**bridas de plástico**](https://s.javinator9889.com/vycCso) de forma que las luces se quedan aseguradas pero podemos quitarlas en cualquier momento cortando las bridas.

Para colocar la luz en su sitio recomiendo usar una estrategia "muy curiosa": como se ha visto anteriormente, el espacio de maniobra es pequeño y el motor por dentro es una lija, por lo que es muy fácil cortarse o hacerse una herida. Como necesitamos sacar los cables **por encima** para poder manipularlos y es difícil introducir el brazo para poder cogerlos, vamos a hacerlo al revés. Primero, metes la luz por el hueco y **la sujetas con los cables que hemos soldado**. Después, como la rejilla es bastante flexible, introducimos la mano por la **rejilla inferior** y, haciendo péndulo con los cables, agarramos la luz DRL haciendo pinza con la mano. Después, basta con sacar la luz a través de la rejilla y ajustarla con las bridas (si los agujeros no vienen perforados se puede hacer a mano con un destornillador o algo afilado):

{{< lazyimage src="images/drl-being-mounted.jpg" caption="Luz DRL sobre la rejilla inferior y con las bridas listas para ser fijada." >}}

Fijamos la luz en la posición que queramos (idealmente lo más pegada a los extremos) y ajustamos las bridas, quitando el plástico sobrante:

{{< lazyimage src="images/drl-mounted.jpg" caption=" " >}}

Si **hacemos la instalación con intermitentes** es muy importante que la **orientación sea la adecuada**: en este caso, los intermitentes de los DRL no parpadean sino que hacen un efecto de desplazamiento. Por legislación, el sentido de dicho efecto debe ser acorde con el sentido del desplazamiento, para evitar la confusión (recordemos que los DRL son un elemento de seguridad pasiva).

Por otra parte, hay que tener en cuenta que la luz emitida por los DRL **es direccional**. Esto se traduce en que serán *altamente visibles* si el observador se encuentra directamente orientado a las luces. Por ello, es muy recomendable que las luces DRL estén orientadas **hacia arriba** de forma que otros vehículos y usuarios de la vía puedan verlas con mayor facilidad:

{{< lazyimage src="images/DRL-sideview.png" caption="Elevación desde la vista lateral. Como las luces son direccionales, situarlas enfocando un punto **superior** al que se encuentran incrementa su visibilidad." >}}

Finalmente, para cumplir con la legislación vigente, **es necesario** que las luces DRL estén, como mucho, desviadas 10º con respecto al sentido de la circulación del vehículo. Si no se cumple con esta regla las luces **no son aptas para la circulación** y nos pueden multar.

{{< lazyimage src="images/straight-lights.png" caption="Orientación de las luces con respecto al sentido de la marcha. Un ángulo superior a 10º impediría la circulación del vehículo." >}}

Por esto es fundamental escoger adecuadamente la posición y la orientación de las luces ya que, en otro caso, **no darán visibilidad al vehículo** y pueden **ser ilegales**, lo que conlleva la correspondiente sanción. Así, las luces en el coche quedarían:

{{< lazyimage src="images/drl-front-mounted.jpg" caption="Luces DRL montadas en la rejilla inferior." >}}

## 3.5. Interconexionado de las luces DRL
Con todos los pasos anteriores estamos listos para **comenzar el conexionado** de las luces. En este caso, vamos a conectar el DRL izquierdo con el derecho. Recordar que es necesario dejar bastante cable de sobra para poder *realizar los montajes del circuito* y *añadir una conexión* en la toma de fusibles del conductor.

Para realizar el conexionado vamos a usar los [**conectores en 'T'**](https://s.javinator9889.com/a47hvq) que permiten interconectar un par de cables con otro par sin necesidad de realizar ninguna soldadura. Para ello, los cables "sin cortar" se pasan por los dos orificios superiores (la '—' de la T) y el otro par de **cables pelados por el extremo** se introducen en los orificios inferiores (la '|' de la T), quedando el conexionado de la siguiente manera:

{{< lazyimage src="images/drl-joint.png" caption="Diagrama del conexionado de los cables en una unión en 'T'." >}}

Es importante **verificar en la serigrafía** que el conexionado es el correcto, ya que según el modelo puede cambiar:

{{< lazyimage src="images/drl-joint-zoom.png" caption="Conexionado de este conector en 'T'. Se puede apreciar cómo los cables quedarían unidos entre sí según la firma que aparece en el conector de plástico." >}}

Una vez nos hemos asegurado cómo se conectan los cables, pasamos a realizar el cortocircuito de ambas luces DRL:

{{< lazyimage src="images/drl-connections.jpg" caption=" " >}}

Aunque el **conector en 'T'** en principio es **resistente al agua**, como medida extra de seguridad añadimos cinta adhesiva alrededor de los cables y los terminales:

{{< lazyimage src="images/secured-connections.jpg" caption="Protección de los terminales con cinta adhesiva. Opcional pero altamente recomendable." >}}

Finalmente, es muy probable que haya **exceso de cable**. Para que no esté colgando y pueda moverse y dañar el vehículo, vamos a fijarlo a la chapa, en el compartimento interior que hemos visto antes:

{{< lazyimage src="images/fixed-1.jpg" caption="Unión de la conexión en 'T' a la carrocería del vehículo." >}}

Por otra parte, como puede que haya cable que sobre lo agrupamos con unas [**bridas**](https://s.javinator9889.com/vycCso) y podemos aprovechar la circuitería del propio coche para mantenerlas fijas:

{{< lazyimage src="images/fixed-2.jpg" caption="Unión del cable sobrante al propio circuito del coche." >}}

## 3.6. Desconexión de la batería
De ahora en adelante, los pasos que vamos a realizar **afectan directamente al circuito del coche** y debemos desconectar la batería. Antes de hacerlo, es necesario cumplir con las siguientes medidas:

 1. Contar con bien **unas zapatillas/botas con suela aislante** o usar unos **guantes de latex** al manipular las conexiones. En principio, unas zapatillas normales son aislantes pero, en caso de dudas, usar unos guantes: no queremos convertirnos nosotros en la conexión a tierra cuando desconectemos el cable.
 2. Observar y ver la **herramienta a usar**: los bornes de las baterías suelen estar fijos con una abrazadera que se suelta aflojando una tuerca. Identificar el diámetro de la misma y escoger la herramienta adecuada.
 3. Localizar algún **sitio seguro** donde dejar el conector. Como vamos a estar manipulando continuamente es mejor buscar un sitio donde apoyar el conector de forma que **ninguna parte metálica haga contacto** y podamos trabajar cómodamente.
 4. **NUNCA** tocar el polo positivo de la batería. Por lo general viene recubierto en plástico, así que por algo será... En un paso posterior será necesario usarlo pero lo haremos tomando unas precauciones especiales.

Sin más dilación, desconectamos el borne negativo de la batería y lo apoyamos en un lugar seguro:

{{< lazyimage src="images/battery-disconnect.jpg" caption=" " >}}

{{< lazyimage src="images/battery-disconnected.jpg" caption=" " >}}

## 3.7. Conexión con los intermitentes (opcional)
Si queremos que las luces reaccionen ante la activación de los intermitentes es necesario hacer un "puente" en la conexión. Sin embargo, para no dañar las conexiones ya existentes del vehículo se hará uso de un [**terminal de empalme**](https://s.javinator9889.com/xhwbaw).

Por otra parte, como vamos a modificar el circuito de los intermitentes es necesario añadir una *resistencia* (o decodificador CANBus) en dicha conexión, en caso de que nuestro vehículo cuente con dicha tecnología. Esto evitará que aparezcan errores **en el cuadro de mandos** debido a una menor intensidad. Se puede identificar fácilmente si un vehículo necesita de dicho decodificador si las luces conectadas **no son sencillamente un alambre** sino que son grandes y alargadas, como las siguientes:

{{< lazyimage src="images/canbus-leds.jpg" caption="Luces LED que usan CANBus. Si no contasen CANBus serían más pequeñas y finas." >}}

El conexionado de la resistencia/decodificador es simple: en el hueco del intermitente desconectamos el cable de la bombilla y añadimos el decodificador de por medio, haciendo las veces de puente:

{{< lazyimage src="images/led-decoder.png" caption="Decodificador LED para CANBus. A la izquierda en gris, los conectores de las bombillas. En el centro, los conectores que van a los cables originales." >}}

> **Nota:** es fundamental identificar previamente tanto **el tipo de conexión con cable** como el tipo de **conexión de bombilla** que tiene nuestro vehículo, ya que de un modelo a otro puede cambiar. Basta para ello con desmontar la luz y verificar qué conexionado usa.

Cuando hemos identificado los terminales, se realiza la conexión:

{{< lazyimage src="images/decoder-on.jpg" caption=" " >}}

Para añadir el terminal de empalme, se realizan los siguientes pasos:
 1. Se pasa **el cable rojo** del decodificador por el hueco libre (sin final) del terminal.
 2. El cable que **viene desde la luz DRL** se pela el extremo (para mayor conductividad) y se introduce por el terminal libre. Es importante identificar que este terminal **tiene un tope al final** que mantiene el cable en su sitio.
 3. Con unos alicates, hacemos presión **sobre la pinza metálica** hasta que esté completamente insertada. Los cables ya estarán empalmados.
 4. Cerramos la **presilla de plástico** y la conexión está realizada.

Igualmente, se deja un vídeo a continuación que muestra dicho proceso:

{{< youtube id="JWlsEoNWDqM" title="Conexionado a intermitentes" >}}

<br />

{{< lazyimage src="images/blinker-connected.jpg" caption="Terminal de empalme ya conectado al intermitente." >}}

Finalmente, al igual que en el paso [3.5.](#35-interconexionado-de-las-luces-drl), aunque la unión **ya sea impermeable** añadimos cinta aislante alrededor para proteger todavía más los cables:

{{< lazyimage src="images/blinker-secured.jpg" caption="Terminal de empalme protegida con cinta aislante para evitar que entre agua." >}}

Si *sobrase cable*, lo agrupamos con una [**brida**](https://s.javinator9889.com/vycCso) y lo fijamos o bien a otro cable o bien al chasis:

{{< lazyimage src="images/blinker-cable-excess.jpg" caption=" " >}}

> Se sitúa el decodificador en una **posición segura** (donde no se mueva demasiado) y **repetimos los pasos con el otro intermitente**.

## 3.8. Conexión del terminal de tierra
Con las **primeras conexiones ya realizadas** debemos *cerrar el circuito* conectando el cable negro a una toma de tierra del motor del vehículo. Para esta operación nos vamos a apoyar en un [**multímetro**](https://s.javinator9889.com/znqgtn), herramienta ideal para detectar tensión, corriente y resistencia de un circuito. Si no contamos con uno, en principio **cualquier punto metálico del chásis** actúa como toma de tierra, pero de esta forma nos aseguramos de ello.

Lo primero que habrá que hacer será comprobar *el conexionado* del circuito, ya que queremos ver si por una parte **no está conectado con la toma positiva** y que sí es un **punto de tierra o masa**.

> **PRECAUCIÓN: SE VA A TRABAJAR DIRECTAMENTE CON EL POLO POSITIVO DE LA BATERÍA. EXTREMAR EL CUIDADO AL MANIPULAR LOS CABLES Y LAS CONEXIONES**

Para esta tarea, haremos uso de un multímetro en el modo de medición de conectividad. Dicho modo se puede localizar porque aparece un icono de un altavoz 🔊 y, cuando hacemos contacto de los terminales del multímetro, emite un sonido:

{{< lazyimage src="images/continuity.jpg" caption="Modo de prueba de conectividad de un multímetro." >}}

La idea es: conectar uno de los terminales del multímetro al **borne positivo de la batería** y el otro en una parte metálica del motor. Si emite un sonido, **no es válido** ya que quiere decir que hay conexión con el positivo. Si no suena, realizamos la misma operación **con el borne negativo** y está vez sí que debe emitir un sonido, indicando que el punto escogido es en efecto **una toma de tierra**. Si bien es cierto que estas comprobaciones no son del todo necesarias (ya que por lo general los puntos metálicos del coche son tierra) sí que es una idea interesante asegurarse de que se escoge el lugar adecuado.

{{< lazyimage src="images/check-connection.jpg" caption=" " >}}

En este caso, un terminal de tierra válido se localiza *al lado de la batería* y es un tornillo metálico que se usa como **toma auxiliar de tierra**:

{{< lazyimage src="images/ground-point.jpg" caption="Toma auxiliar de tierra del vehículo." >}}

Como tenemos el cable de tierra "a pelo", hace falta usar [**terminales de conexión**](https://s.javinator9889.com/KXb6qv) en donde el **extremo del cable** se pela, se introduce por el interior y se aprieta con unos alicates. Es importante asegurarse de **cortar el cable sobrante** y que el extremo **toque directamente** con el recubrimiento de los terminales. Aseguramos la conexión y tenemos las luces conectadas a tierra:

{{< lazyimage src="images/ground-connected.jpg" caption="Terminal de tierra conectado a las luces DLR." >}}

## 3.9. Atravesando el *firewall*
Uno de los pasos críticos en el proyecto es el de llevar la conexión **desde el motor** hasta donde **el asiento del conductor**, donde realizaremos la conexión. Si nos fijamos en el habitáculo donde se encuentra el motor, no hay conexión aparente hacia el interior. Sin embargo, el poder encender las luces o activar diversos elementos eléctricos localizados en el exterior nos informan de que **sí se pueden pasar cables**.

Fijándonos en **la pared del coche**, podemos ver **un trozo de goma** donde un gran cable la atraviesa. Eso es el *firewall*, que permite realizar conexiones desde el capó hasta donde el conductor. Es un elemento muy interesante si queremos *añadir un nuevo claxon* al vehículo o bien luces auxiliares, como vamos a hacer.

Sin embargo, por seguridad, vamos a trabajar desde **dentro del vehículo**. Necesitamos acceder desde los pedales del conductor hacia el muro que separa el motor del habitáculo interior, y localizar **en la parte superior** el trozo de goma que es el *firewall*:

{{< lazyimage src="images/firewall-interior.jpg" caption="Vista interior del *firewall* del vehículo, localizado encima de los pedales." width=500 >}}

Si no estamos seguros de si lo hemos localizado correctamente, a continuación tenéis un vídeo en donde se muestra:

{{< youtube id="8FjMFXXToRM?start=81" title="Car firewall" >}}

La idea es ahora, **con un destornillador**, atravesar el *firewall* desde el interior y localizar la punta desde el exterior. Es importante fijarse en el **tacto que sentimos**: la resistencia de la pared debe ser **sólida** y firme, necesitando hacer fuerza para atravesarla. Si notamos que está flojo o se mueve muy posiblemente estaremos tocando cables, por lo que habrá que buscar otra posición y volver a intentarlo.

{{< lazyimage src="images/broken-firewall.jpg" caption=" " >}}

Pasar el cable **no es sencillo** usando directamente el agujero, ya que es posible que haya una doble pared. Sin embargo, aprovechando el destornillador y el orificio hecho, podemos pasar **una pajita resistente** desde un lado al otro, contando con un canal para poder pasar el cable:

{{< lazyimage src="images/straw-exterior.jpg" caption="Pajita que sirve de canal, desde el motor." >}}

{{< lazyimage src="images/straw-interior.jpg" caption="Pajita que sirve de canal, desde los pedales del conductor." >}}

Ahora solo queda **pasar el cable** de conexión a través de la pajita y recogerlo en el interior:

{{< lazyimage src="images/cable-through-firewall.jpg" caption="Conexionado hacia el interior a través del *firewall*." >}}

> **Nota:** todavía *no quitamos la pajita* para tener una mayor y mejor movilidad en los pasos siguientes.

## 3.10. Conexionado final
Ya llegamos al último paso, la conexión última del circuito. Como ya tenemos el cable en el lado del conductor, vamos a realizar la conexión al **cuadro de fusibles**, como teníamos previsto. Antes de empezar, es importante localizar dónde están los fusibles en el coche. Por lo general, van a estar en el **lateral izquierdo** en la zona del conductor y lo podremos identificar porque hay una caja de este estilo:

{{< lazyimage src="images/fuses-outside.jpg" caption="Caja de acceso a los fusibles." >}}

Sacando la cubierta protectora, podemos ver cómo están distribuídos los fusibles en el vehículo:

{{< lazyimage src="images/fuses-distribution.jpg" caption="Distribución de los fusibles dentro del cuadro de fusibles." >}}

Para este caso vamos a usar la conexión del fusible del **mechero**, ya que es uno de los "no esenciales" que no afectan directamente a elementos de seguridad activa del coche. Podemos identificarlo fácilmente siguiendo la tabla de distribución anterior por el fusible con nombre "**CIG**" (del inglés, *cigarette*). En este caso, el fusible se localiza en la **posición número 9** del cuadro de fusibles principal (fijarse en que en la distribución de fusibles aparece una imagen donde se muestra qué forma tiene el cuadro de fusibles principal y secundario).

En este caso, el fusible a identificar es de $15A$ y está en la hilera de la izquierda:

{{< lazyimage src="images/fuses.jpg" caption="Fusibles del vehículo." >}}

Para sacar los fusibles es necesario utilizar una **herramienta de extracción de fusibles**, que vendrá con el **kit para añadir fusibles**. Dicha herramienta con forma de pinza se sitúa alrededor del *slot* donde está el fusible y permite su extracción y colocación:

{{< lazyimage src="images/fuse-extractor.jpg" caption="Pinza de extracción de fusibles." >}}

Una vez extraído el fusible debemos situarlo en un lugar seguro, ya que lo usaremos más tarde. Por otro lado, podremos saber si nuestro coche utiliza fusibles de perfil bajo o de perfil medio, como es este caso. Se puede saber fácilmente por la longitud de las patas, ya que los nuevos y habituales son de **perfil bajo** y los más "antiguos" (pero los más comunes) son los *mini*:

{{< lazyimage src="images/fuse.jpg" caption=" " >}}

En la página de RS-Components hay una descripción y [guía detallada](https://uk.rs-online.com/web/generalDisplay.html?id=ideas-and-advice/car-fuses-guide) sobre los distintos tipos de fusible que podemos encontrar en un coche. Es fundamental usar los componentes adecuados ya que otros no serán compatibles con nuestra instalación eléctrica:

{{< lazyimage src="images/car_fuses_image.jpg" caption="Distintos tipos de fusibles usados en coches. Fuente: [RS Components Ltd.](https://uk.rs-online.com/web/generalDisplay.html?id=ideas-and-advice/car-fuses-guide)" >}}

Ahora, con el **cable de expansión** de fusibles, situamos el *fusible antiguo* de $15A$ en el *slot* libre y un fusible de entre $1A$ y $3A$ en el otro *slot*. La ubicación es importante ya que uno servirá para el circuito original y el otro para el nuevo. Con esto en mente, el fusible de $1/3A$ para el nuevo circuito irá situado **encima del cable** de unión y el fusible original en el hueco libre que quede:

{{< lazyimage src="images/add-a-circuit.jpg" caption="Fusibles situados sobre la unión final. El fusible original $(15A)$ va situado en el hueco \"libre\". El nuevo fusible $(3A)$ se sitúa encima del cable." >}}

Con las conexiones ya aseguradas, pasamos a mover el cable de conexión **por detrás del cuadro de mandos** y por **encima de los pedales** para sacarlo por el hueco de la caja de fusibles, ya que no debe quedar cable colgando por la zona de los pies. Una vez lo hemos extraído por allí, **cortamos el exceso de cable** de forma que nos sea sencillo trabajar pero no haya cable de más:

{{< lazyimage src="images/cut-excess-fuse.jpg" caption=" " >}}

Usando los **terminales** que vienen con el circuito de extensión de fusibles, **pelamos el extremo del cable** y lo aseguramos dentro del conector con unos alicates:

{{< lazyimage src="images/connection-end-connector.jpg" caption=" " >}}

Cuando hemos comprobado que el conector no se mueve, **unimos los terminales** entre sí y encapsulamos la conexión con la protección de plástico que viene. Si no tuviésemos, se puede usar otro plástico termoretráctil para asegurar la conexión final:

{{< lazyimage src="images/final-connection.jpg" caption=" " >}}

Finalmente, lo último que queda ya es **conectar el fusible** en la caja de fusibles *en la posición que hemos dejado libre* (no usar ninguna otra conexión que estuviera vacía ya que puede estar destinada a otro circuito o no funcionar):

{{< lazyimage src="images/fuse-connected1.jpg" caption="Conexión del circuito expansor de fusibles en la caja de fusibles del vehículo, usando el hueco que hemos dejado libre." width=500 >}}

Si, por un casual, **todavía quedase cable colgando** (ya que el conector es largo) podemos moverlo hacia el conductor con la intención de que no quede **nada visible** pero, más importante, nada que **pueda molestarnos cuando conducimos** (es muy peligroso que podamos pisar el cable mientras estamos pisando los pedales):

{{< lazyimage src="images/fuse-connected2.jpg" caption="Cable extensor de circuitos junto con el resto de elementos electrónicos del vehículo debidamente separado para evitar problemas de seguridad." width=500 >}}

Finalmente, pero no menos importante, **quedará probar al fin el circuito que hemos montado**. Aquí tenéis el vídeo del primer encendido:

{{< youtube id="ji5CJwJd5UM" title="Encendido inicial de los DRL" >}}

😱🥳😱🥳😱🥳 Las luces se ven increíbles, **pero no reaccionan frente a los intermitentes**. ¡NO PREOCUPARSE! Lo más posible es que las hayamos conectado al **negativo** de los intermitentes, por lo que dando la vuelta a la conexión del decodificador **se soluciona el problema**:

{{< lazyimage src="images/led-decoder-turn.png" caption="Si los intermitentes no se encienden cuando los accionamos, con dar la vuelta al conector basta (está conectado a tierra)." >}}

Cuando hayamos comprobado que **todo funciona como debe**, ¡hemos terminado! 🥳