from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Criar gerente dando permissão de super usuário:
class Gerente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        # chama a função de validação de cpf
        self.user.is_superuser = True
        self.user.is_staff = True
        super(Gerente, self).save(*args, **kwargs)