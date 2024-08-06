# Generated by Django 4.1.5 on 2023-02-01 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consultancy', '0004_delete_slots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotno', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('davaillable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consultancy.availability')),
            ],
        ),
    ]
