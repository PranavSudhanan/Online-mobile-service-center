# Generated by Django 4.1.6 on 2023-02-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0006_partsmodel_delete_addpartsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='repairmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=70)),
                ('complaint', models.CharField(max_length=150)),
                ('warranty', models.CharField(max_length=40)),
                ('fname', models.CharField(max_length=70)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
