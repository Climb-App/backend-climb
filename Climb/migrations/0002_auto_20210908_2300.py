# Generated by Django 3.2.6 on 2021-09-08 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Climb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accumulated_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='available_points',
            field=models.IntegerField(null=True),
        ),
    ]
