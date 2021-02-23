---
title: 'Instalar GCam (Google Camera) sin perder datos (no root) – Xiaomi Mi A1 & Mi A2 Lite'
author: Javinator9889
date: 2018-11-12T18:16:55+00:00
draft: false
url: /install-gcam-xiaomi-mi-a1/
cover:
  image: images/thumbnail-1.png
  hidden: false
categories:
  - Google Camera
  - Tutoriales
  - Xiaomi Mi A1
tags:
  - android
  - bootloader
  - gcam
  - google camera
  - install
  - lite
  - mi a1
  - mi a2
  - root
  - tutorial
  - xiaomi

---
La aplicación de Google conocida como _Google Camera_ es considerada una de las [mejores aplicaciones de fotografía][1] que podemos encontrar hoy en día.

En sus inicios, la aplicación estaba disponible **para todos los dispositivos** que tuvieran _Android KitKat 4.4_ o superior, pero tras varios cambios en las políticas de Google pasó a ser una aplicación específica de los dispositivos _Nexus_ y _Pixel_, debido a unas supuestas **limitaciones hardware** que, por suerte, hoy en día encontramos ya en cada vez más dispositivos, encontrándose entre ellos el _Xiaomi Mi A1_.

En este blog vamos a explicar **cómo instalar** paso a paso _Google Camera_ en este dispositivo, sin perder ningún dato durante el proceso y sin **necesidad de _root_**.

<!--more-->

* * *

# _Disclaimer_

```text
  Este tutorial se ha hecho con fines educativos y no busca en ningún momento 
  criticar ninguna marca y/o empresa.

  Así mismo, cada uno es responsable del trato que haga con su dispositivo, 
  no haciéndome ni yo ni, cualquiera relacionado con los grupos de 
  Xiaomi Mi A1 - CASTELLANO [https://goo.gl/VpLnw7] Xiaomi Mi A1 Development
  [https://goo.gl/PaAsyQ], o desarrollador(es) de las distintas aplicaciones 
  y/o métodos para conseguir niveles privilegiados de acceso al dispositivo y 
  otros equipos, ni ninguna persona física implicada directa o indirectamente 
  en los procesos aquí descritos, responsables de cualquier daño, perjurio, 
  pérdida de garantía, avería, percance o mal que le pueda ocurrir al 
  dispositivo durante la realización de los pasos descritos en este tutorial, 
  los cuales se han comprobado que funcionan en las últimas actualizaciones 
  recibidas por el terminal (última comprobación: septiembre, 2019). 
  En caso de que la última actualización no haya sido comprobada todavía, 
  es recomendable esperarse para tener ciertas garantías de éxito.

  Así mismo, este &lt;em>post&lt;/em> se ha hecho de buena fe, buscando ayudar a 
  la comunidad, y es posible que la información no sea todo lo concisa que un 
  determinado usuario necesite o que dicha información no consiga solucionar o 
  alcanzar el fin para la cual fue redactada. En este caso, el susodicho usuario 
  es libre de acceder a diversos foros y grupos para pedir ayuda, no siendo 
  necesario prestársela. De igual manera, el tutorial para el Mi A2 Lite es 
  similar al del Mi A1 exceptuando la parte de las imágenes modificadas del 
  *boot*, por lo que no se asegura completa compatibilidad.

  Recomendamos encarecidamente, en cualquier caso e independientemente del nivel 
  de cada lector de este post, realizar una lectura intensiva y comprensiva 
  del contenido de éste, para evitar los posibles daños mencionados 
  anteriormente causados por la falta de un entendimiento conciso del mismo.
```

## Índice

  1. [**Desbloqueando el _bootloader._**][2]
  2. [**Instalando _Magisk Manager _y obteniendo permiso _root_ (temporalmente).**][3]
  3. [**Configurando el dispositivo para admitir la _GCam_.**][4]
  4. [**Instalando _Google Camera_.**][5]
  5. [**Eliminando _root_ y bloqueando el _bootloader_.**][6]

&nbsp;

## 1. Desbloqueando el _bootloader_. {#bootloader_unlock}

En este paso vamos a proceder al **desbloqueo del _bootloader_** sin **perder datos**: desde la actualización de _mayo_ de 2018, Xiaomi complicó las cosas al impedir el desbloqueo/bloqueo del gestor de arranque (_bootloader_) sin perder **absolutamente todos los datos**.

Para ello, debemos ir a `Ajustes > Sistema > Información del teléfono` y pulsar **siete veces seguidas** sobre _Número de compilación_, hasta que salga un mensaje diciendo 
> *Las opciones para desarrolladores ya están activadas*

(si tenemos el teléfono **cifrado con alguna contraseña**, la introducimos para poder habilitar dichas opciones).

{{< lazyimage src="images/opciones_desarrollador.png" caption="Cómo habilitar las opciones de desarrollador" width=350 >}}

Una vez **hayamos habilitado las _Opciones de desarrollador_**, tendremos una nueva opción en la _pantalla anterior_ que pondrá: &#8220;**Opciones para desarrolladores**&#8220;. Entramos en dicha opción y habilitamos el campo _**Desbloqueo de OEM**_. Introduciremos el PIN o patrón y seleccionamos **Habilitar** cuando nos pida la confirmación.

{{< lazyimage src="images/habilitar_desbloqueo_oem.png" caption="Diálogo de confirmación al habilitar el desbloqueo OEM" width=300 >}}
{{< lazyimage src="images/desbloqueo_oem.png" caption="Opción para habilitar el desbloqueo OEM" width=300 >}}

También va a ser necesario habilitar la **depuración por USB**. Para ello, en las propias _opciones para desarrolladores_, encontramos abajo la opción que nos permite habilitar la **depuración por USB**.

{{< lazyimage src="images/depuracion_usb.png" caption="Opción para habilitar la Depuración por USB y poder usar así `adb`" width=300 >}}

Bien, ahora que ya hemos preparado el dispositivo para admitir el **desbloqueo del _bootloader_** ya podemos pasar al siguiente paso. Para ello:

  * **Apagamos** el terminal normalmente.
  * Mantenemos pulsadas los botones de **Encendido _(E)_** y **bajar volumen _(Vol-)_**: _**E + Vol-**_.
  * Tendrá que aparecer una pantalla como la siguiente, si lo hemos hecho correctamente: 
    {{< lazyimage src="images/fastboot.jpg" caption="Imagen que aparece al reiniciar correctamente en modo *fastboot* en el Xiaomi Mi A1" >}}
    
    A continuación tenemos que descargar _platform tools_ en nuestro equipo (ordenador con **Windows**, **Mac** o **Linux**). Para ello, [accedemos al enlace oficial de _Android Developers_][7] y seleccionamos nuestra versión en base al sistema operativo que tengamos. Una vez hayamos **aceptado los términos y completado la descarga**, extraemos el archivo **.zip** en una carpeta que prefiramos. A ser posible, es **extremadamente recomendable** que dicha carpeta _**no contenga espacios en blanco o caracteres &#8220;extraños&#8221;** _(no contemplados en la gramática inglesa, fuera del ASCII 128)_. En mi caso, lo voy a extraer en la carpeta _&#8220;adb&#8221;_ en la siguiente localización:
    
    ```text
    C:\adb
    ```
    
    Una vez hayamos extraído los archivos, ejecutamos la consola de comandos en **dicha ubicación**. En Windows, basta con poner en la barra de búsqueda _&#8220;cmd&#8221;_.

    {{< lazyimage src="images/cmd_we.png" caption="Ejecutando CMD en la carpeta actual desde Windows Explorer" >}}
    
    > **ATENCIÓN: AHORA VIENEN PASOS CRÍTICOS &#8211; SEGUIRLOS AL PIE DE LA LETRA**
    
    Procedemos al desbloqueo del **bootloader**. Para ello, conectamos el dispositivo *en modo fastboot* y ejecutamos los siguientes comandos:

    * * *
    
    **Comprobamos que se ha detectado el dispositivo**
    
    ```shell
    fastboot devices
    ```
    
    A continuación, _**escribimos únicamente el siguiente comando**_. Antes de ejecutarlo, en nuestro dispositivo, mantenemos pulsado el botón de _**Vol-**_:
    
    ```shell
    fastboot oem unlock
    ```
    
    Si todo ha ido bien y **se ha mantenido el botón _Vol-_ pulsado**, debería aparecer el móvil nuevamente en _modo fastboot_ y la consola de comandos estar así:

    {{< lazyimage src="images/fastboot_oem_unlock.png" caption="Así queda la consola de comandos tras ejecutar `fastboot oem unlock`" >}}
    
    Una vez comprobemos que **estamos nuevamente en modo _fastboot_, **dejamos de pulsar la tecla de _Vol-_ y ejecutamos el siguiente comando para iniciar el sistema operativo:
    
    ```shell
    fastboot reboot
    ```
    
    Ya estás listo para pasar **al punto 2**.
        
    ## 2. Instalando _Magisk Manager_ y obteniendo acceso _root_. {#magisk}
    
    Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]** en la sección anterior.
    
    A continuación vamos a proceder a la instalación de _Magisk Manager_ en nuestro Mi A1. _¿Por qué es esto necesario?_ Bien, es una cuestión interesante ya que &#8220;supuestamente&#8221; este método no utiliza _root_. Es necesario ya que, en el **paso 3** vamos a necesitar modificar unos cuantos parámetros en el dispositivo de manera que éste pueda admitir la instalación de la _GCam_. El resto de métodos (incluído el [método de AridaneAM][8] obtiene acceso _root_ temporalmente para luego retirarlo) también obtienen, de una forma u otra, acceso _root_ para poder realizar la instalación.
    
    El primer paso es instalar la aplicación _Magisk Manager_, para lo que accedemos a [este enlace][9] y descargamos la última versión (el archivo **`.apk`**) que se encuentre disponible (nos fijaremos para ello en que arriba a la izquierda ponga _latest release_):

    {{< lazyimage src="images/magisk_manager_download.png" caption="Dentro de las *releases*, descargamos la última versión disponible" >}}
    
    Una vez descargado el archivo, procedemos a instalarlo. Es posible que **necesitemos dar permiso de instalación** a aplicaciones descargadas desde la tienda, por lo que permitimos que _nuestro navegador web_ pueda instalar **aplicaciones de origen desconocido**.
    
    Cuando hayamos instalado _Magisk Manager_, iniciamos la aplicación. A medida que vayan apareciendo diversos cuadros de diálogo **pidiéndonos que instalemos y actualicemos** _Magisk Manager_, vamos aceptando sucesivamente hasta que nos pida **instalar** _Magisk_ (un archivo `.zip`), donde tendremos que esperar ya que en este momento **no podemos instalarlo**.

    {{< lazyimage src="images/installing_magisk_manager.png" caption="Tras instalar el `.apk` base de Magisk Manager, tendremos que instalar varias actualizaciones para que pueda funcionar correctamente" width=300 >}}

    {{< lazyimage src="images/installing_magisk.png" caption="Tras instalar Magisk Manager e iniciar el teléfono con el parche del *bootloader* correspondiente a la versión de Android, podremos instalar Magisk" width=300 >}}
    
    Ahora, reiniciamos el teléfono en modo _**fastboot**_, apagándolo normalmente y manteniendo pulsados luego los botones de **encendido (_E_)** y **volumen menos (_Vol-_)**: _E + Vol-._
    
    Una vez que hayamos entrado en _fastboot_ (podemos comprobarlo cuando [aparezca una pantalla como ésta][10]), conectamos el dispositivo al equipo y realizamos lo siguiente:
    
      * Descargamos **el último parche** del _boot_ modificado. Para ello, lo podemos hacer desde el siguiente enlace: [Xiaomi Mi A1 patched boot images][11]. Si la imagen que necesitas **no está en esa carpeta**, contacta en los diversos grupos de Telegram que existen, donde podrás pedirlo.  
        &#8211;  [Xiaomi Mi A1 &#8211; CASTELLANO][12]  
        &#8211;  [Xiaomi Mi A1 Development][13]  
        &#8211;  Para el _**Xiaomi Mi A2 Lite**_ &#8211; [Xiaomi Mi A2 & A2 Lite (esp)][14]
      * Guardamos dicho archivo en **la carpeta de _platform tools_**, que descargamos en el [punto anterior][2] y ejecutamos la consola de comandos en esa misma carpeta. Para ello, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][15] (si se usa Windows).
      * **Comprobamos que se ha detectado el dispositivo:** 
        ```shell
        fastboot devices
        ```
    
      * Iniciamos el dispositivo **cargando la nueva imagen** del _bootloader_, sustituyendo `MES` por el mes del que sea el parche _**(jun, jul, sep, etc.)**_:  
        ```shell
        fastboot boot patched_boot_MES.img
        ```
    
    Con esto, ya tendríamos acceso _root_ al terminal temporalmente, sin necesidad de instalar Magisk de forma permanente. Igualmente, ahora se explica cómo instalar Magisk para conservar _root_ en caso de que se quiera.
    
    Listo, ya tenemos el terminal listo para pasar **al paso 3**.
    
    ## [OPCIONAL] Instalando Magisk
    
    Una vez realizados los pasos anteriores, es cierto que podemos instalar Magisk en nuestro terminal sin mucha complicación, por lo que vamos a aprovechar este mismo tutorial para obtener acceso _root_ siempre que queramos en nuestro dispositivo (se parte de que se han realizado todos los pasos anteriores):
    
      * Dejamos que el terminal se inicie normalmente, y cuando lo haya hecho, instalamos **Magisk** desde _Magisk Manager_, seleccionando el método de instalación &#8220;_Direct Install (Recommended)_&#8220;. 

      {{< lazyimage src="images/installing_magisk.png" caption="Tras instalar Magisk Manager e iniciar el teléfono con el parche del *bootloader* correspondiente a la versión de Android, podremos instalar Magisk" width=300 >}}

      {{< lazyimage src="images/magisk_direct_install.png" caption="Método de instalación directa de Magisk usando Magisk Manager" width=300 >}}
      
      * Esperamos a que la instalación termine (puede **llevar algún tiempo**) y reiniciamos el terminal directamente desde la aplicación. 

        {{< lazyimage src="images/magisk_flashing.png" caption="Cuando el proceso de *flashing* termina, reiniciaremos el teléfono directamente desde la app" width=300 >}}

      * Una vez que el **teléfono se ha reiniciado,** comprobaremos que en efecto dispone de acceso _root_, para lo que podremos utilizar una aplicación como [_Root Checker_][16]. 

        {{< lazyimage src="images/root_checker.png" caption="Cuando el terminal se haya reiniciado después de la instalación de Magisk, comprobaremos que tenemos acceso *root*" width=300 >}}

            
    ## 3. Configurando el dispositivo para admitir la _GCam_. {#gcam_conf}
    
    Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]** y obtenido [**acceso _root_**][3] en los apartados anteriores.
    
    Este paso es **fundamental**, ya que vamos a modificar _dos variables internas del dispositivo_ para garantizar que la _Google Camera_ se ejecuta correctamente. Vamos a modificar concretamente **dos campos**: el primero de ellos habilita `HAL3` en el dispositivo, y el segundo `EIS`. Hay que escribir los comandos que aparecen a continuación con sumo cuidado, ya que un paso en falso **podría dejar el dispositivo** inutilizable.
    
    Para ello, conectamos el dispositivo a nuestro equipo y ejecutamos la consola de comandos. Para ello, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][15] (si se usa Windows):
    
      * Solicitamos **acceso al dispositivo**, escribiendo `adb devices` y dando acceso. 
        ```shell
        adb devices
        ```

        {{< lazyimage src="images/unauthorized.png" caption="Si intentamos acceder usando `adb` a un dispositivo sin los permisos suficientes, se rechazará la conexión" >}}
        

        {{< lazyimage src="images/usb_debugging_prompt.png" caption="Cuando se intenta acceder, Android mostrará un mensaje preguntando si queremos permitir la depuración por USB desde ese equipo" >}}          
        
          * Comprobamos que **efectivamente tenemos acceso**. 
          ```shell
          adb devices
          ```


          {{< lazyimage src="images/access_granted.png" caption="Tras aceptar el cuadro de diálogo, disponemos de acceso a la interfaz ADB del terminal" >}}
            
          * Accedemos a la **terminal** dentro del dispositivo y solicitamos acceso _root_: 
            ```shell
            adb shell
            ```
              
            Notaremos que aparece &#8216;$&#8217; como _prompt_ de la shell de Android (**no hay que escribirlo al ejecutar los comandos**, es únicamente indicativo.

            ```shell
            $ su
            ```
              
            {{< lazyimage src="images/su_permission_req.png" caption="Damos acceso *root* al ADB que estamos ejecutando desde el ordenador" width=300 >}}            
            
          * Habilitamos en el terminal **`HAL3`** y **`EIS`** (fijarse en que, para _EIS_, no es &#8220;_enabled_&#8221; sino &#8220;_enable_&#8220;):
            ```shell
            setprop persist.camera.HAL3.enabled 1
            setprop persist.camera.eis.enable 1
            exit
            ```
        
          * Salimos de **ADB** y reiniciamos el terminal. Ya estamos preparados para continuar con el **paso 4**.</ul> 
            
            
    ## 4. Instalando _Google Camera_. {#gcam_install}
    
    Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]**, obtenido [**acceso _root_**][3] y **[habilitado HAL3 y EIS][4]** en los apartados anteriores.
    
    Ahora, tras reiniciar el dispositivo, ya estamos listos para **instalar _Google Camera_**. Este apartado es, sin duda, el más sencillo, ya que únicamente tendremos que descargar la aplicación e instalarla en nuestro dispositivo.
    
    Para ello, accedemos a [este enlace][17] y descargamos **la versión recomendada que aparezca**. Por lo general, es recomendable utilizar las [versiones de Arnova8G2][18], pero podéis utilizar la que queráis.
    
    En este caso, vamos a usar [**<span class="redb">Arnova&#8217;s v8.2:</span> GoogleCamera-Pixel2Mod-Arnova8G2-V8.2.apk (Arnova8G2, 2018-08-13)**][19]. Instalaremos la aplicación y ya podremos usar _Google Camera_.
    
    ## 
    
    * * *
    
    > **AVISO: VERSIONES DE LA GOOGLE CAMERA CON ERRORES**
    
    Existen algunas versiones de la *Google Camera* que, a partir de la versión 9 de Android presentan errores, tales como que **no funciona el autofoco** en la máxima resolución o **los selfies salen de color verde**. Actualmente, hay disponible una Google Camera especialmente creada y optimizada para el Mi A1, la cual podéis encontrar en el siguiente enlace: [MGC Mi A1 Edition](https://s.javinator9889.com/mia1-camera).

    &nbsp;

    {{< lazyimage src="images/gcam_inside.png" caption="Una vez hayamos completado todos los pasos, podremos usar la Google Camera como si tuviéramos un teléfono Pixel" width=300 >}}
    
    ## 5. Eliminando _root_ y bloqueando el _bootloader_. {#cleaning}
    
    Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]** u obtenido [**acceso _root_**][3].
    
    Ahora que ya hemos conseguido al _Google Camera_ funcionando perfectamente, podremos **cerrar el bootloader** y **revocar el acceso _root_**. Para ello, nos dirigiremos a _Magisk Manager_ (si hemos instalado Magisk mediante el método de &#8220;_Direct Install_&#8220;) y pulsaremos sobre `Uninstall > Complete uninstall`. En otro caso, bastaría con reiniciar el terminal **para perder el acceso _root_**.

    &nbsp;

    {{< lazyimage src="images/complete_uninstall.png" caption="Tras haber habilitado la Google Camera desde ADB, podemos quitar perfectamente el acceso *root* ya que no será necesario" width=300 >}}
    
    Dejamos que el proceso termine y se **reinicie el terminal**. Cuando hayamos comprobado que **ya no disponemos de acceso _root_**, apagamos el dispositivo.
    
    > **ATENCIÓN: AHORA VIENEN PASOS CRÍTICOS &#8211; SEGUIRLOS AL PIE DE LA LETRA**
    
    Con el dispositivo ya apagado, **procederemos a bloquear de nuevo el _bootloader_**. Este proceso, al igual que en el **paso 1**, es muy crítico, ya que un paso en falso producirá **la total pérdida de los datos**.
    
    Encendemos el terminal en **modo _fastboot_**, manteniendo pulsadas las teclas de **energía (_E_)** y **bajar volumen (_Vol-_): _E + Vol-_**, y lo **conectamos a nuestro equipo**. Abrimos la consola de comandos en la **carpeta _platform tools_** para ejecutar los siguientes comandos. Para abrir rápidamente la consola en la carpeta indicada, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][15] (si se usa Windows):
    
    * * * 
    **Comprobamos que se ha detectado el dispositivo**
    
    ```shell
    fastboot devices
    ```
    
    A continuación, _**escribimos únicamente el siguiente comando**_. Antes de ejecutarlo, en nuestro dispositivo, mantenemos pulsado el botón de _**Vol-**_:
    
    ```shell
    fastboot oem lock
    ```
    
    Si todo ha ido bien y **hemos realizado el procedimiento correctamente**, el terminal debería iniciarse de nuevo en **modo _fastboot_**. Para terminar con el proceso, reiniciamos el terminal desde la consola:
    
    ```shell
    fastboot reboot
    ```
    
    El terminal **se iniciará correctamente** y ya dispondremos de la _Google Camera_ instalada en nuestro dispositivo con todo su potencial. Finalmente, podríamos revocar el **acceso a la depuración USB** así como **el desbloqueo de OEM**, para lo cual basta desactivarlo en los lugares indicados en el [**paso 1**][2].
    
    Con este modo de instalación, **no perderemos las _OTAs_ y la _GCam_ se podrá seguir usando tras cada actualización**. Si, por cualquier motivo, **no puedes iniciar la _GCam_**, puedes repetir este proceso cuantas veces quieras ya que, en principio, no perderás ningún dato.
    
    &nbsp;
    
    > **_ESTE TUTORIAL ESTÁ BASADO EN LOS VÍDEOS QUE APARECEN A CONTINUACIÓN &#8211; ESTÁN EN INGLÉS, PERO EXPLICAN A LA PERFECCIÓN GRÁFICAMENTE TODO EL PROCESO_**
    
    {{< youtube HbwVsYQajC0 >}}
    * * * 
    {{< youtube Ai5t2cKEw2E>}}

 [1]: https://goo.gl/ZP3v58
 [2]: #bootloader_unlock
 [3]: #magisk
 [4]: #gcam_conf
 [5]: #gcam_install
 [6]: #cleaning
 [7]: https://goo.gl/YReSLX
 [8]: https://goo.gl/ydT31u
 [9]: https://goo.gl/kZntL8
 [10]: https://javinator9889.com/blog/?attachment_id=245
 [11]: https://javinator9889.com/pfiles/Mi%20A1/Boot%20Images/
 [12]: https://goo.gl/VpLnw7
 [13]: https://goo.gl/PaAsyQ
 [14]: https://t.me/XiaomiA2_ES
 [15]: https://javinator9889.com/blog/?attachment_id=248
 [16]: https://goo.gl/X2hmqW
 [17]: https://goo.gl/x3P2kh
 [18]: https://goo.gl/wmzcge
 [19]: https://www.celsoazevedo.com/files/android/google-camera/f/GoogleCamera-Pixel2Mod-Arnova8G2-V8.2.apk