# Generated by Django 3.2.7 on 2025-03-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0015_remove_employeedetails_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='username',
            field=models.CharField(editable=False, max_length=150),
        ),
    ]
