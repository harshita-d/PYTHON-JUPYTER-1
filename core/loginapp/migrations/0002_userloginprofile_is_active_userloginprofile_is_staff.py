# Generated by Django 5.0.4 on 2024-06-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userloginprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userloginprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
