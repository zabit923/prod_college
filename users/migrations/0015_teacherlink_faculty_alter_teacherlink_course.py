# Generated by Django 4.2.5 on 2023-10-22 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_teacherlink_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherlink',
            name='faculty',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.facult'),
        ),
        migrations.AlterField(
            model_name='teacherlink',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.course'),
        ),
    ]