# Generated by Django 3.1.6 on 2021-02-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbookapp', '0004_auto_20210221_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='unit',
            field=models.CharField(max_length=60, null=True),
        ),
    ]