from django.shortcuts import render, redirect
from .models import *
from .forms import *

def task_list(request):
    
    tasks = Task.objects.all()
    
    form = TaskForm
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    all_tasks = {'tasks': tasks, 'form':form}
    
    return render(request, 'tasks/list.html', context=all_tasks)



def updateTask(request, pk):
    task =Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    
    context = {'form': form}
    
    return render(request, 'tasks/task_update.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item': item}
    
    return render(request, 'tasks/task_delete.html', context)
