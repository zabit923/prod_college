# Generated by Django 4.2.5 on 2023-10-20 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_user_course2'),
        ('lessons', '0011_remove_schedules_name2_schedules_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpd',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.course'),
        ),
    ]
