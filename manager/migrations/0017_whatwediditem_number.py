# Generated by Django 4.2.3 on 2023-09-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_welcomesection_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatwediditem',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
