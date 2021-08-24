from django.db import models
from rest_framework import serializers
from .models import Badge,Role,Multiplicator,Reward,TeamUser,Task,Goal,Workspace,CompanyUser
from django.contrib.auth.models import User



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

class UserListModelSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password","token"]      
 
class RoleListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ "name" ]     

class CompanyUserListModelSerializer(serializers.ModelSerializer):
    user=UserListModelSerializer()
    role=RoleListModelSerializer()
    class Meta:
        model = CompanyUser
        fields = ["user","rfc","avatar","address","role"]

class TeamUserListModelSerializer(serializers.ModelSerializer):
    user=UserListModelSerializer()
    role=RoleListModelSerializer()
    class Meta:
        model = TeamUser
        fields = ["user","avatar","points_earned","points_available","multiplicator","role","company_user","workspace","reward"]


 

                                        
# class Workspace_TeamUserListModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workspace_TeamUser
#         fields = ["name","description"]