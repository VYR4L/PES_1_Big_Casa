from django.db import models


class Usuario(models.Models):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    cpf = models.CharField(max_length=9)
    adress = models.CharField(max_length=100)
    is_super_user = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.phone}'