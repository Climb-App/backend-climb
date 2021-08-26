from django.db import models
# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Badge,Role,Multiplicator,Reward,TeamUser,Task,Goal,Workspace,CompanyUser
from rest_framework.authtoken.models import Token
from .models import User



# ''' Company User Models Serializer '''
# class CompanyUserListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = CompanyUser
#         fields = [ "id", "name","email", "username", "password", "role_id" ]

class CompanyUserModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = CompanyUser
        fields = ["user","rfc","avatar","address","role"]


''' Reward Models Serializer '''
class RewardListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Reward
        fields = [ "id", "name", "description", "points_needed", "status", "company_user_id" ]

class RewardModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Reward
        fields = [ "id", "name", "description", "icon", "points_needed", "status", "company_user_id" ]

class RewardRetrieveModelSerializer( serializers.ModelSerializer ):
    company_user_id = CompanyUserModelSerializer
    
    class Meta:
        model = Reward
        fields = [ "id", "name", "description", "icon", "points_needed", "status", "company_user_id" ]

''' Badge Models Serializer '''
class BadgeListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Badge
        fields = [ "id", "name", "description", "points_needed_min", "points_needed_max", "company_user_id" ]

class BadgeModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Badge
        fields = [ "id", "name", "description", "icon", "points_needed_min", "points_needed_max", "company_user_id" ]

class BadgeRetrieveModelSerializer( serializers.ModelSerializer ):
    company_user_id = CompanyUserModelSerializer
    
    class Meta:
        model = Badge
        fields = [ "id", "name", "description", "icon", "points_needed_min", "points_needed_max", "company_user_id" ]

''' Multiplicator '''
class MultiplicatorListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Multiplicator
        fields = [ "id", "name", "streak", "company_user_id" ]

class MultiplicatorRetrieveModelSerializer( serializers.ModelSerializer ):
    company_user_id = CompanyUserModelSerializer

    class Meta:
        model = Multiplicator
        fields = [ "id", "name", "streak", "company_user_id" ]


class WorkspaceRetrieveModelSerializer( serializers.ModelSerializer ):
    company_user_id = CompanyUser
    
    class Meta:
        model = Workspace
        fields = [ "id", "name", "description", "company_user_id" ]

''' Goal'''
class GoalListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Goal
        fields = [ "id", "name", "description", "deadline", "progress", "workspace_id" ]

class GoalRetrieveModelSerializer( serializers.ModelSerializer ):
    workspace_id = Workspace

    class Meta:
        model = Goal
        fields = [ "id", "name", "description", "deadline", "progress", "workspace_id" ]

class WorkspaceListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Workspace
        fields = '__all__'


class UserListModelSerializer (serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]      
 
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

class CompanyUserRetrieveModelSerializer( serializers.ModelSerializer ):
    role = RoleListModelSerializer()
    
    class Meta:
        model = CompanyUser
        fields = ["user","rfc","avatar","address","role"]

 

                                        
# class Workspace_TeamUserListModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workspace_TeamUser
#         fields = ["name","description"]


####### Vic
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
