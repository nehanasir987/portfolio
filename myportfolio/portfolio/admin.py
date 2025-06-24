from django.contrib import admin
from portfolio.models import Project
from .models import Education, Certification


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_title', 'pro_video')
    
admin.site.register(Project, ProjectAdmin)

admin.site.register(Education)
admin.site.register(Certification)


