from django.db import models
from django.db.models import models
# Create your models here.

class WorkSpace(models.Model):
    """Workspace."""
    name=models.CharField(max_length=80) 
    description= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
  #Relations
  ##### ¿Que pasa aqui?
    company_user_id= models.ForeignKey(,on_delete=models.PROTECT,related_name="")
    team_user_id =models.ForeignKey(,on_delete=models.PROTECT,related_name="") 
  #####
    def __str__(self):
        return f"{self.name} {self.description}"

class Rewards(models.Model):
    """Rewards."""
    icon=models.ImageField()#Preguntar
    name=models.CharField(max_length=80) 
    description= models.CharField(max_length=100)
    points_needed =models.integerField()
    status = models.charField(max_length=100)
  #Relations
    
    team_user_id = models.ForeignKey(Team_User,on_delete=models.PROTECT,related_name="Team_Users")
    def __str__(self):
        return f"{self.name} {self.description}" 

class Badge(models.Model):
    """Badge."""
    name=models.CharField(max_length=80) 
    description= models.CharField(max_length=100)
    icon=models.ImageField()#Preguntar https://docs.djangoproject.com/es/3.2/topics/files/
    propoints_needed_min =models.integerField()
    points_needed_max = models.integerField()
  #Relations
    
   
    def __str__(self):
        return f"{self.name} {self.description}"   

class Role(models.Model):
     """Role."""
name = models.CharField(max_length=80)
def __str__(self):
            return f"{self.name}"  

class Multiplicator(models.Model):
    """multiplicator."""
racha=models.IntegerField()
multiplicator=models.floatField()
  #Relations
company_user_id = models.ForeignKey(Company_user,on_delete=models.PROTECT,related_name="Company_users")

def __str__(self):
        return f"{self.racha} {self.multiplicator}"  

class Team_User(models.Model):
    """Team_User."""
    avatar=models.ImageField()#Preguntar
    first_name=models.CharField(max_length=80) 
    last_name=models.CharField(max_length=80)
    email=models.EmailField()
    password=models.CharField()
    racha =models.CharField()
    point_earned=models.IntegerField()
    points_available=models.IntegerField()
    workspace_id=models.integerField()
  #Relations
    role_id = models.ForeignKey(Role,on_delete=models.PROTECT,related_name="Roles")
    badge_id = models.ForeignKey (Badge,on_delete=models.PROTECT,related_name="Badges")
    multiplicator_id = models.ForeignKey (Multiplicator,on_delete=models.PROTECT,related_name="Multiplicators")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"                    

class Company_user(models.Model):
    """Company_user."""
    avatar=models.ImageField()#Preguntar
    name=models.CharField(max_length=80) 
    email=models.EmailField()
    username=models.CharField() 
    password=models.CharField()
    rfc =models.CharField()
    address=models.CharField()
  #Relations
    role_id = models.ForeignKey(Role,on_delete=models.PROTECT,related_name="Roles")
    workspace_id  = models.ForeignKey(WorkSpace,on_delete=models.PROTECT,related_name="Workspaces")
    team_user_id = models.ForeignKey(Team_User,on_delete=models.PROTECT,related_name="Team_users")
    rewards_id  = models.ForeignKey(Rewards,on_delete=models.PROTECT,related_name="Rewards")
    badge_id  = models.ForeignKey(Badge,on_delete=models.PROTECT,related_name="Badges")

    def __str__(self):
        return f"{self.name} {self.username}" 

class Goal(models.Model):
    """Goal."""
    name=models.CharField(max_length=80) 
    description= models.CharField(max_length=100)
    deadline=models.DateTimeField()
    progress=models.integerField()
  #Relations
    workspace_id = models.ForeignKey(WorkSpace,on_delete=models.PROTECT,related_name="Workspaces")
   
    def __str__(self):
        return f"{self.name} {self.description}"        


class Workspace_team_user(models.Model):
    """Workspace_team_user."""
  
  #Relations
    workspace_id  = models.ForeignKey(WorkSpace,on_delete=models.PROTECT,related_name="Workspaces")
    team_user_id = models.ForeignKey(Team_User,on_delete=models.PROTECT,related_name="Team_users")
    def __str__(self):
        return f"{self.name} {self.description}"   

class Task(models.Model):
    """Task."""
    name=models.CharField(max_length=80) 
    description= models.CharField(max_length=100)
    deadline=models.DateTimeField()
    Status_TYPES = (
        ("To Do", "to do","to Do","To do"),
        ("Done", "done"),
        ("Delay", "delay"),
        ("Refused", "refused"),
    )
    type = models.CharField(max_length=50, choices=Status_TYPES, default="To Do")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    messages= models.charField(max_length=)
    messages_refused = models.CharField(max_length=)
  #Relations
    goal_id  = models.ForeignKey(Goal,on_delete=models.PROTECT,related_name="Goals")
    team_user_id = models.ForeignKey(Team_User,on_delete=models.PROTECT,related_name="Team_users")
    def __str__(self):
        return f"{self.name} {self.description}"    

    





       