# Generated by Django 5.1.2 on 2024-10-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymodel',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='job_type',
            field=models.CharField(choices=[('Privet', 'Privet'), ('Semi-Government', 'Semi-Government'), ('Government', 'Government')], default='Privet', max_length=100),
        ),
    ]
