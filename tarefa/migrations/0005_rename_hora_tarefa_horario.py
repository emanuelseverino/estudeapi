# Generated by Django 4.1.3 on 2022-11-29 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0004_rename_horario_tarefa_hora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='hora',
            new_name='horario',
        ),
    ]
