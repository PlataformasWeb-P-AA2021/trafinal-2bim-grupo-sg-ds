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
```
1. Antes de instalar Nginx, actualice las listas de paquetes de su servidor.
    sudo apt update
2. Luego instale Nginx ejecutando el comando:
    sudo apt install nginx
3. Con Nginx instalado correctamente, puede iniciarlo y verificarlo ejecutando:
    sudo systemctl start nginx
    sudo systemctl status nginx
4. Para verificar la versión de Nginx, ejecute:
    sudo dpkg -l nginx
5. Comience habilitando el firewall en Ubuntu 20.04.
    sudo ufw enable
6. Por ahora, dado que no estamos en un servidor encriptado, solo permitiremos el perfil HTTP de Nginx que permitirá el tráfico en el puerto 80.
    sudo ufw allow 'Nginx HTTP'
7. Luego, vuelva a cargar el firewall para que los cambios persistan.
    sudo ufw reload
8. Ahora verifique el estado del firewall para verificar los perfiles que se han permitido.
    sudo ufw status
```

