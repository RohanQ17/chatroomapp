# Generated by Django 5.0.2 on 2024-02-17 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ohayochat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='time_of_text',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='useer',
            new_name='user',
        ),
    ]
