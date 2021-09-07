from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from django.views.generic import TemplateView
from .views import (
    # Authentication
    RegisterView,
    RegisterAdminView,
    RegisterMemberView,
    LoginView,
    LogoutView,
    UserView,
    UserAdminView,
    UserMemberView,
    ChangePasswordView,
    RoleView,

    # Workspaces
    WorkspaceView,
    WorkspaceDetailView,
    WorkspaceGoalsView,
    GoalView,
    GoalsDetailView,
    TaskView,
    TaskDetailView,

#     # Reward
#     RewardView,
#     RewardListCreateAPIView,

#     # Badge
#     BadgeView,
#     BadgeListCreateAPIView,

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
    path('logout/', LogoutView.as_view(), name = 'logout'),

    # Recovery Password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Create Role
    path('role/', RoleView.as_view(), name = 'roleUser'),

    # Workspace
    path( "workspaces/", WorkspaceView.as_view(), name="workspaces" ),
    path( "workspaces/<int:pk>", WorkspaceDetailView.as_view(), name="workspaces-goals" ), #Aprobada
    path( "workspaces/<int:pk>/goals", WorkspaceGoalsView.as_view(), name="goals" ),
    path("goal/", GoalView.as_view(), name="goal"),
    path( "goals/<int:pk>", GoalsDetailView.as_view(), name="goals-tasks" ),
    path("task/", TaskView.as_view(), name="task"),
    path( "task/<int:pk>", TaskDetailView.as_view(), name="task-detail" ),

#     # Reward
#     path( "rewards/", RewardView.as_view(), name="reward" ),
#     path( "rewards_test/", RewardListCreateAPIView.as_view(), name="reward-list-create" ),

#     # Badge
#     path( "badges/", BadgeView.as_view(), name="badge" ),
#     path( "badges_test/", BadgeListCreateAPIView.as_view(), name="badge-list-create" ),

#     # Multiplicator
#     path( "multiplicators/", MultiplicatorView.as_view(), name="multiplicator-list-create" ),
]