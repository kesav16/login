# Generated by Django 3.2.7 on 2025-03-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0017_alter_attendance_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='username',
            field=models.CharField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='working_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
