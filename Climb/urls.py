from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from django.views.generic import TemplateView
from .views import (
    # Authentication
    RegisterView,
    RegisterAdminView,
    RegisterMemberView,
    LoginView,
    # LogoutView,
    UserView,
    UserAdminView,
    UserMemberView,
    ChangePasswordView,
    RoleView,

    # Workspaces
    WorkspaceView,
    WorkspaceDetailView,
    WorkspaceGoalsView,
    GoalCreateView,
    GoalsDetailView,
    TaskCreateView,
    TaskDetailView,

    # Reward
    RewardUserView,
    RewardCreateView,
    RewardDetailView,


    # Badge
    BadgeUserView,
    BadgeCreateView,
    BadgeDetailView,

#     # Multiplicator
#     MultiplicatorView,
)

urlpatterns = [
    # SignUp
    path('register/', RegisterView.as_view(), name = 'register'),
    path('register/admin', RegisterAdminView.as_view(), name = 'register'),
    path('register/member', RegisterMemberView.as_view(), name = 'register'),

    # Login
    path('login/', LoginView.as_view(), name = 'login'),

    # Get User
    path('user/', UserView.as_view(), name = 'users'),
    path('user/admin/<int:pk>', UserAdminView.as_view(), name = 'users'),
    path('user/member/<int:pk>', UserMemberView.as_view(), name = 'users'),


    # Logout
    # path('logout/', LogoutView.as_view(), name = 'logout'),

    # Recovery Password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Create Role
    path('role/', RoleView.as_view(), name = 'roleUser'),

    # Workspace
    path( "workspaces/", WorkspaceView.as_view(), name="workspaces" ),
    path( "workspaces/<int:pk>/", WorkspaceDetailView.as_view(), name="workspaces-goals" ), #Aprobada
    path( "workspaces/<int:pk>/goals", WorkspaceGoalsView.as_view(), name="goals" ),
    path("goals/", GoalCreateView.as_view(), name="goal"),
    path( "goals/<int:pk>/", GoalsDetailView.as_view(), name="goals-tasks" ),
    path("tasks/", TaskCreateView.as_view(), name="task"),
    path( "tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail" ),

    # Reward
    path( "reward/user/", RewardUserView.as_view(), name="reward-member" ),
    path( "reward/", RewardCreateView.as_view(), name="reward" ),
    path( "reward/<int:pk>/", RewardDetailView.as_view(), name="reward-detail" ),


    # Badge
    path( "badges/user/", BadgeUserView.as_view(), name="badge-member" ),
    path( "badges/", BadgeCreateView.as_view(), name="badge" ),
    path( "badges/<int:id>/", BadgeDetailView.as_view(), name="badge-detail" ),

    # Multiplicator
    # path( "multiplicators/", MultiplicatorView.as_view(), name="multiplicator-list-create" ),
]