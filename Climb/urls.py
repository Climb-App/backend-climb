# from django.urls import path
# from rest_framework.authtoken import views as authtoken_views
# from .views import (
#     # Authentication
#     RegisterView,
#     LoginView,
#     UserView,
#     LogoutView,

#     # Workspace
#     WorkspaceView,
#     WorkspaceDetailView,
#     WorkspaceGoalsView,
#     WorkspaceGoalsDetailView,
#     WorkspaceGoalsTaskDetailView,

#     # Reward
#     RewardView,
#     RewardListCreateAPIView,

#     # Badge
#     BadgeView,
#     BadgeListCreateAPIView,

#     # Multiplicator
#     MultiplicatorView,

#     # TeamUser
#     TeamUserView,
# )

# urlpatterns = [
#     # SignUp
#     path('register/', RegisterView.as_view(), name = 'register'),
    
#     # Login
#     path('login/', LoginView.as_view(), name = 'login'),

#     # Get User
#     path('user/', UserView.as_view(), name = 'users'),

#     # Logout
#     path('logout/', LogoutView.as_view(), name = 'logout'),

#     # Workspace
#     path( "workspaces/", WorkspaceView.as_view(), name="workspaces" ),
#     path( "workspaces/<int:pk>", WorkspaceDetailView.as_view(), name="workspaces" ),
#     path( "workspaces/<int:pk>/goals", WorkspaceGoalsView.as_view(), name="workspaces" ),
#     path( "workspaces/<int:pk>/goals/<int:goal_id>", WorkspaceGoalsDetailView.as_view(), name="workspaces" ),
#     path( "workspaces/<int:pk>/goals/<int:goal_id>/<int:task_id>", WorkspaceGoalsTaskDetailView.as_view(), name="workspaces" ),

#     # Reward
#     path( "rewards/", RewardView.as_view(), name="reward" ),
#     path( "rewards_test/", RewardListCreateAPIView.as_view(), name="reward-list-create" ),

#     # Badge
#     path( "badges/", BadgeView.as_view(), name="badge" ),
#     path( "badges_test/", BadgeListCreateAPIView.as_view(), name="badge-list-create" ),

#     # Multiplicator
#     path( "multiplicators/", MultiplicatorView.as_view(), name="multiplicator-list-create" ),

#     # TeamUser
#     # path( "team_users/", TeamUserView.as_view(), name="team_user-list-create" ),

#     # # Goal
#     # path( "goals/", GoalListCreateAPIView.as_view(), name="goal-list-create" ),

#     # path( "team_users/<int:pk>", TeamUserRetrieveUpdateDestroyAPIView.as_view(), name="team_user-retrieve-update-destroy" ),

#     # Task
#     # path( "tasks/", TaskListCreateAPIView.as_view(), name="team_user-list-create" ),
#     # path( "tasks/<int:pk>", TaskRetrieveUpdateDestroyAPIView.as_view(), name="team_user-retrieve-update-destroy" ),
# ]