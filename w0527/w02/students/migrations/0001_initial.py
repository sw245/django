# Generated by Django 5.2.1 on 2025-05-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('hobby', models.CharField()),
                ('interest', models.CharField()),
                ('strength', models.CharField()),
                ('desire', models.CharField()),
            ],
        ),
    ]
