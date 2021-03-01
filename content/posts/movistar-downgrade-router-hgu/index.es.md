---
title: 'Tutorial: Downgrade router HGU Askey y Mitrastar de Movistar ⇒ versión N43'
author: Javinator9889
date: 2019-09-02T15:30:43+00:00
excerpt: ¿Alguna vez te has encontrado ante una versión de un firmware que no funciona del todo bien? Pues este es el caso que ha ocurrido con las últimas actualizaciones de los router de Movistar, y aquí vamos a aprender a cómo volver a una versión anterior mediante el proceso de "downgrade".
url: /movistar-downgrade-router-hgu/
cover: 
  image: images/hgu.jpg
categories:
  - Tutoriales
tags:
  - askey
  - bin
  - downgrade
  - hgu
  - mitrastar
  - movistar
  - router
  - tutorial

---
¿Cuántos nos hemos encontrado ante la situación de que una mala actualización provoca un fallo en cadena de nuestro sistema? ¿Hay tantas funciones nuevas que lo que se ha conseguido es que todo vaya especialmente lento? ¿O sencillamente se ha actualizado solo y lo que en verdad quieres es que se mantenga en una versión de forma estable?

Eso hemos venido a solucionar hoy: **cómo hacer _downgrade_ al router HGU de Movistar**, tanto _Askey_ como _Mitrastar_, manualmente y, de paso, ofrecer soluciones y alternativas para que estos problemas no vuelvan a ocurrir.

<!--more-->

### _Disclaimer_

```text
Ante ninguna situación nos hacemos responsables de cualquier perjuicio que pueda 
suceder a raíz de seguir los pasos explicados en este procedimiento. Si bien el 
mismo es seguro, se tratarán temas de borrado de la información de la ROM y 
similares que, ante una caída de tensión o bien un problema eléctrico, pueden 
acarrear el no funcionamiento e inclusive el reemplazo del producto.

Si continua leyendo usted se convierte en el único responsable de cualquier 
daño que pueda ser ocasionado, no viéndose este sitio ni su autor ni nada 
relacionado con el mismo involucrado y/o relacionado con lo ocurrido.
Se asume en todo momento que el usuario sabe acceder a la configuración del 
router y manejar las opciones básicas del mismo.
```

### 1. Acceso al router

Para realizar este procedimiento, será fundamental poder acceder a nuestro router y configurarlo. Por una parte, dispondremos de acceso vía web usando la **dirección IP por defecto** de la puerta de enlace. En la mayoría de las ocasiones, para Movistar es:

```192.168.1.1```

Si por un casual no fuera esa, dependiendo de vuestros sistemas operativos podréis averiguarlo de una forma u otra:

  * Sistemas basados en Linux:
    ```bash
    ip route show | grep default
    ```

  * Windows:
    ```cmd
    ipconfig
    ```

Una vez obtenidos estos datos, tendremos que introducir la contraseña de acceso a la configuración. Si **no ha cambiado**, la podréis encontrar en la parte inferior del router:

{{< lazyimage src="images/screenshot.2.jpg" caption="Contraseña de configuración del router" >}}

### 2. Copia de seguridad de los ajustes

Si bien este método es bastante seguro, hacer una **copia de seguridad** de los ajustes nunca está de más por si quisiéramos restaurarla en un futuro, al volver a la nueva versión.

Para ello, accedemos a:

> Menú > Otras funcionalidades > Crear / recuperar un perfil

Desde allí, escogeremos la opción de &#8220;**Guardar configuración en archivo**&#8221; y descargaremos el fichero en nuestro equipo.

{{< lazyimage src="images/download-settings.png" caption="Captura de la sección de descarga" >}}

Si esta opción por un casual no sirviera, podríamos realizar el mismo procedimiento accediendo a los ajustes avanzados:

{{< lazyimage src="images/advanced-backup.png" caption="Copia de seguridad desde los ajustes avanzados" >}}

Es muy importante **conservar esta copia de seguridad** dado que nos permitirá restaurar una _versión posterior_ del _firmware_ del router.

> Restaurar una **copia de seguridad** de una versión anterior en una **nueva versión** no tiene asegurado el correcto funcionamiento, ni tampoco a la inversa. Esto es debido a que no tienen por qué ser **actualizaciones acumulativas** y, por tanto, hay opciones que pueden cambiar e incluso desaparecer.

### 3. Descargando el _firmware_ para nuestro dispositivo

Antes de proseguir, es **fundamental** identificar correctamente nuestro dispositivo para verificar si es compatible con el _downgrade_ que queremos hacer. Actualmente, se ofrecen los últimos _**firmware**_ **estables** (versión _N43_ ampliamente probada y verificada) para los siguientes modelos de router:

  1. _**Mitrastar GPT-2541 GNAC.**_
  2. _**Askey RTF3505VW.**_

Para poder saber qué modelo tenemos:

> Menú > Ayuda > Acerca de&#8230;

{{< lazyimage src="images/version.png" caption="Modelo del router desde la web" >}}

Una vez conocido el modelo del router, procedemos a descargar el _firmware_:

  * **Router _Askey_**: <https://s.javinator9889.com/GKAKBn>  
    __Hash (SHA-256):__ `eda948c3dca577c73c7f64fb237a0ed4edb075a1d96865425aae8ea467c6e4cf`
    
    &nbsp;
    
  * **Router _Mitrastar_**: <https://s.javinator9889.com/hC8nPd>  
    __Hash (SHA-256):__ `459fde5ed68746d653f425dc2157e08c7453540a9acfe63a210812673361f18d`
    
### 4. _Downgrade_ del _firmware_

Una vez hayamos obtenido los archivos **.bin**, ya estaremos listos para poder hacer el _downgrade_ de nuestro equipo. Para ello, iremos a:

> Menú > Actualizaciones Firmware > Actualizaciones Firmware desde tu PC

Allí, podremos elegir el archivo que acabamos de descargar e iniciar así **el proceso de actualización**, que en este caso será un _downgrade_.

{{< lazyimage src="images/update-screen.png" caption="Actualización del *firmware* desde el PC" >}}

Si este menú **no se encontrara disponible**, tenemos la misma opción en los _Ajustes avanzados_:

{{< lazyimage src="images/advanced-update.png" caption="Actualización desde los ajustes avanzados" >}}

Una vez le demos a **Actualizar**, veremos una barra de progreso (por lo general) y podremos observar cómo _las luces del router parpadean_. En este instante, es **muy recomendable** desconectar el **cable de fibra óptica**, ya que es posible que queden residuos de la versión anterior que provoquen que el sistema **no se inicie correctamente**.

Una vez haya finalizado, podremos ver desde la pantalla de &#8220;**Más información**&#8221; la nueva versión del _firmware_ que tiene el router.

### 5. Recuperando los ajustes

Hay veces que el instalar el _firmware_ antiguo no conlleva una pérdida de configuraciones, pero es una situación **muy proclive** que puede suceder.

Si al igual que hicimos en el **paso 2** tienes una copia de seguridad de los ajustes anteriores, ahora puede ser un buen momento para recuperarla. El proceso es muy sencillo; vamos a:

> Menú > Otras funcionalidades > Crear / recuperar un perfil

pero esta vez no generaremos una nueva copia de seguridad sino que seleccionaremos la opción de &#8220;**Cargar configuración desde un archivo**&#8220;.

{{< lazyimage src="images/restore-from-file.png" caption="Captura de la sección de carga/descarga" >}}

Al igual que siempre, todo esto lo podremos hacer desde la **configuración avanzada**:

{{< lazyimage src="images/advanced-restore.png" caption="Actualización de las configuraciones desde la sección avanzada" >}}

### 6. Deshabilitando las actualizaciones

Si ahora no queremos que **nuestro dispositivo se actualice automáticamente**, es una buena práctica deshabilitar el acceso remoto por parte de Movistar para evitarlo. En esta ocasión, será necesario hacerlo desde los **Ajustes avanzados**, donde habremos de seguir:

> Menú > Configuración avanzada > Aceptar > Management > TR-069 Client

y deshabilitamos todas las opciones.

{{< lazyimage src="images/tr069.png" caption="Deshabilitando las opciones del cliente TR-069" >}}

Si quisiéramos una **capa extra de seguridad**, podríamos ir a la configuración del _firewall_ del router y bloquear el acceso al puerto _7547_.

### 7. Actualizando el _firmware_

¡OH, MARAVILLOSO, HAN SACADO UNA NUEVA ACTUALIZACIÓN QUE FUNCIONA! y ahora quieres actualizar.

Pues bien, este proceso en principio más sencillo puede resultar algo complejo, debido a las nuevas reestricciones que hemos puesto en el equipo. Como siempre, lo primero que haremos será una **copia de seguridad** y luego valoraremos qué dos opciones queremos usar:

  1. Habilitar de nuevo el cliente _TR-069_ y reiniciar el router, esperando recibir la actualización.
  2. Forzarla usando el botón de _reset_.

En la primera de ellas no tenemos garantías de que vaya a funcionar, ya que no tiene por qué actualizarse el equipo. Sin embargo, con la segunda opción estamos asegurando que se reciba la nueva versión del _firmware_, a costa de perder nuestras configuraciones.

Para poder forzar la actualización, debemos **mantener pulsado el botón de _reset_** del router durante unos **10 segundos** y soltar. Al reiniciarse el equipo, se conectará a los _servidores de Movistar_ y descargaría la nueva versión. Si esto no funciona, entonces tocará esperar a que llegue automáticamente al equipo. Una vez actualizado el mismo, podríamos intentar recuperar una **configuración antigua** del dispositivo pero, como dijimos en el _disclaimer_, no está asegurado que funcione.

### 8. Conclusiones

Llegados a este punto, solo nos queda disfrutar de una versión **estable y rápida** del equipo. Esperemos que haya sido útil y si lo fue, agradecemos enormemente que lo compartieras para ayudar a más gente.

* * *

_Este artículo está basado en la siguiente entrada de blog: <https://www.forocoches.com/foro/showthread.php?t=6803861>_