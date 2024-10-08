# Generated by Django 4.1.5 on 2023-01-28 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0008_hospital'),
        ('Admin', '0007_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='images/')),
                ('proof', models.FileField(upload_to='images/')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('status', models.IntegerField(default=0)),
                ('doj', models.DateField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.department')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.hospital')),
            ],
        ),
    ]
