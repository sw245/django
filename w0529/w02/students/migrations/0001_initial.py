# Generated by Django 5.2.1 on 2025-05-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('sdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
