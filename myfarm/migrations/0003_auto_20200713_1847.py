# Generated by Django 3.0.7 on 2020-07-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfarm', '0002_auto_20200713_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='product',
            field=models.CharField(blank=True, default='SOME STRING', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='product_type',
            field=models.CharField(blank=True, default='SOME STRING', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, default='SOME STRING', max_length=10),
        ),
    ]