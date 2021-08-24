# Generated by Django 3.2.6 on 2021-08-24 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/company_user')),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('progress', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Multiplicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('streak', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiplicators', to='Climb.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/reward')),
                ('points_needed', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='Climb.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspaces', to='Climb.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='TeamUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/team_user')),
                ('points_earned', models.IntegerField()),
                ('points_available', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users_companies', to='Climb.companyuser')),
                ('multiplicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users_mult', to='Climb.multiplicator')),
                ('reward', models.ManyToManyField(to='Climb.Reward')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_users_roles', to='Climb.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teamUsers', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ManyToManyField(to='Climb.Workspace')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateField(blank=True, null=True)),
                ('points_value', models.IntegerField()),
                ('status', models.CharField(choices=[('To Do', 'to do'), ('Done', 'done'), ('Delay', 'delay'), ('Refused', 'refused')], default='To Do', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('message', models.TextField()),
                ('message_refused', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_goal', to='Climb.goal')),
                ('team_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_team_user', to='Climb.teamuser')),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='Climb.workspace'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='Climb.role'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/badge')),
                ('points_needed_min', models.IntegerField()),
                ('points_needed_max', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='badges', to='Climb.companyuser')),
            ],
        ),
    ]
