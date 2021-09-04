from django.contrib import admin
from .models import Badge,Role,Multiplicator,Reward,Task,Goal,Workspace, User
# Register your models here.

admin.site.register(Badge)
admin.site.register(Role)
admin.site.register(Multiplicator)
admin.site.register(Reward)
admin.site.register(Task)
admin.site.register(Goal)
admin.site.register(Workspace)
admin.site.register(User)
