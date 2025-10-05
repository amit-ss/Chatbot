from django.contrib import admin
from team.models import team


class teamAdmin(admin.ModelAdmin):
    list_display = ("name",'title', 'image')
    

admin.site.register(team, teamAdmin)
    
# Register your models here.
