from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser

# Permissions
from .permissions import OnlyAdminCanCreate

# Serializers
from .serializers import (
    RoleListModelSerializer,
    BadgeListModelSerializer,
    MultiplicatorListModelSerializer,
    RewardListModelSerializer,
    TeamUserListModelSerializer,
    TaskListModelSerializer,
    GoalListModelSerializer,
    WorkspaceListModelSerializer,
    CompanyUserListModelSerializer,
)

# Models
from .models import (
    Role,
    Badge,
    Multiplicator,
    Reward,
    TeamUser,
    Task,
    Goal,
    Workspace,
    CompanyUser,
)

# # Create your views here.
class RoleListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Role.objects.all()
    serializer_class = RoleListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = RoleListModelSerializer

        return serializer_class



class BadgeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Badge.objects.all()
    serializer_class = BadgeListModelSerializer


class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Role.objects.all()
    serializer_class = RoleListModelSerializer


class MultiplicatorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Multiplicator.objects.all()
    serializer_class = MultiplicatorListModelSerializer


class RewardsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Reward.objects.all()
    serializer_class = RewardListModelSerializer


class TeamUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = TeamUser.objects.all()
    serializer_class = TeamUserListModelSerializer


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskListModelSerializer


class GoalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Goal.objects.all()
    serializer_class = GoalListModelSerializer


class WorskSpaceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = WorkspaceListModelSerializer

        return serializer_class

class WorkSpaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Workspace.objects.all()
    serializer_class = WorkspaceListModelSerializer
    permission_classes = [IsAuthenticated, OnlyAdminCanCreate]
    # authentication_classes=[TokenAuthentication]
    # sin ponerlo en settings e importando desde aqui pero son diferentes formas de autenticarte


class CompanyUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserListModelSerializer

class CompanyUserListCreateAPIView( generics.ListCreateAPIView ):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = CompanyUserListModelSerializer

        return serializer_class

