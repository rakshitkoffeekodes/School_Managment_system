# Generated by Django 4.2.2 on 2023-11-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Super_admin', '0003_super_admin_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_admin_login',
            name='login_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
