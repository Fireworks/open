from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login
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
    project_submitted = False
    
    if request.method == "POST":
        if 'project_submit' in request.POST:
            submit_form = ProjectForm(request.POST)
            project_submitted = True
        else:
            submit_form = CodeForm(request.POST)
            
        if submit_form.is_valid():
            object = submit_form.save()
            object.users.add(request.user.id)
            object.save()
            return redirect(object)
        else:
            if project_submitted:
                return render(request, "openapp/submit.html", {"project_form": submit_form, "code_form": CodeForm(), "project_submitted": project_submitted})
            else:
                return render(request, "openapp/submit.html", {"project_form": ProjectForm(), "code_form": submit_form, "project_submitted": project_submitted})   
    else:
        return render(request, "openapp/submit.html", {"project_form": ProjectForm(), "code_form": CodeForm(), "project_submitted": project_submitted})

@require_POST
def register(request):
    args = {}

    form = UserCreationForm(request.POST)
    args['form'] = UserCreationForm()

    if form.is_valid():
        new_user = form.save()
        new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request, new_user)
        return HttpResponse(status=201)

    return JsonResponse(form.errors, status=400, safe=False)

@require_POST
def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(status=201)

    return JsonResponse(error="Login details incorrect", status=400, safe=False)