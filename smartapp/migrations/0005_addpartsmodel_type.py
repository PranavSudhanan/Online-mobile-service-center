# Generated by Django 4.1.6 on 2023-02-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0004_addpartsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpartsmodel',
            name='type',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
