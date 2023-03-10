# Generated by Django 4.1.6 on 2023-02-12 22:19

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Device ID')),
                ('active', models.BooleanField()),
                ('labels', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, null=True, size=None)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='core.company')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('data', models.JSONField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='core.device')),
            ],
        ),
    ]
