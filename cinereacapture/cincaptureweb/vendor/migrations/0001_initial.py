# Generated by Django 5.0.8 on 2024-08-17 19:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=46)),
                ('service_name', models.CharField(max_length=46)),
                ('code', models.CharField(max_length=46)),
                ('description', models.CharField(max_length=46)),
                ('status', models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspend')], default='active', max_length=46)),
                ('timeStamp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=46)),
                ('branch', models.CharField(max_length=46)),
                ('code', models.CharField(max_length=46)),
                ('description', models.CharField(max_length=46)),
                ('status', models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspend')], default='active', max_length=46)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]