from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import F
from openapp.models import *
from openapp.forms import *

def home(request):
    search_form = BasicSearchForm();
    projects = Project.objects.all().order_by('-created')[:10]
    code_snippets = Code.objects.all().order_by('-created')[:10]
    return render(request, "openapp/home.html", {"code_snippets": code_snippets, "projects": projects, "search_form": search_form})

def search(request):
    return render(request, "openapp/search.html")

def user(request, user_id):
    return render(request, "openapp/user.html", {"user": get_object_or_404(User, id=user_id), "code_snippets": Code.objects.filter(users=user_id),
                                                 "projects": Project.objects.filter(users=user_id)})

def code(request, code_id):
    return render(request, "openapp/code.html", {"code": get_object_or_404(Code, id=code_id)})

def project(request, pid):
    comment_submitted = False
    if request.method == "POST" and not request.user.is_anonymous():
        if 'comment_submit' in request.POST:
            submit_form = ProjectCommentForm(request.POST)
            comment_submitted = True
        else:
            submit_form = ProjectFeedbackForm(request.POST)
        if submit_form.is_valid():
            object = submit_form.save(commit=False)
            object.user = request.user
            object.project = Project.objects.get(id=pid)
            object.save()
            return HttpResponseRedirect("")
    return render(request, "openapp/project.html", {"project": get_object_or_404(Project, id=pid), "project_comments": ProjectComment.objects.filter(project=pid),
                                                    "project_comment_form": ProjectCommentForm(), "project_feedback": ProjectFeedback.objects.filter(project=pid).order_by('-rating'),
                                                    "project_feedback_form": ProjectFeedbackForm(), "comment_submitted": comment_submitted})

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

@require_POST
def code_vote(request):
    isUp = request.POST['isUp']
    codeId = request.POST['modelId']

    obj = Code.objects.get(pk=codeId)
    print obj

    if isUp == 'true':
        obj.rating += 1;
    else:
        obj.rating -= 1;

    obj.save();

    return HttpResponse(status=201)

@require_POST
def project_vote(request):
    isUp = request.POST['isUp']
    projectId = request.POST['modelId']

    obj = Project.objects.get(pk=projectId)
    print isUp

    if isUp == 'true':
        obj.rating += 1;
    else:
        obj.rating -= 1;

    obj.save();

    return HttpResponse(status=201)
