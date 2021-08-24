from Climb.views import RoleListCreateAPIView
from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from .views import (
    # Role
    RoleListCreateAPIView,
    RoleRetrieveUpdateDestroyAPIVIew,

    # CompanyUser
    CompanyUserListCreateAPIView,
    CompanyUserRetrieveUpdateDestroyAPIView,

    # Reward
    RewardListCreateAPIView,
    RewardsRetrieveUpdateDestroyAPIView,

    # Badge
    BadgeListCreateAPIView,
    BadgeRetrieveUpdateDestroyAPIView,

    # Multiplicator
    MultiplicatorListCreateAPIView,
    MultiplicatorRetrieveUpdateDestroyAPIView,

    # Workspace
    WorkSpaceRetrieveUpdateDestroyAPIView,
    WorskSpaceListCreateAPIView,

    # Goal
    GoalListCreateAPIView,
    GoalRetrieveUpdateDestroyAPIView,

    # TeamUser
    TeamUserListCreateAPIView,
    # TeamUserRetrieveUpdateDestroyAPIView,

    # Task
    # TaskListCreateAPIView,
    # TaskRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # SignUp
    # path( "users/", CompanyUserRetrieveUpdateDestroyAPIView.as_view(), name="sign_up" ),
    
    # Login
    path("token-auth/", authtoken_views.obtain_auth_token, name="token-auth"),

    # Role
    path( "roles/", RoleListCreateAPIView.as_view(), name="role-list-create" ),
    path( "roles/<int:pk>", RoleRetrieveUpdateDestroyAPIVIew.as_view(), name="role-retrieve-update-destroy" ),

    # CompanyUser
    path( "company_user/", CompanyUserListCreateAPIView.as_view(), name="company_user-list-create" ),
    path( "company_user/<int:pk>", CompanyUserRetrieveUpdateDestroyAPIView.as_view(), name="company_user-retrieve-update-destroy" ),

    # Reward
    path( "rewards/", RewardListCreateAPIView.as_view(), name="reward-list-create" ),
    path( "rewards/<int:pk>", RewardsRetrieveUpdateDestroyAPIView.as_view(), name="reward-retrieve-update-destroy" ),

    # Badge
    path( "badges/", BadgeListCreateAPIView.as_view(), name="badge-list-create" ),
    path( "badges/<int:pk>", BadgeRetrieveUpdateDestroyAPIView.as_view(), name="badge-retrieve-update-destroy" ),

    # Multiplicator
    path( "multiplicators/", MultiplicatorListCreateAPIView.as_view(), name="multiplicator-list-create" ),
    path( "multiplicators/<int:pk>", MultiplicatorRetrieveUpdateDestroyAPIView.as_view(), name="multiplicator-retrieve-update-destroy" ),

    # Workspace
    path( "workspaces/", WorskSpaceListCreateAPIView.as_view(), name="Workspace-list-create" ),
    path( "workspaces/<int:pk>", WorkSpaceRetrieveUpdateDestroyAPIView.as_view(), name="Workspace-retrieve-update-destroy" ),

    # Goal
    path( "goals/", GoalListCreateAPIView.as_view(), name="goal-list-create" ),
    path( "goals/<int:pk>", GoalRetrieveUpdateDestroyAPIView.as_view(), name="goal-retrieve-update-destroy" ),

    # TeamUser
    path( "team_users/", TeamUserListCreateAPIView.as_view(), name="team_user-list-create" ),
    # path( "team_users/<int:pk>", TeamUserRetrieveUpdateDestroyAPIView.as_view(), name="team_user-retrieve-update-destroy" ),

    # Task
    # path( "tasks/", TaskListCreateAPIView.as_view(), name="team_user-list-create" ),
    # path( "tasks/<int:pk>", TaskRetrieveUpdateDestroyAPIView.as_view(), name="team_user-retrieve-update-destroy" ),
]