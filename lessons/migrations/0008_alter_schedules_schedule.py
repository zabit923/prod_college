# Generated by Django 4.2.5 on 2023-10-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_alter_schedules_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule',
            field=models.FileField(max_length=300, upload_to='', verbose_name='PDF ссылка на расписание'),
        ),
    ]
