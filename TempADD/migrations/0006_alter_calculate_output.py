# Generated by Django 4.0.4 on 2022-05-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TempADD', '0005_rename_field_sum_calculate_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculate',
            name='output',
            field=models.BigIntegerField(),
        ),
    ]
