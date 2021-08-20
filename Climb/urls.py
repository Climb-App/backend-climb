from django.urls import path
from rest_framework.authtoken import views as authtoken_views



urlpatterns = [
     # Login
    path("Login/", authtoken_views.obtain_auth_token, name="Login"),
]