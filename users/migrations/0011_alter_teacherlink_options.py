# Generated by Django 4.2.5 on 2023-10-09 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_course_options_alter_facult_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacherlink',
            options={'verbose_name': 'Ссылка учителя', 'verbose_name_plural': 'Ссылки учителя'},
        ),
    ]