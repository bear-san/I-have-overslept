# Generated by Django 2.1.2 on 2019-01-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_auto_20190120_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='targetTeacher',
            field=models.CharField(default='', max_length=100),
        ),
    ]