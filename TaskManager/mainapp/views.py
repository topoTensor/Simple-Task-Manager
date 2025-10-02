from django.http import HttpResponse
from django.shortcuts import render
from .models import TaskModel
from datetime import datetime

time_format = "%Y-%m-%d"

# Create your views here.
def home_view(request):
    tasks = get_tasks(request)

    context = {"tasks" : tasks}
    return render(request, "mainapp/home.html", context)

def search_view(request):
    search = request.GET.get("search", "")

    request.session['search'] = search
    
    tasks = TaskModel.objects.filter( name__icontains = search )

    context = {"tasks" : tasks}
    return render(request, "mainapp/partials/task-table.html", context)

def get_tasks(request):
    task_filter = request.session.get("task_filter", "")
    search = request.session.get("search", "")

    tasks = TaskModel.objects.all()
    if task_filter:
        tasks = tasks.order_by(task_filter)
    if search:
        tasks = tasks.filter( name__icontains = search )

    return tasks

def filter_tasks_view(request):
    task_filter = request.GET.get("select")
    reverse = request.GET.get("reverse", "off")
    if reverse == "on":
        task_filter = '-'+task_filter
        
    request.session['task_filter'] = task_filter

    tasks = get_tasks(request)
    context = {"tasks" : tasks}
    return render(request, "mainapp/partials/task-table.html", context)

def delete_view(request):
    task_id = request.POST.get("task_id")
    task = TaskModel.objects.get(pk=task_id)
    task.delete()
    return HttpResponse("")

def new_task_view(request):

    if request.method == "POST":
        name = request.POST.get("new_task_username", "")
        content = request.POST.get("new_task_content", "")
        startdate = request.POST.get("new_task_startdate", "")
        deadline = request.POST.get("new_task_deadline", "")
        importance = request.POST.get("new_task_importance", "0")
        if len(importance) == 0:
            importance = 0

        if len(content) > 1000:
            context = {"cause" : "The content length exceeds 1000 letters."}
            return render(request, "mainapp/partials/new-task-failed-alert.html", context)

        elif name and content and startdate and deadline:
            TaskModel.objects.create(name=name, content=content, start_date=startdate, deadline_date=deadline, importance=importance)
            
            tasks = get_tasks(request)

            context = {'tasks' : tasks}
            return render(request, "mainapp/partials/new-task-success-alert.html", context)
        else:
            context = {'cause' : 'One of the inputs is empty'}
            return render(request, "mainapp/partials/new-task-failed-alert.html", context)
    else:
        return HttpResponse("")
    
def task_get(request, attr, default):
    res = request.POST.get(attr, "")
    if res == "":
        return default
    else:
        return res
    
def edit_task_view(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = TaskModel.objects.filter(pk=task_id).get()
        name = task_get(request, "input_name", task.name)
        content = task_get(request, "input_content", task.content)
        start_date = task_get(request, "input_start_date", task.start_date)
        if type(start_date) == str:
            start_date = datetime.strptime(start_date, time_format)
        deadline_date = task_get(request, "input_deadline_date", task.deadline_date)
        if type(deadline_date) == str:
            deadline_date = datetime.strptime(deadline_date, time_format)
        importance = task_get(request, "input_importance", task.importance)

        task.name=name
        task.content=content
        task.start_date = start_date
        task.deadline_date = deadline_date
        task.importance=importance

        task.save()

        context = {
            "task" : task,
        }

        return render(request, "mainapp/partials/task_tr_partial.html", context)
    else:
        return HttpResponse("")
    
