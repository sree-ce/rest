# Generated by Django 4.0.2 on 2022-02-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userdetails_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile_number',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]
