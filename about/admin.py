from django.contrib import admin
from .models import Factor, SubFactor, Person, TestResult
# Register your models here.
admin.site.register(Factor)
admin.site.register(SubFactor)
admin.site.register(Person)
admin.site.register(TestResult)
