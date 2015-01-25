from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from openapp.models import *

def home(request):
    projects = Project.objects.all()
    return render(request, "openapp/home.html", {"projects": projects})

def project(request, pid):
    return render(request, "openapp/project.html", {"project": get_object_or_404(Project, id=pid)})