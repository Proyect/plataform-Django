from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    birthdate = models.DateField()
    email = models.EmailField()
    address = models.CharField()  