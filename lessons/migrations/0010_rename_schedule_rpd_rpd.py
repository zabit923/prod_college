# Generated by Django 4.2.5 on 2023-10-20 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_rpd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rpd',
            old_name='schedule',
            new_name='rpd',
        ),
    ]