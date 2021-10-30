import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              'O nome de usuário só pode conter letras, digitos ou os '
                                              'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True,)
    first_name = models.CharField('Nome', max_length=150, blank=False)
    last_name = models.CharField('Sobrenome', max_length=150, blank=True)
    is_active = models.BooleanField('Ativo', blank=True, default=True)
    is_staff = models.BooleanField('Staff', blank=True, default=False)
    created_at = models.DateTimeField(
        'Data de Entrada', auto_now_add=True)  # Data de criação
    last_login = models.DateTimeField(
        'Último Login', auto_now=True)  # Ultimo login
    updated_at = models.DateTimeField(
        'Data de Modificação', auto_now=True)  # Data de modificação
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


def usuario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.username)


signals.pre_save.connect(usuario_pre_save, sender=User)


class PasswordReset(models.Model):
    # quando tem uma relação de 1 para muitos, a chave fica no filho
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário',
        related_name='resets',
    )
    
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return f'{self.user} - {self.created_at}'

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']
        
# class Endereco(models.Model):
#     ESTADO_CHOICES = (
#         ('AC', 'Acre'),
#         ('AL', 'Alagoas'),
#         ('AP', 'Amapá'),
#         ('AM', 'Amazonas'),
#         ('BA', 'Bahia'),
#         ('CE', 'Ceará'),
#         ('DF', 'Distrito Federal'),
#         ('ES', 'Espírito Santo'),
#         ('GO', 'Goiás'),
#         ('MA', 'Maranhão'),
#         ('MT', 'Mato Grosso'),
#         ('MS', 'Mato Grosso do Sul'),
#         ('MG', 'Minas Gerais'),
#         ('PA', 'Pará'),
#         ('PB', 'Paraíba'),
#         ('PR', 'Paraná'),
#         ('PE', 'Pernambuco'),
#         ('PI', 'Piauí'),
#         ('RJ', 'Rio de Janeiro'),
#         ('RS', 'Rio Grande do Sul'),
#         ('RO', 'Rondônia'),
#         ('RR', 'Roraima'),
#         ('SC', 'Santa Catarina'),
#         ('SP', 'São Paulo'),
#         ('SE', 'Sergipe'),
#         ('TO', 'Tocantins'),
#     )

#     street = models.CharField(max_length=200, null=False, blank=False)
#     number = models.IntegerField(null=False, blank=False)
#     complement = models.CharField(max_length=200, null=False, blank=False)
#     district = models.CharField(max_length=50, null=False, blank=False)
#     city = models.CharField(max_length=100, null=False, blank=False)
#     country = models.CharField(max_length=50, null=False, blank=False)


# class Profile(models.Model):
#     SEXO_CHOICES = (
#         ('F', 'Feminino'),
#         ('M', 'Masculino'),
#         ('N', 'Neuma das Opções'),
#     )

#     full_name = models.CharField('Nome completo', max_length=100, blank=False)
#     cpf = models.CharField('CPF', max_length=11)
#     rg = models.CharField('RG', max_length=7)
#     birth_date = models.DateTimeField('Data de nascimento')
