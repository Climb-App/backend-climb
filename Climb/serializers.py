from django.db import models
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (
    User,
    Badge, 
    Role, 
    Multiplicator, 
    Reward, 
    Task, 
    Goal, 
    Workspace
    )


 #### Serializadores para crear Nuevos Roles de Usuarios
class RoleListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ 'id', 'name' ]     

class RoleModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ 'name' ] 

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

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'rfc',
            'email',
            'password', 
            'address',
            'role',
            'avatar',
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

class UserMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password', 
            'role',
            'company',
            'avatar',
            'available_points',
            'accumulated_points'
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

class UsersMemberSerializer(serializers.ModelSerializer):
    # role = RoleModelSerializer()
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'role',
            'company',
        ]


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'role',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class GoalSerializer( serializers.ModelSerializer ):    
    class Meta:
        model = Goal
        fields = [ "id", "name", "description", "deadline", "progress", "workspace" ]


# class UserTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields = [
#             "id",
#             "name"
#         ]

class TaskSerializer( serializers.ModelSerializer ):
    # user = UserTaskSerializer()
    class Meta:
        model = Task
        fields = [ "id", "name", "description", "deadline", "points_value", "status", "start_date", "end_date", "message", "message_refused", "goal", "user" ]

class GoalDetailSerializer( serializers.ModelSerializer ):
    tasks_goal = TaskSerializer( many=True )
    
    class Meta:
        model = Goal
        fields = [ "id", "name", "description", "deadline", "progress", "workspace", "tasks_goal" ]

class WorkspacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'user',
        ]


class WorkspacesUserSerializer(serializers.ModelSerializer):

    user = UsersMemberSerializer()

    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'user',
        ]
class WorkspaceDetailSerializer(serializers.ModelSerializer):
    goals = GoalSerializer( many=True )
    
    class Meta:
        model = Workspace
        fields = [
            'id',
            'name',
            'description',
            'user',
            'goals'
        ]

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = [
            'id',
            'name',
            'description',
            'icon',
            'points_needed',
            'status',
            'user'
        ]

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = [
            'id',
            'name',
            'description',
            'icon',
            'points_needed_min',
            'points_needed_max',
            'user'
        ]

# class MultiplicatorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Multiplicator
#         fields = [
#             'id',
#             'name',
#             'streak',
#             'company_user'
#         ]