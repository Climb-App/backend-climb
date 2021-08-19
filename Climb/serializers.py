from django.db import models
from rest_framework import serializers
from .models import Badge,Role,Multiplicator,Rewards,Team_User,Task,Goal,WorkSpace,Company_user,Workspace_team_user

class BadgeListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ["name","description"]

class RoleListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["name"]
        
class MultiplicatorListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiplicator
        fields = ["racha","multiplicator"]

class RewardsListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = ["name","description"]

class Team_UserListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_User
        fields = ["first_name","last_name","email"]

class TaskListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name","description","type"]

class GoalListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ["name","description","deadline"]

class WorkSpaceListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = ["name","description"]

class Company_userListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_user
        fields = ["name","email","username","rfc"]
                                        
# class Workspace_team_userListModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workspace_team_user
#         fields = ["name","description"]                                        