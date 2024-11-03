# Generated by Django 5.1.2 on 2024-10-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customusermodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='type',
            field=models.CharField(choices=[('Job Seeker', 'Job Seeker'), ('Viewer', 'Viewer'), ('Employee', 'Employee')], default='Viewer', max_length=40),
        ),
    ]