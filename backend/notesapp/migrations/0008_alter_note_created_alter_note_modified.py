# Generated by Django 4.0 on 2022-01-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0007_alter_note_created_alter_note_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]