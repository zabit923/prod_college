# Generated by Django 4.2.5 on 2023-11-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_personalteacherlinks_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalteacherlinks',
            name='link',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='personalteacherlinks',
            name='title',
            field=models.CharField(),
        ),
    ]
