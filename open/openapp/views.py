from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from openapp.models import *
from openapp.forms import *

def home(request):
    projects = Project.objects.all()
    return render(request, "openapp/home.html", {"projects": projects})

def project(request, pid):
    return render(request, "openapp/project.html", {"project": get_object_or_404(Project, id=pid)})

def submit(request):
    if request.method == "POST":
        object = ProjectForm(request.POST).save()
        return redirect(object)
    else:
        return render(request, "openapp/submit.html", {"form": ProjectForm({"owner": request.user})})