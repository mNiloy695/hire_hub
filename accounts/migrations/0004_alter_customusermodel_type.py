# Generated by Django 5.1.2 on 2024-10-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customusermodel_company_alter_customusermodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='type',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Viewer', 'Viewer'), ('Job Seeker', 'Job Seeker')], default='Viewer', max_length=40),
        ),
    ]