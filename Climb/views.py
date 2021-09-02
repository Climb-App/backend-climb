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
    # User
    UserSerializer,

    # Workspace
    WorkspacesSerializer,

    # Reward
    RewardSerializar,
    RewardModelSerializer,
    RewardListModelSerializer,
    RewardRetrieveModelSerializer,

    # Multiplicator
    MultiplicatorSerializar,

    # Badge
    BadgeSerializar,
    BadgeListModelSerializer,
    BadgeModelSerializer,

    # TeamUser
    TeamUserSerializar,
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

''' Workspace '''
class WorkspaceView( APIView ): 
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        workspaces = Workspace.objects.filter(company_user=payload['id']).first()

        serializer = WorkspacesSerializer(workspaces)

        return Response(serializer.data)

''' Reward '''
class RewardListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Reward.objects.all()
    serializer_class = RewardListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            # print(self.request.data)
            # print(CompanyUser.objects.all())
            serializer_class = RewardModelSerializer

        return serializer_class

class RewardsRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Reward.objects.all()
    serializer_class = RewardRetrieveModelSerializer

class RewardView( APIView ):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        rewards = Reward.objects.filter(company_user=payload['id']).first()

        serializer = RewardSerializar(rewards)

        return Response(serializer.data)

''' Badge '''
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

class BadgeView( APIView ):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        badges = Badge.objects.filter(company_user=payload['id']).first()

        serializer = BadgeSerializar(badges)

        return Response(serializer.data)

''' Multiplicator '''
class MultiplicatorView( APIView ):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        multiplicators = Multiplicator.objects.filter(company_user=payload['id']).first()

        serializer = MultiplicatorSerializar(multiplicators)

        return Response(serializer.data)

''' TeamUser '''
class TeamUserView( APIView ):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        team_users = TeamUser.objects.filter(company_user=payload['id']).first()

        serializer = TeamUserSerializar(team_users)

        return Response(serializer.data)
