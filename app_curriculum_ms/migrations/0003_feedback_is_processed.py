# Generated by Django 5.0.6 on 2024-06-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_curriculum_ms', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]