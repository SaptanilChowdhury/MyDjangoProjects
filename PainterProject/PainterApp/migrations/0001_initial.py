# Generated by Django 4.0.4 on 2022-05-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('painting_name', models.CharField(max_length=100)),
                ('painter_name', models.CharField(max_length=50)),
            ],
        ),
    ]
