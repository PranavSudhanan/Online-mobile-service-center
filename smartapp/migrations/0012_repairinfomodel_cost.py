# Generated by Django 4.1.6 on 2023-02-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0011_recyclemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairinfomodel',
            name='cost',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
