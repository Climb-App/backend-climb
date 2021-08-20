from django.db import models
from rest_framework import serializers
from .models import Badge,Role,Multiplicator,Reward,TeamUser,Task,Goal,Workspace,CompanyUser

class RoleListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ "name" ]

class BadgeListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ["name","description"]
        
class MultiplicatorListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiplicator
        fields = ["racha","multiplicator"]

class RewardListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ["name","description"]

class TeamUserListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamUser
        fields = ["first_name","last_name","email"]

class TaskListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name","description","type"]

class GoalListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ["name","description","deadline"]

class WorkspaceListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ["name","description"]

class CompanyUserListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = ["name","email","username","rfc"]
                                        
# class Workspace_TeamUserListModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workspace_TeamUser
#         fields = ["name","description"]