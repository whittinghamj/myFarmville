# Generated by Django 3.0.7 on 2020-07-14 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfarm', '0006_auto_20200713_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='option',
        ),
    ]