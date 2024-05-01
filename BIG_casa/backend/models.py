from django.db import models


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    cpf = models.CharField(max_length=9, unique=True)
    adress = models.CharField(max_length=100)

    class Meta:
        app_label = 'BIG_casa'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.phone}"
    

class Gerente(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    cpf = models.CharField(max_length=9, unique=True)
    adress = models.CharField(max_length=100)

    class Meta:
        app_label = 'BIG_casa'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.phone}"
    