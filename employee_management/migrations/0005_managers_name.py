# Generated by Django 4.2.7 on 2023-12-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0004_managers_alter_employee_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
