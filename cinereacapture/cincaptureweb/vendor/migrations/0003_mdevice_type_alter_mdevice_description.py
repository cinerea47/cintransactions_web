# Generated by Django 5.0.8 on 2024-08-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_remove_servicevendor_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdevice',
            name='type',
            field=models.CharField(choices=[('active', 'Mobile Phone'), ('suspended', 'Personal Computer'), ('suspended', 'POS Terminal')], default='active', max_length=46),
        ),
        migrations.AlterField(
            model_name='mdevice',
            name='description',
            field=models.CharField(max_length=92),
        ),
    ]
