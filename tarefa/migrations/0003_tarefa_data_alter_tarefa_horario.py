# Generated by Django 4.1.3 on 2022-11-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0002_alter_tarefa_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='horario',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
