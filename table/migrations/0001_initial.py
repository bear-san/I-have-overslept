# Generated by Django 2.1.2 on 2019-01-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(default='', max_length=100)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=100)),
                ('fireTime', models.IntegerField()),
                ('status', models.IntegerField()),
                ('targetTeacher', models.CharField(default='', max_length=100)),
                ('isContact', models.BooleanField(default=False)),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('university', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='timetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256)),
                ('teacher', models.CharField(default='', max_length=256)),
                ('level', models.IntegerField()),
                ('week', models.IntegerField()),
                ('time', models.IntegerField()),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('room', models.CharField(default='', max_length=256)),
                ('target_id', models.CharField(default='', max_length=256)),
                ('quater', models.IntegerField()),
                ('year', models.IntegerField()),
                ('isNotification', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('target_id', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('admission_year', models.IntegerField()),
                ('permission_level', models.IntegerField()),
            ],
        ),
    ]
