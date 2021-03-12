# Generated by Django 3.1.7 on 2021-03-12 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_muser_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chat')),
            ],
        ),
        migrations.CreateModel(
            name='MetaUser',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('is_online', models.BooleanField()),
                ('pass_date', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
                ('company', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='MUser',
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('metauser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.metauser')),
                ('tarif', models.IntegerField(choices=[(0, 'No Tar'), (1, 'First Tar'), (2, 'Second Tar'), (3, 'Third Tar')])),
            ],
            bases=('api.metauser',),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('metauser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.metauser')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
            bases=('api.metauser',),
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metauser'),
        ),
    ]