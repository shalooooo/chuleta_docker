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
		RUN apt-get update && apt-get install figlet -y
	# construir un contenedor a partir de un docker file
	docker build -t NOMBRE_IMAGEN:VERSION
	# muestra comandos ejecutados en la imagen especificada
	docker image history ID_IMAGEN
	# corre un contenedor con nginx version 1.15.7 y lo deja corriendo como daemon
	docker run -d nginx:1.15.7
	# correr un comando dentro de un contenedor que ya esta corriendo
	docker exec -it $CONTEINER_ID bash
	# correr contenedor persistente nginx especificando version y ademas copia index.html a directorio nginx/html dentro del contenedor
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

	
	

### 