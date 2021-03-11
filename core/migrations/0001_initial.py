# Generated by Django 3.1.7 on 2021-03-09 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20, verbose_name='número de telefone')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('endereco', models.CharField(blank=True, max_length=250, verbose_name='endereço')),
                ('bairro', models.CharField(blank=True, max_length=100)),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('cidade', models.CharField(blank=True, max_length=150)),
                ('data_add', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]