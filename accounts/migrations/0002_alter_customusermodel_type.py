# Generated by Django 5.1.2 on 2024-10-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='type',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Viewer', 'Viewer'), ('Job Seeker', 'Job Seeker')], default='Viewer', max_length=40),
        ),
    ]
