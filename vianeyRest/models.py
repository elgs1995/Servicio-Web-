from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=100,blank=True,default='')
    contrasenaUsuario = models.CharField(max_length=100,blank=True,default='')
    class Meta:
        ordering = ('nombreUsuario',)


class Persona(models.Model):
    nombrePersona =  models.CharField(max_length=100,blank=True,default='')
    apeliidoPPersona = models.CharField(max_length=100,blank=True,default='')
    apellidoMPersona =  models.CharField(max_length=100,blank=True,default='')
    licenciaturaPersona = models.CharField(max_length=100,blank=True,default='')
    semestrePersona = models.CharField(max_length=100,blank=True,default='')

    class Meta:
        ordering = ('nombrePersona',)


class Materia(models.Model):
    nombreMateria = models.CharField(max_length=100,blank=True,default='')
    primerParcialMateria = models.CharField(max_length=100,blank=True,default='')
    segundoParcialMateria = models.CharField(max_length=100,blank=True,default='')
    tercerParcialMateria = models.CharField(max_length=100,blank=True,default='')
    ordinarioMateria = models.CharField(max_length=100,blank=True,default='')
    class Meta:
        ordering = ('nombreMateria',)
