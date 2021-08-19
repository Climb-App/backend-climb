from django.shortcuts import render
from rest_framework import generics

# Create your views here.

#Serializers
from .serializers import (
 BadgeListModelSerializer, 
 RoleListModelSerializer, 
 MultiplicatorListModelSerializer,
 RewardsListModelSerializer,
 Team_UserListModelSerializer,
 TaskListModelSerializer, 
 GoalListModelSerializer, 
 WorkSpaceListModelSerializer,
 Company_userListModelSerializer,
 )


#Models
from .models import (
    Badge,
    Role,
    Multiplicator,
    Rewards,
    Team_User,
    Task,
    Goal,
    WorkSpace,
    Company_user,
)

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

    queryset = Rewards.objects.all()
    serializer_class = RewardsListModelSerializer

class Team_userRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Team_User.objects.all()
    serializer_class = Team_UserListModelSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskListModelSerializer    

class GoalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Goal.objects.all()
    serializer_class = GoalListModelSerializer  

class WorkSpaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceListModelSerializer  

class WorkSpaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Company_user.objects.all()
    serializer_class = Company_userListModelSerializer  