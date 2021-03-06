# Generated by Django 3.1.7 on 2021-03-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('is_online', models.BooleanField()),
                ('is_driver', models.BooleanField()),
                ('card', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('carddate', models.CharField(max_length=4)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('passport', models.FileField(upload_to='')),
                ('pass_date', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
                ('company', models.CharField(max_length=30)),
            ],
        ),
    ]
