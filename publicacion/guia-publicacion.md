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

<<<<<<< HEAD
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
Se debe instalar nginx de la siguiente forma
```
=======
## Pasos Ngnix
### Instalación Ngnix

>>>>>>> de8c1b64aada4f0b6799ca7955e334eb90906710
1. Antes de instalar Nginx, actualice las listas de paquetes de su servidor.
``` 
sudo apt update    
```
2. Luego instale Nginx ejecutando el comando:
``` 
sudo apt install nginx
```
3. Con Nginx instalado correctamente, puede iniciarlo y verificarlo ejecutando:
``` 
sudo systemctl start nginx
sudo systemctl status nginx
```
4. Para verificar la versión de Nginx, ejecute:
``` 
sudo dpkg -l nginx
```
5. Comience habilitando el firewall en Ubuntu 20.04.
``` 
sudo ufw enable
```
6. Por ahora, dado que no estamos en un servidor encriptado, solo permitiremos el perfil HTTP de Nginx que permitirá el tráfico en el puerto 80.
``` 
sudo ufw allow 'Nginx HTTP'
```
7. Luego, vuelva a cargar el firewall para que los cambios persistan.
``` 
sudo ufw reload
```
8. Ahora verifique el estado del firewall para verificar los perfiles que se han permitido.
``` 
sudo ufw status
```
### Vincular Gunicorn con Ngnix
1) Crear un archivo **sites-available** de nginx; la ruta de acceso es: /etc/nginx/sites-available/. Se debe ingresar con permisos de administrador (sudo).

```
sudo touch /etc/nginx/sites-available/departamentoCatastros
```
2) En el archivo se puede usar la siguiente estructura
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
5) En un navegador con las siguientes direcciones se debe deplegar el proyecto a través de nginx:
* http://localhost:81
* http://0.0.0.0:81
* http://127.0.0.0:81
