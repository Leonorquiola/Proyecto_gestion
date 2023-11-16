# Generated by Django 4.2.6 on 2023-11-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0002_alter_movimiento_montomovimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentabancaria',
            name='estado',
            field=models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('BLOQUEADO', 'BLOQUEADO')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='montoMovimiento',
            field=models.FloatField(),
        ),
    ]
