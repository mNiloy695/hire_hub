# Generated by Django 5.1.2 on 2024-10-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_applymodel_status_alter_company_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='job_type',
            field=models.CharField(choices=[('Semi-Government', 'Semi-Government'), ('Privet', 'Privet'), ('Government', 'Government')], default='Privet', max_length=100),
        ),
    ]
