---
title: Instalar Android 10 (Q) en el Mi A1
author: Javinator9889
date: 2019-11-21T13:29:27+00:00
url: /instalar-android-10-mi-a1/
cover: 
  image: images/Android-10-Easter-Egg.jpg
categories:
  - Tutoriales
  - Xiaomi Mi A1
tags:
  - android 10
  - mi a1
  - q
  - tutorial

---
La nueva versión del sistema operativo de Google, [Android 10][1], trae muchas **novedades** y **ventajas** frente a la anterior, Android Pie. Entre ellas, están una mejora en _la privacidad_, una _mejor gestión_ de los permisos, el _modo oscuro_ y una _mejora en rendimiento_.

Si bien hay rumores sobre si Xiaomi actualizará el Mi A1 (_tissot_) a Android 10, hoy vamos a ver **cómo poder instalarlo** nosotros manualmente con un poco de paciencia y pericia.

Ya que, oficialmente, no hay **ninguna versión del sistema** para el terminal, vamos a instalar lo que se conoce como _GSI_: _Generic System Image_. Básicamente, es una **imagen genérica del sistema** la cual solo necesita del _kernel_ y del _vendor_ para funcionar. Por suerte, la comunidad del Mi A1 es muy activa, y existen _kernel_ muy actualizados (como **[DPA][2]**) así como _vendor_ funcionales. De este modo, podemos tener el sistema actualizado siempre a la última versión sin necesidad de que algún desarrollador o la propia Xiaomi se dedique a hacer una versión del sistema operativo **específica para el móvil**. Además, en este caso, las últimas versiones _GSI_ ofrecen un rendimiento **similar o mejor** frente a una _ROM_ dedicada.

<!--more-->

# _Disclaimer_

```
  Este tutorial se ha hecho con fines educativos y no busca en ningún
  momento criticar ninguna marca y/o empresa.

  Así mismo, cada uno es responsable del trato que haga con su dispositivo, 
  no haciéndome ni yo ni, cualquiera relacionado con los grupos de
  [Xiaomi Mi A1 - CASTELLANO](https://goo.gl/VpLnw7) o 
  [Xiaomi Mi A1 Development](https://goo.gl/PaAsyQ), o desarrollador(es) 
  de las distintas aplicaciones y/o métodos para conseguir niveles privilegiados
  de acceso al dispositivo y otros equipos, ni ninguna persona física implicada 
  directa o indirectamente en los procesos aquí descritos, responsables de 
  cualquier daño, perjurio, pérdida de garantía, avería, percance o mal 
  que le pueda ocurrir al dispositivo durante la realización de los pasos 
  descritos en este tutorial, los cuales se han comprobado que funcionan 
  en las últimas actualizaciones recibidas por el terminal. En caso de 
  que la última actualización no haya sido comprobada todavía, es recomendable 
  esperarse para tener ciertas garantías de éxito.

  Así mismo, este post se ha hecho de buena fe, buscando ayudar a la comunidad, 
  y es posible que la información no sea todo lo concisa que un determinado 
  usuario necesite o que dicha información no consiga solucionar o alcanzar el 
  fin para la cual fue redactada. En este caso, el susodicho usuario es libre de 
  acceder a diversos foros y grupos para pedir ayuda, 
  no siendo necesario prestársela.

  Recomendamos encarecidamente, en cualquier caso e independientemente del nivel 
  de cada lector de este post, realizar una lectura intensiva y comprensiva del 
  contenido de éste, para evitar los posibles daños mencionados anteriormente 
  causados por la falta de un entendimiento conciso del mismo.
```

<!-- # Índice

  1. **[Instalando un _custom recovery._][3]**
  2. **[Re-particionando el dispositivo _(Treble)._][4]**
  3. **[Formateando las particiones.][5]**
  4. **[Instalando la imagen _boot_, _vendor_ y _system_.][6]**
  5. [**Pasos finales en la instalación.**][7]
  6. [**Sección de ayuda (faq, actualizaciones, etc)**][8] -->

## 1. Instalando un _custom recovery_ {#custom_recovery}

Ya que necesitamos cambiar el sistema operativo, vamos a tener que instalar un _custom recovery_. El menú de recuperación _(recovery)_ es un elemento del sistema el cual nos permite, como dice el nombre, **recuperar el teléfono** en caso de errores. Las versiones personalizadas, además de las distintas opciones de recuperación, te permiten modificar las **entrañas del dispositivo** sin necesidad de tener grandes conocimientos e intentando mantener todo en su sitio. Aquí, lo vamos a usar para cambiar las _particiones_ del terminal e instalar el **nuevo sistema operativo**.

En este caso, vamos a usar el [TWRP de Giovix92][9] &#8211; también es posible usar el de [CosmicDan][10], pero hace tiempo que no se actualiza y Giovix cogió el relevo del proyecto. La instalación es muy sencilla:

  * Vamos al siguiente enlace: <https://s.javinator9889.com/giovix_twrp> y descargamos el zip con el _boot_ y el instalador.
  {{< lazyimage src="images/twrp.png" >}}
  * Descomprimimos el **archivo _boot_** &#8211; vamos a usar de ahora en adelante la carpeta &#8220;Mi A1&#8221; para este proyecto.

A continuación, tendremos que **desbloquear el _bootloader_** &#8211; aquí no se va a explicar, ya que se muestra en el tutorial de la Google Camera: <https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/#bootloader_unlock>. Seguid los pasos ahí explicados y no tendréis problemas.

* * *

En este momento, necesitamos tener a mano **un ordenador** y un **cable USB Tipo-C**, ya que vamos a necesitar ejecutar comandos. Iniciamos el dispositivo en modo _fastboot,_ manteniendo pulsado el botón de **encendido (_E_)** junto con **bajar volumen (_Vol-_)** y entraremos en modo _fastboot_.

{{< lazyimage src="images/fastboot.jpg" caption="Imagen que aparece al reiniciar correctamente en modo **fastboot** en el Xiaomi Mi A1" >}}

Si has seguido los pasos anteriores, tendrás las herramientas de _fastboot_ guardadas en la carpeta _**adb.**_ En este caso, **mueves los archivos** descargados anteriormente a dicha carpeta, y abres una _consola de comandos._

{{< lazyimage src="images/cmd_we.png" caption="Ejecutando CMD en la carpeta actual desde Windows Explorer" >}}

A continuación, ejecutamos los siguientes comandos:

```shell
fastboot devices
```

Comprobamos que aparece nuestro dispositivo

```shell
fastboot boot boot-recovery.img
```

E iniciamos el sistema con la imagen del _recovery_.

Una vez dentro, vamos al apartado &#8220;_Install_&#8221; y seleccionamos el **archivo zip** que hemos descargado anteriormente &#8211; el archivo se puede enviar por MTP, conectando el terminal al ordenador, o bien guardándolo en la tarjeta SD.

{{< lazyimage src="images/twrp-screen.png" caption="Vista principal de TWRP" >}}

Una vez se haya completado el proceso, vamos al menú &#8220;_Reboot_&#8221; y seleccionamos la opción &#8220;_Recovery&#8221;_. Si todo ha ido bien, debería iniciarse en el _recovery_ directamente, sin necesidad ya de ejecutar comandos.

{{< lazyimage src="images/rebootold.png" caption="Menú de reinicio en TWRP" width=300 >}}

## 2. Re-particionando el dispositivo _(Treble)_ {#treble}

Las _ROMs GSI_ necesitan que el dispositivo esté particionado siguiendo la configuración _Treble_, esto es, disponer de una partición _vendor_ así como _dual-boot_ AB. El Mi A1 ya tiene por defecto la configuración de _dual-boot_, por lo que únicamente queda generar la partición _vendor_.

> **ATENCIÓN: ESTO ELIMINARÁ TODOS LOS DATOS DEL ALMACENAMIENTO INTERNO &#8211; APPS, MULTIMEDIA, ETC.**

Es importante tener en cuenta que el procedimiento actual **eliminará por completo** todos los datos que hay en nuestro dispositivo, así que es recomendable usar TWRP para hacer un _backup_ del sistema.

Usando el TWRP de Giovix, el procedimiento es muy sencillo:

  * Vamos a &#8220;_Advanced_&#8221; y ahí, &#8220;_**Tissot Manager**&#8220;._
  * Pulsamos en la opción que dice &#8220;_Treble&#8221;_ y, una vez aceptado, el proceso comenzará.
  * **Reiniciamos** de nuevo en _recovery_, esta vez con el terminal ya _trebleizado_.

{{< lazyimage src="images/treble-menu.png" caption="Menú Treble en TWRP" width=300 >}}

Tenéis más información sobre el proceso de _Treble_ en el siguiente enlace: [\[GUIDE\] \[Q&A\] [TREBLE] From Stock to Treble &#8211; everything you need to know!][13]

## 3. Formateando las particiones {#formatting}

Ahora que hemos hecho _Treble_ en el Mi A1, necesitamos _formatear_ las particiones del terminal para poder instalar la _**custom ROM**._ 

> **ATENCIÓN: LOS PASOS QUE SE DESCRIBEN A CONTINUACIÓN SON CRÍTICOS Y PUEDEN DEJAR EL DISPOSITIVO INUTILIZABLE &#8211; HACER COPIA DE SEGURIDAD**

Necesitamos, por cada _slot_ del dispositivo, formatear las siguientes particiones:

  * _system_
  * _vendor_
  * _dvalik_
  * _data_
  * _internal storage_

{{< lazyimage src="images/format-partitions.png" caption="Particiones a formatear" width=300 >}}

Una vez hechos los _wipes_, tenemos que cambiar el _slot_ activo. Para ello, nos dirigimos al menú &#8220;_Reboot_&#8221; y anotamos en el _slot_ en que estamos:

{{< lazyimage src="images/slots.png" caption="*Slots* en TWRP" >}}

de manera que cambiamos al _slot_ inactivo, en este caso, _**slot B.**_ Le damos a &#8220;_Recovery&#8221;_ y se debería iniciar en _recovery._ Antes de hacer ningún _wipe_, comprobamos que en efecto el _slot_ activo es el **B**, ya que en otro caso el sistema no funcionará. Si no se ha cambiado el _slot,_ reiniciamos en el _bootloader_ y ejecutamos el siguiente comando desde el ordenador:

```shell
fastboot --set-active=b  # se cambia b por el slot en cuestión
```

y reiniciamos en _recovery_ de nuevo (_**Botón de encendido + Vol. +**_).

Una vez hayamos completado los formateos, procedemos al siguiente paso.

## 4. Instalando la imagen _boot_, _vendor_ y _system_ {#installing}

Ahora quedan los pasos **más importantes**: la instalación de las diferentes partes del sistema.

Por una parte, hace falta instalar _boot_ (el _kernel_). En el siguiente enlace, podéis descargar los _boot_ para diferentes tipos de _kernel_: <https://www.elranchodecornelio.com/a1index/content/treble/boot.html>.

Del mismo modo, también podéis instalar un _kernel_ personalizado. El que ahora mismo funciona mejor en todo el Mi A1 es el _kernel DPA,_ el cual podéis descargar desde aquí: <https://t.me/dpakernel>. Si queréis obtener una lista completa de las características, el enlace es este: <https://telegra.ph/DPA-Features-11-07>.

El _vendor_ se puede descargar desde el siguiente enlace: <https://www.elranchodecornelio.com/a1index/content/treble/vendor.html>. Tanto el _vendor_ de Flex como el Sooti muy bien. Además, Chon Doe ha desarrollado su propio _vendor_ con un gran rendimiento, el cual podéis obtener desde aquí: <https://s.javinator9889.com/vendor_chondoe>.

Finalmente, las _ROMs GSI_ se pueden descargar desde este enlace: <https://www.elranchodecornelio.com/a1index/content/treble/qgsi.html>. De forma particular, las más recomendables son las _ExpressLuke GSI_: <https://sourceforge.net/projects/expressluke-gsis/files/>. Las _ROMs_ que son compatibles con el Mi A1 son todas aquellas que sean **ARM64 A/B** &#8211; no confundir con **A64 A/B**.

Una vez descargada la _ROM_, si está en formato _**img.xz**_, hay que descomprimirlo para obtener la imagen _**img**_. En Linux, se puede usar el comando `unxz`; en Windows, se puede usar un descompresor como WinRAR o similar.

Movemos todos los archivos al dispositivo (recomendable la tarjeta SD) y procedemos a instalarlos en el siguiente orden:

  * Instalamos _boot_ como imagen _boot_ en el sistema (hay que seleccionar la opción &#8220;_Install image_&#8220;) 
    {{< lazyimage src="images/flash-boot.png" caption="Instalando el kernel como partición `boot`" width=300 >}}
    
      * A continuación, instalamos el **zip** con el _vendor_ (volvemos a seleccionar la opción _&#8220;Install_ _zip_&#8220;).
      * Finalmente, instalamos **la imagen del sistema** (seleccionando la opción &#8220;_Install image_&#8220;). 
        {{< lazyimage src="images/install-system.png" caption="Instalación de la imagen del sistema en la partición `system`" width=300 >}}
        
          * No tiene por qué ser necesario, pero **por seguridad** instalamos de nuevo el _TWRP Recovery_ (opción &#8220;_Install zip_&#8220;).
          * Reiniciamos en _recovery_ de nuevo.</ul> 
        
        Al reiniciar, debemos comprobar, al igual que **en el paso anterior**, que el sistema todavía **es capaz de cambiar el _slot_ activo**. En otro caso, habrá que realizar el procedimiento anterior para habilitar de nuevo el **cambio de _slot_**.
        
        ## 5. Pasos finales en la instalación {#finishing}
        
        Una vez hemos llegado aquí, lo más difícil ya está hecho. Ahora, toca cambiar el tamaño de la **partición del sistema**. Debido al proceso de hacer _Treble_, la imagen de _system_ queda más pequeña de lo normal, de forma que no se pueden añadir más componentes.
        
        Para cambiar el tamaño de la partición, vamos al menú &#8220;_Wipe_&#8221; y seleccionamos la partición _System_. Ahora, en lugar de deslizar para formatear, vamos a _**Repair or Change filesystem**_ y seleccionamos la opción que dice &#8220;_Resize file system_&#8220;. Si el proceso falla (código de error **1**), no te preocupes: reinicia en _recovery_ de nuevo y vuelve a intentarlo hasta que funcione.

        {{< lazyimage src="images/repair-fs.png" caption="En el menú *wipe*, opción para cambiar y modificar el sistema de ficheros" >}}
        
        Finalmente, instalamos las **Google Apps** (para tener acceso a las apps de Google, como la Play Store, etc.) y **Magisk,** en ambos casos _solo si queremos_, ya que no es imprescindible.
        
        Las **Google Apps** se pueden descargar desde aquí: <https://www.elranchodecornelio.com/thegappsinstaller> &#8211; sirven por igual las _Mini-ME_ y _Standard._
        
        **Magisk** puede ser descargado desde el siguiente enlace: <https://github.com/topjohnwu/Magisk/releases> &#8211; es **importante** que la versión de Magisk sea **mayor a la 17**, en otro caso fallará.

        {{< lazyimage src="images/android10.jpg" width=400 >}}
                
        Y ya estaría, tenemos instalada una _ROM_ Android 10 en el Mi A1 😱
        
        Si te ha sido útil, por favor dedica un minuto a compartirlo 🙂
        
        ## 6. Sección de ayuda [Q & A] {#qa}
        
        ### Bootloop
        
        El terminal entra en _bootloop_ cuando nunca se llega a iniciar el sistema. Si te ocurre esto, lo más probable es porque **el TWRP ya no es capaz de cambiar de _slot_**. Si sigues teniendo acceso al _recovery_, solucionarlo es muy sencillo:
        
          * Inicia a _fastboot_ manteniendo pulsadas las teclas de _**Power** **(E)**_ y **bajar volumen _(Vol -)_**.
          * Conecta el móvil al PC y comprueba que el ordenador es capaz de encontrarlo (puede que necesites descargar los _drivers_; puedes hacerlo desde este enlace: <https://goo.gl/YReSLX>): 
            ```shell
            fastboot devices
            ```
        
          * Finalmente, hacemos que el móvil cambie de _slot_ &#8211; si estaba en el _slot A,_ se cambia al _slot B_ y viceversa: 
            ```shell
            fastboot current-slot    # anotamos el slot actual
            fastboot --set-active=b  # ponemos el otro slot
            ```
        
          * Reiniciamos en _recovery_ y comprobamos que, en efecto, podemos ya cambiar el _slot_ desde allí.
        
        Tras seguir estos pasos, se suele poder iniciar el sistema. Igualmente, es recomendable volver a seguir los pasos para **evitar errores**.
        
        ### Error en la partición _data_
        
        Hay muchas veces en las que, al hacer un _wipe_ sobre la partición _data_, se produce un fallo que se muestra **con texto en rojo en la pantalla**.

        {{< lazyimage src="images/data-err.jpg" caption="Error en la partición `data`" >}}
        
        Para solucionar esto, los pasos a seguir son muy sencillos (obviamente, se borrarán todos los datos en esa partición):
        
          * En el _recovery_, revisar que, en los ajustes, la opción **&#8220;_Use rm -rf instead of formatting_&#8220;** esté desactivada.
          * Ve al menú _Wipe_ y selecciona la opción _Format data_. Cuando te pregunte por la confirmación, escribe _yes_ y el error debería de haberse ido.
        
        ### Instalando una _ROM_ normal (no _Treble_)
        
        Para instalar una _ROM_ normal, es tan sencillo como ir al menú _Install_ y seleccionar el zip instalable de dicha _ROM:_ las particiones _vendor_ y _boot_ no afectan a la instalación, en principio.
        
        ### Sistema congelado por la _GCam_
        
        La actualización de Android 10 tiene algunos problemas con las cámaras de Google (no es por usar _GSI_, está generalizado inclusive en los teléfonos Pixel, el cual provoca que el sistema se congele, se reinicie y se desconfigure.
        
        Para solucionar este problema, hay que ejecutar las siguientes órdenes, o bien usando ADB o bien ejecutando una consola como _root_ (por ejemplo, [Termux][15]):
        
        ```shell
        settings put global setup_wizard_has_run 1
        settings put secure user_setup_complete 1
        settings put global device_provisioned 1
        ```
        
        Hay algunas _GCam_ que evitan este problema, puedes buscarlas si estás interesado en poder usarlas sin muchos problemas (la que he probado y que funciona es la _Razer V2.0_ o algunas _GCam 5_).
        
        ### Actualización del sistema
        
        Si hay una nueva **actualización del sistema**, la forma de proceder es muy sencilla, y si se siguen los siguientes pasos no habrá ningún problema:
        
          1. Descargamos la _nueva actualización_ y la descomprimimos. Además, descargaremos las _GApps (Google Apps)_ en caso de que las necesitemos (en el punto [**5. Pasos finales en la instalación.**][7] viene detalladas qué _Google Apps_ se pueden usar y cuáles son recomendables). Si es la primera vez que hacemos una actualización del sistema, es imprescindible **instalar también la imagen _boot_**. En el punto **[4. Instalando la imagen _boot_, _vendor_ y _system_.][6]** se detalla cómo descargarlo e instalarlo.
          2. Ponemos el archivo **img** en una carpeta que tengamos localizada, preferiblemente en la tarjeta SD.
          3. Apagamos el terminal y lo **iniciamos en modo** _recovery_ (pulsando el botón de **encendido (E)** y **subir volumen (Vol. +)**).
          4. Cambiamos el _slot activo_. Para ello, vamos al menú _**Reboot**_ y seleccionamos el otro _slot_ (si estamos en el _slot A_, por ejemplo, elegimos el _slot B_ y viceversa). Después, reiniciamos de nuevo en _recovery_. 
             {{< lazyimage src="images/slots.png" caption="Cambio de *slot* en TWRP" >}}
            
              Esto permite **instalar la actualización en el otro _slot_**, de manera que si algún paso de la actualización fuera mal o existiera algún error, podríamos **cambiar al _slot_ anterior** y recuperar nuestro dispositivo sin errores.
            
              * Una vez el dispositivo se haya iniciado de nuevo, comprobamos que en efecto se ha cambiado el _slot_, y nos dirigimos al menú _**Install**_. Allí, navegamos hasta la ruta en la que hemos descargado anteriormente la **actualización de la ROM** y escogemos la opción de _**Install image**_.
                {{< lazyimage src="images/install-system.png" caption="Instalando la imagen del sistema" width=300 >}}
                
                Seleccionamos el archivo **img** que hemos descomprimido anteriormente y lo instalamos. Cuando haya finalizado la instalación, vamos al menú de _**Reboot**_ y reiniciamos de nuevo en _recovery_.  
                Si, además, es la primera vez que actualizamos el sistema por este método, será necesario **instalar la imagen _boot_** también. Para ello, en la ruta donde se haya descargado, la seleccionamos y la instalamos por el mismo método por el que hemos instalado el sistema. En principio no sería necesario, pero por precacución después de hacer este paso **también instalaremos el _recovery_** de nuevo.

                {{< lazyimage src="images/flash-boot.png" caption="Instalando *boot* como partición `boot`" width=300 >}}
                
              * Ahora, cambiamos el tamaño a la partición del sistema. Para ello, seleccionamos la opción _**Wipe**_ y marcamos la partición _System_. Pulsando el botón _**Repair or change filesystem**_, accedemos a un nuevo menú en el cual debemos escoger la opción de _**Resize** **filesystem**_.

                {{< lazyimage src="images/repair-fs.png" >}}  
                
                Una vez el proceso haya finalizado sin errores (si hay algún problema, reiniciamos de nuevo en _recovery_ y volvemos a intentar el proceso), estamos listos para instalar los _extras_ que usemos.

              * Finalmente, procedemos a **instalar las _GApps_** en caso de que queramos usarlas. Al igual que en el paso 5, vamos a la ruta donde estén descargadas y seleccionamos la opción _**Install zip**_. Escogemos las _GApps_ que queramos usar y las instalamos.
              * Ya estamos listos para iniciar de nuevo en el sistema y disfrutar de la **nueva actualización** de la _ROM_.

 [1]: https://www.android.com/android-10/
 [2]: https://t.me/dpakernel
 [3]: #custom_recovery
 [4]: #treble
 [5]: #formatting
 [6]: #installing
 [7]: #finishing
 [8]: #qa
 [9]: https://forum.xda-developers.com/mi-a1/development/recovery-twrp-3-3-1-0-tissot-manager-t3976117
 [10]: https://forum.xda-developers.com/mi-a1/development/treble-twrp-installer-treble-manager-t3793637/page28
 [11]: https://blog.javinator9889.com/wp-content/uploads/2019/11/Captura-de-pantalla-de-2019-11-21-12-32-50.png
 [12]: data:image/png;base64,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
 [13]: https://forum.xda-developers.com/mi-a1/how-to/treble-stock-to-treble-everything-to-t3793734
 [14]: https://blog.javinator9889.com/wp-content/uploads/2019/11/photo_2019-11-21_14-22-14.jpg
 [15]: https://play.google.com/store/apps/details?id=com.termux&hl=es_419
 [16]: https://blog.javinator9889.com/wp-content/uploads/2019/11/Screenshot_2019-11-21-13-04-41-e1574342307980.png