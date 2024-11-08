# Generated by Django 5.1.2 on 2024-10-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_applymodel_resume_alter_applymodel_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applymodel',
            options={'ordering': ['-apply_date']},
        ),
        migrations.AlterField(
            model_name='applymodel',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='time',
            field=models.CharField(blank=True, choices=[('Half-time', 'Half-time'), ('Full-Time', 'Full-Time')], default='Full-Time', max_length=20, null=True),
        ),
    ]
