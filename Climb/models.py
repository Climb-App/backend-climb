from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField( max_length=50 )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class CompanyUser(models.Model):
    user= models.OneToOneField(to=User,on_delete=models.CASCADE,related_name='companies')
    avatar = models.ImageField( upload_to="avatar/company_user", blank=True )
    rfc = models.CharField( max_length=13, blank=True, null=True )
    address = models.CharField( max_length=255 )
    role = models.ForeignKey( Role, on_delete=models.CASCADE, related_name="roles" )
    created_at = models.DateTimeField(auto_now_add=True)

    #Relations

    def __str__(self):
        return f"{self.user.username}"

class Reward(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    icon = models.ImageField( upload_to="icon/reward", blank=True, null=True )
    points_needed = models.IntegerField()
    status = models.CharField( max_length=50 )
    company_user = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="rewards" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Badge(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    icon = models.ImageField( upload_to="icon/badge", blank=True, null=True )
    points_needed_min = models.IntegerField()
    points_needed_max = models.IntegerField()
    company_user = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="badges" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class Multiplicator(models.Model):
    name = models.CharField( max_length=100 )
    streak = models.IntegerField()
    company_user = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="multiplicators" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Workspace(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    company_user = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="workspaces" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class Goal(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    deadline = models.DateField()
    progress = models.IntegerField()
    workspace = models.ForeignKey( Workspace, on_delete=models.CASCADE, related_name="goals" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class TeamUser(models.Model):
    user= models.OneToOneField(to=User,on_delete=models.CASCADE,related_name='teamUsers')
    avatar = models.ImageField( upload_to="avatar/team_user", blank=True )
    points_earned = models.IntegerField()
    points_available = models.IntegerField()
    multiplicator = models.ForeignKey( Multiplicator, on_delete=models.CASCADE, related_name="team_users_mult" )
    role = models.ForeignKey( Role, on_delete=models.CASCADE, related_name="team_users_roles" )
    company_user = models.ForeignKey( CompanyUser, on_delete=models.CASCADE, related_name="team_users_companies" )
    workspace = models.ManyToManyField( Workspace ) #ManyToMany
    reward = models.ManyToManyField( Reward ) #ManyToMany
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
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField()
    message_refused = models.TextField()
    goal = models.ForeignKey( Goal, on_delete=models.CASCADE, related_name="tasks_goal" )
    team_user = models.ForeignKey( TeamUser, on_delete=models.CASCADE, related_name="tasks_team_user" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
