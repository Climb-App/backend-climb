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
    WorkspaceRetrieveModelSerializer,

    # Workspace
    WorkspacesSerializer,
    WorkspaceDetailSerializer,

    # Goal
    GoalSerializer,
    GoalDetailSerializer,

    # Taks
    TaskSerializer,

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

        user = User.objects.filter(id=payload['id'])

        serializer = UserSerializer(user, many=True)

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

        # segunda consulta para que me traiga el id del company_user
        company_user = CompanyUser.objects.filter( user__id=payload['id'] ).first()
        
        workspaces = Workspace.objects.filter(company_user_id=company_user)

        serializer = WorkspacesSerializer(workspaces, many = True)

        return Response(serializer.data)
    
    def post( self, request ):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        serializer = WorkspacesSerializer( data = request.data )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response( serializer.errors )

class WorkspaceDetailView( APIView ):
    def get( self, request, pk ):
        workspace = Workspace.objects.filter( id = pk ).first()
        workspace_serializer = WorkspaceDetailSerializer( workspace )

        return Response( workspace_serializer.data )

class WorkspaceGoalsView( APIView ):
    def get( self, request, pk ):
        goals = Goal.objects.filter( workspace = pk )
        goals_serializer = GoalSerializer( goals, many=True )

        return Response( goals_serializer.data )

class WorkspaceGoalsDetailView( APIView ):
    def get( self, request, pk, goal_id ):
        goal = Goal.objects.filter( id = goal_id ).first()
        goal_serializer = GoalDetailSerializer( goal )

        return Response( goal_serializer.data )

class WorkspaceGoalsTaskDetailView( APIView ):
    def get( self, request, pk, goal_id, task_id ):
        task = Task.objects.filter( id = task_id ).first()
        task_serializer = TaskSerializer( task )

        return Response( task_serializer.data )


''' Reward '''
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
