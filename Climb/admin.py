from django.contrib import admin
from .models import Badge,Role,Multiplicator,Rewards,Team_User,Task,Goal,WorkSpace,Company_user,Workspace_team_user
# Register your models here.

admin.site.register(Badge)
admin.site.register(Role)
admin.site.register(Multiplicator)
admin.site.register(Rewards)
admin.site.register(Team_User)
admin.site.register(Task)
admin.site.register(Goal)
admin.site.register(WorkSpace)
admin.site.register(Company_user)
admin.site.register(Workspace_team_user)

