# Generated by Django 2.1.2 on 2019-01-20 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_auto_20190120_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='target',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='targetTeacher',
        ),
    ]
