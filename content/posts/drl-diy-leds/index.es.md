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
| 9 | Decodificador/resistencia LED | Necesario | https://s.javinator9889.com/b7l74p |
| 10 | Luces DRL impermeables | Necesario | https://s.javinator9889.com/ZzyPeN |

**Materiales para realizar pruebas - opcional pero altamente recomendado:**

|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 11 | Porta pilas | Opcional | https://s.javinator9889.com/C9XJLm |
| 12 | Interruptores | Opcional | https://s.javinator9889.com/T6oqMZ |
| 13 | Placas PCB | Opcional - alternativa: protoboard (14) | https://s.javinator9889.com/uBGU63 |
| 14 | Protoboard | Opcional - alternativa: placas PCB (13) | https://s.javinator9889.com/Xtp0AE |
| 15 | Pines "de paso" de corriente | Opcional | https://s.javinator9889.com/gMjx58 |
| 16 | Pilas "AA" | Opcional | https://s.javinator9889.com/NbqA4Z |

A lo largo de la entrada se irán detallando para qué son cada uno de los elementos anteriores y su utilidad. Se deriva al lector la responsabilidad de evaluar si un elemento opcional es necesario o no.

# 2. Pasos previos
Con la intención de que todo el proceso se realice bien a la primera, vamos a preparar el entorno.

{{< lazyimage src="images/vehicle-sketch.png" >}}

{{< lazyimage src="images/elec.png" >}}