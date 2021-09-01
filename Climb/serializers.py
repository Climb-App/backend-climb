from django.db import models
# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Badge,Role,Multiplicator,Reward,TeamUser,Task,Goal,Workspace,CompanyUser
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'password', 
            'role',
            'is_superuser',
            'is_staff',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class WorkspacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'company_user'
        ]

class RewardSerializar(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = [
            'id',
            'name',
            'description',
            'points_needed',
            'status',
            'company_user'
        ]

class BadgeSerializar(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = [
            'id',
            'name',
            'description',
            'icon',
            'points_needed_min',
            'points_needed_max',
            'company_user'
        ]

class MultiplicatorSerializar(serializers.ModelSerializer):
    class Meta:
        model = Multiplicator
        fields = [
            'id',
            'name',
            'streak',
            'company_user'
        ]

class TeamUserSerializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'company_user'
        ]