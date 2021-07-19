from django.db import models

# Create your models here.

class Barrio(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (
                self.nombre,
                self.siglas)
        
class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (
                self.nombre,
                self.apellido,
                self.cedula,
                self.correo)        

class Casa(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="casas")
    direccion = models.CharField(max_length=60)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name="barriosCasa")
    valorBien = models.DecimalField(max_digits=10, decimal_places=2)
    colorInmueble = models.CharField(max_length=30)
    numCuartos = models.IntegerField()
    numPisos = models.IntegerField()

    def __str__(self):
        return "%s %s %s %.2f %s %d %d" % (
                self.propietario,
                self.direccion,
                self.barrio,
                self.valorBien,
                self.colorInmueble,
                self.numCuartos,
                self.numPisos)
        
class Departamento(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="departamentos")
    direccion = models.CharField(max_length=60)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name="barriosDepartamento")
    valorBien = models.DecimalField(max_digits=10, decimal_places=2)
    numCuartos = models.IntegerField()
    valorMantenimiento = models.DecimalField(max_digits=10, decimal_places=2)   

    def __str__(self):
        return "%s %s %s %.2f %d %.2f" % (
                self.propietario,
                self.dirrecion,
                self.barrio,
                self.valorBien,
                self.numCuartos,
                self.valorMantenimiento)

