# Generated by Django 4.2.6 on 2023-10-24 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0003_remove_quiz_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='scheduledTime',
        ),
    ]