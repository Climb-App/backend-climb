from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

# Permissions
from .permissions import OnlyAdminCanCreate

# Serializers
from .serializers import (
    # Users
    UserSerializer,

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
    # TeamUserRetrieveModelSerializer,

    # Task
    # TaskListModelSerializer,
    # TaskRetrieveModelSerializer,
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
    User,
)


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='token', value=token, httponly=True)

        response.data = {
            'token': token
        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()

        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }

        return response


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

