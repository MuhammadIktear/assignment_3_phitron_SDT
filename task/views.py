from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import TaskForm
from .models import Task

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form, 'text': 'no'})

def show_task(request):
    data=Task.objects.all()
    return render(request,'show_task.html',{'data':data})

def edit_task(request,id):
    post=Task.objects.get(pk=id)
    post_form=TaskForm(instance=post)
    if request.method=='POST':
        post_form=TaskForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_task')

    return render(request,'add_Task.html',{'form':post_form,'text':'yes'})
        
def del_task(request,id):
    post=Task.objects.get(pk=id)
    post.delete()
    return redirect('show_task')