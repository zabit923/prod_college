# Generated by Django 4.2.5 on 2023-10-22 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_rpd_facult_alter_schedules_facult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedules',
            name='facult',
        ),
    ]