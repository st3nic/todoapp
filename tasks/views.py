from django.shortcuts import render
from .models import Task

from django.views.generic.edit import DeleteView, CreateView, UpdateView

def tasks(request):
    tasks = Task.objects.all()
    context ={
        'tasks':tasks
    }
    print(context)
    return render(request, 'tasks/index.html', context)

class TaskCreatView(CreateView):
    model = Task
    fields = '__all__'
    template_name='tasks/task_create.html'
    success_url = '/'

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name='tasks/task_update.html'
    success_url ="/"

class TaskDeleteView(DeleteView):
    model = Task
    success_url ="/"
    template_name='tasks/task_delete.html'

