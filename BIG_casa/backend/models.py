from django.db import models


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    cpf = models.CharField(max_length=9, unique=True)
    adress = models.CharField(max_length=100)
    annual_leave = models.FloatField()
    day_off = models.DateField()
    extra_time = models.DateField()


class Gerente(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    cpf = models.CharField(max_length=9, unique=True)
    adress = models.CharField(max_length=100)
