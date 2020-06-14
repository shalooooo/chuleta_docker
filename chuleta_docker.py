### CentOS
	# Validacion de paquetes instalados
	rpm -aq | grep paquete
	yum list installed | grep wget
	## Servicios
		# informacion del servicio 
		systemctl help servicio
		# consultar dependencias del servicio o una unidad
		systemctl list-dependencies servicio
		# servicios que se usarán después de iniciar un servicio
		systemctl list-dependencies --before cron
		# iniciar servicio
		systemctl start servicio
		# status de un servicio
		systemctl status servicio
		# reiniciar servicio
		systemctl restart servicio
		# recargar configuracion de un servicio sin reiniciarlo
		systemctl reload servicio
		# detener un servicio
		systemctl stop servicio
		# arranque de forma automática al iniciar el ordenador
		systemctl enable servicio
		# que al arrancar el ordenador no se cargue un servicio
		systemctl disable servicio
		# enmascarar un servicio: que no se pueda iniciar manualmente ni automáticamente después de iniciar la sesión
		systemctl mask servicio
		# desenmascarar un servicio
		systemctl unmask servicio

### Docker
	# Instalacion docker
	curl -fsSL https://get.docker.com -o get.docker.sh
	sh get-docker.sh
	yum install -y -q yum-utils
	#yum -y install docker-engine
	yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
	___
	sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
	dnf list docker-ce --showduplicates | sort -r
	sudo dnf install docker-ce-<version>
	sudo dnf install docker-ce-3:18.09.1-3.el7
	# Docker
	docker -v
	# Desactivar firewall
	sudo systemctl disable firewalld
	sudo systemctl enable --now docker
	sudo usermod -aG docker $USER
	# muestra contenedores corriendo 
	docker ps
	# corre el contenedor hello-world
	docker run hello-world
	# descargar imagen del registro publico de docker
	docker pull alpine
	# descarga imagen especificando version
	docker pull alpine:3.7
	# correr contenedor ejecutando un comando dentro de el
	docker run alpine ls -l
	# correr contenedor con terminal interactiva
	docker run -it alpine sh
	# correr un comando dentro de un contenedor que ya se encuentre corriendo
	docker exec -it $ID_CONTENEDOR sh
	# correr un contenedor ubuntu y obtener un shell
	docker run -ti ubuntu /bin/bash
	# visualizar todos los contenedores incluyendo los muertos
	docker ps -a
	# crear imagen a partir de un contenedor u otras imagenes
	docker commit $ID_CONTENEDOR
	# listar imagenes de contenedores docker
	docker image ls
	# taguear imagen docker
	docker image tag $ID_IMAGEN nombre_imagen
	# taguear imagen docker con version
	docker image tag $ID_IMAGEN nombre_imagen:version
	# Docker file
	vim Dockerfile
		FROM ubuntu 
		# es recmendable instalar todo lo necesario en una misma linea por temas de cache
		# --no-install-recommends sirve para no instalar los paquetes recomendados por apt
		RUN apt-get update && apt-get install --no-install-recommends figlet -y / openjdk-8-jdk vim ssh
		# NOTA: es recomandable no instalar ssh ni vim ni ningun paquete que no sea productivo
		# ssh deja una brecha de seguridad al permitir conexiones externas
		# vim ocupa espacio innecesario en el contenedor productivo, cuando la edicion de texto deberia realizarce por medios externos
		
		# copiar archivo local dentro del contenedor, siempre es mejor dejar el copiado del codigo de la aplicacion al final del Dockerfile por temas de cache
		# tambien es recomandable copiar explucisvamente los archivos de la aplicacion, sacar todo aquello que no influya en la ejecucion de la aplicacion
		COPY /ruta_local/archivo /ruta_contenedor		
		# trae archivos de rutas remotas (sustituye wget), es recomandable solo usarlo para rutas remotas, para rutas locales use COPY
		ADD ejemplo.com/archivo /ruta_contenedor
		
		# ejecuta aplicacion java
		CMD ["java", "-jar", "/ruta_app/app.jar"]
		
	# construir un contenedor a partir de un docker file
	docker build -t NOMBRE_IMAGEN:VERSION
	# muestra comandos ejecutados en la imagen especificada
	docker image history ID_IMAGEN
	# corre un contenedor con nginx version 1.15.7 y lo deja corriendo como daemon
	docker run -d nginx:1.15.7
	# correr un comando dentro de un contenedor que ya esta corriendo
	docker exec -it $CONTEINER_ID bash
	# correr contenedor persistente nginx especificando version y ademas copia index.html a directorio nginx/html dentro del contenedor, el ':ro' significa read only para que no se pueda reescribir el archivo
	docker run -v ~/docker/index.html:/usr/share/nginx/html/index.html:ro -d nginx:1.15.7
	# correr contenedor persistente nginx especificando version y ademas copia index.html a directorio nginx/html dentro del contenedor, ademas apunta el puerto 8080 local al puerto 80 del contenedor
	docker run -v ~/docker/index.html:/usr/share/nginx/html/index.html:ro -p 8080:80 -d nginx:1.15.7
	# corre un contenedor mysql 8.0.13 y añade la variable de entorno MYSQL_ROOT_PASSWORD especificando la clave del usuario root del servidor
	docker run -e MYSQL_ROOT_PASSWORD=miclave -d mysql:8.0.13
	# corre un contenedor igual al anterior, ademas mapea un volumen desde la carpeta /mysql-data local hasta la carpeta /var/lib/mysql del contenedor
	docker run -e MYSQL_ROOT_PASSWORD=miclave -v ~/mysql-data:/var/lib/mysql -d mysql:8.0.13
	# modificar archivo docker-compose.yaml
	vi docker-compose.yaml
	# leer el archivo docker-compose.yaml y ejecutar comandos para crear contenedores y ambiente especificado en el archivo, ademas dejarlo como daemon
	docker-compose up -d
	# archivo docker-compose.yaml
	version: '3.1'
	services:
	  wordpress:
	    image: wordpress:php7.2-apache
	    restart: always # para que se inicie al iniciar la maquina, en casos de reinicios
	    ports:
	      - 8080:80
	    environment:
	      WORDPRESS_DB_HOST: mysql
	      WORDPRESS_DB_USER: root
	      WORDPRESS_DB_PASSWORD: root
	      WORDPRESS_DB_NAME: wordpress
	    links:
	      - mysql:mysql

	  mysql:
	    image: mysql:8.0.13
	    restart: unless-stopped # si se detuvo el servicio manualmente no se vuelve a iniciar en un reinicio
	    restart: on-failure:10 # si se sobrepasan los 10 errores e intentos de iniciar el contenedor se paran los intentos por iniciarlo
	    command: --default-authentication-plugin=mysql_native_password
	    environment:
	      MYSQL_DATABASE: wordpress
	      MYSQL_ROOT_PASSWORD: root
	    volumes:
	      - ~/docker/mysql-data:/var/lib/mysql
	
	

	# bajar imagen de jenkins con alipine linux
	docker pull jenkins:2.60.3-alpine
	# bajar imagen de gitlab community edition 
	docker pull gitlab/gitlab-ce
	# bajar imagen de rundeck
	docker pull rundeck/rundeck:3.1.2

	
	
	# estadisticas de los contenedores corriendo
	docker stats
	
	# borra todos lo contenedores parados, incluyendo los volumenes parados, las redes e imagenes que no esten en uso por al menos un contenedor
	docker system prune
	
	# inspeccionar un contenedor para obtener sus datos como variables de entorno, ips, volumenes, etc.
	docker inspect {id|nombre_contenedor}
	
	# copiar un archivo desde el entorno actual hacia dentro del contenedor
	docker cp {nombre_archivo} {id|nombre_contenedor}:/ruta/donde/quieres/que/se/pegue/el/archivo
	
	# visualizar las ultimas 10 lineas del log del contenedor
	docker logs --tail=10 {id|nombre_contenedor}
	
	# visualizar las ultimas 50 lineas del log junto con el timestamp de la escritura de esa linea de log
	docker logs --tail=50 -t {id|nombre_contenedor}
	
	# PARA LOS CONTENEDORES QUE NO INICIAN
	# ejemplo iniciando un contenedor nginx para que nos de una terminal en vez de iniciar el servicio
	# sirve para depurar los errores desde dentro del contenedor, si no tiene bash se puede usar 'sh'
	docker run -it -v /ruta_local:/ruta_contenedor --entrypoint=bash nginx
### 