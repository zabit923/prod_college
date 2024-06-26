# Generated by Django 4.2.5 on 2023-10-05 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_course_facult_teacherlink_course_faculty_user_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='facult',
            options={'verbose_name': 'Факультет', 'verbose_name_plural': 'Факультеты'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='faculty',
            new_name='facult',
        ),
    ]
