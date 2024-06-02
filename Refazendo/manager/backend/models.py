from django.db import models
from django.contrib.auth.models import User
import re


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
    def validate_cpf(self):
        # regex para cpf
        if self.cpf == re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}"):
            return True
        else:
            return False
    
    def save(self, *args, **kwargs):
        # chama a função de validação de cpf
        self.validate_cpf()
        super(Usuario, self).save(*args, **kwargs)
    
