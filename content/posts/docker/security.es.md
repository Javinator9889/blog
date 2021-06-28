---
title: '5. Análisis de seguridad en Docker'
author: Javinator9889
date: 2021-06-28T16:55:00+02:00
series: ["Docker"]
cover:
  image: images/cover.png
categories:
  - Docker
url: "docker/security"
tags:
  - docker
  - linux
  - contenedores
  - docker-compose
  - orchestration
  - kubernetes
  - swarm
  - security
  - qué es
draft: true
---

> Esta entrada es parte de un conjunto de entradas extraídas directamente
del artículo ya escrito que versa sobre este tema, el cual es completamente
accesible y se puede leer en la siguiente dirección:

Seguridad en Docker {#sec:security}
===================

A lo largo de todo el documento se ha visto cómo la tecnología de
contenedores ha enfocado gran parte de su esfuerzo en la seguridad:
desde el diseño inicial hasta la implementación final las
características de seguridad de los contenedores han supuesto un punto
de inflexión en estas tecnologías.

La cuestión es: ¿cuánto de seguros son? En común todas las tecnologías
tienen un "fallo" de base: requieren de permisos de administrador para
ejecutarse. Eso o bien el usuario que gestiona los contenedores
pertenece a un grupo privilegiado, que sería equivalente a ejecutar
"todos" los comandos como administrador.

En esta sección se va a tratar por una parte la seguridad en Docker
desde el punto de vista de más bajo nivel, como es la comunicación con
el kernel; hasta aspectos más "elevados" como son diferencias con otras
soluciones como `chroot`, cómo afecta el *firewall* a la seguridad de
los contenedores y cómo de seguras son las comunicaciones entre
contenedores.

Análisis de la pila Docker
--------------------------

Anteriormente, en la imagen
[16](#fig:docker-interface){reference-type="ref"
reference="fig:docker-interface"} se muestra cómo el motor Docker
interactúa con el kernel de Linux para proveer aislamiento. Entre otras
librerías, Docker usa en particular los *cgroups* [@Cgroups2021] y los
*namespaces* de Linux [@LinuxNamespaces2021].

Sendas funcionalidades del kernel ofrecen una gran capa de seguridad y
aislamiento de procesos de forma nativa en todas las máquinas Linux, y
Docker aprovecha esa infraestructura para proteger los contenedores a un
nivel muy bajo: a nivel de kernel.

Este planteamiento ya augura un buen presagio en tanto que no se usan
aplicaciones externas o librerías de terceros para el aislamiento y
protección de capas sino que se usa una arquitectura a bajo nivel
ampliamente depurada y probada como es el kernel de Linux. Además, esto
permite también una gran portabilidad, ya que el "único requisito" para
ejecutar Docker sería contar con un kernel de Linux.

A la hora de hablar o revisar la seguridad de Docker, existen cuatro
áreas primordiales en las que indagar [@DockerSecurity2021]:

-   La seguridad intrínseca del kernel así como su soporte para
    *namespaces* y *cgroups*.

-   La superficie de ataque sobre el servicio de Docker en sí.

-   Lagunas en las configuraciones de un contenedor o bien por defecto o
    bien introducidas por el usuario.

-   Las características de seguridad del kernel y su interacción con
    Docker.

### Linux kernel *namespaces* {#linux-kernel-namespaces .unnumbered}

A nivel de funcionamiento, Docker es similar a los contenedores LXC y
comparten los mismos mecanismos de seguridad. Por ende, cuando se crea
un contenedor con el comando `docker run` internamente se están creando
un conjunto de *namespaces* y *cgroups* para el contenedor.

El primero ofrece la primera y mayor forma de aislamiento -- un proceso
que se ejecuta dentro de un *namespace* es incapaz de ver (y mucho menos
afectar) a otros procesos en ejecución en otro contenedor o en la
máquina anfitriona.

Esto llega al nivel de que cada contenedor tiene su propia pila de
protocolos de red, lo cual implica que un contenedor nunca tendrá acceso
privilegiado a *sockets* o interfaces de otro contenedor o del sistema
anfitrión. Sin embargo, si se configura correctamente un sistema
anfitrión las comunicaciones entre contenedores pueden existir
perfectamente, a través de la misma interfaz de red. Si por el contrario
se expone el puerto del contenedor entonces otros equipos podrán
enviarle mensajes o *pings* al contenedor, paquetes TCP/UDP y establecer
distintos tipos de conexiones. Sin embargo, se pueden restringir si es
necesario: a fin de cuentas, la interfaz por defecto que usan los
contenedores es la tipo puente, que implica que en apariencia son
equipos conectados a un *switch*.

Por otra parte, los *namespaces* de Linux tienen la ventaja de que son
prestaciones probadas y testeadas a lo largo del tiempo, introducidas en
el año 2008 en la versión `2.6.15`. Además, su diseño y arquitectura se
basa en un intento de mejora sustancial de OpenVZ [@OpenVZ2021],
desarrollado en 2005.

En un estudio realizado en el año 2018
[@sunSecurityNamespaceMaking2018], se detectaron ciertos problemas
residentes en el kernel que impedían a los contenedores hacer uso de
características avanzadas de seguridad del kernel: no se pueden aplicar
políticas para comprobar la integridad, regular la ejecución de código,
control de acceso, etc. que permiten prevenir problemas de seguridad
referentes a la aplicación. Ante el intento de añadir nuevas opciones al
kernel que permitan el acceso a dichos recursos, se descartaron debido a
ser solución *ad-hoc* que suponían muchas veces una brecha de seguridad
más allá de una opción real.

Sin embargo, en dicho estudio se proponen los *security namespaces*, una
característica del kernel que permitiría la ejecución de contenedores
con la totalidad de las prestaciones disponibles produciendo una
latencia menor al $0.7\%$ en las llamadas al sistema.

Esta característica ha seguido evolucionando hasta nuestros días en la
forma de los *user namespaces*, que son los usados e implementados
actualmente por Docker. Un problema común del usuario `root` en Linux no
es que sea necesariamente el administrador sino las posibilidades que
tiene (en particular, las Linux kernel *capabilites*
[@CapabilitiesLinuxManual]): estas capacidades se pueden otorgar o bien
mediante un escalador de privilegios (por ejemplo, usar el comando
`sudo`) o mediante el ajuste de permisos, como el `SUID` o un cambio de
*namespace*. Esto se aprovecha por el motor Docker para definir qué
posibilidades tiene un contenedor, que pueden ser añadidas o
restringidas por el usuario.

El problema es cuando un usuario define un contenedor que requiere de
más capacidades de las que él mismo tiene. Por defecto, los contenedores
se ejecutan siempre como `root`, por lo que la situación anterior es
perfectamente posible, y conlleva posibles abusos en forma de fallo de
seguridad.

Con el uso de los *user namespaces* este problema se puede abordar
fácilmente: un *namespace* es a fin de cuentas un "mapa" en donde un UID
y GID virtuales se mapean con los UID/GID reales y se exponen en la ruta
`/proc` [@blogEvolvingContainerSecurity2021]. El mapeo presenta la
siguiente forma (figura [27](#fig:ns-mapping){reference-type="ref"
reference="fig:ns-mapping"}):

![Mapeo de los UID del *namespace* del contenedor al *namespace* del
sistema
[@blogEvolvingContainerSecurity2021].[]{label="fig:ns-mapping"}](pictures/ns_mapping.png){#fig:ns-mapping
width="\linewidth"}

¿Por qué es potente esta característica del sistema?:

-   Permite, por una parte, definir ciertos UIDs únicamente dentro del
    contenedor. De esta forma, si un UID no está relacionado con un UID
    real del equipo anfitrión, al intentar examinar un fichero con dicho
    UID aparecerá un error del tipo `overflowuid` en los ficheros de
    `/proc` [@DocumentationProcSys].

-   Desde el punto de vista de un *namespace* de usuario el contenedor
    se ejecuta con UID $0$ cuando en realidad está usando un rango de
    valores mapeados en dicho *namespace*.

-   Los subsistemas Linux pueden ejecutar la función "`ns_capable`" (que
    permite definir si una tarea tiene en realidad mayores capacidades)
    usando un *namespace* específico de un recurso. De esta forma, los
    procesos pueden realizar acciones "privilegiadas" sin tener en
    realidad privilegios sobre el sistema anfitrión.

En la actualidad, el servicio Docker inicia los contenedores siempre con
las capacidades mínimas posibles [@DockerSecurity2021]: por ejemplo,
servidores web que únicamente necesitan exponer un puerto protegido
($< 1024$) se le garantiza el permiso `net_bind_service` en lugar de
ejecutarse como administrador.

Esto permite que diversos procesos que siempre se ejecutan como
administrador (SSH, cron, módulos del kernel, ...) usen un usuario con
menos privilegios y se les garantice únicamente acceso a las
características que necesitan. Algunas operaciones además son
directamente gestionadas por Docker en lugar de por las aplicaciones que
se ejecutan:

-   El acceso mediante SSH se realiza mediante un único servidor
    gestionado por Docker.

-   Los procesos `cron` se ejecutan como usuario estándar, cuando es
    posible.

-   La gestión de *logs* se delega a Docker u otro servicio.

-   La gestión del *hardware* es irrelevante, lo que se traduce en que
    instrucciones como `udevd` nunca serán necesarias.

-   La gestión de las redes sucede fuera de los contenedores, lo cual
    implica que un contenedor nunca tendrá que ejecutar tareas con
    `ifconfig`, `route` o `ip`.

La implicación directa es que los contenedores no necesitan permisos de
administrador reales (al menos, no todos) y se restringen las
posibilidades del mismo. Por ende, se pueden aplicar algunas medidas de
seguridad que impliquen denegar todas las operaciones de montaje,
impedir el acceso a sockets, prohibir ciertas operaciones sobre discos
(particionado, cambiar permisos, etc.), denegar la carga de módulos del
kernel y demás.

Así, si un intruso es capaz de acceder a un contenedor y escalar
privilegios hasta ser `root`, el daño que podrá hacer sobre el sistema
estará limitado. Pero esto siempre ha de ir acompañado de una gestión
competente: cuando se crea un contenedor, lo ideal sería quitar todas
aquellas capacidades del contenedor que no sean necesarias o no se vayan
a usar.

### Linux *control groups* {#linux-control-groups .unnumbered}

Los grupos de control de Linux no son necesariamente una característica
de seguridad sino de control y regulación de acceso a los recursos. En
el estudio mencionado anteriormente ([@sunSecurityNamespaceMaking2018])
uno de los problemas que se vieron en comparación con las máquinas
virtuales era la restricción del acceso a los recursos y la limitación
de ciertas acciones.

Durante bastante tiempo los contenedores Docker no contaban con una
limitación en la cantidad de recursos disponibles hasta que se adaptó el
motor de ejecución para trabajar con los *cgroups*, que existen en Linux
desde el 2006 (versión `2.6.24` [@DockerSecurity2021]).

Esta característica se incluye en el apartado de seguridad porque
permite proteger a un contenedor de ataques de denegación de servicio,
"molestar" a otro contenedor, etc.

### Ataque al servicio de Docker {#ataque-al-servicio-de-docker .unnumbered}

La ejecución de contenedores implica el uso del servicio de Docker para
ello. Si no se ha optado por el modo "sin privilegios", dicho servicio
se ejecutará siempre como `root`, por lo que será uno de los elementos
más atacados y vulnerables que existan.

En general, sobre el servicio Docker no se pueden tomar muchas acciones
en lo referente a privilegios o código fuente pero sí se pueden aplicar
ciertas restricciones sobre el uso. Lo primero es restringir qué
usuarios pueden interactuar con el servicio de Docker, ya que es una
implicación directa de seguridad. En Docker, se puede hacer *bind
mounts* del directorio raíz del sistema (`/`) dentro de un directorio
`/host` en el contenedor. Desde allí, se puede acceder a cualquier
fichero, directorio o dispositivo sin restricciones ni limitaciones.

Es por este motivo por el que Docker CLI utiliza una API REST contra un
socket UNIX en lugar de usar la dirección `127.0.0.1`, ya que permite
ajustar los permisos del socket usando el sistema de permisos de Linux.
Bajo esta premisa, si se decidiese crear un contenedor que expusiera una
API REST bajo HTTP habría que dedicar especial atención a qué ficheros
se puede acceder y controlar todavía más los parámetros que se reciben.
Inclusive aunque se restrinja el acceso a la API únicamente a la red
local mediante el uso de *firewalls*, otros contenedores podrían
comprometer el sistema. Por ello, es obligatorio proteger los
*endpoints* usando HTTPS y certificados digitales, y altamente
recomendable que solo sea accesible a través de una VPN.

Por otra parte, el servicio Docker es potencialmente vulnerable a otras
entradas como la carga de una imagen desde el disco con `docker load` o
desde la red con `docker pull`. Por ello, el primer paso desde la
versión `1.10.0` de Docker es la de crear una jaula `chroot` en donde
desempaquetar la imagen y preparar el entorno. Para evitar estos
problemas se puede configurar el servidor Docker para que únicamente
trabaje con imágenes firmadas -- DCT (*Docker Content Trust*).

Esta característica es nativa al servicio de Docker y se puede usar
directamente desde Docker CLI. Mediante esta herramienta, un usuario que
publique una imagen podrá firmarla y darle la seguridad a los clientes
de que se está usando una imagen oficial. Las claves de firma se
disgregan en tres tipos de claves:

-   Claves offline, para la firma inicial de la imagen asociada a un
    usuario.

-   Clave de etiquetado (*tag key*), asociada a un repositorio de
    imágenes.

-   Clave de tiempo (*timestamp key*), asociada a un repositorio y
    creada por Docker.

Todas las claves se generan a raíz de la clave offline, también conocida
como "*root key*" (figura [28](#fig:keys){reference-type="ref"
reference="fig:keys"}):

![Distribución de las claves para la firma de imágenes en Docker
[@ContentTrustDocker2021].[]{label="fig:keys"}](pictures/trust_components.png){#fig:keys
width="\linewidth"}

### Mayor protección de Docker {#mayor-protección-de-docker .unnumbered}

Una de las características fundamentales de que se ejecute sobre el
kernel de Linux es que Docker está directamente integrado con otras
herramientas de seguridad.

Aunque el motor Docker deshabilite ciertas posibilidades sobre los
contenedores esto no implica que otros sistemas no se puedan usar en
conjunto. Por ejemplo:

-   Se puede ejecutar un kernel con GRSEC [@Grsecurity] y PAX [@PaX2019]
    para añadir opciones de seguridad tanto en la compilación como en
    tiempo de ejecución. Por otra parte, mediante el uso de técnicas de
    seguridad como la aleatorización de direcciones se mitigan muchas
    vulnerabilidades del sistema. Lo interesante es que no es necesaria
    ninguna interacción por parte de Docker ya que son características
    que se aplican a lo largo de todo el sistema.

-   Si la aplicación viene con un modelo de seguridad que use AppArmor o
    SELinux se puede integrar directamente dentro de Docker, sin
    necesidad de hacer ningún cambio. Esto otorgará una capa extra de
    seguridad que se complementa con la restricción de las capacidades
    del contenedor.

En principio, cualquier herramienta externa se podría usar dentro de un
contenedor Docker para proteger el acceso y añadir más capas de
seguridad. Esto se hace principalmente sobre sistemas de ficheros en red
o compartidos con otros contenedores, donde la seguridad es crítica.

Diferencias fundamentales con `chroot`
--------------------------------------

Desde las primeras versiones de Linux, el concepto de "enjaular" ya
existía. Crear un `chroot` se traduce en que una aplicación se ejecuta
sobre un directorio definido como si dicho directorio fuese la raíz. Por
ejemplo, se crea un `chroot` en la ruta `/home/user/jail`. Cualquier
proceso que se ejecute dentro de dicha ruta pensará que se está
ejecutando sobre la raíz `/`, y no tendrá acceso al sistema de ficheros
que haya por encima.

Esta característica fue uno de los primeros pasos en la creación y
configuración de *sandboxes*, y además añadía cierta portabilidad porque
siempre se podía comprimir dicho directorio, llevarlo a otro equipo y
trabajar sobre sus contenidos directamente. Además, como en ese
directorio el árbol UNIX no se respeta del todo, es posible aislar un
proceso del resto excluyendo el directorio `/proc` o `/run` de la jaula.

¿Qué diferencias existen con Docker? A lo largo de todo el documento, ya
se tiene una idea muy clara de qué permite Docker. Principalmente,
Docker presenta un mecanismo de aislamiento mucho más sofisticado. En
una jaula es necesario renunciar a ciertos permisos o características
para poder trabajar con seguridad. A veces es posible que no sea
sencillo ejecutar un proceso o aplicación en una jaula y la
configuración que se diseñe podría dañar directamente al sistema, ya que
una jaula siempre se ejecuta como administrador. Por su parte, el
aislamiento con Docker se consigue mediante los *namespaces* de Linux.

Por otra parte, en Docker los procesos tiene su propia tarjeta de red,
su propio identificador (*hostname*), memoria dedicada, limitación de
recursos, ... Es decir, es una solución mucho más sofisticada.

Docker se compara más a una máquina virtual ya que permite usar un
sistema distinto al que está instalado, mientras que en una jaula se
comparte todo del sistema anfitrión. Por ende, la característica
principal que diferencia una solución de otra es la capacidad de aislar
procesos, recursos, memoria y red.

Seguridad en las comunicaciones de red -- *firewall*
----------------------------------------------------

Internamente, Docker utiliza un *firewall* para aislar las
comunicaciones de red. En particular, el *firewall* empleado es
`iptables` [@DockerIptables2021]. Esta herramienta está directamente
embebida dentro del kernel de Linux, lo cual asegura una gran
compatibilidad universal y un gran rendimiento, ya que trabaja
directamente sobre el *hardware* cuando es posible.

Cuando se configura un contenedor o una red, el servicio de Docker
inserta las reglas necesarias en las tablas de `iptables`. Esto se
realiza sobre el sistema, por lo que es posible que exista conflicto con
reglas que puedan existir ya.

Sin embargo, esto abre nuevas opciones: configurar tus propias reglas
para restringir el acceso a ciertos contenedores. Docker tiene su propio
conjunto de reglas (`DOCKER`) y luego tiene un grupo de reglas
destinadas al usuario (`DOCKER-USER`). En este último un administrador
puede definir qué reglas quiere aplicar a los contenedores.

La versatilidad de esto permite, por una parte, definir que las
conexiones al servicio de Docker solo se realicen desde una red interna:

``` {style="bash" caption="Restricción de las conexiones a Docker según un rango de IPs \autocite{DockerIptables2021}."}
sudo iptables -I DOCKER-USER -m iprange -i <external-interface> ! --src-range 192.168.1.1-192.168.1.3 -j DROP
```

Si, por otra parte, Docker actúa como si fuese un router, se pueden
permitir ciertas conexiones desde una interfaz hasta otra:

``` {style="bash" caption=""}
sudo iptables -I DOCKER-USER -i <source-interface> -o <destination-interface> -j ACCEPT
```

Una característica interesante es que se puede combinar con otros
sistemas de *firewall* como `firewalld` y, en un futuro, se plantea
adoptar `nftables` como nuevo gestor de peticiones de red (es el
sustituto de `iptables` en las nuevas versiones de Linux).

Conclusiones
------------

Los contenedores, en apariencia, son muy seguros. Si se toman las
medidas pertinentes y se ejecutan los procesos como un usuario sin
privilegios, es muy complejo que pueda haber un fallo de seguridad
usando esta tecnología.

Si además se combina lo anterior con una capa extra de seguridad como
puede ser AppArmor, SELinux, GRSEC y reglas de *firewall* que gestionen
las comunicaciones, se tiene una solución estanca en donde desplegar
cómodamente las aplicaciones, de una forma fácil, sencilla y funcional.

En diversos estudios se ha visto cómo Docker ofrece una capa de
seguridad muy densa tanto por encima de las aplicaciones como por
debajo, a nivel de kernel. Sin embargo, se han detectado varios fallos
de seguridad en lo referente a las interfaces que pueden ser
aprovechados para hacer ARP *spoofing* y MAC *flooding*. Esto se debe a
que principalmente no añade ningún tipo de filtro al tráfico de red que
circula por la interfaz [@buiAnalysisDockerSecurity2015]. Sin embargo,
esto se puede subsanar añadiendo reglas de *firewall* que regulen y
filtren los paquetes que circulan por la interfaz.

Otro problema podría surgir de ejecutar los contenedores en modo
privilegiado, lo cual implica que es casi como si se estuviera
ejecutando en la máquina anfitriona con privilegios `root`. Aunque hay
que tener en cuenta que esta característica casi nunca se usa debido a
sus implicaciones de seguridad y a que la gran mayoría de contenedores
no requieren de esta opción para funcionar.

Se ve que efectivamente el aislamiento que ofrece Docker es muy eficaz
y, combinado con unas buenas prácticas, explica la gran evolución y
crecimiento de este tipo de tecnologías durante los últimos años. Eso
combinado con la gran velocidad en el desarrollo y en la ejecución que
presenta lo ha convertido en la "opción ganadora" que se ha mantenido al
alza durante los últimos 4 años.
