# Generated by Django 5.0.8 on 2024-09-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_servicetransactions_day_servicetransactions_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetransactions',
            name='transactionID',
            field=models.CharField(max_length=46, unique=True),
        ),
    ]
