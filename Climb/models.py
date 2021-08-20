from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField( max_length=50 )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class CompanyUser(models.Model):
    name = models.CharField( max_length=100 )
    email = models.EmailField()
    username = models.CharField( max_length=50 )
    password = models.CharField( max_length=255 )
    avatar = models.ImageField( upload_to="avatar/company_user", blank=True, null=True )
    rfc = models.CharField( max_length=13, blank=True, null=True )
    address = models.CharField( max_length=255, blank=True, null=True )
    role_id = models.ForeignKey( Role, on_delete=models.CASCADE, related_name="roles" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Reward(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    icon = models.ImageField( upload_to="icon/reward", blank=True, null=True )
    points_needed = models.IntegerField()
    status = models.CharField( max_length=50 )
    company_user_id = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="rewards" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Badge(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    icon = models.ImageField( upload_to="icon/badge", blank=True, null=True )
    points_needed_min = models.IntegerField()
    points_needed_max = models.IntegerField()
    company_user_id = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="badges" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class Multiplicator(models.Model):
    name = models.CharField( max_length=100 )
    streak = models.IntegerField()
    company_user_id = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="multiplicators" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Workspace(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    company_user_id = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="workspaces" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class Goal(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    deadline = models.DateField( blank=True, null=True )
    progress = models.IntegerField( default=0 )
    workspace_id = models.ForeignKey( Workspace, on_delete=models.CASCADE, related_name="goals" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class TeamUser(models.Model):
    first_name = models.CharField( max_length=100 )
    last_name = models.CharField( max_length=100 )
    username = models.CharField( max_length=50 )
    email = models.EmailField()
    password = models.CharField( max_length=255 )
    avatar = models.ImageField( upload_to="avatar/team_user", blank=True, null=True )
    points_earned = models.IntegerField( blank=True, null=True )
    points_available = models.IntegerField( blank=True, null=True )
    multiplicator_id = models.ForeignKey( Multiplicator, on_delete=models.CASCADE, related_name="team_users_mult", blank=True, null=True )
    role_id = models.ForeignKey( Role, on_delete=models.CASCADE, related_name="team_users_roles" )
    company_user_id = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="team_users_companies" )
    workspace_id = models.ManyToManyField( Workspace ) #ManyToMany
    reward_id = models.ManyToManyField( Reward ) #ManyToMany
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    Status_TYPES = (
        ("To Do", "to do"),
        ("Done", "done"),
        ("Delay", "delay"),
        ("Refused", "refused"),
    )

    name = models.CharField( max_length=100 )
    description = models.TextField()
    deadline = models.DateField( blank=True, null=True )
    points_value = models.IntegerField()
    status = models.CharField( max_length=50, choices=Status_TYPES, default="To Do" )
    start_date = models.DateField( auto_now=True )
    end_date = models.DateField( blank=True, null=True )
    message = models.TextField( blank=True, null=True )
    message_refused = models.TextField( blank=True, null=True )
    goal_id = models.ForeignKey( Goal, on_delete=models.CASCADE, related_name="tasks_goal", blank=True, null=True )
    team_user_id = models.ForeignKey( TeamUser, on_delete=models.CASCADE, related_name="tasks_team_user", blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
