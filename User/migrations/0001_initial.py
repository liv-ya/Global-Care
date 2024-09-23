# Generated by Django 4.1.5 on 2023-02-03 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consultancy', '0005_slots'),
        ('Guest', '0008_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(max_length=50)),
                ('appointment_status', models.IntegerField(default=0)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consultancy.slots')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newuser')),
            ],
        ),
    ]