# Generated by Django 4.2.5 on 2023-09-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]