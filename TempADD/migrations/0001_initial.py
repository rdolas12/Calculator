# Generated by Django 4.0.4 on 2022-05-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
                ('output', models.IntegerField()),
            ],
        ),
    ]