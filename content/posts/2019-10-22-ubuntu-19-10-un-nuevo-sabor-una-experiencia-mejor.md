---
title: Ubuntu 19.10 – un nuevo sabor, una experiencia mejor
author: Javinator9889
type: post
date: 2019-10-22T09:14:34+00:00
url: /ubuntu-19-10-un-nuevo-sabor-una-experiencia-mejor/
featured_image: /wp-content/uploads/2019/10/Ermine_lines_by_Gustavo_Brenner-88x88.png
categories:
  - Reviews
tags:
  - 19.10
  - canonical
  - drivers
  - linux
  - nvidia
  - review
  - ubuntu
  - update

---
Como quizás hayáis escuchado estos últimos días, el **10 de octubre** se liberó la nueva versión de Ubuntu: &#8220;_Ubuntu 19.10 Eoan Ermine&#8221;_.

¿Qué trae nueva esta versión? ¿Qué ventajas podemos encontrar? Ya os adelanto que los cambios **no son demasiados** respecto a la versión anterior (_19.04_) pero **sí notorios** en el día a día y la experiencia de uso, y ya os adelanto que os van a gustar.

Sin más dilación, vamos a por ello.

<!--more-->

## Drivers NVIDIA directamente incluidos en la imagen ISO

<div style="width: 1152px" class="wp-caption aligncenter">
  <a href="https://www.omgubuntu.co.uk/wp-content/uploads/2019/05/nvidia-iso.jpg"><img loading="lazy" class="size-large" src="https://www.omgubuntu.co.uk/wp-content/uploads/2019/05/nvidia-iso.jpg" alt="nvidia drivers on iso" width="1142" height="631" /></a>
  
  <p class="wp-caption-text">
    NVIDIA drivers in Ubuntu ISO &#8211; source: https://www.omgubuntu.co.uk/
  </p>
</div>

Ahora, cuando instalemos las _nuevas versiones de Ubuntu_ tendremos siempre disponible la opción de realizar la instalación **usando los drivers privativos de NVIDIA**. Si bien esta medida ha causado bastante polémica (debido al porqué del _open source_ y la sensación de algunos desarrolladores y usuarios de que se está &#8220;saltando&#8221;), es un gran progreso ya que es un claro intento de **acercar Linux al usuario de escritorio**. En particular, este año se ha intentado [aunar fuerzas][1] y, en particular, Linus Torvalds ha hecho un llamamiento para evitar la fragmentación en los entornos de escritorio, buscando así que el usuario vea atractivo y factible el usar un sistema basado en Linux como su lugar de trabajo y ocio para el día a día.

> Si bien es cierto Ubuntu ya disponía de los **drivers _Open Source_**, en muchas situaciones estos no funcionaban bien y **hacían imposible la instalación** de una distribución basada en Linux.

Con la inclusión de los drivers privativos no se hace otra cosa sino esta misma: facilitar la instalación en los nuevos dispositivos. Si bien es cierto Ubuntu ya disponía de los **drivers _Open Source_**, en muchas situaciones estos no funcionaban bien y **hacían imposible la instalación** de una distribución basada en Linux.

Ahora, con la nueva incorporación de los drivers privativos en la ISO, aunque no se esté respetando en su totalidad la mentalidad que defiende la [FSF][2], se está permitiendo que **nuevos usuarios** accedan a este entorno de escritorio.

## NVIDIA _On-demand_

[<img loading="lazy" class="aligncenter size-large" src="https://www.muylinux.com/wp-content/uploads/2019/09/NVIDIA-Optimus.png" alt="NVIDIA On-demand" width="718" height="479" />][3]Con la nueva actualización de Ubuntu se incorporan los nuevos **drivers de NVIDIA** _435.21_, los cuales actualizan la aplicación _NVIDIA Profiler_ y permiten el uso de la tarjeta gráfica _**on-demand**_ (bajo demanda).

Esto es algo que se ha solicitado mucho a lo largo de los años, ya que era una característica **propia de Windows** y ahora se ha incorporado a la familia Linux. Si bien es cierto que es una &#8220;primera versión&#8221;, el rendimiento que nos brinda es excelente y no es necesario realizar ya el procedimiento de **cerrar la sesión para cambiar entre motores gráficos**. Ahora, basta con añadir unas premisas al programa que queramos ejecutar para que funcione directamente con la **tarjeta gráfica**:

<pre class="brush: bash; title: ; notranslate" title="">__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia
</pre>

Si bien es cierto que esto puede ser **complicado** y **tedioso**, aquí tenéis un script que os permitirá ejecutar _cualquier aplicación_ con los drivers integrados: <https://s.javinator9889.com/nvrun>.

Una vez hayáis descargado el script, le dais permisos de ejecución y lo movéis a alguna ruta que esté en vuestro _path_:

<pre class="brush: bash; title: ; notranslate" title="">chmod a+x nvrun
sudo mv nvrun /usr/local/bin
which nvrun
# /usr/local/bin/nvrun
glxinfo | grep vendor
nvrun glxinfo | grep vendor
</pre>

[<img loading="lazy" class="aligncenter size-full wp-image-527" src="https://blog.javinator9889.com/wp-content/uploads/2019/10/Captura-de-pantalla-de-2019-10-22-10-46-46.png" alt="nvrun command" width="544" height="176" srcset="https://blog.javinator9889.com/wp-content/uploads/2019/10/Captura-de-pantalla-de-2019-10-22-10-46-46.png 544w, https://blog.javinator9889.com/wp-content/uploads/2019/10/Captura-de-pantalla-de-2019-10-22-10-46-46-300x97.png 300w" sizes="(max-width: 544px) 100vw, 544px" />][4]

Por si tenéis curiosidad, el contenido del script es el siguiente:

<pre class="brush: bash; title: ; notranslate" title="">#!/bin/bash

__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia "$@"
</pre>

#### Extra: autocompletado en la consola

Si, además, queréis que al pulsar la tecla **tabulador** se autocomplete el script anterior, basta con ejecutar la siguiente orden en el terminal:

<pre class="brush: bash; title: ; notranslate" title="">complete -F _command nvrun
</pre>

## Soporte ZFS

[<img loading="lazy" class="aligncenter size-large" src="https://149366088.v2.pressablecdn.com/wp-content/uploads/2019/10/ubuntu-19.10-installer-750x422.jpeg" alt="ZFS support" width="750" height="422" />][5]Esta nueva versión incluye **soporte para el sistema de archivos ZFS**. Todo sea dicho, es una versión experimental, pero Ubuntu ha sido la primera distribución en incluir este sistema de archivos de **forma nativa**. Entre otras características, ZFS permite crear _pooling_ de discos, auto-reparación, instantáneas del sistema, entre otros.

## Inicio del sistema (aún) más rápido

[<img loading="lazy" class="aligncenter size-large" src="https://cache.desktopnexus.com/thumbseg/2464/2464369-bigthumbnail.jpg" alt="Linux rocket" width="450" height="253" />][6]

Si bien es cierto que muchos no notaremos esta nueva mejora, ahora el sistema arranca todavía **más rápido**. Esto es debido al nuevo método de compresión _LZ4_. Si queréis comprobar cómo de rápido es vuestro sistema, podéis usar la herramienta [_systemd-analyze_][7].

Tras realizar varios _benchmark_, se puede apreciar que en efecto el inicio de Ubuntu 19.10 es más rápido frente a las versiones anteriores.

## GNOME 3.34

[<img loading="lazy" class="aligncenter size-large" src="https://www.omgubuntu.co.uk/wp-content/uploads/2019/01/gnome-shell-performance.jpg" alt="GNOME 3.34" width="1200" height="630" />][8]Tras las **últimas actualizaciones de GNOME**, las cuales traen un mejor rendimiento, esto no hace más que crecer. GNOME 3.34 tiene, según los desarrolladores, una **gran mejora** en rendimiento. Nuestra experiencia: la misma.

Si bien venía de la versión de Ubuntu 19.04, la cual ya incorporaba grandes mejoras en rendimiento en lo que a escritorio se refiere, esta nueva actualización da una sensación de fluidez que nunca antes se había visto en el entorno de escritorio en Linux.

Junto a las ya evidentes mejoras, hay un nuevo pequeño **rediseño** en el sistema, mezclando el _tema oscuro con el tema claro_. Además, se ha perfeccionado la búsqueda y eso ha radicado en que la **tienda de aplicaciones** es todavía más rápida.

## Otras mejoras en el sistema

[<img loading="lazy" class="aligncenter size-large" src="https://149366088.v2.pressablecdn.com/wp-content/uploads/2019/09/linux-5.3.jpg" alt="Linux kernel 5.3" width="800" height="449" />][9]Ubuntu 19.10 trae la última versión del kernel de Linux **5.3**, la cual trae:

  * Soporte para AMDGPU Navi.
  * 16 millones de nuevas direcciones IPv4.
  * Soporte para pantallas compatibles con Intel HDR.
  * Soporte mejorado para NVIDIA Jetson Nano.
  * Soporte para los teclados de los MacBook y MacBook Pro.
  * Mejora en la velocidad de los sistemas EXT4.

Por su lado, Ubuntu trae nuevas actualizaciones y versiones de las **aplicaciones integradas:**

  * glibc 2.3
  * OpenJDK 11
  * gcc 9.2
  * Python 3.7.5
  * PHP 7.3.8
  * golang 1.12
  * Ruby 2.25
  * Perl 5.28.1
  * LibreOffice 6.3
  * Firefox 69
  * Transmission 2.9.4
  * Gedit 3.34
  * Y mucho más

## Descarga de Ubuntu 19.10

Si queréis obtener la nueva versión de Ubuntu 19.10, podéis hacerlo desde la página oficial: <https://ubuntu.com/download/desktop>.

¿Qué os parece la nueva versión de Ubuntu? ¿Hay algo que echáis en falta? Decídmelo en los comentarios, estaré encantado de leeros.

 [1]: https://www.genbeta.com/linux/gnome-kde-uniran-fuerzas-para-construir-mejor-ecosistema-aplicaciones-linux
 [2]: https://www.fsf.org
 [3]: https://www.muylinux.com/wp-content/uploads/2019/09/NVIDIA-Optimus.png
 [4]: https://blog.javinator9889.com/wp-content/uploads/2019/10/Captura-de-pantalla-de-2019-10-22-10-46-46.png
 [5]: https://149366088.v2.pressablecdn.com/wp-content/uploads/2019/10/ubuntu-19.10-installer-750x422.jpeg
 [6]: https://cache.desktopnexus.com/thumbseg/2464/2464369-bigthumbnail.jpg
 [7]: https://itsfoss.com/check-boot-time-linux/
 [8]: https://www.omgubuntu.co.uk/wp-content/uploads/2019/01/gnome-shell-performance.jpg
 [9]: https://149366088.v2.pressablecdn.com/wp-content/uploads/2019/09/linux-5.3.jpg