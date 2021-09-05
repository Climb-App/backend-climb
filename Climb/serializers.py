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


# ''' Company User Models Serializer '''
# class CompanyUserListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = CompanyUser
#         fields = [ "id", "name","email", "username", "password", "role_id" ]

# class CompanyUserModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = CompanyUser
#         fields = ["user","rfc","avatar","address"]


# ''' Reward Models Serializer '''
# class RewardListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = Reward
#         fields = [ "id", "name", "description", "points_needed", "status", "company_user" ]

# class RewardModelSerializer( serializers.ModelSerializer ):
#     # Serializador post
#     class Meta:
#         model = Reward
#         fields = [ "id", "name", "description", "icon", "points_needed", "status", "company_user" ]

# # class RewardRetrieveModelSerializer( serializers.ModelSerializer ):
# #     company_user_id = CompanyUserModelSerializer

#     class Meta:
#         model = Reward
#         fields = [ "id", "name", "description", "icon", "points_needed", "status", "company_user" ]

# ''' Badge Models Serializer '''
# class BadgeListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = Badge
#         fields = [ "id", "name", "description", "points_needed_min", "points_needed_max", "company_user" ]

# class BadgeModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = Badge
#         fields = [ "id", "name", "description", "icon", "points_needed_min", "points_needed_max", "company_user" ]

# # class BadgeRetrieveModelSerializer( serializers.ModelSerializer ):
# #     company_user_id = CompanyUserModelSerializer
    
#     class Meta:
#         model = Badge
#         fields = [ "id", "name", "description", "icon", "points_needed_min", "points_needed_max", "company_user" ]

# ''' Multiplicator '''
# class MultiplicatorListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = Multiplicator
#         fields = [ "id", "name", "streak", "company_user" ]

# class MultiplicatorRetrieveModelSerializer( serializers.ModelSerializer ):
#     company_user_id = CompanyUserModelSerializer

    # class Meta:
    #     model = Multiplicator
    #     fields = [ "id", "name", "streak", "company_user" ]


# class WorkspaceRetrieveModelSerializer( serializers.ModelSerializer ):
#     company_user_id = CompanyUser
#     class Meta:
#         model = Workspace
#         fields = [ "id", "name", "description", "company_user" ]

# ''' Goal'''
# class GoalListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = Goal
#         fields = [ "id", "name", "description", "deadline", "progress", "workspace_id" ]

# class GoalRetrieveModelSerializer( serializers.ModelSerializer ):
#     workspace_id = Workspace

#     class Meta:
#         model = Goal
#         fields = [ "id", "name", "description", "deadline", "progress", "workspace_id" ]

# class WorkspaceListModelSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = Workspace
#         fields = '__all__'


# class UserListModelSerializer (serializers.ModelSerializer):
  
#     class Meta:
#         model = User
#         fields = ["first_name","last_name","email","username","password"]      
 

 #### Serializadores para crear Nuevos Roles de Usuarios
class RoleListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ 'id', 'name' ]     

class RoleModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ 'name' ] 


# class CompanyUserListModelSerializer(serializers.ModelSerializer):
#     user=UserListModelSerializer()
#     role=RoleListModelSerializer()
    
#     class Meta:
#         model = CompanyUser
#         fields = ["user","rfc","avatar","address","role"]



# class TeamUserListModelSerializer(serializers.ModelSerializer):
#     user=UserListModelSerializer()
#     role=RoleListModelSerializer()
#     class Meta:
#         model = TeamUser
#         fields = ["user","avatar","points_earned","points_available","multiplicator","role","company_user","workspace","reward"]

# class CompanyUserRetrieveModelSerializer( serializers.ModelSerializer ):
#     role = RoleListModelSerializer()
#     user=UserListModelSerializer()
    
#     class Meta:
#         model = CompanyUser
#         fields = ["user","rfc","avatar","address","role"]

 

 #######################################################                                   


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
            'company'
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

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'role',
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

# class RecoveryPassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User 
#         fields = ['password']
        
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#         def create(self, validated_data):
#             password = validated_data.pop('password', None)
#             instance = self.Meta.model(**validated_data)
#             if password is not None:
#                 instance.set_password(password)
#             instance.save()
#             return instance

#         def update(self, instance, validated_data):
#             instance.password = validated_data['password']
#             self.Meta.create(instance.password)

#             return Response({"Message": "success"})


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

class TaskSerializer( serializers.ModelSerializer ):
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



# class RewardSerializar(serializers.ModelSerializer):
#     class Meta:
#         model = Reward
#         fields = [
#             'id',
#             'name',
#             'description',
#             'points_needed',
#             'status',
#             'company_user'
#         ]

# class BadgeSerializar(serializers.ModelSerializer):
#     class Meta:
#         model = Badge
#         fields = [
#             'id',
#             'name',
#             'description',
#             'icon',
#             'points_needed_min',
#             'points_needed_max',
#             'company_user'
#         ]

# class MultiplicatorSerializar(serializers.ModelSerializer):
#     class Meta:
#         model = Multiplicator
#         fields = [
#             'id',
#             'name',
#             'streak',
#             'company_user'
#         ]

# class TeamUserSerializar(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'username',
#             'email',
#             'password',
#             'company_user'
#         ]