# Generated by Django 3.2.6 on 2021-09-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Climb', '0004_alter_goal_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
