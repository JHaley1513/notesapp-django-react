# Generated by Django 4.0 on 2022-01-31 20:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0006_alter_note_created_alter_note_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 20, 30, 5, 929364, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 20, 30, 5, 929486, tzinfo=utc)),
        ),
    ]
