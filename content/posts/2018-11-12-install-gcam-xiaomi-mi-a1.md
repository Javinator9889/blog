---
title: 'Instalar GCam (Google Camera) sin perder datos (no root) – Xiaomi Mi A1 & Mi A2 Lite'
author: Javinator9889
type: post
date: 2018-11-12T18:16:55+00:00
url: /install-gcam-xiaomi-mi-a1/
featured_image: /wp-content/uploads/2018/11/thumbnail-1.png
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

En sus inicios, la aplicación estaba disponible **para todos los dispositivos** que tuvieran _Android KitKat 4.4 _o superior, pero tras varios cambios en las políticas de Google pasó a ser una aplicación específica de los dispositivos _Nexus _y _Píxel_, debido a unas supuestas **limitaciones hardware** que, por suerte, hoy en día encontramos ya en cada vez más dispositivos, encontrándose entre ellos el _Xiaomi Mi A1_.

En este blog vamos a explicar **cómo instalar** paso a paso _Google Camera_ en este dispositivo, sin perder ningún dato durante el proceso y sin **necesidad de _root_**.

<!--more-->

* * *

# _Disclaimer_

<p style="text-align: center;">
  <code>Este tutorial se ha hecho con fines educativos y no busca en ningún momento criticar ninguna marca y/o empresa. </code>
</p>

<p style="text-align: center;">
  <code>Así mismo, cada uno es responsable del trato que haga con su dispositivo, no haciéndome ni yo ni, cualquiera relacionado con los grupos de &lt;a href="https://goo.gl/VpLnw7">Xiaomi Mi A1 - CASTELLANO&lt;/a> o &lt;a href="https://goo.gl/PaAsyQ">Xiaomi Mi A1 Development&lt;/a>, o desarrollador(es) de las distintas aplicaciones y/o métodos para conseguir niveles privilegiados de acceso al dispositivo y otros equipos, ni ninguna persona física implicada directa o indirectamente en los procesos aquí descritos, responsables de cualquier daño, perjurio, pérdida de garantía, avería, percance o mal que le pueda ocurrir al dispositivo durante la realización de los pasos descritos en este tutorial, los cuales se han comprobado que funcionan en las últimas actualizaciones recibidas por el terminal (&lt;em>última comprobación: septiembre, 2019&lt;/em>). En caso de que la última actualización no haya sido comprobada todavía, es recomendable esperarse para tener ciertas garantías de éxito. </code>
</p>

<p style="text-align: center;">
  <code>Así mismo, este &lt;em>post&lt;/em> se ha hecho de buena fe, buscando ayudar a la comunidad, y es posible que la información no sea todo lo concisa que un determinado usuario necesite o que dicha información no consiga solucionar o alcanzar el fin para la cual fue redactada. En este caso, el susodicho usuario es libre de acceder a diversos foros y grupos para pedir ayuda, no siendo necesario prestársela. De igual manera, el tutorial para el Mi A2 Lite es similar al del Mi A1 exceptuando la parte de las imágenes modificadas del &lt;em>boot&lt;/em>, por lo que no se asegura completa compatibilidad.</code>
</p>

<p style="text-align: center;">
  <code>Recomendamos encarecidamente, en cualquier caso e independientemente del nivel de cada lector de este &lt;em>post&lt;/em>, realizar una lectura intensiva y comprensiva del contenido de éste, para evitar los posibles daños mencionados anteriormente causados por la falta de un entendimiento conciso del mismo.</code>
</p>

## Índice

  1. [**Desbloqueando el _bootloader._**][2]
  2. [**Instalando _Magisk Manager _y obteniendo permiso _root_ (temporalmente).**][3]
  3. [**Configurando el dispositivo para admitir la _GCam_.**][4]
  4. [**Instalando _Google Camera_.**][5]
  5. [**Eliminando _root_ y bloqueando el _bootloader_.**][6]

&nbsp;

## 1. Desbloqueando el _bootloader_. {#bootloader_unlock}

En este paso vamos a proceder al **desbloqueo del _bootloader_** sin **perder datos**: desde la actualización de _mayo _de 2018, Xiaomi complicó las cosas al impedir el desbloqueo/bloqueo del gestor de arranque (_bootloader_) sin perder **absolutamente todos los datos**.

Para ello, debemos ir a `Ajustes > Sistema > Información del teléfono` y pulsar **siete veces seguidas** sobre _Número de compilación_, hasta que salga un mensaje diciendo &#8220;_Las opciones para desarrolladores ya están activadas_&#8221; (si tenemos el teléfono **cifrado con alguna contraseña**, la introducimos para poder habilitar dichas opciones).

&nbsp;

<div id="attachment_239" style="width: 586px" class="wp-caption aligncenter">
  <a href="https://javinator9889.sytes.net/blog/?attachment_id=239"><img aria-describedby="caption-attachment-239" loading="lazy" class="wp-image-239 size-large" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/opciones_desarrollador-576x1024.png" alt="" width="576" height="1024" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
  
  <p id="caption-attachment-239" class="wp-caption-text">
    Cómo habilitar las opciones de desarrollador
  </p>
</div>

&nbsp;

Una vez **hayamos habilitado las **_Opciones de desarrollador_, tendremos una nueva opción en la _pantalla anterior_ que pondrá: &#8220;**Opciones para desarrolladores**&#8220;. Entramos en dicha opción y habilitamos el campo _**Desbloqueo de OEM**__. _Introduciremos el PIN o patrón y seleccionamos **Habilitar** cuando nos pida la confirmación.

<div id='gallery-5' class='gallery galleryid-235 gallery-columns-2 gallery-size-large'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/habilitar_desbloqueo_oem/'><img width="576" height="1024" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-576x1024.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-5-242" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-5-242'>
      Confirmation dialog for enabling OEM unlock
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/desbloqueo_oem/'><img width="576" height="1024" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-576x1024.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-5-241" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-5-241'>
      Option for enabling OEM unlock
    </dd>
  </dl>
  
  <br style="clear: both" />
</div>

También va a ser necesario habilitar la **depuración por USB**. Para ello, en las propias _opciones para desarrolladores_, encontramos abajo la opción que nos permite habilitar la **depuración por USB**.

<div id="attachment_244" style="width: 586px" class="wp-caption aligncenter">
  <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/depuracion_usb/" rel="attachment wp-att-244"><img aria-describedby="caption-attachment-244" loading="lazy" class="wp-image-244 size-large" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/depuracion_usb-576x1024.png" alt="" width="576" height="1024" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
  
  <p id="caption-attachment-244" class="wp-caption-text">
    Opción para poder habilitar la Depuración por USB y así usar adb
  </p>
</div>

&nbsp;

Bien, ahora que ya hemos preparado el dispositivo para admitir el **desbloqueo del _bootloader_** ya podemos pasar al siguiente paso. Para ello:

  * **Apagamos** el terminal normalmente.
  * Mantenemos pulsadas los botones de **Encendido _(E)_** y **bajar volumen _(Vol-)_**: _**E + Vol-**_.
  * Tendrá que aparecer una pantalla como la siguiente, si lo hemos hecho correctamente: 
    <div id="attachment_245" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/fastboot/" rel="attachment wp-att-245"><img aria-describedby="caption-attachment-245" loading="lazy" class="wp-image-245" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/fastboot-1024x576.jpg" alt="" width="600" height="338" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot-1024x576.jpg 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot-300x169.jpg 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot-768x432.jpg 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot.jpg 1920w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-245" class="wp-caption-text">
        Imagen que aparece al reiniciar correctamente en modo fastboot en el Xiaomi Mi A1
      </p>
    </div>
    
    &nbsp;</li> </ul> 
    
    A continuación tenemos que descargar _platform tools_ en nuestro equipo (ordenador con **Windows**, **Mac** o **Linux**). Para ello, [accedemos al enlace oficial de _Android Developers_][7] y seleccionamos nuestra versión en base al sistema operativo que tengamos. Una vez hayamos **aceptado los términos y completado la descarga**, extraemos el archivo **.zip** en una carpeta que prefiramos. A ser posible, es **extremadamente recomendable** que dicha carpeta _**no contenga espacios en blanco o caracteres &#8220;extraños&#8221;** (__no contemplados en la gramática inglesa, fuera del ASCII 128)_. En mi caso, lo voy a extraer en la carpeta _&#8220;adb&#8221;_ en la siguiente localización:
    
    `C:\adb`
    
    Una vez hayamos extraído los archivos, ejecutamos la consola de comandos en **dicha ubicación**. En Windows, basta con poner en la barra de búsqueda _&#8220;cmd&#8221;_.
    
    <div id="attachment_248" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/cmd_we/" rel="attachment wp-att-248"><img aria-describedby="caption-attachment-248" loading="lazy" class="wp-image-248" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/cmd_we-1024x695.png" alt="" width="600" height="407" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we-1024x695.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we-300x204.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we-768x521.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we.png 1179w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-248" class="wp-caption-text">
        Ejecutando CMD en la carpeta actual desde Windows Explorer
      </p>
    </div>
    
    &nbsp;
    
    ## <span style="color: #ff0000;">ATENCIÓN: AHORA VIENEN PASOS CRÍTICOS &#8211; SEGUIRLOS AL PIE DE LA LETRA</span>
    
    <span style="color: #000000;">Procedemos al desbloqueo del <em>bootloader</em>. Para ello, conectamos el dispositivo <em>en modo fastboot</em> y ejecutamos los siguientes comandos:</span>
    
    **Comprobamos que se ha detectado el dispositivo:**
    
    <pre class="brush: bash; title: ; notranslate" title="">fastboot devices</pre>
    
    A continuación, _**escribimos únicamente el siguiente comando**_. Antes de ejecutarlo, en nuestro dispositivo, mantenemos pulsado el botón de _**Vol-**__:_
    
    <pre class="brush: bash; title: ; notranslate" title="">fastboot oem unlock</pre>
    
    Si todo ha ido bien y **se ha mantenido el botón _Vol-_ pulsado**, debería aparecer el móvil nuevamente en _modo fastboot_ y la consola de comandos estar así:
    
    <div id="attachment_255" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/fastboot_oem_unlock/" rel="attachment wp-att-255"><img aria-describedby="caption-attachment-255" loading="lazy" class="wp-image-255" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/fastboot_oem_unlock-1024x594.png" alt="" width="600" height="348" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock-1024x594.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock-300x174.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock-768x446.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock.png 1196w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-255" class="wp-caption-text">
        Así se queda la consola de comandos tras ejecutar &#8220;<code>fastboot oem unlock</code>&#8220;
      </p>
    </div>
    
    Una vez comprobemos que **estamos nuevamente en modo _fastboot_, **dejamos de pulsar la tecla de _Vol-_ y ejecutamos el siguiente comando para iniciar el sistema operativo:
    
    <pre class="brush: bash; title: ; notranslate" title="">fastboot reboot</pre>
    
    Ya estás listo para pasar **al punto 2**.
    
    &nbsp;
    
    ## 2. Instalando _Magisk Manager_ y obteniendo acceso _root_. {#magisk}
    
    Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]_ _**en la sección anterior.
    
    A continuación vamos a proceder a la instalación de _Magisk Manager_ en nuestro Mi A1. _¿Por qué es esto necesario?_ Bien, es una cuestión interesante ya que &#8220;supuestamente&#8221; este método no utiliza _root_. Es necesario ya que, en el **paso 3** vamos a necesitar modificar unos cuantos parámetros en el dispositivo de manera que éste pueda admitir la instalación de la _GCam_. El resto de métodos (incluído el [método de AridaneAM][8] obtiene acceso _root_ temporalmente para luego retirarlo) también obtienen, de una forma u otra, acceso _root_ para poder realizar la instalación.
    
    El primer paso es instalar la aplicación _Magisk Manager_, para lo que accedemos a [este enlace][9] y descargamos la última versión (el archivo `<strong>.apk</strong>`) que se encuentre disponible (nos fijaremos para ello en que arriba a la izquierda ponga _latest release_):
    
    <div id="attachment_259" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/magisk_manager_download/" rel="attachment wp-att-259"><img aria-describedby="caption-attachment-259" loading="lazy" class="wp-image-259" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/magisk_manager_download-1024x626.png" alt="" width="600" height="367" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_manager_download-1024x626.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_manager_download-300x183.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_manager_download-768x469.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_manager_download.png 1039w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-259" class="wp-caption-text">
        Dentro de las &#8220;<em>releases</em>&#8220;, descargaremos la última que esté disponible
      </p>
    </div>
    
    Una vez descargado el archivo, procedemos a instalarlo. Es posible que **necesitemos dar permiso de instalación** a aplicaciones descargadas desde la tienda, por lo que permitimos que _nuestro navegador web_ pueda instalar **aplicaciones de origen desconocido**.
    
    Cuando hayamos instalado _Magisk Manager_, iniciamos la aplicación. A medida que vayan apareciendo diversos cuadros de diálogo **pidiéndonos que instalemos y actualicemos** _Magisk Manager_, vamos aceptando sucesivamente hasta que nos pida **instalar **_Magisk_ (un archivo .zip), donde tendremos que esperar ya que en este momento **no podemos instalarlo**.
    
    <div id='gallery-6' class='gallery galleryid-235 gallery-columns-2 gallery-size-full'>
      <dl class='gallery-item'>
        <dt class='gallery-icon portrait'>
          <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/installing_magisk_manager/'><img width="330" height="564" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk_manager.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-6-261" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk_manager.png 330w, https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk_manager-176x300.png 176w" sizes="(max-width: 330px) 100vw, 330px" /></a>
        </dt>
        
        <dd class='wp-caption-text gallery-caption' id='gallery-6-261'>
          Tras instalar el .apk base de Magisk Manager, tendremos que instalar varias actualizaciones para que pueda funcionar correctamente.
        </dd>
      </dl>
      
      <dl class='gallery-item'>
        <dt class='gallery-icon portrait'>
          <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/installing_magisk/'><img width="339" height="583" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-6-260" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png 339w, https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk-174x300.png 174w" sizes="(max-width: 339px) 100vw, 339px" /></a>
        </dt>
        
        <dd class='wp-caption-text gallery-caption' id='gallery-6-260'>
          Tras instalar Magisk Manager e iniciar el teléfono con el parche del bootloader correspondiente a la versión de Android, podremos instalar Magisk
        </dd>
      </dl>
      
      <br style="clear: both" />
    </div>
    
    Ahora, reiniciamos el teléfono en modo _**fastboot**__,_ apagándolo normalmente y manteniendo pulsados luego los botones de **encendido (_E_) **y **volumen menos (_Vol-_)**: _E + Vol-._
    
    Una vez que hayamos entrado en _fastboot_ (podemos comprobarlo cuando [aparezca una pantalla como ésta][10]), conectamos el dispositivo al equipo y realizamos lo siguiente:
    
      * Descargamos **el último parche** del _boot_ modificado. Para ello, lo podemos hacer desde el siguiente enlace: [Xiaomi Mi A1 patched boot images][11]. Si la imagen que necesitas **no está en esa carpeta**, contacta en los diversos grupos de Telegram que existen, donde podrás pedirlo.  
        &#8211;  [Xiaomi Mi A1 &#8211; CASTELLANO][12]  
        &#8211;  [Xiaomi Mi A1 Development][13]  
        &#8211;  Para el _**Xiaomi Mi A2 Lite** _&#8211; [Xiaomi Mi A2 & A2 Lite (esp)][14]
      * Guardamos dicho archivo en **la carpeta de _platform tools_**, que descargamos en el [punto anterior][2] y ejecutamos la consola de comandos en esa misma carpeta. Para ello, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][15] (si se usa Windows).
      * **Comprobamos que se ha detectado el dispositivo:** <pre class="brush: bash; title: ; notranslate" title="">fastboot devices</pre>
    
      * Iniciamos el dispositivo **cargando la nueva imagen** del _bootloader_, sustituyendo `MES` por el mes del que sea el parche _**(jun, jul, sep, etc.)**_: <pre class="brush: bash; title: ; notranslate" title="">fastboot boot patched_boot_MES.img</pre>
    
    Con esto, ya tendríamos acceso _root_ al terminal temporalmente, sin necesidad de instalar Magisk de forma permanente. Igualmente, ahora se explica cómo instalar Magisk para conservar _root_ en caso de que se quiera.
    
    Listo, ya tenemos el terminal listo para pasar **al paso 3**.
    
    ## [OPCIONAL] Instalando Magisk
    
    Una vez realizados los pasos anteriores, es cierto que podemos instalar Magisk en nuestro terminal sin mucha complicación, por lo que vamos a aprovechar este mismo tutorial para obtener acceso _root_ siempre que queramos en nuestro dispositivo (se parte de que se han realizado todos los pasos anteriores):
    
      * Dejamos que el terminal se inicie normalmente, y cuando lo haya hecho, instalamos **Magisk** desde _Magisk Manager_, seleccionando el método de instalación &#8220;_Direct Install (Recommended)_&#8220;. <div id='gallery-7' class='gallery galleryid-235 gallery-columns-2 gallery-size-full'>
          <dl class='gallery-item'>
            <dt class='gallery-icon portrait'>
              <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/installing_magisk/'><img width="339" height="583" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-7-260" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png 339w, https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk-174x300.png 174w" sizes="(max-width: 339px) 100vw, 339px" /></a>
            </dt>
            
            <dd class='wp-caption-text gallery-caption' id='gallery-7-260'>
              Tras instalar Magisk Manager e iniciar el teléfono con el parche del bootloader correspondiente a la versión de Android, podremos instalar Magisk
            </dd>
          </dl>
          
          <dl class='gallery-item'>
            <dt class='gallery-icon portrait'>
              <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/magisk_direct_install/'><img width="353" height="581" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_direct_install.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-7-263" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_direct_install.png 353w, https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_direct_install-182x300.png 182w" sizes="(max-width: 353px) 100vw, 353px" /></a>
            </dt>
            
            <dd class='wp-caption-text gallery-caption' id='gallery-7-263'>
              Método de instalación directo de Magisk usando Magisk Manager
            </dd>
          </dl>
          
          <br style="clear: both" />
        </div>
    
      * Esperamos a que la instalación termine (puede **llevar algún tiempo**) y reiniciamos el terminal directamente desde la aplicación. 
        <div id="attachment_264" style="width: 178px" class="wp-caption aligncenter">
          <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/magisk_flashing/" rel="attachment wp-att-264"><img aria-describedby="caption-attachment-264" loading="lazy" class="wp-image-264 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/magisk_flashing-168x300.png" alt="" width="168" height="300" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_flashing-168x300.png 168w, https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_flashing.png 337w" sizes="(max-width: 168px) 100vw, 168px" /></a>
          
          <p id="caption-attachment-264" class="wp-caption-text">
            Cuando el proceso de &#8220;flashing&#8221; termina, reiniciaremos el teléfono directamente desde la aplicación.
          </p>
        </div>
        
        &nbsp;</li> 
        
          * Una vez que el **teléfono se ha reiniciado,** comprobaremos que en efecto dispone de acceso _root_, para lo que podremos utilizar una aplicación como [_Root Checker_][16]. 
            <div id="attachment_265" style="width: 191px" class="wp-caption aligncenter">
              <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/root_checker/" rel="attachment wp-att-265"><img aria-describedby="caption-attachment-265" loading="lazy" class="wp-image-265 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/root_checker-181x300.png" alt="" width="181" height="300" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/root_checker-181x300.png 181w, https://blog.javinator9889.com/wp-content/uploads/2018/11/root_checker.png 341w" sizes="(max-width: 181px) 100vw, 181px" /></a>
              
              <p id="caption-attachment-265" class="wp-caption-text">
                Cuando el terminal haya reiniciado después de la instalación de Magisk, comprobaremos que tenemos acceso root.
              </p>
            </div></li> </ul> 
            
            &nbsp;
            
            ## 3. Configurando el dispositivo para admitir la _GCam_. {#gcam_conf}
            
            Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]_ _**y obtenido [**acceso _root_**][3] en los apartados anteriores.
            
            Este paso es **fundamental**, ya que vamos a modificar _dos variables internas del dispositivo_ para garantizar que la _Google Camera_ se ejecuta correctamente. Vamos a modificar concretamente **dos campos**: el primero de ellos habilita `HAL3` en el dispositivo, y el segundo `EIS`. Hay que escribir los comandos que aparecen a continuación con sumo cuidado, ya que un paso en falso **podría dejar el dispositivo **inutilizable.
            
            Para ello, conectamos el dispositivo a nuestro equipo y ejecutamos la consola de comandos. Para ello, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][15] (si se usa Windows):
            
              * Solicitamos **acceso al dispositivo**, escribiendo `adb devices` y dando acceso. <pre class="brush: bash; title: ; notranslate" title="">adb devices</pre>
                
                <div id='gallery-8' class='gallery galleryid-235 gallery-columns-1 gallery-size-large'>
                  <dl class='gallery-item'>
                    <dt class='gallery-icon landscape'>
                      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/unauthorized/'><img width="629" height="358" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-1024x583.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-8-266" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-1024x583.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-300x171.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-768x437.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized.png 1203w" sizes="(max-width: 629px) 100vw, 629px" /></a>
                    </dt>
                    
                    <dd class='wp-caption-text gallery-caption' id='gallery-8-266'>
                      Si intentamos acceder usando &#8220;adb&#8221; a un dispositivo sin los permisos suficientes, el terminal rechazará la conexión.
                    </dd>
                  </dl>
                  
                  <br style="clear: both" />
                  
                  <dl class='gallery-item'>
                    <dt class='gallery-icon portrait'>
                      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/usb_debugging_prompt/'><img width="335" height="565" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/usb_debugging_prompt.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-8-267" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/usb_debugging_prompt.png 335w, https://blog.javinator9889.com/wp-content/uploads/2018/11/usb_debugging_prompt-178x300.png 178w" sizes="(max-width: 335px) 100vw, 335px" /></a>
                    </dt>
                    
                    <dd class='wp-caption-text gallery-caption' id='gallery-8-267'>
                      Cuando se nos deniega el acceso, Android mostrará un mensaje indicando que si queremos permitir el acceso desde el equipo.
                    </dd>
                  </dl>
                  
                  <br style="clear: both" />
                </div></li> 
                
                  * Comprobamos que **efectivamente tenemos acceso**. <pre class="brush: bash; title: ; notranslate" title="">adb devices</pre>
                    
                    <div id="attachment_268" style="width: 310px" class="wp-caption aligncenter">
                      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/access_granted/" rel="attachment wp-att-268"><img aria-describedby="caption-attachment-268" loading="lazy" class="wp-image-268 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/access_granted-300x145.png" alt="" width="300" height="145" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/access_granted-300x145.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/access_granted-768x371.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/access_granted-1024x494.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/access_granted.png 1199w" sizes="(max-width: 300px) 100vw, 300px" /></a>
                      
                      <p id="caption-attachment-268" class="wp-caption-text">
                        Tras aceptar el cuadro de diálogo, disponemos de acceso a la interfaz ADB del terminal.
                      </p>
                    </div>
                    
                    &nbsp;</li> 
                    
                      * Accedemos a la **terminal** dentro del dispositivo y solicitamos acceso _root_: <pre class="brush: bash; title: ; notranslate" title="">adb shell</pre>
                        
                        Notaremos que aparece &#8216;$&#8217; como _prompt_ de la shell de Android (**no hay que escribirlo al ejecutar los comandos**, es únicamente indicativo).
                        
                        <pre class="brush: bash; title: ; notranslate" title="">$ su</pre>
                        
                        <div id="attachment_269" style="width: 187px" class="wp-caption aligncenter">
                          <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/su_permission_req/" rel="attachment wp-att-269"><img aria-describedby="caption-attachment-269" loading="lazy" class="wp-image-269 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/su_permission_req-177x300.png" alt="" width="177" height="300" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/su_permission_req-177x300.png 177w, https://blog.javinator9889.com/wp-content/uploads/2018/11/su_permission_req.png 343w" sizes="(max-width: 177px) 100vw, 177px" /></a>
                          
                          <p id="caption-attachment-269" class="wp-caption-text">
                            Damos acceso root al ADB que estamos ejecutando en el ordenador.
                          </p>
                        </div>
                        
                        &nbsp;</li> 
                        
                          * Habilitamos en el terminal **`HAL3`** y **`EIS`** (fijarse en que, para _EIS_, no es &#8220;_enabled_&#8221; sino &#8220;_enable_&#8220;): <pre class="brush: bash; title: ; notranslate" title="">setprop persist.camera.HAL3.enabled 1</pre>
                            
                            <pre class="brush: bash; title: ; notranslate" title="">setprop persist.camera.eis.enable 1</pre>
                            
                            <pre class="brush: bash; title: ; notranslate" title="">exit</pre>
                        
                          * Salimos de **ADB** y reiniciamos el terminal. Ya estamos preparados para continuar con el **paso 4**.</ul> 
                        
                        &nbsp;
                        
                        ## 4. Instalando _Google Camera_. {#gcam_install}
                        
                        Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2], **obtenido [**acceso _root_**][3] y **[habilitado HAL3 y EIS][4]** en los apartados anteriores.
                        
                        Ahora, tras reiniciar el dispositivo, ya estamos listos para **instalar _Google Camera_**. Este apartado es, sin duda, el más sencillo, ya que únicamente tendremos que descargar la aplicación e instalarla en nuestro dispositivo.
                        
                        Para ello, accedemos a [este enlace][17] y descargamos **la versión recomendada que aparezca**. Por lo general, es recomendable utilizar las [versiones de Arnova8G2][18], pero podéis utilizar la que queráis.
                        
                        En este caso, vamos a usar [**<span class="redb">Arnova&#8217;s v8.2:</span> GoogleCamera-Pixel2Mod-Arnova8G2-V8.2.apk (Arnova8G2, 2018-08-13)**][19]. Instalaremos la aplicación y ya podremos usar _Google Camera_.
                        
                        ## 
                        
                        * * *
                        
                        ## <span style="color: #ff0000;">AVISO: VERSIONES DE LA GOOGLE CAMERA CON ERRORES</span>
                        
                        <span style="color: #000000;">Existen algunas versiones de la <em>Google Camera</em> que, a partir de la versión 9 de Android presentan errores, tales como que <strong>no funciona el autofoco</strong> en la máxima resolución o <strong>los selfies salen de color verde</strong>. Actualmente, hay disponible una Google Camera especialmente creada y optimizada para el Mi A1, la cual podéis encontrar en el siguiente enlace: <a href="https://s.javinator9889.com/mia1-camera">MGC Mi A1 Edition</a>.</span>
                        
                        <div id="attachment_272" style="width: 586px" class="wp-caption aligncenter">
                          <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/gcam_inside/" rel="attachment wp-att-272"><img aria-describedby="caption-attachment-272" loading="lazy" class="wp-image-272 size-large" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/gcam_inside-576x1024.png" alt="" width="576" height="1024" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
                          
                          <p id="caption-attachment-272" class="wp-caption-text">
                            Una vez hayamos completado todos los pasos, podremos usar la Google Camera como si tuviéramos un teléfono Píxel.
                          </p>
                        </div>
                        
                        &nbsp;
                        
                        ## 5. **Eliminando _root_ y bloqueando el _bootloader_.** {#cleaning}
                        
                        Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2] **u obtenido [**acceso _root_**][3].
                        
                        Ahora que ya hemos conseguido al _Google Camera_ funcionando perfectamente, podremos **cerrar el bootloader** y **revocar el acceso _root_**. Para ello, nos dirigiremos a _Magisk Manager_ (si hemos instalado Magisk mediante el método de &#8220;_Direct Install_&#8220;) y pulsaremos sobre `Uninstall > Complete uninstall`. En otro caso, bastaría con reiniciar el terminal **para perder el acceso _root_**.
                        
                        <div id="attachment_273" style="width: 183px" class="wp-caption aligncenter">
                          <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/complete_uninstall/" rel="attachment wp-att-273"><img aria-describedby="caption-attachment-273" loading="lazy" class="wp-image-273 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/complete_uninstall-173x300.png" alt="" width="173" height="300" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/complete_uninstall-173x300.png 173w, https://blog.javinator9889.com/wp-content/uploads/2018/11/complete_uninstall.png 335w" sizes="(max-width: 173px) 100vw, 173px" /></a>
                          
                          <p id="caption-attachment-273" class="wp-caption-text">
                            Tras haber habilitado la Google Camera desde ADB, podemos quitar perfectamente el acceso root ya que no será necesario.
                          </p>
                        </div>
                        
                        Dejamos que el proceso termine y se **reinicie el terminal**. Cuando hayamos comprobado que **ya no disponemos de acceso _root_**, apagamos el dispositivo.
                        
                        ## <span style="color: #ff0000;">ATENCIÓN: AHORA VIENEN PASOS CRÍTICOS &#8211; SEGUIRLOS AL PIE DE LA LETRA</span>
                        
                        Con el dispositivo ya apagado, **procederemos a bloquear de nuevo el _bootloader_**. Este proceso, al igual que en el **paso 1**, es muy crítico, ya que un paso en falso producirá **la total pérdida de los datos**.
                        
                        Encendemos el terminal en **modo _fastboot_**, manteniendo pulsadas las teclas de **energía (_E_) **y **bajar volumen (_Vol-_): _E + Vol-_**_, _y lo **conectamos a nuestro equipo**. Abrimos la consola de comandos en la **carpeta _platform tools_** para ejecutar los siguientes comandos. Para abrir rápidamente la consola en la carpeta indicada, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][15] (si se usa Windows):
                        
                        **Comprobamos que se ha detectado el dispositivo:**
                        
                        <pre class="brush: bash; title: ; notranslate" title="">fastboot devices</pre>
                        
                        A continuación, _**escribimos únicamente el siguiente comando**_. Antes de ejecutarlo, en nuestro dispositivo, mantenemos pulsado el botón de _**Vol-**__:_
                        
                        <pre class="brush: bash; title: ; notranslate" title="">fastboot oem lock</pre>
                        
                        Si todo ha ido bien y **hemos realizado el procedimiento correctamente**, el terminal debería iniciarse de nuevo en **modo _fastboot_**. Para terminar con el proceso, reiniciamos el terminal desde la consola:
                        
                        <pre class="brush: bash; title: ; notranslate" title="">fastboot reboot</pre>
                        
                        El terminal **se iniciará correctamente **y ya dispondremos de la _Google Camera_ instalada en nuestro dispositivo con todo su potencial.  Finalmente, podríamos revocar el **acceso a la depuración USB** así como **el desbloqueo de OEM**, para lo cual basta desactivarlo en los lugares indicados en el [**paso 1**][2].
                        
                        Con este modo de instalación, **no perderemos las _OTAs_ y la _GCam_ se podrá seguir usando tras cada actualización**. Si, por cualquier motivo, **no puedes iniciar la _GCam_**, puedes repetir este proceso cuantas veces quieras ya que, en principio, no perderás ningún dato.
                        
                        &nbsp;
                        
                        ##### _ESTE TUTORIAL ESTÁ BASADO EN LOS VÍDEOS QUE APARECEN A CONTINUACIÓN &#8211; ESTÁN EN INGLÉS, PERO EXPLICAN A LA PERFECCIÓN GRÁFICAMENTE TODO EL PROCESO_

 [1]: https://goo.gl/ZP3v58
 [2]: #bootloader_unlock
 [3]: #magisk
 [4]: #gcam_conf
 [5]: #gcam_install
 [6]: #cleaning
 [7]: https://goo.gl/YReSLX
 [8]: https://goo.gl/ydT31u
 [9]: https://goo.gl/kZntL8
 [10]: https://javinator9889.sytes.net/blog/?attachment_id=245
 [11]: https://javinator9889.sytes.net/pfiles/Mi%20A1/Boot%20Images/
 [12]: https://goo.gl/VpLnw7
 [13]: https://goo.gl/PaAsyQ
 [14]: https://t.me/XiaomiA2_ES
 [15]: https://javinator9889.sytes.net/blog/?attachment_id=248
 [16]: https://goo.gl/X2hmqW
 [17]: https://goo.gl/x3P2kh
 [18]: https://goo.gl/wmzcge
 [19]: https://www.celsoazevedo.com/files/android/google-camera/f/GoogleCamera-Pixel2Mod-Arnova8G2-V8.2.apk