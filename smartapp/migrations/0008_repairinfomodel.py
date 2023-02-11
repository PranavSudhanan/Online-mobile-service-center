# Generated by Django 4.1.6 on 2023-02-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0007_repairmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='repairinfomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=70)),
                ('complaint', models.CharField(max_length=150)),
                ('warranty', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=70)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
