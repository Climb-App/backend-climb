from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template


# Create your models here.
####### Modelo para reset de password

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    token = {"token" : "token={}".format( reset_password_token.key)}

    content = get_template('reset_password.html').render(token)

    message = EmailMultiAlternatives(
        # title:
        subject = "Recupera tu contrasena {user}".format(user=reset_password_token.user.email),
        # message:
        body = '',
        # from:
        from_email = "climb.app.back@gmail.com",
        # to:
        to = [reset_password_token.user.email],
        cc=[]
    )

    message.attach_alternative(content, 'text/html')
    message.send()


class Role(models.Model):
    name = models.CharField( max_length=50, default="Member" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    role = models.ForeignKey( Role, on_delete=models.CASCADE, related_name="team_users_roles" )
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    avatar = models.CharField(max_length=1000, blank=True )
    rfc = models.CharField( max_length=13, blank=True, null=True )
    address = models.CharField( max_length=255 )
    company = models.IntegerField( null=True )
    available_points = models.IntegerField( null=True )
    accumulated_points = models.IntegerField( null=True )
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} {self.email}"

class Workspace(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    user = models.ManyToManyField( User )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"
        
class Reward(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    icon = models.CharField(max_length=1000,blank=True, null=True )
    points_needed = models.IntegerField()
    status = models.CharField(blank=True, max_length=50 )
    user = models.ManyToManyField( User )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Badge(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    icon = models.CharField(max_length=1000, blank=True, null=True )
    points_needed_min = models.IntegerField()
    points_needed_max = models.IntegerField()
    user = models.ManyToManyField( User )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class Multiplicator(models.Model):
    name = models.CharField( max_length=100 )
    streak = models.IntegerField()
    user = models.ManyToManyField( User )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Goal(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField()
    deadline = models.DateField()
    progress = models.IntegerField()
    workspace = models.ForeignKey( Workspace, on_delete=models.CASCADE, related_name="goals" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description}"

class Task(models.Model):
    Status_TYPES = (
        ("To Do", "to do"),
        ("Done", "done"),
        ("Delay", "delay"),
        ("Refused", "refused"),
    )

    name = models.CharField( max_length=100 )
    description = models.TextField()
    deadline = models.DateField( blank=True) # Falta Migrarlo a la BD
    points_value = models.IntegerField()
    status = models.CharField( max_length=50, choices=Status_TYPES, default="To Do" )
    start_date = models.DateField(auto_now_add=True) # Falta Migrarlo a la BD
    end_date = models.DateField(null=True) # Falta Migrarlo a la BD
    message = models.TextField(null=True) # Falta Migrarlo a la BD
    message_refused = models.TextField(null=True,blank=True)
    goal = models.ForeignKey( Goal, on_delete=models.CASCADE, related_name="tasks_goal" )
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name="tasks_user" )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"