from django.db import models

# Create your models here.

class adltest(models.Model):
    valor1 = models.IntegerField()
    campo1 = models.CharField(max_length=100)



