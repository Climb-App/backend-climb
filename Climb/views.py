from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser

# Permissions
from .permissions import OnlyAdminCanCreate

# Serializers
from .serializers import (
    RoleListModelSerializer,
)

# Models
from .models import (
    Role,
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


# # Serializers
# from .serializers import (
#     BadgeListModelSerializer,
#     RoleListModelSerializer,
#     MultiplicatorListModelSerializer,
#     RewardsListModelSerializer,
#     Team_UserListModelSerializer,
#     TaskListModelSerializer,
#     GoalListModelSerializer,
#     WorkSpaceListModelSerializer,
#     Company_userListModelSerializer,
# )


# # Models
# from .models import (
#     Badge,
#     Role,
#     Multiplicator,
#     Reward,
#     TeamUser,
#     Task,
#     Goal,
#     Workspace,
#     CompanyUser,
# )

# class CompanyUserListCreateAPIView( generics.ListCreateAPIView ):
#     queryset = Company_user.objects.all()
#     serializer_class = Company_userListModelSerializer

#     def get_serializer_class(self):
#         serializer_class = self.serializer_class
#         if self.request.method == "POST":
#             serializer_class = Company_userListModelSerializer

#         return serializer_class

# class BadgeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Badge.objects.all()
#     serializer_class = BadgeListModelSerializer


# class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Role.objects.all()
#     serializer_class = RoleListModelSerializer


# class MultiplicatorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Multiplicator.objects.all()
#     serializer_class = MultiplicatorListModelSerializer


# class RewardsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Rewards.objects.all()
#     serializer_class = RewardsListModelSerializer


# class Team_userRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Team_User.objects.all()
#     serializer_class = Team_UserListModelSerializer


# class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Task.objects.all()
#     serializer_class = TaskListModelSerializer


# class GoalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Goal.objects.all()
#     serializer_class = GoalListModelSerializer


# class WorskSpaceListCreateAPIView(generics.ListCreateAPIView):
#     queryset = WorkSpace.objects.all()
#     serializer_class = WorkSpaceListModelSerializer

#     def get_serializer_class(self):
#         serializer_class = self.serializer_class
#         if self.request.method == "POST":
#             serializer_class = WorkSpaceListModelSerializer

#         return serializer_class

# class WorkSpaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = WorkSpace.objects.all()
#     serializer_class = WorkSpaceListModelSerializer
#     permission_classes = [IsAuthenticated, OnlyAdminCanCreate]
#     # authentication_classes=[TokenAuthentication]
#     # sin ponerlo en settings e importando desde aqui pero son diferentes formas de autenticarte


# class WorkSpaceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Company_user.objects.all()
#     serializer_class = Company_userListModelSerializer
