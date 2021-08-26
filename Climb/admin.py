from django.contrib import admin
from .models import Badge,Role,Multiplicator,Reward,TeamUser,Task,Goal,Workspace,CompanyUser, User
# Register your models here.

admin.site.register(Badge)
admin.site.register(Role)
admin.site.register(Multiplicator)
admin.site.register(Reward)
admin.site.register(TeamUser)
admin.site.register(Task)
admin.site.register(Goal)
admin.site.register(Workspace)
admin.site.register(CompanyUser)
admin.site.register(User)
