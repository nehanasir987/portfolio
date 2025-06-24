from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from portfolio import views
from . import views

urlpatterns = [
    path('', views.index, name='home'),            # 👈 Default root URL
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]