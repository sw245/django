# Generated by Django 5.2.1 on 2025-05-30 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('tel', models.CharField(default='010-0000-0000', max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('hobby', models.CharField(max_length=100)),
                ('mdate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
