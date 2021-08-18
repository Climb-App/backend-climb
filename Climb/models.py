from django.db import models


# Create your models here.

class Badge(models.Model):
    """Badge."""
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    # Preguntar https://docs.djangoproject.com/es/3.2/topics/files/
    icon = models.ImageField()
    propoints_needed_min = models.IntegerField()
    points_needed_max = models.IntegerField()
  # Relations

    def __str__(self):
        return f"{self.name} {self.description}"

class Role(models.Model):
    """Role."""
    name = models.CharField(max_length=80)
    def __str__(self):
      return f"{self.name}"


class Multiplicator(models.Model):
    """multiplicator."""
    racha = models.IntegerField()
    multiplicator = models.FloatField()
# Relations
    def __str__(self):
      return f"{self.racha} {self.multiplicator}"


class Rewards(models.Model):
    """Rewards."""
    icon = models.ImageField()
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    points_needed = models.IntegerField()
    status = models.CharField(max_length=100)
  # Relations

    def __str__(self):
        return f"{self.name} {self.description}"


class Team_User(models.Model):
    """Team_User."""
    avatar = models.ImageField()
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    racha = models.IntegerField()
    point_earned = models.IntegerField()
    points_available = models.IntegerField()
    workspace_id = models.IntegerField()
  # Relations
    role_id = models.ForeignKey(
        Role, on_delete=models.PROTECT, related_name="Roles_TeamUser")
    badge_id = models.ForeignKey(
        Badge, on_delete=models.PROTECT, related_name="Badges_TeamUser")
    multiplicator_id = models.ForeignKey(
        Multiplicator, on_delete=models.PROTECT, related_name="Multiplicators_TeamUser")
    rewards_id = models.ForeignKey(
        Rewards, on_delete=models.PROTECT, related_name="Rewards_TeamUser")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    """Task."""
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    Status_TYPES = (
        ("To Do", "to do"),
        ("Done", "done"),
        ("Delay", "delay"),
        ("Refused", "refused"),
    )
    type = models.CharField(
        max_length=50, choices=Status_TYPES, default="To Do")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    messages = models.CharField(max_length=255)
    messages_refused = models.CharField(max_length=255)
  # Relations
    team_user_id = models.ForeignKey(
        Team_User, on_delete=models.PROTECT, related_name="Team_users_Task")

    def __str__(self):
        return f"{self.name} {self.description}"


class Goal(models.Model):
    """Goal."""
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    progress = models.IntegerField()
  # Relations
    task_id = models.ForeignKey(
        Task, on_delete=models.PROTECT, related_name="Tasks_Goal")

    def __str__(self):
        return f"{self.name} {self.description}"


class WorkSpace(models.Model):
    """Workspace."""
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
  # Relations
    goal_id = models.ForeignKey(
        Goal, on_delete=models.PROTECT, related_name="Goals_Workspace")

    def __str__(self):
        return f"{self.name} {self.description}"


class Company_user(models.Model):
    """Company_user."""
    avatar = models.ImageField()
    name = models.CharField(max_length=80)
    email = models.EmailField()
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    rfc = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
  # Relations
    role_id = models.ForeignKey(
        Role, on_delete=models.PROTECT, related_name="Roles_Company_user")
    workspace_id = models.ForeignKey(
        WorkSpace, on_delete=models.PROTECT, related_name="Workspaces_Company_user")
    team_user_id = models.ForeignKey(
        Team_User, on_delete=models.PROTECT, related_name="Team_users_Company_user")
    rewards_id = models.ForeignKey(
        Rewards, on_delete=models.PROTECT, related_name="Rewards_Company_user")
    badge_id = models.ForeignKey(
        Badge, on_delete=models.PROTECT, related_name="Badges_Company_user")
    multiplicator_id = models.ForeignKey(
        Multiplicator, on_delete=models.PROTECT, related_name="Multiplicators_Company_user")

    def __str__(self):
        return f"{self.name} {self.username}"


class Workspace_team_user(models.Model):
    """Workspace_team_user."""
  # Relations
    team_user_id = models.ForeignKey(
        Team_User, on_delete=models.PROTECT, related_name="Team_users_Workspace_team_user")

    def __str__(self):
        return f"{self.name} {self.description}"
