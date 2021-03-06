# Generated by Django 3.0.4 on 2020-04-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='born',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Urodziny'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Adres e-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('M', 'Mężczyzna'), ('F', 'Kobieta'), ('U', 'Nieokreślono')], default=None, max_length=1, null=True, verbose_name='Płeć'),
        ),
    ]
