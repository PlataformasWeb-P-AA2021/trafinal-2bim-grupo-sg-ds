# Trabajo Final - Segundo Bimestre

## Problemática
En el municipio de un cantón del Ecuador se necesita generar un pequeño sistema para el departamento de catastros. 

## Tecnologías usadas

- Python
- Flask
- Django-Rest-Framework
- Nginx
- Gunicorn
- Mysql

## Pasos Ngnix
### Instalación Ngnix

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
