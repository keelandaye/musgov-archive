# Generated by Django 2.0.7 on 2018-08-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_bill_bill_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='logo_url',
            field=models.URLField(default='https://einfon.com/wp-content/uploads/2017/05/Flag-Of-USA.jpg'),
        ),
    ]
