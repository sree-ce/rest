# Generated by Django 4.0.2 on 2022-03-01 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userdetails_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
    ]