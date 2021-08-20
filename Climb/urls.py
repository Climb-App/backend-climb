from Climb.views import RoleListCreateAPIView
from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from .views import RoleListCreateAPIView

urlpatterns = [
    # SignUp
    # path( "users/", CompanyUserListCreateAPIView.as_view(), name="sign_up" ),
    
    # # Login
    # path("token-auth/", authtoken_views.obtain_auth_token, name="token-auth"),

    # Role
    path( "roles/", RoleListCreateAPIView.as_view(), name="workspaces" )
]