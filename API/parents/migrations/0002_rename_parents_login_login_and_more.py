# Generated by Django 4.2.2 on 2023-11-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parents_login',
            new_name='login',
        ),
        migrations.RenameModel(
            old_name='Parents_profile',
            new_name='profile',
        ),
        migrations.RenameModel(
            old_name='Parents_register',
            new_name='register',
        ),
        migrations.RenameModel(
            old_name='Parents_Report',
            new_name='Report',
        ),
    ]
