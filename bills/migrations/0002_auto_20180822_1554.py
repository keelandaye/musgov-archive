# Generated by Django 2.0.7 on 2018-08-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date_first_posted',
            field=models.DateField(),
        ),
    ]
