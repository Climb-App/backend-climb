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
    RoleListModelSerializer,
    RoleModelSerializer,

    # Workspace
    WorkspacesSerializer,
    WorkspaceDetailSerializer,

    # Goal
    GoalSerializer,
    GoalDetailSerializer,

    # Taks
    TaskSerializer,

    # Reward
    RewardSerializer,

    # Badge
    BadgeSerializer,

    # Multiplicator
    # MultiplicatorSerializar,
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

    def send_email(mail):
        pass

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

        # response.set_cookie(key='token', value=token, httponly=True)

        response.data = {
            'token': token
        }

        return response

# Vista para pedir al backend informacion del usuario logueado, enviando el token.
class UserView(APIView):

    def get(self, request):
        # El backend recibe token del cliente 
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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

class UserAdminView(APIView):
    
    ### En este get se esta obteniendo el id directamente del payload y no desde los params, de hecho el pk no esta teniendo ningun uso
    def get(self, request, pk):
        # El backend recibe token del cliente 
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        # Si el token no llega con la peticion, devuelve error de autentificacion
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        # Se decodifica y regresa data del usuario logueado al cliente.
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()

        serializer = UserAdminSerializer(user)

        return Response(serializer.data)

    def patch(self, request, pk):
    
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()

        serializer = UserAdminSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data="wrong parameters")

    # delete method for remove user with pk
    def delete( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()
        user.delete()

        return Response( 'User deleted' )

class UserMemberView(APIView):
   
    def get(self, request, pk):
        
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        # Si el token no llega con la peticion, devuelve error de autentificacion
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        # Se decodifica y regresa data del usuario logueado al cliente.
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()

        serializer = UserMemberSerializer(user)

        return Response(serializer.data)

    def patch(self, request, pk):
    
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()

        serializer = UserMemberSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data="wrong parameters")

    # delete method for remove user with pk
    def delete( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=pk).first()
        user.delete()

        return Response( 'User deleted' )


# Vista para desloguear al usuario.
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         # response.delete_cookie('token')
#         response.data = {
#             'message': 'success'
#         }

#         return response


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, request): #######

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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
    # Obtiene los workspaces relacionados con el usuario que hace la peticion
    def get(self, request):
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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
    
    # Crea un nuevo workspaces
    def post( self, request ):
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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
    #Obtiene el detalle del workspace mediante su Id
    def get( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        workspace = Workspace.objects.filter( id = pk ).first()
        workspace_serializer = WorkspaceDetailSerializer( workspace )

        return Response( workspace_serializer.data )

    # Actualiza un workspace mediante su Id
    def patch(self, request, pk):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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

    # delete method for remove workspace with pk
    def delete( self, request, pk ):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        workspace = Workspace.objects.filter(id=pk).first()
        workspace.delete()

        return Response( 'Workspace deleted' )

class WorkspaceGoalsView( APIView ):

    # Obtiene los goals de un workspace
    def get( self, request, pk ):
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        goals = Goal.objects.filter( workspace = pk )
        goals_serializer = GoalSerializer( goals, many=True )

        return Response( goals_serializer.data )

class GoalCreateView(APIView):
    pass

    #Post


class GoalsDetailView( APIView ):
    def get( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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
    
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

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

    # delete method for remove workspace with pk
    def delete( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        goal = Goal.objects.filter(id=pk).first()
        goal.delete()

        return Response( 'Goal deleted' )


class TaskCreateView( APIView ):
    pass

    #Post

class TaskDetailView( APIView ):
    def get( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        task = Task.objects.filter( id = pk ).first()
        task_serializer = TaskSerializer( task )

        return Response( task_serializer.data )

    def patch(self, request, pk):
    
        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        taks = Task.objects.filter( id = pk ).first()
        serializer = TaskSerializer(taks, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(data="wrong parameters")

    # delete method for remove workspace with pk
    def delete( self, request, pk ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        task = Task.objects.filter(id=pk).first()
        task.delete()

        return Response( 'Task deleted' )



# Reward
class RewardUserView(APIView):
    def get(self, request):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        # Filtramos los rewards que ha ganado el usuario que hace la peticion
        reward = Reward.objects.filter(user__id=payload['id'])

        serializer = RewardSerializer(reward, many = True)

        return Response(serializer.data)

class RewardDetailView(APIView):
    def get(self, request, pk):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        # Filtramos los rewards que ha ganado el usuario que hace la peticion
        reward = Reward.objects.filter( id = pk )

        serializer = RewardSerializer(reward, many = True)

        return Response(serializer.data)

    # Patch

    # Delete


class RewardCreateView(APIView):
    def post( self, request ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        serializer = RewardSerializer( data = request.data )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response( serializer.errors )


# Badge
class BadgeUserView(APIView):
    def get(self, request):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        badges = Badge.objects.filter(user__id=payload['id'])

        serializer = BadgeSerializer(badges, many = True)

        return Response(serializer.data)


class BadgeDetailView(APIView):
    def get(self, request, pk):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        # Filtramos los rewards que ha ganado el usuario que hace la peticion
        badges = Badge.objects.filter( id = pk )

        serializer = BadgeSerializer(badges, many = True)

        return Response(serializer.data)

    # Patch

    # Delete


class BadgeCreateView( APIView ):
    def post( self, request ):

        # token = request.COOKIES.get('token')
        token = request.headers['Authorization']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        serializer = BadgeSerializer( data = request.data )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response( serializer.errors )


# Multiplicator
# class MultiplicatorView( APIView ):
#     def get(self, request):
#         token = request.COOKIES.get('token')
#         token = request.headers['Authorization']

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         multiplicators = Multiplicator.objects.filter(company_user=payload['id']).first()

#         serializer = MultiplicatorSerializer(multiplicators)

#         return Response(serializer.data)