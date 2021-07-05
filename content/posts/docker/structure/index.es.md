---
title: '2. Estructura de Docker: contenedores y comunicaciones'
author: Javinator9889
date: 2021-06-28T16:55:00+02:00
series: ["Docker"]
cover:
  image: images/cover.png
categories:
  - Docker
url: "docker/structure"
tags:
  - docker
  - linux
  - contenedores
  - structure
  - qué es
draft: true
---

> Esta entrada es parte de un conjunto de entradas extraídas directamente
del artículo ya escrito que versa sobre este tema, el cual es completamente
accesible y se puede leer en la siguiente dirección:

Docker
======

Ahora que ya se han introducido los contenedores, las tecnologías de
virtualización y tendencias de uso, se va a explicar cómo funciona
Docker en profundidad. Por una parte, se va a ver cómo es la estructura
de un contenedor Docker, cómo se comunica con el kernel de Linux, cómo
se aísla del resto del sistema y cómo funciona a nivel de discos
virtuales, interfaces de red y gestión de recursos.

Por otra parte, se comentarán diversos ejemplos y estructuras básicas
que permiten la creación de un contenedor aislado, la comunicación de
varios contenedores y el despliegue de una aplicación basada en
múltiples contenedores funcionando simultáneamente.

Finalmente, se comentarán tecnologías de orquestación de contenedores,
como son los clústers de Kubernetes y Docker Swarm y qué planes hay
previstos de cara al desarrollo e innovación de Docker como cliente y
gestor de contenedores, para dar pié a un análisis de la seguridad real
de los contenedores, en el punto [3](#sec:security){reference-type="ref"
reference="sec:security"}.

Estructura de un Docker
-----------------------

Docker ofrece un mecanismo de comunicación con un entorno aislado
llamado contenedor, que ha sido introducido anteriormente. Los
contenedores por defecto están aislados, son seguros y empaquetan todo
lo necesario para funcionar, por lo que no necesitan nada del sistema
que está por debajo.

Internamente, Docker utiliza la arquitectura "cliente--servidor" para
gestionar tanto las comunicaciones y contenedores. Por una parte, el
cliente de Docker se comunica con el *daemon*, el cual es el encargado
de realizar las tareas pesadas: construir (*build*), levantar (*run*) y
distribuir (*distribute*) los contenedores Docker.

Lo interesante del servicio en ejecución de Docker es que puede
funcionar o bien en la misma máquina que el cliente o bien sobre otra
máquina diferente. Esto es gracias a que la comunicación del cliente con
el servicio se realiza mediante *sockets* de UNIX, que proveen de una
alta velocidad; o bien mediante interfaces de red, haciendo uso de la
API REST de Docker.

### La arquitectura Docker {#la-arquitectura-docker .unnumbered}

Toda la arquitectura de Docker se puede resumir en la siguiente figura
(figura [12](#fig:docker-arch){reference-type="ref"
reference="fig:docker-arch"}):

![Arquitectura cliente--servidor de Docker
[@DockerOverview2021].[]{label="fig:docker-arch"}](pictures/docker-arch.png){#fig:docker-arch
width="\linewidth"}

De la imagen anterior destacan tres bloques principales: el cliente, el
servidor (*docker host*) y el registro (*registry*). Por una parte, el
cliente es la principal forma de comunicarse con el servicio de Docker.
Ejecutando comandos como `docker run` se envían al servicio peticiones
mediante la API REST interna que gestionan los contenedores.

Por su lado, el servicio está gestionado por el *Docker daemon*, llamado
`dockerd`. Dicho servicio escucha de forma activa las peticiones API
entrantes y gestiona los objetos de Docker, como las imágenes,
contenedores, interfaces de red y volúmenes. Además, un servicio puede
comunicarse con otros servicios para gestionar a su vez otros
contenedores.

Finalmente, los registros de Docker (no confundir con los *logs*, que
también se traduce como "registro") son un repositorio en donde se
almacenan imágenes Docker. Por defecto, se hace uso de Docker Hub, que
es el registro principal y al cual el servicio de Docker solicita
imágenes cuando no las encuentra, y en donde cualquier usuario puede
publicar la imagen que quiera. Pero, además, una persona puede hospedar
su propio registro privado (al igual que si se desplegase un servidor
Nexus).

Uno de los conceptos fundamentales que se han mencionado anteriormente
son los "objetos Docker". Esa nomenclatura se usa para agrupar y
mencionar a todo aquello que se crea y genera cuando se trabaja con el
servicio de Docker: imágenes, contenedores, interfaces de red,
*plugins*, volúmenes y demás.

### Imágenes {#imágenes .unnumbered}

Una imagen conforma una plantilla de solo lectura la cual contiene
instrucciones para crear un contenedor Docker. Por lo general, las
imágenes se basan en otras ya existentes con configuraciones
adicionales.

Un caso habitual es una imagen basada en `ubuntu-server` sobre la cual
se instala un servidor Apache y la aplicación NodeJS que hemos
desarrollado. Con esto, tendríamos una imagen la cual se basa en Ubuntu,
que ejecuta un servidor Apache y que tiene una aplicación NodeJS, junto
con los ajustes pertinentes para un correcto funcionamiento, definiendo
así una imagen nueva (figura
[13](#fig:sample-image){reference-type="ref"
reference="fig:sample-image"}):

![La nueva imagen que habríamos definido basándose en las premisas
anteriores.[]{label="fig:sample-image"}](pictures/sample-image.png){#fig:sample-image
width="\linewidth"}

Cuando se quiere crear una nueva imagen se utiliza un fichero
`Dockerfile` el cual incluye las directivas necesarias para construir
una imagen desde cero (o basándose en una ya existente). Además, el
funcionamiento de este tipo de ficheros es muy similar a los `Makefile`
en tanto que, cuando se realiza algún cambio sobre el mismo, solo se
reconstruyen en aquellas imágenes que hayan cambiado las capas
modificadas. Esto se traduce en imágenes mucho más pequeñas, ligeras y
rápidas en comparación, por ejemplo, a las máquinas virtuales.

### Contenedores {#contenedores-1 .unnumbered}

Un contenedor es una instancia de una imagen que puede ser ejecutada.
Las operaciones básicas sobre contenedores son: crear, iniciar, parar,
mover o eliminar. Además, se pueden conectar una o varias redes,
volúmenes de datos o inclusive definir y crear una nueva imagen a partir
del estado actual.

Por defecto, un contenedor está bastante bien aislado del resto de
contenedores en la máquina anfitriona. Sin embargo, se puede definir y
controlar cómo de aislada está una red, un almacenamiento o los
subsistemas que están por debajo.

Es fundamental tener en cuenta que un contenedor está directamente
definido por la imagen que lo crea y por las configuraciones iniciales
que se le dan en el momento de la creación. Sin embargo, todos los
cambios efectuados durante su ciclo de vida que no sean de imagen o de
configuración desaparecerán una vez el contenedor se detenga y se
elimine (esto incluye todo el sistema de ficheros que hay por debajo).

### Almacenamiento {#almacenamiento .unnumbered}

Dada la situación anterior, es necesario buscar alguna manera de
persistir la información de los contenedores. Por defecto, los datos que
se generan y gestionan en un contenedor de Docker son directamente
gestionados por el servicio de Docker y se trabaja con ellos sobre una
capa escribible asociada al contenedor [@ManageDataDocker2021]. Esto se
traduce en:

-   Los datos no son persistentes, por lo que eliminar el contenedor
    eliminará la información.

-   La capa escribible de un contenedor está asociada a dicho
    contenedor, por lo que resulta complejo para otros procesos extraer
    información de ella.

-   Además, dicha capa está directamente asociada a la máquina
    anfitriona en donde el contenedor está ejecutándose, por lo que es
    muy complejo mover los datos de un sitio a otro.

-   Realizar escrituras sobre la capa escribible de un contenedor
    necesita de un driver que gestione el sistema de ficheros. Usando el
    kernel de Linux, este driver ofrece una sistema de ficheros
    `UnionFS`, configurado a partir de la unión de varios sistemas de
    ficheros [@UnionFS2020]. Esto conlleva una penalización en
    rendimiento en comparación con el uso de volúmenes de datos, que
    trabajan directamente sobre el sistema de ficheros del anfitrión.

Por defecto, existen dos formas de persistir los datos de un contenedor:
mediante el uso de volúmenes o mediante *bind mounts*, es decir, asociar
un directorio en el host con un directorio en el contenedor.

![Posibles ubicaciones en donde se almacena la información en
contenedores Docker
[@ManageDataDocker2021].](pictures/types-of-mounts.png){width=".7\linewidth"}

### --- Volúmenes {#volúmenes .unnumbered}

Los volúmenes ofrecen un almacenamiento persistente completamente
gestionado por Docker, por lo que hay que crearlos de forma explícita
con "`docker volume create`".

Cuando se crea un volúmen, los datos se alojan directamente en la
máquina anfitriona. Si se asocia a un contenedor, el volumense monta
como un directorio dentro del mismo, mostrando un funcionamiento similar
a *bind mounts*. La principal diferencia es que los volúmenes ofrecen un
entorno completamente aislado de almacenamiento, gestionado por Docker y
portable.

Aprovechando lo anterior, es posible montar un volumen en varios
contenedores abriendo la posibilidad de que compartan datos entre ellos.
Además, los volúmenes son independientes de los contenedores que los
usan: si ningún contenedor usa un volúmen, este sigue existiendo hasta
que se elimine manualmente ("`docker volume prune`").

Por otra parte, como los volúmenes son gestionados por Docker permite
disponer de *volume drivers* para almacenar datos en equipos remotos.

Para resumir, se indican las características principales de los
volúmenes [@UseVolumes2021]:

-   Son fáciles de manejar, hacer copias de seguridad y de migrar a
    otros servidores.

-   Se pueden gestionar completamente desde la interfaz de línea de
    comandos de Docker.

-   Funcionan tanto en Windows como en Linux.

-   Están diseñados para que puedan ser compartidos por varios
    contenedores de forma segura.

-   Se pueden almacenar los datos en equipos remotos o proveedores de
    servicios en la nube.

-   El rendimiento en plataformas paganas (MacOS y Windows) es mejor que
    con *bind mounts*.

-   No incrementan el tamaño del contenedor sino del volumen en sí.

Los volúmenes se almacenan en el área de Docker, aislados del sistema
dentro del sistema (figura
[14](#fig:volumes-location){reference-type="ref"
reference="fig:volumes-location"}):

![Ubicación del almacenamiento de los volúmenes en Docker
[@UseVolumes2021].[]{label="fig:volumes-location"}](pictures/types-of-mounts-volume.png){#fig:volumes-location
width=".7\linewidth"}

### --- *Bind mounts* {#bind-mounts .unnumbered}

Los montajes de sistema de ficheros dentro de los contenedores llevan
existiendo desde el lanzamiento inicial de Docker. Su funcionamiento es
simple: utilizando los mecanismos de los sistemas operativos
anfitriones, un directorio (o fichero) en el equipo anfitrión se monta
dentro del contenedor en una ruta en específico. Si el fichero o
directorio no existe, se crea bajo demanda en el momento de la creación
del contenedor.

Es importante tener en cuenta que este tipo de sistema de ficheros está
mucho más limitado que un volumen y pueden suponer un gran fallo de
seguridad en tanto a que es posible acceder a ficheros sensibles del
sistema.

Hay que tener en cuenta que los contenedores Docker siempre se ejecutan
como súper usuario (administrador), por lo que un proceso malicioso
podría editar, modificar, leer y eliminar ficheros fundamentales del
sistema anfitrión si no se ha tenido cuidado con el directorio a montar.

Sin embargo, es una opción muy interesante para almacenar datos que son
modificados con cierta regularidad o que no interesa "persistirlos". Por
ejemplo, ficheros de configuración (para cambiarla bajo demanda),
directorios que contengan *logs*, etc.

Los *bind mounts* se almacenan en el sistema de ficheros anfitrión
(figura [15](#fig:bind-location){reference-type="ref"
reference="fig:bind-location"}):

![Ubicación del almacenamiento de los *bind mounts* en Docker
[@UseBindMounts2021].[]{label="fig:bind-location"}](pictures/types-of-mounts-bind.png){#fig:bind-location
width=".7\linewidth"}

### --- ¿Cuándo usar volúmenes o *bind mounts*? {#cuándo-usar-volúmenes-o-bind-mounts .unnumbered}

Basándose en la documentación oficial de Docker [@ManageDataDocker2021],
hay unos casos para unos o para otros, según se requiera (tabla
[\[tab:mount-cases\]](#tab:mount-cases){reference-type="ref"
reference="tab:mount-cases"}):

C.25\|\|C.25\|C.25\|C.25\|C.25\|C.25\|C.25\|C.25 & **Compartir datos
entre contenedores** & **Gestionar ajustes** & **Estructura del FS** &
**Copias de seguridad** & **Datos en la nube** & **Alto rendimiento** &
**Versiones del código fuente**\
**Volúmenes** & & & & & (nativo) & (en Docker Desktop) &\
***Bind mounts*** & & & & & (usando un sistema de ficheros en la nube,
como SAMBA) & (depende del sistema de ficheros del anfitrión) &\

### Interfaces de red {#interfaces-de-red .unnumbered}

Docker ofrece un potente mecanismo de gestión de redes para permitir la
comunicación entre contenedores y con elementos externos. Una de las
motivaciones principales detrás de la gestión propia de la red por parte
de Docker es la de que las aplicaciones no sepan si están dentro de un
contenedor o si tienen que comunicarse con el exterior o con una carga
de trabajo externa a Docker, sino que van a comunicarse directamente sin
necesidad de ninguna configuración externa.

Indiferentemente de si el servicio se está ejecutando en una máquina
Linux y otro en una máquina Windows, la comunicación entre ellas se va a
realizar completamente independiente a la plataforma.

La gestión de las redes y aislamiento de las mismas se realiza mediante
una manipulación directa de `iptables`. Esto se hace así porque el
*firewall* nativo de Linux tiene una grandísima potencia, es muy
configurable y se ejecuta directamente a nivel de kernel, lo cual reduce
el *overhead* que pudiera presentar si fuese una aplicación a nivel de
usuario.

Esto conlleva que las rutas del *firewall* que se hubiesen creado
previamente deben aparecer antes de las creadas por Docker (para que
tengan mayor peso) y permiten llevar la ejecución de contenedores Docker
a distintos tipos de *hardware*: servidores, routers (en donde Docker
actúa como router) y equipos embebidos.

Por defecto, Docker expone los siguientes drivers
[@NetworkingOverview2021]:

-   `bridge`: el driver que se usa por defecto, si no se especifica
    ninguno. Se destina este tipo de driver cuando las aplicaciones se
    ejecutan de forma aislada y solo necesitan comunicarse con el
    exterior o, si por el contrario, hace falta que múltiples
    contenedores se comuniquen entre sí.

-   `host`: elimina el aislamiento de red con el sistema anfitrión,
    usando la interfaz del sistema (por lo que se debe ajustar el
    *firewall* y la red, si necesita alguna característica especial).

-   `overlay`: interconecta múltiples servicios de Docker (que pueden
    estar en máquinas distintas) para facilitar la comunicación entre
    clústers de Docker Swarm o contenedores entre sí.

-   `macvlan`: asigna una dirección MAC al contenedor de forma que
    parezca que es una máquina física, por lo que se realiza el
    enrutamiento según las direcciones MAC.

-   `none`: deshabilita todas las comunicaciones de red para el
    contenedor, se suele usar conjunto a un driver personalizado.

-   *Network plugins*: cada persona puede desarrollar su propio driver
    de red para que cumpla con una función específica.

### Interfaz a bajo nivel {#interfaz-a-bajo-nivel .unnumbered}

Docker, para funcionar, necesita del kernel de Linux por debajo. ¿Por
qué esta caracterización? Todo se debe a medidas de seguridad.

Por lo general, un contenedor de Docker se asemeja mucho a los
contenedores LXC de Linux nativos, incluyendo entre otros
características de seguridad. Si observamos los requisitos de la
interfaz Docker (figura [16](#fig:docker-interface){reference-type="ref"
reference="fig:docker-interface"}) vemos que inclusive hace uso de la
librería de LXC:

![Interfaz de Docker con respecto al kernel de Linux. Fuente: Wikipedia
[@DockerSoftware2021].[]{label="fig:docker-interface"}](pictures/Docker-linux-interfaces.png){#fig:docker-interface
width=".3\linewidth"}

El principal mecanismo de aislamiento son los *Linux kernel namespaces*,
consistentes en una "venda en los ojos" hacia los procesos que se
ejecutan dentro de un contenedor.

Lo siguiente que entra en juego son los *control groups* (`cgroups`),
necesarios para limitar el acceso a los recursos del sistema.

Todas estas capas se analizarán en mayor profundidad más adelante, en el
punto [3](#sec:security){reference-type="ref" reference="sec:security"}.

Creación de un contenedor
-------------------------

La creación de un contenedor siempre se realiza de la misma manera:
mediante un fichero `Dockerfile`. Los `Dockerfile` son ficheros del
estilo de los `Makefile` que contienen unas reglas básicas que definen
lo que será una imagen de un contenedor.

El comando que crea una imagen es `docker build`, el cual toma las
instrucciones que aparecen en el fichero y las va ejecutando una a una
hasta que se produce un error o finaliza correctamente.

Un fichero `Dockerfile` cuenta con multitud de directivas que permiten
personalizar y configurar cómo va a funcionar
[@DockerfileReference2021]. Aquí se van a introducir algunas de las más
importantes (o las más usadas) [@jethvaHowDockerfileWorks]:

-   `FROM`: define una imagen base de partida sobre la que construir.

-   `ADD`: copia ficheros y directorios dentro de la imagen del
    contenedor. Además, acepta URLs como parámetro y las descarga
    directamente dentro.

-   `RUN`: añade capas a la imagen base, instalando aplicaciones,
    librerías y componentes.

-   `CMD`: especifica qué comandos se deben ejecutar al iniciarse el
    contenedor. Es importante tener en cuenta que solo puede existir una
    instrucción `CMD` en el fichero `Dockerfile` (si no, se usa solo el
    último que aparezca). Su funcionalidad principal es la de establecer
    los valores por defecto de un contenedor en ejecución.

-   `ENTRYPOINT`: es la instrucción "principal" de un `Dockerfile`.
    Especifica el punto de entrada de un contenedor que se quiere que
    funcione como un ejecutable. Por ejemplo, el siguiente comando
    "`docker run -it --rm -p 80:80 nginx`" ejecuta un servidor NGINX de
    forma interactiva, publica el puerto 80 y, cuando finaliza su
    ejecución, se elimina.

-   `ENV`: define las variables del entorno del contenedor que se usarán
    en tiempo de ejecución.

-   `COPY`: con una funcionalidad similar a `ADD` pero con más
    limitaciones.

-   `EXPOSE`: define en qué puertos la aplicación estará escuchando.

-   `USER`: especifica el UID (o el nombre del usuario) que se usará
    internamente en el contenedor para ejecutar las aplicaciones.

-   `VOLUME`: define volúmenes de datos a crear o un punto de montaje
    del contenedor en tiempo de ejecución.

-   `WORKDIR`: especifica la ubicación en donde se ejecutará el comando
    en tiempo de ejecución.

-   `LABEL`: especifica etiquetas del contenedor en forma de metadatos.
    Se conforman de parejas clave--valor que especifican información
    relativa a la imagen dentro del contenedor como, por ejemplo, la
    versión, el nombre del paquete, etc.

Por lo general, un `Dockerfile` comienza con la especificación de una
imagen de partida (ya que no es habitual crear una imagen desde cero) y,
a continuación, se procede a instalar diversos paquetes y capas que
puedan ser necesarias para nuestra aplicación. A continuación se copian
los paquetes y requisitos de la aplicación dentro de la imagen y se
ejecuta la compilación o preparación del paquete, si fuera necesario.
Finalmente, se especifica el punto de entrada del contenedor y los
argumentos que recibirá, si recibe. Además, si es necesario se añaden
los puertos expuestos y volúmenes necesarios para el funcionamiento.

En el código
[\[lst:dockerfile-example\]](#lst:dockerfile-example){reference-type="ref"
reference="lst:dockerfile-example"} se tiene un ejemplo de un
`Dockerfile` completo [@BestPracticesWriting2021]:

``` {#lst:dockerfile-example style="Dockerfile" caption="Ejemplo de \texttt{Dockerfile} para una aplicación Go \cite{BestPracticesWriting2021}." label="lst:dockerfile-example"}
# syntax=docker/dockerfile:1
FROM golang:1.16-alpine AS build

# Install tools required for project
# Run `docker build --no-cache .` to update dependencies
RUN apk add --no-cache git
RUN go get github.com/golang/dep/cmd/dep

# List project dependencies with Gopkg.toml and Gopkg.lock
# These layers are only re-built when Gopkg files are updated
COPY Gopkg.lock Gopkg.toml /go/src/project/
WORKDIR /go/src/project/
# Install library dependencies
RUN dep ensure -vendor-only

# Copy the entire project and build it
# This layer is rebuilt when a file changes in the project directory
COPY . /go/src/project/
RUN go build -o /bin/project

# This results in a single layer image
FROM scratch
COPY --from=build /bin/project /bin/project
ENTRYPOINT ["/bin/project"]
CMD ["--help"]
```

En el fichero anterior se establece una imagen de partida
`golang:1.16-alpine` que contiene los binarios de Go en una distribución
de muy poco peso (proyecto Linux Alpine). Esta imagen se obtiene desde
[Docker Hub](https://hub.docker.com/_/golang).

A continuación, instala el paquete `git` y el gestor de dependencias de
Go. Después, copia el proyecto en sí e instala las dependencias en la
ruta `/go/src/project`. Finalmente, copia el directorio actual en dicha
ruta y define una nueva imagen partiendo de la de Golang en donde se
ejecuta el proyecto compilado con las opciones `--help` por defecto.

Cuando se define un contenedor es recomendable instalar solo aquellas
dependencias que sean necesarias. Esto permite una mayor y mejor
mantenibilidad, reduce la complejidad y el tiempo de construcción de la
imagen.

Por otra parte, se recomienda encarecidamente desacoplar la aplicación:
por ejemplo, un servidor web posiblemente requiera de varias
aplicaciones en ejecución. Es recomendable separarlas en contenedores y
habilitar la comunicación entre ellos a encapsularlo todo en un único
contenedor. Esto facilita, entre otros, un escalado horizontal en donde
si se requieren de más imágenes se crean.

Además, el número de capas se debe mantener lo más pequeño posible: las
instrucciones `RUN`, `COPY` y `ADD` crean capas, mientras que otras
instrucciones solo crean imágenes intermedias.

Finalmente, es importante construir el `Dockerfile` teniendo en cuenta
que Docker usa una caché interna. Si se quiere deshabilitar se puede
hacer con la opción `--no-cache=true` en el comando `docker build`. Sin
embargo, es recomendable hacer uso de la caché interna de Docker ya que
agiliza el proceso de construcción.

Comunicación entre contenedores
-------------------------------

La comunicación entre contenedores presenta dos formas posibles:

1.  O bien mediante la comunicación mediante una red o un *socket*.

2.  O bien mediante ficheros compartidos en un volúmen o carpeta.

Evidentemente, cada una presenta sus ventajas. Sin embargo, la primera
opción es la escogida por lo general. ¿Por qué?

Habilitar la comunicación mediante una red asegura que solo los
contenedores especificados reciben la información en cuestión. Si se usa
un directorio compartido se corre el riesgo de que otra aplicación pueda
ver la información y eso no es seguro.

Por otra parte, las comunicaciones vía red facilitan la escucha pasiva
mediante el uso de puertos: si se tiene un puerto publicado, basta con
escuchar allí a la espera de peticiones. Si se pretende realizar una
comunicación mediante un directorio compartido es necesario o bien hacer
*polling* cada 'x' segundos o bien usar algún mecanismo del kernel (como
`inotify`) para ser notificados cuando se realice alguna acción sobre un
fichero en cuestión.

Finalmente, comunicaciones basadas en la red permiten identificar quién
es el emisor que está al otro lado, escuchando o recibiendo información.
Sin embargo, en comunicaciones basadas en ficheros cualquiera puede
acceder y no se sabe necesariamente qué proceso es el último que ha
editado o leído un fichero.

La forma de comunicar dos contenedores vía red se realiza principalmente
mediante puentes (conexiones tipo *bridge*). Este tipo de interfaz es
nativa de Docker y muy fácil de configurar. Por defecto, un contenedor
usará este tipo de red para realizar sus comunicaciones con el exterior
y con otros equipos, por lo que usarla para conectar varios contenedores
es sencillo. Existen dos formas de hacerlo:

1.  Durante la creación, especificando la red a la que conectarse.

2.  En tiempo de ejecución, usando el cliente Docker para indicarle a un
    contenedor que se debe unir a una red.

### Conexión {#conexión .unnumbered}

Para realizar la conexión entre contenedores se utilizan siempre redes
virtuales. El tipo de red puede variar según se necesite, pero
principalmente se usan las tipo puente (mencionadas anteriormente) y las
redes *overlay*, más específicas para casos más concretos que se
mencionarán más adelante.

En estas redes el contenedor cuenta con una dirección IP única asignada
por el servicio Docker (`dockerd`) y, opcionalmente, un *hostname* que
permite la identificación directa y sencilla del contenedor.

Por defecto, Docker crea una interfaz *bridge* para el contenedor y se
puede usar para comunicar dos contenedores. Sin embargo, el nombre de
las redes no es fácilmente accesible y menos el de los contenedores. La
idea principal radica en el uso de la IP única asignada a dicha
interfaz: si se obtiene la dirección de un contenedor, otro podrá enviar
información directamente a esa IP.

La forma de configurar esta conexión es la siguiente:

1.  Se comprueba que la red a la que se quieran conectar los
    contenedores esté en ejecución. Esto se consigue gracias al comando
    `docker network ls`:

    ![image](pictures/network-ls.png){width=".6\linewidth"}

2.  Se inician los contenedores (o se obtiene su ID) para
    posteriormente, poder obtener su IP. Se puede obtener el
    identificador de un contenedor mediante el comando
    `docker container ls`:

    ![image](pictures/container-ls.png){width=".5\linewidth"}

3.  Finalmente, se obtiene la dirección IP interna del contenedor. Para
    ello, se pueden usar herramientas externas como
    [Portainer](https://www.portainer.io/) o directamente desde el
    terminal mediante comandos:
    `docker inspect <container-id> | grep IPAddress`:

    ![image](pictures/ip-address.png){width=".5\linewidth"}

Con la dirección IP ya podemos empezar a comunicarnos con el contenedor,
tanto desde dentro de Docker como desde la máquina anfitriona. Esto se
puede comprobar fácilmente haciendo un `ping` a la IP (figura
[17](#fig:ping){reference-type="ref" reference="fig:ping"}):

![Desde la máquina anfitriona nos podemos comunicar con el contenedor
mediante la
IP.[]{label="fig:ping"}](pictures/container-ping.png){#fig:ping
width=".6\linewidth"}

------------------------------------------------------------------------

La opción anterior sin embargo es bastante tediosa y no permite
realizarlo fácilmente en pocas líneas. Es por ello por lo que existe la
opción de redes definidas por el usuario (*user-defined bridge network*
[@donohueHowCommunicateDocker2020]).

Cuando un grupo de contenedores se unen a una red tipo puente definida
por el usuario ya no es necesario tener el control sobre la dirección IP
de cada contenedor sino que basta con referenciar al contenedor por su
nombre (figura [18](#fig:user-defined-network){reference-type="ref"
reference="fig:user-defined-network"}):

![Interfaz de red tipo puente definida por el usuario para facilitar la
comunicación entre contenedores
[@donohueHowCommunicateDocker2020].[]{label="fig:user-defined-network"}](pictures/user-defined-bridge.png){#fig:user-defined-network
width=".7\linewidth"}

De esta forma, si se ejecuta una base de datos dentro de un contenedor
(por ejemplo, una base tipo PostgreSQL), la conexión se puede realizar
directamente escribiendo:

`postgresql://psql-container:5432`

lo cual facilita mucho la labor de depuración y desarrollo.

El proceso de creación y conexión en este caso es de la siguiente forma:

1.  Se crea una red definida por el usuario de tipo puente, mediante el
    comando `docker network create <name>`. Por debajo Docker se
    encargará de gestionar todo lo necesario:

    ![image](pictures/network-create.png){width=".5\linewidth"}

2.  A continuación se crea el contenedor y se le asigna la red que
    acabamos de crear. Es importante en este paso asignarle también un
    nombre al contenedor para que sea fácilmente accesible. Lo primero
    se consigue con la opción `--network <network-name>` y lo segundo
    con la directiva `--name <container-name>`:

    ![image](pictures/container-create.png){width=".9\linewidth"}

3.  Finalmente, creamos el/los otro(s) contenedor(es) y les asociamos
    igualmente la red que hemos creado. En este caso, vamos a ejecutar
    una terminal básica que va a realizar una petición al servidor de
    NGINX que acabamos de levantar con el comando `wget`. Para acceder
    se pone directamente el nombre del contenedor de NGINX y el puerto
    al que se quiere acceder, no hace falta usar la IP:

    ![image](pictures/nginx-wget.png){width=".9\linewidth"}

Lo interesante de este método no es solo que no haga falta saber la IP
del contenedor (la cual entre reinicios puede cambiar) sino que además
permite la conexión "en caliente" de un contenedor a la red: si durante
la creación no le hemos asignado la red no habría problema ya que existe
un método de poder unir el contenedor a la red. Este comando es
`docker network connect <network-name> <container-name/ID>` y permite
gestionar las interfaces de red de un contenedor fácilmente
[@DockerNetworkConnect2021]. Es el reemplazo del antiguo comando
`--link`, ya en deshuso [@LegacyContainerLinks2021] el cual unía dos
contenedores por medio de una red puente.

### Redes *overlay* {#redes-overlay .unnumbered}

Otra forma de conectar contenedores es mediante las redes *overlay*.
Dichas redes permiten conectar múltiples clústers de Docker (en
particular, *Swarm*) entre sí para facilitar el intercambio de
información. Sin embargo, el modo de funcionamiento ya no se limita
únicamente a una red local sino a una red WAN para la que es necesario
añadir orquestación mediante Kubernetes o Docker Swarm.

El procedimiento sin embargo es muy similar al de crear una red tipo
puente personalizada, solo se alteran algunos pasos:

1.  Inicializamos un clúster de *Swarm* y exponemos la IP a la cual
    otros nodos podrán unirse. Esto se hace con:

    `docker swarm init --advertise-addr <IP-address>`

2.  Tras la creación se generará un token el cual se usará para unirse
    al clúster de Swarm:

    `docker swarm join --token <Swarm-token>`

    Este paso es necesario ya que, en otro caso, estaremos trabajando
    sobre el servicio local de Docker y no sobre el clúster de Swarm.

3.  A continuación, creamos la red *overlay*. En este caso, el comando
    difiere en que hay que añadir el tipo de red que se quiere crear:

    `docker network create -d overlay <network-name>`

    ![image](pictures/network-create-overlay.png){width=".6\linewidth"}

4.  Como se está trabajando sobre Docker Swarm, se han de crear
    servicios (no contenedores) que se ejecutarán de forma distribuida a
    lo largo del clúster. En este caso, a modo de demostración se va a
    crear un servicio de NGINX que sea similar al del ejemplo anterior:

    `docker service create --name nginx-server -d --network ssr-overlay nginx`

    ![image](pictures/nginx-service-create.png){width=".6\linewidth"}

5.  Finalmente, se crea otro servicio que en este caso va a acceder
    directamente al servicio de NGINX mediante el comando `wget`:

    `docker service create --network ssr-overlay --name bb -d busybox wget -q -O- nginx-server:80`

    ![image](pictures/nginx-wget-swarm.png){width=".9\linewidth"}

Como se puede ver, también se pueden conectar los contenedores a través
de redes *overlay* y usando directamente el nombre del contenedor. Su
configuración es bastante más compleja y añade más pasos, que se
explicarán con más detalle en el punto
[2.5](#sec:swarm){reference-type="ref" reference="sec:swarm"}.