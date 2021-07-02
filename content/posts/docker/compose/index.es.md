---
title: '3. Aplicaciones multicontenedor - docker-compose'
author: Javinator9889
date: 2021-06-28T16:55:00+02:00
series: ["Docker"]
cover:
  image: images/cover.png
categories:
  - Docker
url: "docker/compose"
tags:
  - docker
  - linux
  - contenedores
  - docker-compose
  - qué es
draft: true
---

> Esta entrada es parte de un conjunto de entradas extraídas directamente
del artículo ya escrito que versa sobre este tema, el cual es completamente
accesible y se puede leer en la siguiente dirección:

Despliegue de aplicaciones multi--contenedores. `docker-compose` {#sec:compose}
----------------------------------------------------------------

Uno de los principales puntos que se han visto durante el desarrollo del
documento es la necesidad de comunicar contenedores y de distribuir
aplicaciones en var­ias imágenes Docker.

Un *stack* típico de aplicaciones sería un servidor XAMPP: un contenedor
ejecutando Apache que se comunica con una base de datos MySQL y que
utiliza un *backend* basado en PHP. Se puede construir una única imagen
la cual se componga de esas tres aplicaciones y sus dependencias. Sin
embargo, según se recomienda desde Docker, lo ideal para no añadir
demasiada complejidad sería crear un contenedor mínimo para cada
aplicación que funcione de forma aislada del resto pero que se comunique
con ello.

Si bien esta tarea se podría realizar manualmente con los comandos que
se han visto anteriormente, existe una herramienta llamada
"`docker-compose`" la cual gestiona clústers de contenedores que se
ejecutan a la vez y que dependen unos de otros.

### ¿Qué es Docker Compose? {#qué-es-docker-compose .unnumbered}

Docker Compose es una herramienta basada en Python que se usa para
definir aplicaciones multicontenedor dentro de Docker. Se basa en el
formato de ficheros YAML para definir los servicios de la aplicación y,
con un único comando, preparar su ejecución y trabajar con dichos
servicios [@OverviewDockerCompose2021].

La definición de un servicio de Compose se define en tres pasos:

1.  Definir los ficheros `Dockerfile` de cada uno de los entornos de la
    aplicación.

2.  Definir qué servicios componen la aplicación en un fichero
    `docker-compose.yml`.

3.  Ejecutar el comando "`docker compose up`" para lanzar la aplicación
    al completo.

Un fichero `docker-compose.yml` tiene una forma como esta (código
[\[lst:compose\]](#lst:compose){reference-type="ref"
reference="lst:compose"}):

``` {#lst:compose style="docker-compose" caption="Estructura típica de un fichero de Docker Compose \cite{OverviewDockerCompose2021}." label="lst:compose"}
version: "3.9"  # optional since v1.27.0
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    links:
      - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
```

La estructura que se sigue habitualmente se define por las siguientes
claves en el fichero YAML [@DockerComposeTutorial]:

-   `version: "XY"` define qué versión de Docker Compose se está usando.
    Esta línea, aunque opcional desde la versión `v1.27.0`, es
    fundamental ya que las características de Docker Compose varían
    según la versión que se esté usando. Es importante que en este caso
    una versión posterior no implica que "sea mejor" sino que algunas
    características cambian de nombre, otras aparecen y otras se
    eliminan.

-   `services` -- esta sección define los distintos contenedores que se
    van a crear. En el ejemplo del código
    [\[lst:compose\]](#lst:compose){reference-type="ref"
    reference="lst:compose"}, se crean dos servicios: uno primero que es
    `web` que se construye sobre el directorio actual; y un segundo con
    nombre `redis` que usa la imagen de Redis desde Docker Hub.

-   `build` especifica la ubicación del fichero `Dockerfile`. En en
    ejemplo del código
    [\[lst:compose\]](#lst:compose){reference-type="ref"
    reference="lst:compose"} se usa el directorio actual '`.`' como
    ubicación para construir el contenedor.

-   `ports` especifica los puertos mapeados del contenedor en cuestión.
    Es el equivalente a la opción `-p` del comando `docker`.

-   `volumes` define los volúmenes que se van a usar en el contenedor.
    En particular es como usar la opción `-v` a la hora de crear un
    contenedor. Por ende, se puede usar un directorio para hacer *bind
    mounts*, usar el nombre de un volúmen, etc.

-   `links` permite unir un contenedor a otro. En este caso, se
    especifica a qué contenedor se puede acceder.

-   `image` permite definir un servicio en un `docker-compose` usando
    una imagen ya existente en Docker Hub, si no se dispone del
    `Dockerfile` apropiado.

-   `environment` define las variables del entorno del contenedor y sus
    respectivos valores. Equivalente a la opción `-e` del comando
    `docker`.

Así, con la estructura del fichero ya definida, usando el comando
`docker-compose` se puede [@OverviewDockerCompose2021]:

-   Iniciar, parar y reconstruir servicios.

-   Ver el estado de los servicios en ejecución.

-   Volcar los registros de ejecución en tiempo real (*stream view*).

-   Ejecutar un único comando en un servicio.

Tras esta idea se ha construido una forma muy potente y simple de crear
aplicaciones multicontenedor. Aprovechando las características de
Docker, Compose permite ejecutar distintos entornos aislados en el mismo
anfitrión. Por ejemplo, de esta forma, una aplicación Docker Compose
puede contar con varios entornos según en donde se quiera ejecutar. Por
ejemplo, se puede tener un entorno de desarrollo, otro de CI y uno de
producción en el mismo *host*. Esto se consigue gracias a los nombres de
proyecto, característica fundamental de Docker Compose para distinguir y
aislar entornos.

Otro punto interesante es que se puede actualizar el fichero
"`docker-compose.yml`" cuando se necesite y la construcción de los
contenedores se realizará únicamente para aquellos que hayan cambiado.
Esto da una gran agilidad a la hora de presentar actualizaciones en un
entorno de producción y potencia la idea de microservicios, en donde
solo se actualiza lo que se necesita.

Esto afecta también a cómo se gestionan los datos de los contenedores.
Si el volumen asociado a un contenedor ya existía se sigue usando el
mismo, en ningún momento se "tira abajo" y se empieza desde cero.

Finalmente, una de las características más interesantes de Docker
Compose es que soporta las variables del entorno. Esto se traduce en que
un mismo fichero YAML de Docker Compose puede producir distintas
configuraciones según el entorno en que se encuentre. Aprovechando esta
característica, se pueden definir y usar ficheros `.env` para establecer
las variables del entorno que se usarán a la hora de desplegar los
servicios y trabajar con los contenedores.

### Comandos Docker Compose {#comandos-docker-compose .unnumbered}

De entre todas las opciones que ofrece Compose, algunas son muy
interesantes por las potencias que ofrecen y sus utilidades
[@DockerComposeTutorial]:

-   `docker-compose build` prepara las imágenes construyendo los
    servicios, listos para ser lanzados. Si una imagen es del
    repositorio *online* no se hace nada.

-   `docker-compose images` lista las imágenes que se han construido
    desde el fichero actual.

-   `docker-compose stop` detiene los servicios en ejecución actuales.

-   `docker-compose run <service>` crea los contenedores para el
    servicio especificado.

-   `docker-compose up` inicia todo el proceso de despliegue de los
    servicios: primero, construye las imágenes necesarias y luego inicia
    cada uno de los contenedores especificados.

-   `docker-compose ps` lista todos los contenedores del
    `docker-compose.yml` actual.

-   `docker-compose down` detiene todos los contenedores y limpia sus
    datos, redes e imágenes.

### Caso real {#caso-real .unnumbered}

A modo de demostración, se va a crear un *stack* Wordpress, NGINX,
PHP-FPM y MySQL para desplegar un servidor web Wordpress de forma
sencilla (basándose en el ejemplo de Digital Ocean
[@ComoInstalarWordPress]).

Asumiendo que los ficheros de configuración de NGINX ya están preparados
así como las dependencias necesarias, se pasa a definir los ficheros de
Docker Compose. Por una parte, para la base de datos, se van a definir
las credenciales en un fichero `.env`:

``` {style="bash" caption=""}
MYSQL_ROOT_PASSWORD="password-random"
MYSQL_USER="wordpress_user"
MYSQL_PASSWORD="wordpress-random-password"
```

A continuación, se pasa a definir cada uno de los servicios que
compondrá la aplicación. El primero de ellos será la base de datos MySQL
(código [\[lst:compose-mysql\]](#lst:compose-mysql){reference-type="ref"
reference="lst:compose-mysql"}):

``` {#lst:compose-mysql style="docker-compose" caption="Servicio de MySQL para el \textit{stack} Wordpress." label="lst:compose-mysql"}
version: '3'

services:
  db:
    image: mysql:8.0
    container_name: db
    restart: unless-stopped
    env_file: .env
    environment:
      - MYSQL_DATABASE=wordpress
    volumes:
      - dbdata:/var/lib/mysql
    command: '--default-authentication-plugin=mysql_native_password'
    networks:
      - app-network
```

Lo primero que se especifica es la versión de Docker Compose que se
necesita, en este caso, la $3$. Para este caso en particular, se va a
usar la imagen de MySQL versión 8.0 (clave `image`) con nombre "`db`" y
que se debe reiniciar hasta que se detenga (clave `restart`). En lo
referente a las variables del entorno, se define el nombre de la base de
datos asignando la clave `MYSQL_DATABASE` y se define un volumen
"`dbdata`" el cual almacenará los datos de MySQL de forma persistente.
Finalmente, se especifican algunas opciones iniciales al comando inicial
de MySQL y se especifica la red en la que estará conectada.

A continuación, se define el servicio de Wordpress (código
[\[lst:compose-wordpress\]](#lst:compose-wordpress){reference-type="ref"
reference="lst:compose-wordpress"}):

``` {#lst:compose-wordpress style="docker-compose" caption="Servicio de Wordpress." label="lst:compose-wordpress"}
  wordpress:
    depends_on:
      - db
    image: wordpress:5.1.1-fpm-alpine
    container_name: wordpress
    restart: unless-stopped
    env_file: .env
    environment:
      - WORDPRESS_DB_HOST=db:3306
      - WORDPRESS_DB_USER=$MYSQL_USER
      - WORDPRESS_DB_PASSWORD=$MYSQL_PASSWORD
      - WORDPRESS_DB_NAME=wordpress
    volumes:
      - wordpress:/var/www/html
    networks:
      - app-network
```

En este caso, la configuración es similar al de MySQL pero se añade una
directiva que define el orden de inicio de los contenedores
(`depends_on`). Se va a usar la imagen de `wordpress:5.1.1-fpm-alpine`
que es la versión de Wordpress `5.1.1` con PHP-FPM por detrás en la
versión *alpine*, derivada del proyecto Alpine Linux que busca un tamaño
reducido de las imágenes. A continuación, se especifica el fichero que
contiene las variables del entorno (`env_file`) y se definen las
opciones de Wordpress. Finalmente, se crea un volúmen que contendrá los
datos de Wordpress y se asocia al directorio `/var/www/html` dentro del
contenedor y se define la red a la que se conecta.

Por último, pero no menos importante, se define el servidor web en sí.
En este caso, se usa NGINX (código
[\[lst:compose-nginx\]](#lst:compose-nginx){reference-type="ref"
reference="lst:compose-nginx"}):

``` {#lst:compose-nginx style="docker-compose" caption="Servicio de NGINX." label="lst:compose-nginx"}
  webserver:
    depends_on:
      - wordpress
    image: nginx:1.15.12-alpine
    container_name: webserver
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - wordpress:/var/www/html
      - ./nginx-conf:/etc/nginx/conf.d
    networks:
      - app-network
```

De la configuración anterior es importante fijarse en que, por una
parte, se expone el puerto `80` (HTTP) al exterior (opción `ports`) y se
reutiliza el volúmen de Wordpress. Además, se hace un *bind mounts* del
fichero "`nginx-conf`" dentro del directorio `/etc/nginx/conf.d`. Esto
permite realizar cambios en la configuración de NGINX y que se puedan
aplicar directamente.

Finalmente, al final del fichero, se añade la especificación de la red y
de los volúmenes (código
[\[lst:compose-end\]](#lst:compose-end){reference-type="ref"
reference="lst:compose-end"}):

``` {#lst:compose-end style="docker-compose" caption="Especificación de los volúmenes y de las redes." label="lst:compose-end"}
volumes:
  wordpress:
  dbdata:

networks:
  app-network:
    driver: bridge
```

Quedando un fichero `docker-compose.yml` así:

``` {style="docker-compose" caption=""}
version: '3'

services:
  db:
    image: mysql:8.0
    container_name: db
    restart: unless-stopped
    env_file: .env
    environment:
      - MYSQL_DATABASE=wordpress
    volumes:
      - dbdata:/var/lib/mysql
    command: '--default-authentication-plugin=mysql_native_password'
    networks:
      - app-network

  wordpress:
    depends_on:
      - db
    image: wordpress:5.1.1-fpm-alpine
    container_name: wordpress
    restart: unless-stopped
    env_file: .env
    environment:
      - WORDPRESS_DB_HOST=db:3306
      - WORDPRESS_DB_USER=$MYSQL_USER
      - WORDPRESS_DB_PASSWORD=$MYSQL_PASSWORD
      - WORDPRESS_DB_NAME=wordpress
    volumes:
      - wordpress:/var/www/html
    networks:
      - app-network

  webserver:
    depends_on:
      - wordpress
    image: nginx:1.15.12-alpine
    container_name: webserver
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - wordpress:/var/www/html
      - ./nginx-conf:/etc/nginx/conf.d
    networks:
      - app-network

volumes:
  wordpress:
  dbdata:

networks:
  app-network:
    driver: bridge
```

Después de realizar varias configuraciones iniciales, el servidor
Wordpress ya estará completamente funcional y disponible (ver el ejemplo
completo en la web de Digital Ocean [@ComoInstalarWordPress]).