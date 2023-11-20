from django.db import models

class Factor(models.Model):
    name = models.CharField(max_length=100)  # 'nombre' changed to 'name'
    weighting = models.IntegerField()  # 'ponderacion' changed to 'weighting'

    def __str__(self):
        return self.name

class SubFactor(models.Model):
    factor = models.ForeignKey(Factor, related_name='subfactors', on_delete=models.CASCADE)  # 'subfactores' changed to 'subfactors'
    name = models.CharField(max_length=100)  # 'nombre' changed to 'name'
    weighting = models.IntegerField()  # 'ponderacion' changed to 'weighting'

    def __str__(self):
        return f"{self.factor.name} - {self.name}"  # 'nombre' changed to 'name'

class Person(models.Model):  # 'Persona' changed to 'Person'
    # Basic fields
    name = models.CharField(max_length=100, default='Default value')  # 'nombre' changed to 'name', 'Valor por defecto' changed to 'Default value'
    age = models.IntegerField()  # 'edad' changed to 'age'
    gender = models.CharField(max_length=10)  # 'sexo' changed to 'gender'
    neighborhood = models.CharField(max_length=100)  # 'colonia' changed to 'neighborhood'
    city = models.CharField(max_length=100)  # 'ciudad' remains the same
    education = models.CharField(max_length=200)  # 'estudios' changed to 'education'
    job_position = models.CharField(max_length=100)  # 'puesto_laboral' changed to 'job_position'
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)  # 'ingreso_mensual' changed to 'monthly_income'
    marital_status = models.CharField(max_length=50)  # 'estado_civil' changed to 'marital_status'
    monthly_expenditure = models.DecimalField(max_digits=10, decimal_places=2)  # 'gasto_mensual' changed to 'monthly_expenditure'

    # Fields for capabilities, skills, and competencies
    capabilities = models.TextField()  # 'capacidades' changed to 'capabilities'
    skills = models.TextField()  # 'habilidades' changed to 'skills'
    competencies = models.TextField()  # 'competencias' changed to 'competencies'

    def __str__(self):
        return f"{self.name} - {self.job_position}"  # 'nombre' and 'puesto_laboral' changed to 'name' and 'job_position'

def default_person_function():
    # Return the ID of an existing Person, or None if no Person exists
    person = Person.objects.first()
    if person:
        return person.id
    return None

class TestResult(models.Model):  # 'ResultadoTest' changed to 'TestResult'
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=default_person_function)
    subfactor = models.ForeignKey(SubFactor, on_delete=models.CASCADE)
    points = models.IntegerField()  # 'puntos' changed to 'points'

    def __str__(self):
        return f"{self.person} - {self.subfactor} - Points: {self.points}"  # 'Puntos' changed to 'Points'
