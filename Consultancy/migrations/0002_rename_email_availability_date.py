# Generated by Django 4.1.5 on 2023-01-31 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consultancy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='email',
            new_name='date',
        ),
    ]
