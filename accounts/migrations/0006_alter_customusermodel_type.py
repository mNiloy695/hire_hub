# Generated by Django 5.1.2 on 2024-10-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customusermodel_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='type',
            field=models.CharField(choices=[('Viewer', 'Viewer'), ('Employee', 'Employee'), ('Job Seeker', 'Job Seeker')], default='Viewer', max_length=40),
        ),
    ]