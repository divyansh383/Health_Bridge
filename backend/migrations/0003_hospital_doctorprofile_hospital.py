# Generated by Django 4.1.2 on 2023-03-27 07:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_user_is_doctor_doctorprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('address', models.TextField(max_length=500)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='hospital',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.hospital'),
        ),
    ]
