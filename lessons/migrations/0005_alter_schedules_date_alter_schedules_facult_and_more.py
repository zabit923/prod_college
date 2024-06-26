# Generated by Django 4.2.5 on 2023-10-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_schedules_alter_lecture_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='date',
            field=models.CharField(max_length=150, verbose_name='Дата действия расписания'),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='facult',
            field=models.CharField(max_length=150, verbose_name='Название факультета'),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='schedule',
            field=models.CharField(max_length=300, verbose_name='PDF ссылка на расписание'),
        ),
    ]
