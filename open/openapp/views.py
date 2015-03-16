from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from openapp.models import *
from openapp.forms import *

def home(request):
    projects = Project.objects.all()
    return render(request, "openapp/home.html", {"projects": projects})

def search(request):
    return render(request, "openapp/search.html")

def code(request, code_id):
    return render(request, "openapp/code.html", {"code": get_object_or_404(Code, id=code_id)})

def project(request, pid):
    return render(request, "openapp/project.html", {"project": get_object_or_404(Project, id=pid)})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def submit(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            object = project_form.save()
            object.users.add(request.user.id)
            object.save()
            return redirect(object)
        return render(request, "openapp/submit.html", {"project_form": project_form, "code_form": code_form})
    else:
        return render(request, "openapp/submit.html", {"project_form": ProjectForm(), "code_form": CodeForm()})

@require_POST
def register(request):
    args = {}

    form = UserCreationForm(request.POST)
    args['form'] = UserCreationForm()

    if form.is_valid():
        form.save()
        return HttpResponse(status=201)

    return JsonResponse(form.errors, status=400, safe=False)