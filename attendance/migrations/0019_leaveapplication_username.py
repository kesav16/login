# Generated by Django 3.2.7 on 2025-03-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_auto_20250305_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='username',
            field=models.CharField(default=1, editable=False, max_length=150),
            preserve_default=False,
        ),
    ]
