from django.db import models

from django.db import models

class Project(models.Model):
    pro_title = models.CharField(max_length=100)
    pro_icon = models.CharField(max_length=10, default="💼")  # Emoji
    created_on = models.DateField(auto_now_add=True)
   # pro_image = models.ImageField(upload_to='projects/')
    pro_video = models.FileField(upload_to='project_videos/', null=True, blank=True)   
    pro_desc = models.TextField()
    github_link = models.URLField()
    tech_stack = models.CharField(max_length=200)

    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]

    def __str__(self):
        return self.pro_title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} - {self.institute}"



class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    description = models.TextField()
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.provider}"