# Generated by Django 5.0.8 on 2024-08-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_alter_servicetransactions_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetransactions',
            name='day',
            field=models.CharField(max_length=46, null=True),
        ),
        migrations.AddField(
            model_name='servicetransactions',
            name='time',
            field=models.CharField(max_length=46, null=True),
        ),
    ]
