from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    Role,
    CompanyUser,
    Reward,
    Badge,
    Multiplicator,
    Workspace,
    Goal,
    TeamUser,
    Task,
)

''' Role Models Serializer '''
class RoleListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Role
        fields = [ "id", "name" ]

''' Company User Models Serializer '''
class CompanyUserListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = CompanyUser
        fields = [ "id", "name","email", "username", "password", "role_id" ]

class CompanyUserModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = CompanyUser
        fields = [ "id", "name", "email", "username", "password", "role_id", "rfc", "address", "avatar" ]

class CompanyUserRetrieveModelSerializer( serializers.ModelSerializer ):
    role_id = RoleListModelSerializer
    
    class Meta:
        model = CompanyUser
        fields = [ "id", "name", "email", "username", "password", "role_id", "rfc", "address", "avatar" ]

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

''' Workspace '''
class WorkspaceListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Workspace
        fields = [ "id", "name", "description", "company_user_id" ]

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

''' TeamUser '''
class TeamUserListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = TeamUser
        fields = [ "id", "first_name", "last_name", "username", "email", "password", "avatar", "points_earned", "multiplicator_id", "role_id", "company_user_id", "workspace_id", "reward_id" ]

class TeamUserRetrieveModelSerializer( serializers.ModelSerializer ):
    multiplicator_id = Multiplicator
    role_id = Role
    company_user = CompanyUser
    workspace_id = Workspace
    reward_id = Reward

    class Meta:
        model = TeamUser
        fields = [ "id", "first_name", "last_name", "username", "email", "password", "avatar", "points_earned", "multiplicator_id", "role_id", "company_user_id", "workspace_id", "reward_id" ]

''' Task '''
class TaskListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Task
        fields = [ "id", "name", "description", "deadline", "points_value", "status", "start_date", "end_date", "goal_id", "team_user_id" ]

class TaskRetrieveModelSerializer( serializers.ModelSerializer ):
    goal_id = Goal
    team_user_id = TeamUser

    class Meta:
        model = Task
        fields = [ "id", "name", "description", "deadline", "points_value", "status", "start_date", "end_date", "goal_id", "team_user_id" ]

