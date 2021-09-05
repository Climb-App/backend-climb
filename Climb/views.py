from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   


# Permissions
from .permissions import OnlyAdminCanCreate

# Serializers
from .serializers import (
    # User
    UserSerializer,
    UserAdminSerializer,
    UserMemberSerializer,
    UserGetSerializer,
    # RecoveryPassSerializer,
    RoleListModelSerializer,
    RoleModelSerializer,
    # WorkspaceRetrieveModelSerializer,

    # Workspace
    WorkspacesSerializer,
    WorkspaceDetailSerializer,

    # Goal
    GoalSerializer,
    GoalDetailSerializer,

    # Taks
    TaskSerializer,

    # Reward
    # RewardSerializar,
    # RewardModelSerializer,
    # RewardListModelSerializer,
    # RewardRetrieveModelSerializer,

    # Multiplicator
    # MultiplicatorSerializar,

    # Badge
    # BadgeSerializar,
    # BadgeListModelSerializer,
    # BadgeModelSerializer,

    # # TeamUser
    # TeamUserSerializar,
)

# Models
from .models import (
    Role,
    Reward,
    Badge,
    Multiplicator,
    Workspace,
    Goal,
    Task,
    User,
)


# Create your views here.

# Vista para crear SuperUsuarios
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Vista para creae Usuarios Admin (CompanyUsers)
class RegisterAdminView(APIView):
    def post(self, request):
        serializer = UserAdminSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Vista para Crear Usuarios Leader and Member (TeamUsers)
class RegisterMemberView(APIView):
    def post(self, request):
        serializer = UserMemberSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Vista para Login de todos los usuarios, devuelve el token y lo setea en la cookie.
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        # Busca el email en la BD y almacena la informacion en user.
        user = User.objects.filter(email=email).first()

        # Si no existe, devuelve error de autentificacion al response del usuario
        if user is None:
            raise AuthenticationFailed("User not found!")
        
        # Si existe user, verifica la contraseña, si es incorrecta devuelve error de autentificacion al response del usuario
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        # JWT encripta el id y envia token al cliente.
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

# Vista para pedir al backend informacion del usuario logueado, enviando el token.
class UserView(APIView):

    def get(self, request):
        # El backend recibe token del cliente 
        token = request.COOKIES.get('token')

        # Si el token no llega con la peticion, devuelve error de autentificacion
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        # Se decodifica y regresa data del usuario logueado al cliente.
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id'])

        serializer = UserGetSerializer(user, many=True)

        return Response(serializer.data)

    def patch(self, request):
    
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()

        if user.role__id == 1:
            serializer = UserAdminSerializer(user, data=request.data, partial=True)
        else:
            serializer = UserMemberSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data="wrong parameters")

# Vista para desloguear al usuario.
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }

        return response

# class RecoveryPassView(PasswordResetView):
#     def patch(self, request):
        
#         token = request.COOKIES.get('token')
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()

#         serializer = RecoveryPassSerializer(user, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(data="wrong parameters")


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, request): #######

        token = request.COOKIES.get('token')
        # Si el token no llega con la peticion, devuelve error de autentificacion
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        # Se decodifica y regresa data del usuario logueado al cliente.
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        return user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object(request)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# Vista que permite crear nuevos roles de usuarios y listarlos
class RoleView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = RoleModelSerializer

        return serializer_class

# ''' Workspace '''
class WorkspaceView( APIView ): 
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        # Filtramos los workspaces del usuario que hace la peticion
        workspaces = Workspace.objects.filter(user__id=payload['id'])

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

        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        workspace = Workspace.objects.filter( id = pk ).first()
        workspace_serializer = WorkspaceDetailSerializer( workspace )

        return Response( workspace_serializer.data )

    def patch(self, request, pk):

        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        workspace_object = Workspace.objects.filter( id = pk ).first()
        serializer = WorkspacesSerializer(workspace_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data="wrong parameters")

class WorkspaceGoalsView( APIView ):
    def get( self, request, pk ):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        goals = Goal.objects.filter( workspace = pk )
        goals_serializer = GoalSerializer( goals, many=True )

        return Response( goals_serializer.data )

class GoalsDetailView( APIView ):
    def get( self, request, pk ):

        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        goal = Goal.objects.filter( id = pk ).first()
        goal_serializer = GoalDetailSerializer( goal )

        return Response( goal_serializer.data )

    def patch(self, request, pk):
    
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        goal_object = Goal.objects.filter( id = pk ).first()
        serializer = GoalSerializer(goal_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data="wrong parameters")

# class WorkspaceGoalsTaskDetailView( APIView ):
#     def get( self, request, pk, goal_id, task_id ):
#         task = Task.objects.filter( id = task_id ).first()
#         task_serializer = TaskSerializer( task )

#         return Response( task_serializer.data )


# ''' Reward '''
# class RewardListCreateAPIView( generics.ListCreateAPIView ):
#     queryset = Reward.objects.all()
#     serializer_class = RewardListModelSerializer

#     def get_serializer_class(self):
#         serializer_class = self.serializer_class
#         if self.request.method == "POST":
#             serializer_class = RewardModelSerializer

#         return serializer_class

# class RewardsRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
#     queryset = Reward.objects.all()
#     serializer_class = RewardRetrieveModelSerializer

# class RewardView( APIView ):
#     def get(self, request):
#         token = request.COOKIES.get('token')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         rewards = Reward.objects.filter(company_user=payload['id']).first()

#         serializer = RewardSerializar(rewards)

#         return Response(serializer.data)

# ''' Badge '''
# class BadgeListCreateAPIView( generics.ListCreateAPIView ):
#     queryset = Badge.objects.all()
#     serializer_class = BadgeListModelSerializer

#     def get_serializer_class(self):
#         serializer_class = self.serializer_class
#         if self.request.method == "POST":
#             serializer_class = BadgeModelSerializer

#         return serializer_class

# class BadgeRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
#     queryset = Badge.objects.all()
#     serializer_class = BadgeListModelSerializer

# class BadgeView( APIView ):
#     def get(self, request):
#         token = request.COOKIES.get('token')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         badges = Badge.objects.filter(company_user=payload['id']).first()

#         serializer = BadgeSerializar(badges)

#         return Response(serializer.data)

# ''' Multiplicator '''
# class MultiplicatorView( APIView ):
#     def get(self, request):
#         token = request.COOKIES.get('token')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         multiplicators = Multiplicator.objects.filter(company_user=payload['id']).first()

#         serializer = MultiplicatorSerializar(multiplicators)

#         return Response(serializer.data)

# ''' TeamUser '''
# class TeamUserView( APIView ):
#     def get(self, request):
#         token = request.COOKIES.get('token')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         team_users = TeamUser.objects.filter(company_user=payload['id']).first()

#         serializer = TeamUserSerializar(team_users)

#         return Response(serializer.data)
