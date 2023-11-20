from django.db import models

class Factor(models.Model):
    nombre = models.CharField(max_length=100)
    ponderacion = models.IntegerField()

    def __str__(self):
        return self.nombre

class SubFactor(models.Model):
    factor = models.ForeignKey(Factor, related_name='subfactores', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ponderacion = models.IntegerField()

    def __str__(self):
        return f"{self.factor.nombre} - {self.nombre}"


class Persona(models.Model):
    # Campos básicos
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    colonia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estudios = models.CharField(max_length=200)
    puesto_laboral = models.CharField(max_length=100)
    ingreso = models.DecimalField(max_digits=10, decimal_places=2)
    estado_civil = models.CharField(max_length=50)

    # Campos para capacidades, habilidades y competencias
    capacidades = models.TextField()
    habilidades = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.puesto_laboral}"

class ResultadoTest(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    subfactor = models.ForeignKey(SubFactor, on_delete=models.CASCADE)
    puntos = models.IntegerField()

    def __str__(self):
        return f"{self.persona} - {self.subfactor} - Puntos: {self.puntos}"
