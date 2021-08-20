from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser

# Permissions
from .permissions import OnlyAdminCanCreate

# Serializers
from .serializers import (
    # Role
    RoleListModelSerializer,

    # CompanyUser
    CompanyUserListModelSerializer,
    CompanyUserModelSerializer,
    CompanyUserRetrieveModelSerializer,

    # Reward
    RewardListModelSerializer,
    RewardModelSerializer,
    RewardRetrieveModelSerializer,

    # Badge
    BadgeListModelSerializer,
    BadgeModelSerializer,

    # Multiplicator
    MultiplicatorListModelSerializer,
    MultiplicatorRetrieveModelSerializer,

    # Workspace
    WorkspaceListModelSerializer,
    WorkspaceRetrieveModelSerializer,

    # Goal
    GoalListModelSerializer,
    GoalRetrieveModelSerializer,

    # TeamUser
    TeamUserListModelSerializer,
    TeamUserRetrieveModelSerializer,

    # Task
    TaskListModelSerializer,
    TaskRetrieveModelSerializer,
)

# Models
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

# Create your views here.

''' Role Views '''
class RoleListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Role.objects.all()
    serializer_class = RoleListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = RoleListModelSerializer

        return serializer_class

class RoleRetrieveUpdateDestroyAPIVIew( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Role.objects.all()
    serializer_class = RoleListModelSerializer

''' CompanyUser Views '''
class CompanyUserListCreateAPIView( generics.ListCreateAPIView ):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = CompanyUserModelSerializer

        return serializer_class

class CompanyUserRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserRetrieveModelSerializer

''' Reward Views '''
class RewardListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Reward.objects.all()
    serializer_class = RewardListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = RewardModelSerializer

        return serializer_class

class RewardsRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Reward.objects.all()
    serializer_class = RewardRetrieveModelSerializer

''' Badge Views '''
class BadgeListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Badge.objects.all()
    serializer_class = BadgeListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = BadgeModelSerializer

        return serializer_class

class BadgeRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Badge.objects.all()
    serializer_class = BadgeListModelSerializer

''' Multiplicator '''
class MultiplicatorListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Multiplicator.objects.all()
    serializer_class = MultiplicatorListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = MultiplicatorListModelSerializer

        return serializer_class

class MultiplicatorRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Multiplicator.objects.all()
    serializer_class = MultiplicatorRetrieveModelSerializer

''' Workspace '''
class WorskSpaceListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = WorkspaceListModelSerializer

        return serializer_class

class WorkSpaceRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceRetrieveModelSerializer

''' Goal '''
class GoalListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Goal.objects.all()
    serializer_class = GoalListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = GoalListModelSerializer

        return serializer_class

class GoalRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Goal.objects.all()
    serializer_class = GoalRetrieveModelSerializer

''' TeamUser '''
class TeamUserListCreateAPIView( generics.ListCreateAPIView ):
    queryset = TeamUser.objects.all()
    serializer_class = TeamUserListModelSerializer

def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = TeamUserListModelSerializer

        return serializer_class

class TeamUserRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = TeamUser.objects.all()
    serializer_class = TeamUserRetrieveModelSerializer

'''Task'''
class TaskListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Task.objects.all()
    serializer_class = TaskListModelSerializer

def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = TaskListModelSerializer

        return serializer_class

class TaskRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Task.objects.all()
    serializer_class = TaskRetrieveModelSerializer
