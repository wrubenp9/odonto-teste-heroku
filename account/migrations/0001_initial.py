# Generated by Django 3.2.8 on 2021-10-28 14:18

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('first_name', models.CharField(max_length=150, verbose_name='Nome')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Sobrenome')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Ativo')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='Staff')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Último Login')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Modificação')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(blank=True, default=False, verbose_name='Confirmado?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resets', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Nova Senha',
                'verbose_name_plural': 'Novas Senhas',
                'ordering': ['-created_at'],
            },
        ),
    ]