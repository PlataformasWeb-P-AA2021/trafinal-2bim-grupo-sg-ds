# Información general
Esta página muestra como cargar un proyecto de Django en Gunicorn y Nginx en un sistema operativo Ubuntu(Linux)

## Prerequisitos 
* Python 3.XX instalado
* PIP-Python
* Django
* Proyecto django ya elaborado

# Cargar aplicación en Gunicorn
## Requisitos
Se debe tener instalado gunicorn en nuestro SO, para ello se ejecutan los comandos:
> sudo apt update
> sudo apt install gunicorn

Se debe tener instalado gunicorn como instancia de python para ello ejecutamos
> pip install gunicorn)
## Desarollo
Se debe modificar la variable **ALLOWED_HOSTS**, esta se encuentra en la sub carpeta del proyecto Django, por ejemplo en este caso: *departamamentoCatastros/departamentoCatastros/settings.py*
Esta variable es una lista de los hosts permitidos, se puede incluir varias direcciones para levantar el servidor, inlcuida la dirrecion IP de nuestro disopositivo, en este caso solo usaremos el servidor por defecto y el servidor 0.0.0.0, quedando de esta forma.
> ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]  

Ahora debemos añadir el directorio de los archivos estaticos a las urls del proyecto, para ello en la ruta *departamamentoCatastros/departamentoCatastros/urls.py* importamos de django dicha funcionalidad desde django con el comando
> from django.contrib.staticfiles.urls import staticfiles_urlpatterns

Y añadimos el metodo a la lista de *urlpatterns* directamente o al finalizar la variable con 
>  urlpatterns += staticfiles_urlpatterns()

Ahora volvemos al directorio principal y desde la consola ejecutamos para recolectar todo el contenido estatico en una carpeta
> python manage.py collectstatic

Finalmente desde ese directorio podemos ejecutar el comando para levantar el servidor en uno de los hosts que añadimos al *settings.py* anteriormente y en este caso la subcarpeta del proyecto se llama *departamentoCatastros* es por ello que el comando queda de esta forma
> gunicorn --bind 0.0.0.0:8000 departamentoCatastros.wsgi


# Cargar aplicación en Ngnix
## Requisitos
Antes de instalar Nginx, actualice las listas de paquetes del servidor
``` 
sudo apt update    
```
Luego se instala Nginx ejecutando el comando
``` 
sudo apt install nginx
```
Con Nginx instalado correctamente, se puede iniciar y verificar en que estado esta ejecutando el comando
``` 
sudo systemctl start nginx
sudo systemctl status nginx
```

## Enlazamiento entre el servidor Gunicorn y Nginx

1) Agregar un servicio en el sistema operativo; mismo que será encargado de levantar el proyecto de django mediante gunicorn. Luego el servicio será usado por nginx.

2) En el directorio **/etc/systemd/system/** agregar un archivo con la siguiente extensión y estructura. Se debe usar **sudo** para acceder y crear el archivo.
* Nombre del archivo **departamentoCatastros.service** (En el archivo agregar la siguiente información).

```
[Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=davisalex22
# el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory=/home/davisalex22/trafinal-2bim-grupo-sg-ds/proyecto-django/departamentoCatastros

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=/usr/bin/python3.6"

# Detallar el comando para iniciar el servicio
ExecStart=/usr/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 departamentoCatastros.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; departamentoCatastros el nombre del proye>
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor d>
WantedBy=multi-user.target
```
3) Iniciar y habilitar el proceso a través de los siguiente comandos:
```
sudo systemctl start departamentoCatastros
sudo systemctl enable departamentoCatastros
```
4) Verificar que todo esté en orden con el servicio, usar el comando:
```
sudo systemctl status departamentoCatastros
```

5) Este paso es importante, se debe verificar que el archivo .sock esté creado en el directorio del proyecto.
Ejemplo:
![](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo-sg-ds/blob/main/publicacion/img/directorio.PNG) 


## Configuración servidor Nginx
1) Se debe crear un archivo en el directorio **etc/nginx/sites-available**. AL ingresar se debe requiere permisos de administrador (sudo) y se usa el siguiente comando.

```
sudo touch /etc/nginx/sites-available/departamentoCatastros
```
2) Ahora nos debemos dirigir al directorio **etc/nginx/sites-**
3) En el archivo se puede usar la siguiente estructura
```
server {
    listen 81;
    server_name localhost;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/davisalex22/trafinal-2bim-grupo-sg-ds/proyecto-django/depart>
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/davisalex22/trafinal-2bim-grupo-sg-ds/proy>
    }
}
```
3) Iniciar un enlace simbólico del archivo creado en el directorio sites-available.

```
sudo ln -s /etc/nginx/sites-available/departamentoCatastros /etc/nginx/sites-enabled
```
4) Iniciar o reiniciar el servicio de nginx.

```
sudo service nginx start
sudo service nginx status
```
![](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo-sg-ds/blob/main/publicacion/img/funcionamientoNginx.PNG) 

5) En un navegador con las siguientes direcciones se debe deplegar el proyecto a través de nginx:
* http://localhost:81
* http://0.0.0.0:81
* http://127.0.0.0:81
![](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo-sg-ds/blob/main/publicacion/img/paginaDesplegada.PNG) 
