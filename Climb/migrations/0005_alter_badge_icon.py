# Generated by Django 3.2.6 on 2021-09-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Climb', '0004_auto_20210901_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
