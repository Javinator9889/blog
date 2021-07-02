---
title: '4. Orquestación de contenedores: Kubernetes y Docker Swarm'
author: Javinator9889
date: 2021-06-28T16:55:00+02:00
series: ["Docker"]
cover:
  image: images/cover.png
categories:
  - Docker
url: "docker/orchestration"
tags:
  - docker
  - linux
  - contenedores
  - docker-compose
  - orchestration
  - kubernetes
  - swarm
  - qué es
draft: true
---

> Esta entrada es parte de un conjunto de entradas extraídas directamente
del artículo ya escrito que versa sobre este tema, el cual es completamente
accesible y se puede leer en la siguiente dirección:

"Orquestación" de contenedores {#sec:swarm}
------------------------------

Todo lo anterior lleva al punto crítico en donde se encuentran los
contenedores y tecnologías como Docker actualmente: ¿cómo se automatiza
el despliegue? ¿Cómo se realizan escalados automáticos? ¿Cómo se guardan
recursos, se conservan y se reutilizan más tarde? Bienvenidos a la
orquestación de contenedores.

Actualmente las herramientas de orquestación están en boga y son la
clave del desarrollo basado en contenedores. Ofrecen una gran
polivalencia y flexibilidad a la hora de desplegar aplicaciones a lo
largo de clústers distribuidos de una forma relativamente sencilla y
accesible.

Herramientas como Kubernetes, Minikube, AWS EKS o Docker Swarm son de
las más sonadas y utilizadas actualmente. El primero de ellos es
actualmente el más usado a nivel mundial. Kubernetes es una herramienta
de código abierto diseñada por Google que permite orquestar contenedores
a lo largo de una red distribuida de nodos. Minikube por su parte es una
versión local de Kubernetes con las mismas características, muy útil
para desplegar aplicaciones en entornos locales y hacer pruebas antes de
un despliegue global. AWS EKS es la solución nativa de Amazon para su
servicio en la nube de orquestación. Se basa en Kubernetes y permite
realizar una gestión individualizada de los contenedores para ajustar el
pago y los recursos destinados. Finalmente, Docker Swarm es la solución
nativa de Docker para la orquestación de contenedores. Se gestiona con
el propio CLI de Docker y, aunque no es tan popular como otras
herramientas, está ganando fuerza debido a su gran facilidad de uso.

### ¿Por qué es importante la orquestación de contenedores? {#por-qué-es-importante-la-orquestación-de-contenedores .unnumbered}

Es fundamental intentar vislumbrar el porqué han ganado tanto peso estas
herramientas de orquestación ya que es la clave de muchas empresas. La
organización en contenedores automatiza la implementación, la gestión,
la escalabilidad y la conexión en red de los contenedores. Empresas que
necesiten implementar y gestionar cientos o miles de *hosts* usando
contenedores Linux se benefician directamente de la orquestación de
contenedores [@QueEsOrganizacion].

En particular, estas tecnologías han visto un gran auge con la aparición
de los microservicios organizados en contenedores. Con ellas se pueden
desplegar más instancias de un microservicio si la carga del sistema es
elevada o reducir los contenedores según sea la demanda. Por otra parte,
los microservicios son muy útiles en la gestión de los ciclos de vida de
los contenedores, en particular para los equipos de DevOps: una
integración correcta en los flujos de trabajo de CI/CD permiten definir
la base de las aplicaciones nativas en la nube.

Es por ello por lo que las tecnologías de orquestación han proliferado y
permiten definir automatizar y gestionar muchas tareas
[@QueEsOrganizacion]:

-   Preparación e implementación.

-   Configuración y programación.

-   Asignación de recursos.

-   Disponibilidad de contenedores.

-   Ajusta o eliminación de contenedores según la carga del sistema.

-   Equilibrio de cargas y enrutamiento de tráfico.

-   Supervisión del estado de los contenedores.

-   Configuración de aplicaciones en función del contenedor en que se
    vayan a ejecutar.

-   Protección de las interacciones entre contenedores.

Con todas estas tareas automatizadas, es más sencillo gestionar
aplicaciones distribuidas. Todo esto es necesario debido a la naturaleza
ligera y efímera de los contenedores, en donde el ciclo de vida de
alguno de ellos puede llegar a ser de unos pocos segundos (como en
microservicios). Así, la orquestación viene a ofrecer los siguientes
beneficios [@ContainerOrchestration]:

-   Simplicidad en las operaciones, el gran beneficio de la
    orquestación: según lo expuesto anteriormente, las aplicaciones
    basadas en contenedores pueden introducir una gran complejidad y
    generar muchísimos datos. Con la orquestación es más simple
    gestionarlo.

-   Resiliencia, permitiendo el reinicio y escalado de los contenedores
    necesarios según se necesite de forma automática.

-   Seguridad, ya que se reduce el error humano.

### Herramientas de orquestación

### Kubernetes {#kubernetes .unnumbered}

![Logo de Kubernetes
[@ArchivoKubernetesLogo].[]{label="fig:k8s-logo"}](pictures/kubernetes-logo.png){#fig:k8s-logo
width="\linewidth"}

Kubernetes es actualmente la herramienta de orquestación más utilizada
por las compañías que basan sus aplicaciones en contenedores
[@ContainerAdoptionTrends]. Fue una herramienta de código libre creada
por Google y donada a la *Cloud Native Computing Foundation*, quien lo
gestiona ahora.

Dado que los contenedores son una buena manera de desplegar
aplicaciones, la gestión en entornos de producción se cede a
herramientas como K8s que se aseguran de que no exista tiempo de
*downtime* (K8s son las siglas de "Kubernetes", donde el 8 representa
las ocho letras entre la 'K' y la 's'). Por ejemplo, si un contenedor se
cae y no ofrece servicio, automáticamente otro se crea y se levanta y
suple al anterior [@WhatKubernetes].

K8s ofrece un *framework* para poder ejecutar sistemas distribuidos de
forma resiliente. Gestiona automáticamente el escalado y el control de
fallos de la aplicación, ofrece patrones de despliegue y más opciones,
entre las que se destacan [@WhatKubernetes]:

-   Descubrimiento de servicios y balanceo de carga: mediante el uso de
    direcciones DNS o direcciones IP, K8s puede exponer un contenedor a
    la red. Si por un casual el tráfico es elevado, aprovechando el
    mecanismo anterior se puede redirigir automáticamente a un
    contenedor con poca carga o que pueda servir la operación de una
    forma más eficaz.

-   Orquestación del almacenamiento: Kubernetes permite gestionar el
    almacenamiento local, en la nube o en proveedores para los
    contenedores que lo necesiten.

-   *rollouts* y *rollbacks*: mediante la descripción de los estados en
    los que se pueden encontrar los contenedores (como el estado
    "deseable"), Kubernetes puede modificar el estado para alcanzar
    dicho estado deseable o bien volver a un estado controlable. Un
    ejemplo sería el despliegue de nuevos contenedores, eliminar los ya
    existentes y adoptar sus recursos para continuar desde el estado en
    que se dejó.

-   Gestión de los recursos: se puede configurar un clúster de
    Kubernetes para que use una cantidad específica de CPU y de RAM y
    automáticamente se distribuirán los servicios para hacer el uso más
    eficiente posible de los recursos.

-   Autocuidado: si un contenedor falla, se reinicia; si no funciona
    como se espera, se reemplaza; si no hay respuesta en un plazo de
    tiempo, se finaliza. Todo esto se hace de forma transparente al
    usuario y nunca se ofrecen servicios que todavía no estén
    disponibles.

-   Gestión de "secretos" y configuraciones: K8s facilita la gestión de
    información sensible como contraseñas, claves OAuth, etc.,
    permitiendo la actualización de dichos valores sin necesidad de
    desplegar de nuevo la aplicación y sin exponer dicha información al
    exterior.

Sin embargo, es fundamental tener en cuenta qué operaciones nunca va a
realizar Kubernetes y que lo diferencian de otras soluciones o
alternativas. Por una parte, Kubernetes no es una PaaS (*Platform as a
Service*) tradicional. Esto se debe a que K8s no es monolítico y aunque
comparte muchas características comunes con un PaaS otras son libres,
configurables y se ajustan por el usuario.

Por otra parte, las aplicaciones no están limitadas en principio: si se
puede ejecutar en un contenedor debería funcionar correctamente en
Kubernetes. Además, Kubernetes en ningún momento despliega código fuente
o construye una aplicación. Esto se aplica directamente en los entornos
de CI/CD, en donde los requisitos y las funciones se determinan por el
equipo de trabajo.

En lo referente a servicios a nivel de aplicación, Kubernetes no ofrece
mecanismos como *middlewares*, *frameworks* de procesamiento de datos,
bases de datos, cache o sistemas de almacenamiento en clústers de forma
nativa. Dichos componentes se pueden ejecutar en K8s pero se han de
configurar mediante mecanismos externos.

Un factor muy importante es que no hay mecanismos de registro,
monitorización o alertas: existen ciertas integraciones como prueba de
concepto y mecanismos de recolección y exportación de métricas de
funcionamiento.

### ¿Cómo funciona Kubernetes? {#cómo-funciona-kubernetes .unnumbered}

Cuando se despliega a Kubernetes, se crea un clúster. Un clúster se
compone de un conjunto de máquinas (llamadas nodos) que ejecutan
aplicaciones en contenedores. Es requisito que cada clúster contenga al
menos un único nodo.

Dicho nodo aloja lo que se conoce como "*pods*", un conjunto de
componentes de la aplicación que se ejecutan en el nodo. Esto se apoya
de un "*control plane*" que gestiona los nodos y los *pods* en el
clúster. Idealmente, en un entorno de producción, este *control plane*
se ejecuta a lo largo de múltiples equipos y un clúster se despliega en
múltiples nodos, ofreciendo una alta disponibilidad y tolerancia a
fallos. Un entorno completo de Kubernetes se muestra en la figura
[20](#fig:k8s-cluster){reference-type="ref"
reference="fig:k8s-cluster"}:

![Componentes de Kubernetes
[@KubernetesComponents].[]{label="fig:k8s-cluster"}](pictures/components-of-kubernetes.png){#fig:k8s-cluster
width="\linewidth"}

### El *control plane* de Kubernetes {#el-control-plane-de-kubernetes .unnumbered}

Los componentes *control plane* permiten tomar decisiones globales en lo
referente al clúster y detectar y responder a eventos que se den en el
clúster.

De entre todos los componentes que existen, algunos importantes son:

-   `kube-apiserver` es un componente que expone la API de Kubernetes.
    Está diseñado para escalar horizontalmente desplegando más
    instancias y se pueden ejecutar múltiples instancias para balancear
    la carga del sistema.

-   `etcd` es un almacenamiento de alto rendimiento basado en
    clave--valor que se usa para almacenar los datos de los clústers.

-   `kube-scheduler` monitoriza los *pods* que se han creado sin ningún
    nodo asignado a él y planifica su ejecución y en qué nodo se
    ejecutarán. Para definirlo se tienen en cuenta factores como los
    requisitos individuales y grupales de recursos, las características
    del *software*, *hardware* y de seguridad, la localización de los
    datos, etc.

-   `kube-controller-manager` ejecuta los procesos `controller`. Estos
    controladores se definen según en donde se vayan a ejecutar:

    -   Controladores de nodos que gestionan qué sucede cuando un nodo
        se cae.

    -   Controladores de trabajo que gestionan cómo los *pods* ejecutan
        tareas.

    -   Controladores de los *endpoints* que exponen dichos *endpoints*
        a los servicios que los necesiten.

    -   Controladores de cuentas y tokens para la gestión del acceso a
        la API.

-   `cloud-controller-manager` es similar a `kube-controller-manager`
    con la diferencia de que está destinado a la gestión de los
    controladores según el proveedor *cloud* que se esté usando.

### Componentes de los nodos {#componentes-de-los-nodos .unnumbered}

Estos componentes se ejecutan en cada nodo y son el entorno de ejecución
real de Kubernetes:

-   `kubelet` es un agente que se ejecuta en cada nodo del clúster y se
    asegura de que los contenedores se estén ejecutando en un *pod*.
    Tomando los valores definidos en `PodSpecs` se asegura de que los
    contenedores descritos en esa especificación se estén ejecutando y
    no contengan fallos. Es importante tener en cuenta que `kubelet`
    solo gestiona contenedores creados dentro de Kubernetes.

-   `kube-proxy` es un proxy de red que se ejecuta en cada nodo e
    implementa parte del concepto de servicio. Este componente gestiona
    las reglas de red de los nodos y aprovecha los mecanismos del
    sistema operativo para redirigir el tráfico. En otro caso, lo hace
    él mismo.

-   *Container runtime* es la capa de ejecución de los contenedores en
    sí. Aquí aparecen tecnologías como Docker, containerd, etc.

### Ejemplo aplicación en Kubernetes {#ejemplo-aplicación-en-kubernetes .unnumbered}

Para completar esta sección, se va a exponer un ejemplo de cómo
desplegar una aplicación en Kubernetes basándose en la guía publicada en
la documentación oficial [@UseServiceAccess].

En este ejemplo se van a desplegar dos instancias de una aplicación
"Hello World", se va a crear un servicio que expone un puerto del nodo y
se accederá a la aplicación en ejecución.

*Nota: se asume que se tiene instalada la herramienta de gestión de
Kubernetes `kubectl` y un servicio de Kubernetes local, como
`minikube`.*

Lo primero será definir la aplicación de Kubernetes que queremos
desplegar. Al igual que con Docker Compose, la definición se basa en
ficheros YAML (código
[\[lst:kubernetes\]](#lst:kubernetes){reference-type="ref"
reference="lst:kubernetes"}):

``` {#lst:kubernetes style="kubernetes" caption="Configuración de una aplicación ``Hello World'' en Kubernetes." label="lst:kubernetes"}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  selector:
    matchLabels:
      run: load-balancer-example
  replicas: 2
  template:
    metadata:
      labels:
        run: load-balancer-example
    spec:
      containers:
        - name: hello-world
          image: gcr.io/google-samples/node-hello:1.0
          ports:
            - containerPort: 8080
              protocol: TCP
```

En el fichero anterior se define, por una parte, la versión de la API de
Kubernetes que se quiere usar. A continuación, el tipo de aplicación que
se quiere desplegar (clave `kind`). Puede ser: `Pod`, `DaemonSet`,
`Deployment` o `Service`. Después aparece la definición de las
especificaciones del Pod que se va a desplegar. En este caso, se define
un selector que va a ejecutar aplicaciones con una etiqueta
"`load-balancer-example`", se van a tener dos réplicas y se parte de una
plantilla que define la etiqueta y el contenedor que va a ejecutar, en
este caso una aplicación NodeJS que se expone en el puerto 8080.

Con el fichero ya definido se despliega la aplicación en el clúster:

``` {style="bash" caption=""}
kubectl apply -f hello-application.yaml
```

Esto habrá creado el despliegue (`Deployment`) y el conjunto de réplicas
que contendrá los dos pods. Para obtener información sobre el
despliegue:

``` {style="bash" caption=""}
kubectl get deployments hello-world
kubectl describe deployments hello-world
```

![Información sobre los despliegues en
Kubernetes.[]{label="fig:deployments"}](pictures/kubectl-deployments.png){#fig:deployments
width=".9\linewidth"}

A continuación, se crea un servicio que expondrá el despliegue anterior:

``` {style="bash" caption=""}
kubectl expose deployment hello-world --type=NodePort --name=example-service
kubectl describe services example-service
```

![Información sobre el servicio recién desplegado de
Kubernetes.[]{label="fig:k8s-service"}](pictures/k8s-service.png){#fig:k8s-service
width=".9\linewidth"}

La salida anterior (imagen [22](#fig:k8s-service){reference-type="ref"
reference="fig:k8s-service"}) nos indica información sobre lo que está
en ejecución, el puerto de destino dentro del contenedor y el puerto
expuesto en el valor `NodePort`. Para comprobar que la aplicación
funciona, obtenemos la dirección IP del clúster de Kubernetes (comando
`kubectl cluster-info`) y accedemos directamente desde el navegador o
desde el terminal, a la dirección `http://<node-ip>:<node-port>` (figura
[23](#fig:hello-k8s){reference-type="ref" reference="fig:hello-k8s"}):

![El clúster de Kubernetes responde a nuestra petición
web.[]{label="fig:hello-k8s"}](pictures/hello-kubernetes.png){#fig:hello-k8s
width=".5\linewidth"}

------------------------------------------------------------------------

### Docker Swarm {#docker-swarm .unnumbered}

![Logotipo de Docker Swarm
[@Swarm].[]{label="fig:docker-logo"}](pictures/swarm-logo.png){#fig:docker-logo
width=".5\linewidth"}

Docker Swarm es la solución nativa de Docker para orquestación de
contenedores. Cuando se hace una instalación de Docker automáticamente
se ha instalado el gestor Swarm para manejar motores de Docker.

Esta solución es muy interesante ya que no hace falta instalar ninguna
herramienta externa (como puede ser `kubectl`) sino que se trabaja
directamente desde Docker CLI. Durante mucho tiempo esta herramienta no
existía de forma nativa sino como un proyecto por separado, Docker
"Classic" Swarm [@DockerClassicswarm2021]. Sin embargo, tras la
evolución de otras herramientas de gestión y la falta de desarrollo de
la empresa encargada de dicho repositorio, en 2018 finalizó oficialmente
su soporte y se pasó a trabajar de forma activa en SwarmKit
[@DockerSwarmkit2021]. Esta última herramienta se integra de forma
nativa en el motor Docker desde la versión 1.12 en adelante.

Entre todas las características de Docker Swarm, algunas interesantes
son [@SwarmModeOverview2021]:

-   Gestión de clústeres integrados directamente en el motor Docker, sin
    necesidad de *software* adicional para crear o gestionar un Docker
    Swarm.

-   Diseño descentralizado: en lugar de definir quiénes son los nodos y
    sus roles en el momento del despliegue (como Kubernetes) se gestiona
    la especialización en tiempo de ejecución. Esto permite generar un
    clúster de Swarm desde una única imagen y luego decidir quién es
    quién.

-   Modelo de servicios declarativo, en donde se define el estado
    deseado de varios servicios en el *stack* que conforma la
    aplicación. Por ejemplo, una aplicación puede estar definida por un
    servidor web que se comunica con otros servicios mediante una cola
    de mensajes y una base de datos como *backend*.

-   Escalado: por cada servicio se especifican cuántas tareas se quieren
    desplegar. Cuando se hace un reescalado Docker Swarm se adapta
    automáticamente añadiendo o eliminando tareas para mantener el
    estado deseado.

-   Gestión del estado deseado: el gestor Swarm monitoriza de forma
    activa los contenedores y mantiene el estado deseado cuando suceden
    inconvenientes. Por ejemplo, si se cuenta con un servicio con 10
    réplicas y un *host* que tenía 2 falla, Docker Swarm creará dos
    nuevas réplicas para reemplazar a aquellas que ya no están,
    asignándolas a los nodos que estén disponibles.

-   Red de múltiples *host*: mediante las redes *overlay*, que se vieron
    anteriormente, varios nodos se interconectan entre sí y se comunican
    como si no hubiera red de por medio. Docker Swarm se encarga de
    distribuir las direcciones y gestionar las redes.

-   Descubrimiento de servicios: el gestor Swarm asigna un DNS único a
    cada servicio y hace balanceo de carga automático entre ellos,
    permitiendo el acceso individual a cada contenedor mediante el
    nombre DNS asignado.

-   Balanceo de carga: se definen los puertos a exponer y
    automáticamente Docker Swarm distribuye la carga entre los nodos.

-   Seguro por defecto, ya que las comunicaciones utilizan autenticación
    mútua y cifrado basados en TLS.

-   Actualizaciones contínuas: se puede realizar una actualización
    incremental de cada una de las réplicas y, si en algún momento algo
    va mal, se puede recuperar la versión anterior.

### ¿Cómo funciona Docker Swarm? {#cómo-funciona-docker-swarm .unnumbered}

La idea principal detrás de este mecanismo de gestión de contenedores es
su integración directa dentro de Docker. Esto se consigue mediante el
uso de la herramienta SwarmKit, la cual es un proyecto por separado de
Docker que se integra en el mismo e implementa la capa de orquestación
de Docker.

Por ende, un *swarm* consiste en múltiples *hosts* Docker que se
ejecutan en modo Swarm y actúan como gestores, esto es, definen la
delegación y los miembros; o como trabajadores, que ejecutan los
servicios de Swarm. Ambos roles no son excluyentes, por los que un
*host* Docker puede actuar de las dos maneras a la vez.

Al definir un Swarm se especifica el estado ideal del mismo: número de
réplicas, recursos de memoria y red disponibles, puertos expuestos, etc.
Mientras se esté ejecutando, Docker intenta mantener ese estado deseado.
Por ello, cuando un nodo ya no está activo se planifican las tareas
pendientes en otro nodo (como se vio anteriormente).

Uno de los factores diferenciales principales de Docker Swarm es que se
pueden actualizar las configuraciones de los servicios (incluidas redes
y almacenamiento) sin la necesidad de recrear el servicio:
automáticamente, aquellos contenedores con una configuración anterior
serán reemplazados por los nuevos que cumplan con la nueva
configuración. Por otra parte, que un anfitrión Docker esté en modo
Swarm no impide que se puedan ejecutar contenedores de forma estándar en
el mismo, lo cual brinda una gran potencia a este mecanismo.

Es importante recalcar que la definición de los servicios Swarm se hace
a partir de un fichero de Docker Compose: si se tiene un conjunto de
contenedores definidos en un fichero `docker-compose.yml` versión 3.0 o
superior, se puede desplegar una pila Swarm desde ese mismo fichero sin
necesidad de ninguna configuración extra.

![Arquitectura de Docker Swarm
[@IndepthExplanationSwarm].[]{label="fig:swarm-arch"}](pictures/swarm-arch.jpeg){#fig:swarm-arch
width="\linewidth"}

En la figura [25](#fig:swarm-arch){reference-type="ref"
reference="fig:swarm-arch"} se define cómo sería la arquitectura de
Docker Swarm en un entorno ya desplegado. Es importante fijarse en que
el sistema, en comparación con Kubernetes, es muy similar: hay un punto
de entrada, que en Kubernetes era el *control plane*, y a continuación
el motor de gestión de Swarm, que distribuye las tareas entre
contenedores y se encarga de gestionar y monitorizar tanto a los nodos
como a los recursos. Después, cada motor Docker tendrá su aplicación en
ejecución y ofrecerá el servicio cuando lo solicite [@SwarmModeKey2021].

### Los nodos en Swarm {#los-nodos-en-swarm .unnumbered}

Un nodo es una instancia del motor Docker que participa en el clúster.
En un mismo equipo se pueden ejecutar múltiples nodos Docker, pero en un
entorno de producción estarán distribuidos a lo largo de un conjunto de
múltiples máquinas físicas y en la nube.

Cuando se despliega una aplicación en el Swarm se envía el servicio al
nodo gestor. Dicho nodo genera unidades de trabajo (tareas) y las
reparte entre los nodos trabajadores. Por otra parte, dichos nodos
también definen la orquestación y las funciones de gestión del clúster
requeridas para mantener el estado deseado.

De esta forma, los nodos trabajadores reciben y ejecutan las tareas
recibidas por el nodo gestor. Por defecto, todos los nodos son nodos
trabajadores pero se puede configurar y especificar que un nodo en
particular sea únicamente un gestor. Cuando un nodo trabajador finaliza
su tarea, notifica al nodo gestor para que este pueda perseverar el
estado del sistema como se espera [@SwarmModeKey2021].

### Los servicios y las tareas {#los-servicios-y-las-tareas .unnumbered}

Un servicio es una definición de tarea que se ejecuta en un nodo
trabajador dentro de un clúster Swarm, definiendo así la estructura
principal de Docker Swarm y la interacción principal de un usuario con
el mismo.

Los servicios al final son imágenes Docker con un comando asociado a los
mismos, que luego se convertirán en contenedores en ejecución. En
particular, un servicio puede estar replicado y será distribuido entre
varias réplicas; o bien el servicio es global y se ejecutará en todos
los nodos Swarm [@SwarmModeKey2021].

### Balanceo de carga {#balanceo-de-carga .unnumbered}

Una de las características principales de Docker Swarm es el uso de
"Ingress" como gestor de la carga para exponer los servicios y repartir
el trabajo entre los nodos. Esto se consigue asignando manualmente un
puerto donde se quiera publicar la aplicación o bien se designará
automáticamente.

De esta forma, proveedores externos acceden directamente al puerto
expuesto y Swarm gestionará las peticiones entre los distintos
servicios, de manera que en apariencia se accede siempre al mismo nodo.
Internamente se usa un servicio DNS que se asigna automáticamente a cada
tarea y, gracias al balanceador de carga nativo que tiene, distribuye
las peticiones.

### Ejemplo de aplicación en Docker Swarm {#ejemplo-de-aplicación-en-docker-swarm .unnumbered}

Una de las grandes ventajas que presenta Docker Swarm es que utiliza la
sintaxis de Docker Compose para definir sus servicios, con algunos
añadidos no soportados por el mismo.

Para este ejemplo, se va a desplegar una instancia de GitLab CE con
hasta cuatro réplicas para operaciones de CI/CD automatizadas. El
fichero que lo define es (código
[\[lst:gitLab\]](#lst:gitLab){reference-type="ref"
reference="lst:gitLab"}):

``` {#lst:gitlab style="docker-compose" caption="\texttt{docker-compose.yml} para una instancia de GitLab y 4 \textit{runners}." label="lst:gitlab"}
version: "3.6"
services:
  gitlab:
    image: gitlab/gitlab-ee:latest
    ports:
      - "22:22"
      - "80:80"
      - "443:443"
    volumes:
      - $GITLAB_HOME/data:/var/opt/gitlab
      - $GITLAB_HOME/logs:/var/log/gitlab
      - $GITLAB_HOME/config:/etc/gitlab
    environment:
      GITLAB_OMNIBUS_CONFIG: "from_file('/omnibus_config.rb')"
    configs:
      - source: gitlab
        target: /omnibus_config.rb
    secrets:
      - gitlab_root_password
  gitlab-runner:
    image: gitlab/gitlab-runner:alpine
    deploy:
      mode: replicated
      replicas: 4
configs:
  gitlab:
    file: ./gitlab.rb
secrets:
  gitlab_root_password:
    file: ./root_password.txt
```

En el fichero anterior se puede ver que la estructura es muy similar a
la de Docker Compose. Sin embargo, aparecen algunas claves nuevas que no
existían con anterioridad:

-   `services` define los servicios que conformarán la aplicación.

-   `deploy` define el modo de despliegue (`mode`) y la cantidad de
    réplicas que se usarán (`replicas`). Si no se especifica, se usa una
    única réplica.

-   `configs` define de forma común la configuración que tendrán las
    réplicas.

-   `secrets` define contraseñas o información sensible que necesitarán
    las réplicas en tiempo de ejecución.

Aunque en este caso se haya usado un fichero `docker-compose.yml`
adaptado para Docker Swarm, se podría perfectamente haber usado el
fichero descrito en el apartado [2.4](#sec:compose){reference-type="ref"
reference="sec:compose"} en el que se desplegaba una aplicación
Wordpress con NGINX y MySQL.

Se definen los ficheros necesarios y se pasa a desplegar el servicio
(figura [26](#fig:gitlab-swarm){reference-type="ref"
reference="fig:gitlab-swarm"}):

``` {style="bash" caption=""}
docker stack deploy --compose-file docker-compose.yml gitlab-stack
```

![Despliegue del Swarm con GitLab en su
interior.[]{label="fig:gitlab-swarm"}](pictures/gitlab-swarm.png){#fig:gitlab-swarm
width=".7\linewidth"}

![image](pictures/gitlab-deployed.png){width="\linewidth"}

Líneas futuras de desarrollo e innovación
-----------------------------------------

Docker es una tecnología muy en boga hoy en día. Sin embargo, varios
problemas durante el desarrollo y la falta de actualizaciones con
características demandadas han llevado al "rey" a caerse.

Parece que en los últimos meses (a junio de 2021) se han puesto las
pilas y han retomado con fuerza el desarrollo de su motor de ejecución y
herramienta de orquestación. Uno de los problemas que se encuentran
muchas empresas a la hora de desplegar contenedores es su naturaleza
efímera y no persistente que, si bien es cierto es su gran ventaja,
muchas veces puede jugar en su contra.

Sería necesario un modelo de contenedor sostenible en el tiempo, que se
mantenga por sí mismo y que no requiera de atención por parte del
gestor. Parece ser que cada vez la tendencia tiene más hacia allí y
Docker está enfocando sus esfuerzos en escuchar a la comunidad y
mantenerse como líder.

Otro factor crítico fue la noticia de *deprecation* de Docker dentro de
Kubernetes [@DonPanicKubernetes2020]: en favor del estándar de
contenedores `containerd` las imágenes nativas de Kubernetes se
sustituyen por aquellas basadas en CRI (*Container Runtime Interface*).
Si bien esto no deja de lado a Docker ya que se sigue pudiendo ejecutar
en Kubernetes, es un golpe duro ya que las empresas están centrando sus
esfuerzos en otras tecnologías de contenedores.

Es por ello por lo que Docker está apostando en su tecnología de
orquestación, Swarm, para intentar imponerse como nuevo líder en gestión
de contenedores. Es una tarea compleja (principalmente porque Kubernetes
es el líder) pero tiene muchos factores a su favor, como la fácil
integración y la sencillez en las operaciones.