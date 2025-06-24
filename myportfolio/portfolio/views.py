from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Project


from .models import Project, Education, Certification  # 👈 Add these imports

def index(request):
    skills = [ 
        {"name": "HTML5", "icon": "fab fa-html5", "desc": "Clean & semantic markup, SEO friendly structure."},
        {"name": "CSS3", "icon": "fab fa-css3-alt", "desc": "Responsive layouts, Grid & Flexbox, modern styling."},
        {"name": "Bootstrap", "icon": "fab fa-bootstrap", "desc": "Responsive design, components, and utilities."},
        {"name": "Python / Django", "icon": "fab fa-python", "desc": "Backend development, REST API, ORM, secure apps."},
        {"name": "Git / GitHub", "icon": "fab fa-github", "desc": "Version control, collaboration, and project management."}
    ]
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    
    return render(request, 'portfolio/index.html', {
        "skills": skills,
        "educations": educations,
        "certifications": certifications
    })



def project(request):
    return render(request, 'portfolio/project.html')

def contact(request):
    return render(request, 'portfolio/contact.html')


def project(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project.html', {'projects': projects})

