---
title: Install GCam (Google Camera) without loosing data (no root) – Xiaomi Mi A1
author: Javinator9889
type: post
date: -001-11-30T00:00:00+00:00
draft: true
url: /?p=340
featured_image: /wp-content/uploads/2018/11/thumbnail-1.png
categories:
  - Sin categoría

---
The Google application known as _Google Camera_ is considered one of the [best photography applications][1] we can use nowadays.

When it was launched, the application was originally available for **all devices** that were, at least, _Android KitKat 4.4_ (or higher), but after some changes on Google&#8217;s policies _Google Camera_ became to be Google&#8217;s _Pixel and_ _Nexus_ exclusively, because of supposed **hardware limitations** that we found nowadays on more devices, one of them: _Xiaomi Mi A1_.

Here we are going to explain **how to install** step-by-step the _Google Camera _app on this device, without **losing data** and **without keeping _root_**.

<!--more-->

* * *

# _Disclaimer_

<p style="text-align: center;">
  <code> This tutorial has been made for educational purposes and does not seek at any time to criticize any brand and/or company. </code>
</p>

<p style="text-align: center;">
  <code> Likewise, everyone is responsible for the treatment they do with their device, not making me or anybody related to the groups &lt;a href="https: //goo.gl/VpLnw7">Xiaomi My A1 - SPANISH &lt;/a> or &lt;a href="https://goo.gl/PaAsyQ"> Xiaomi Mi A1 Development &lt;/a>, or developer(s) of the different applications and/or methods to achieve privileged levels of access to the device and other equipment, or any individual directly or indirectly involved in the processes described herein, responsible for any damage, perjury, loss of warranty, damage, mishap or misconduct It may happen to the device during the performance of the steps described in this tutorial, which have been verified to work in the latest updates received by the terminal (&lt;em>last check: December, 2018&lt;/em>). In case the last update has not been checked yet, it is advisable to wait for certain guarantees of success.</code>
</p>

<p style="text-align: center;">
  <code> Likewise, this &lt;em> post&lt;/em> has been done in good faith, seeking to help the community, and the information may not be all concise that a certain user needs or that said information does not manage to solve or reach the purpose for which it was written. In this case, the aforementioned user is free to access various forums and groups to ask for help, not being necessary to lend it.</code>
</p>

<p style="text-align: center;">
  <code> We strongly recommend, in any case and independently of the level of each reader of this &lt;em> post&lt;/em>, to carry out an intensive and comprehensive reading of the content of this one, to avoid the possible damages mentioned above caused by the lack of a concise understanding of it.</code>
</p>

## Index

  1. [**Unlocking the _bootloader__._**][2]
  2. [**Installing _Magisk Manager_ and obtaining temporary _root_ permissions.**][3]
  3. [**Setting up the device for admitting the _GCam_.**][4]
  4. [**Installing the _Google Camera_.**][5]
  5. [**Removing _root_ and locking the _bootloader_.**][6]

&nbsp;

## 1. Unlocking the _bootloader_. {#bootloader_unlock}

In this step, we are going to **unlock the _bootloader_** without **losing data**: since _May update (2018)_, Xiaomi decided to make the users lost all their data while **locking/unlocking** the _bootloader_.

For achieving that, we are going to `Settings > System > About phone` and click **seven times on** _Build number_, until we get a toast notification saying that the &#8220;_Developer options are enabled_&#8221; (or something similar, like &#8220;_No need, you are a developer_&#8220;). If we have out phone **encrypted with a password** we now put it in order to enable that options.

&nbsp;

<div id="attachment_239" style="width: 586px" class="wp-caption aligncenter">
  <a href="https://javinator9889.sytes.net/blog/?attachment_id=239"><img aria-describedby="caption-attachment-239" loading="lazy" class="wp-image-239 size-large" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/opciones_desarrollador-576x1024.png" alt="" width="576" height="1024" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/opciones_desarrollador.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
  
  <p id="caption-attachment-239" class="wp-caption-text">
    Cómo habilitar las opciones de desarrollador
  </p>
</div>

&nbsp;

Once that the **Developer ****options are** **enabled**, we will have a new option at the same system screen that says: &#8220;**Developer options**&#8220;. We click on it and then, we must enable _**OEM unlocking**_. We put our PIN or password and we click on the **Enable** option.

<div id='gallery-1' class='gallery galleryid-340 gallery-columns-2 gallery-size-large'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/habilitar_desbloqueo_oem/'><img width="576" height="1024" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-576x1024.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-1-242" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/habilitar_desbloqueo_oem.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-1-242'>
      Confirmation dialog for enabling OEM unlock
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/desbloqueo_oem/'><img width="576" height="1024" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-576x1024.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-1-241" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/desbloqueo_oem.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-1-241'>
      Option for enabling OEM unlock
    </dd>
  </dl>
  
  <br style="clear: both" />
</div>

In addition, enabling **USB debugging **is also necessary. For that, at the same _developer options_, we choose to enable **USB debugging**.

<div id="attachment_244" style="width: 586px" class="wp-caption aligncenter">
  <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/depuracion_usb/" rel="attachment wp-att-244"><img aria-describedby="caption-attachment-244" loading="lazy" class="wp-image-244 size-large" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/depuracion_usb-576x1024.png" alt="" width="576" height="1024" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/depuracion_usb.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
  
  <p id="caption-attachment-244" class="wp-caption-text">
    Option for enabling USB debugging
  </p>
</div>

&nbsp;

Now we are ready for **unlocking the _bootloader _** and continue with the pending tutorial:

  * We **turn off** our device normally.
  * We keep pressed the keys of **Power _(P)_** and **volume down**** _(Vol-)_**: _**P + Vol-**_.
  * Then, a screen as in the picture below should appear if we did it correctly: 
    <div id="attachment_245" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/fastboot/" rel="attachment wp-att-245"><img aria-describedby="caption-attachment-245" loading="lazy" class="wp-image-245" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/fastboot-1024x576.jpg" alt="" width="600" height="338" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot-1024x576.jpg 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot-300x169.jpg 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot-768x432.jpg 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot.jpg 1920w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-245" class="wp-caption-text">
        Fastboot mode on Mi A1
      </p>
    </div>
    
    &nbsp;</li> </ul> 
    
    Now, we have to download _platform tools_ on your device (computer with **Windows**, **Mac** o **Linux**). For that, [we access to the official site of _Android Developers_][7] and we choose the version based on your operative system. Once we have accepted the **terms and conditions and completed the download**, we extract the **.zip** file inside a directory. If it was possible, it is **extremly recommended** that this does not contain any _**blank space**__ **or &#8220;strange&#8221; char **(any non-English char, outside from the ASCII 128)_. I will extract the file on the &#8220;_adb_&#8221; folder, at the following location:
    
    `C:\adb`
    
    Once we extracted the files, we must now execute the command prompt at **that location**. On Windows, is as simple as writing &#8220;_cmd_&#8221; on the search bar:
    
    <div id="attachment_248" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/cmd_we/" rel="attachment wp-att-248"><img aria-describedby="caption-attachment-248" loading="lazy" class="wp-image-248" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/cmd_we-1024x695.png" alt="" width="600" height="407" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we-1024x695.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we-300x204.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we-768x521.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/cmd_we.png 1179w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-248" class="wp-caption-text">
        Running command prompt inside a folder in Windows
      </p>
    </div>
    
    &nbsp;
    
    ## <span style="color: #ff0000;">WARNING: NOW THERE ARE CRITICAL STEPS &#8211; FOLLOW THEM TO THE LETTER</span>
    
    <span style="color: #000000;">We proceed to unlock the <em>bootloader</em>. For that, we connect the device in <em>fastboot mode</em> and execute the following commands:</span>
    
    **We check that the device is connected:**
    
    <pre class="brush: bash; title: ; notranslate" title="">fastboot devices</pre>
    
    Now, we _**only write the following** **command**_. Before executing it, we must keep pressed _**Vol-**_ on our device:
    
    <pre class="brush: bash; title: ; notranslate" title="">fastboot oem unlock</pre>
    
    If everything went well and we **keeped pressed _Vol-_**, our device should reboot into _fastboot mode again_ and the command prompt should be:
    
    <div id="attachment_255" style="width: 610px" class="wp-caption aligncenter">
      <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/fastboot_oem_unlock/" rel="attachment wp-att-255"><img aria-describedby="caption-attachment-255" loading="lazy" class="wp-image-255" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/fastboot_oem_unlock-1024x594.png" alt="" width="600" height="348" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock-1024x594.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock-300x174.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock-768x446.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/fastboot_oem_unlock.png 1196w" sizes="(max-width: 600px) 100vw, 600px" /></a>
      
      <p id="caption-attachment-255" class="wp-caption-text">
        Command prompt after executing &#8220;<code>fastboot oem unlock</code>&#8220;
      </p>
    </div>
    
    Once we checked **we effectively are in _fastboot_ mode**, we can stop pressing _Vol-_ and we execute the following command for starting Android:
    
    <pre class="brush: bash; title: ; notranslate" title="">fastboot reboot</pre>
    
    Now you can continue to the **second step**.
    
    &nbsp;
    
    ## 2. **Installing _Magisk Manager_ and obtaining temporary _root_ permissions.** {#magisk}
    
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
    
    <div id='gallery-2' class='gallery galleryid-340 gallery-columns-2 gallery-size-full'>
      <dl class='gallery-item'>
        <dt class='gallery-icon portrait'>
          <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/installing_magisk_manager/'><img width="330" height="564" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk_manager.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-2-261" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk_manager.png 330w, https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk_manager-176x300.png 176w" sizes="(max-width: 330px) 100vw, 330px" /></a>
        </dt>
        
        <dd class='wp-caption-text gallery-caption' id='gallery-2-261'>
          Tras instalar el .apk base de Magisk Manager, tendremos que instalar varias actualizaciones para que pueda funcionar correctamente.
        </dd>
      </dl>
      
      <dl class='gallery-item'>
        <dt class='gallery-icon portrait'>
          <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/installing_magisk/'><img width="339" height="583" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-2-260" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png 339w, https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk-174x300.png 174w" sizes="(max-width: 339px) 100vw, 339px" /></a>
        </dt>
        
        <dd class='wp-caption-text gallery-caption' id='gallery-2-260'>
          Tras instalar Magisk Manager e iniciar el teléfono con el parche del bootloader correspondiente a la versión de Android, podremos instalar Magisk
        </dd>
      </dl>
      
      <br style="clear: both" />
    </div>
    
    Ahora, reiniciamos el teléfono en modo _**fastboot**__,_ apagándolo normalmente y manteniendo pulsados luego los botones de **encendido (_E_) **y **volumen menos (_Vol-_)**: _E + Vol-._
    
    Una vez que hayamos entrado en _fastboot_ (podemos comprobarlo cuando [aparezca una pantalla como ésta][10]), conectamos el dispositivo al equipo y realizamos lo siguiente:
    
      * Descargamos **el último parche** del _bootloader_ modificado. Para ello, lo podemos hacer desde el siguiente enlace: [Xiaomi Mi A1 patched boot images][11]. Si la imagen que necesitas **no está en esa carpeta**, contacta en los diversos grupos de Telegram que existen, donde podrás pedirlo.  
        &#8211;  [Xiaomi Mi A1 &#8211; CASTELLANO][12]  
        &#8211;  [Xiaomi Mi A1 Development][13]
      * Guardamos dicho archivo en **la carpeta de _platform tools_**, que descargamos en el [punto anterior][2] y ejecutamos la consola de comandos en esa misma carpeta. Para ello, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][14] (si se usa Windows).
      * **Comprobamos que se ha detectado el dispositivo:** <pre class="brush: bash; title: ; notranslate" title="">fastboot devices</pre>
    
      * Iniciamos el dispositivo **cargando la nueva imagen** del _bootloader_, sustituyendo `MES` por el mes del que sea el parche _**(jun, jul, sep, etc.)**_: <pre class="brush: bash; title: ; notranslate" title="">fastboot boot patched_boot_MES.img</pre>
    
      * Dejamos que el terminal se inicie normalmente, y cuando lo haya hecho, instalamos **Magisk** desde _Magisk Manager_, seleccionando el método de instalación &#8220;_Direct Install (Recommended)_&#8220;. <div id='gallery-3' class='gallery galleryid-340 gallery-columns-2 gallery-size-full'>
          <dl class='gallery-item'>
            <dt class='gallery-icon portrait'>
              <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/installing_magisk/'><img width="339" height="583" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-3-260" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk.png 339w, https://blog.javinator9889.com/wp-content/uploads/2018/11/installing_magisk-174x300.png 174w" sizes="(max-width: 339px) 100vw, 339px" /></a>
            </dt>
            
            <dd class='wp-caption-text gallery-caption' id='gallery-3-260'>
              Tras instalar Magisk Manager e iniciar el teléfono con el parche del bootloader correspondiente a la versión de Android, podremos instalar Magisk
            </dd>
          </dl>
          
          <dl class='gallery-item'>
            <dt class='gallery-icon portrait'>
              <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/magisk_direct_install/'><img width="353" height="581" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_direct_install.png" class="attachment-full size-full" alt="" loading="lazy" aria-describedby="gallery-3-263" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_direct_install.png 353w, https://blog.javinator9889.com/wp-content/uploads/2018/11/magisk_direct_install-182x300.png 182w" sizes="(max-width: 353px) 100vw, 353px" /></a>
            </dt>
            
            <dd class='wp-caption-text gallery-caption' id='gallery-3-263'>
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
        
          * Una vez que el **teléfono se ha reiniciado,** comprobaremos que en efecto dispone de acceso _root_, para lo que podremos utilizar una aplicación como [_Root Checker_][15]. 
            <div id="attachment_265" style="width: 191px" class="wp-caption aligncenter">
              <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/root_checker/" rel="attachment wp-att-265"><img aria-describedby="caption-attachment-265" loading="lazy" class="wp-image-265 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/root_checker-181x300.png" alt="" width="181" height="300" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/root_checker-181x300.png 181w, https://blog.javinator9889.com/wp-content/uploads/2018/11/root_checker.png 341w" sizes="(max-width: 181px) 100vw, 181px" /></a>
              
              <p id="caption-attachment-265" class="wp-caption-text">
                Cuando el terminal haya reiniciado después de la instalación de Magisk, comprobaremos que tenemos acceso root.
              </p>
            </div></li> </ul> 
            
            Listo, ya tenemos el terminal listo para pasar **al paso 3**.
            
            &nbsp;
            
            ## 3. Configurando el dispositivo para admitir la _GCam_. {#gcam_conf}
            
            Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2]_ _**y obtenido [**acceso _root_**][3] en los apartados anteriores.
            
            Este paso es **fundamental**, ya que vamos a modificar _dos variables internas del dispositivo_ para garantizar que la _Google Camera_ se ejecuta correctamente. Vamos a modificar concretamente **dos campos**: el primero de ellos habilita `HAL3` en el dispositivo, y el segundo `EIS`. Hay que escribir los comandos que aparecen a continuación con sumo cuidado, ya que un paso en falso **podría dejar el dispositivo **inutilizable.
            
            Para ello, conectamos el dispositivo a nuestro equipo y ejecutamos la consola de comandos. Para ello, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][14] (si se usa Windows):
            
              * Solicitamos **acceso al dispositivo**, escribiendo `adb devices` y dando acceso. <pre class="brush: bash; title: ; notranslate" title="">adb devices</pre>
                
                <div id='gallery-4' class='gallery galleryid-340 gallery-columns-1 gallery-size-large'>
                  <dl class='gallery-item'>
                    <dt class='gallery-icon landscape'>
                      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/unauthorized/'><img width="629" height="358" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-1024x583.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-4-266" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-1024x583.png 1024w, https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-300x171.png 300w, https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized-768x437.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/unauthorized.png 1203w" sizes="(max-width: 629px) 100vw, 629px" /></a>
                    </dt>
                    
                    <dd class='wp-caption-text gallery-caption' id='gallery-4-266'>
                      Si intentamos acceder usando &#8220;adb&#8221; a un dispositivo sin los permisos suficientes, el terminal rechazará la conexión.
                    </dd>
                  </dl>
                  
                  <br style="clear: both" />
                  
                  <dl class='gallery-item'>
                    <dt class='gallery-icon portrait'>
                      <a href='https://blog.javinator9889.com/install-gcam-xiaomi-mi-a1/usb_debugging_prompt/'><img width="335" height="565" src="https://blog.javinator9889.com/wp-content/uploads/2018/11/usb_debugging_prompt.png" class="attachment-large size-large" alt="" loading="lazy" aria-describedby="gallery-4-267" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/usb_debugging_prompt.png 335w, https://blog.javinator9889.com/wp-content/uploads/2018/11/usb_debugging_prompt-178x300.png 178w" sizes="(max-width: 335px) 100vw, 335px" /></a>
                    </dt>
                    
                    <dd class='wp-caption-text gallery-caption' id='gallery-4-267'>
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
                        
                        Para ello, accedemos a [este enlace][16] y descargamos **la versión recomendada que aparezca**. Por lo general, es recomendable utilizar las [versiones de Arnova8G2][17], pero podéis utilizar la que queráis.
                        
                        En este caso, vamos a usar [**<span class="redb">Arnova&#8217;s v8.2:</span> GoogleCamera-Pixel2Mod-Arnova8G2-V8.2.apk (Arnova8G2, 2018-08-13)**][18]. Instalaremos la aplicación y ya podremos usar _Google Camera_.
                        
                        <div id="attachment_272" style="width: 586px" class="wp-caption aligncenter">
                          <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/gcam_inside/" rel="attachment wp-att-272"><img aria-describedby="caption-attachment-272" loading="lazy" class="wp-image-272 size-large" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/gcam_inside-576x1024.png" alt="" width="576" height="1024" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside-576x1024.png 576w, https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside-169x300.png 169w, https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside-768x1365.png 768w, https://blog.javinator9889.com/wp-content/uploads/2018/11/gcam_inside.png 1080w" sizes="(max-width: 576px) 100vw, 576px" /></a>
                          
                          <p id="caption-attachment-272" class="wp-caption-text">
                            Una vez hayamos completado todos los pasos, podremos usar la Google Camera como si tuviéramos un teléfono Píxel.
                          </p>
                        </div>
                        
                        &nbsp;
                        
                        ## 5. **Eliminando _root_ y bloqueando el _bootloader_.** {#cleaning}
                        
                        Si estás en este paso, se supone que ya **[has desbloqueado el _bootloader_][2] **u obtenido [**acceso _root_**][3].
                        
                        Ahora que ya hemos conseguido al _Google Camera_ funcionando perfectamente, podremos **cerrar el bootloader** y **revocar el acceso _root_**. Para ello, nos dirigiremos a _Magisk Manager_ y pulsaremos sobre `Uninstall > Complete uninstall`.
                        
                        <div id="attachment_273" style="width: 183px" class="wp-caption aligncenter">
                          <a href="https://javinator9889.sytes.net/blog/install-gcam-xiaomi-mi-a1/complete_uninstall/" rel="attachment wp-att-273"><img aria-describedby="caption-attachment-273" loading="lazy" class="wp-image-273 size-medium" src="https://javinator9889.sytes.net/blog/wp-content/uploads/2018/11/complete_uninstall-173x300.png" alt="" width="173" height="300" srcset="https://blog.javinator9889.com/wp-content/uploads/2018/11/complete_uninstall-173x300.png 173w, https://blog.javinator9889.com/wp-content/uploads/2018/11/complete_uninstall.png 335w" sizes="(max-width: 173px) 100vw, 173px" /></a>
                          
                          <p id="caption-attachment-273" class="wp-caption-text">
                            Tras haber habilitado la Google Camera desde ADB, podemos quitar perfectamente el acceso root ya que no será necesario.
                          </p>
                        </div>
                        
                        Dejamos que el proceso termine y se **reinicie el terminal**. Cuando hayamos comprobado que **ya no disponemos de acceso _root_**, apagamos el dispositivo.
                        
                        ## <span style="color: #ff0000;">ATENCIÓN: AHORA VIENEN PASOS CRÍTICOS &#8211; SEGUIRLOS AL PIE DE LA LETRA</span>
                        
                        Con el dispositivo ya apagado, **procederemos a bloquear de nuevo el _bootloader_**. Este proceso, al igual que en el **paso 1**, es muy crítico, ya que un paso en falso producirá **la total pérdida de los datos**.
                        
                        Encendemos el terminal en **modo _fastboot_**, manteniendo pulsadas las teclas de **energía (_E_) **y **bajar volumen (_Vol-_): _E + Vol-_**_, _y lo **conectamos a nuestro equipo**. Abrimos la consola de comandos en la **carpeta _platform tools_** para ejecutar los siguientes comandos. Para abrir rápidamente la consola en la carpeta indicada, basta con escribir _&#8220;cmd_&#8221; directamente en la [barra de navegación del explorador de Windows][14] (si se usa Windows):
                        
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
 [14]: https://javinator9889.sytes.net/blog/?attachment_id=248
 [15]: https://goo.gl/X2hmqW
 [16]: https://goo.gl/x3P2kh
 [17]: https://goo.gl/wmzcge
 [18]: https://www.celsoazevedo.com/files/android/google-camera/f/GoogleCamera-Pixel2Mod-Arnova8G2-V8.2.apk