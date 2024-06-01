from django.shortcuts import render, redirect

import category
from .forms import categoryForm
from .models import Category

def add_category(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = categoryForm()
    return render(request, 'add_category.html', {'form': form ,'text':'yes'})
def view_category(request, id):
    post = Category.objects.get(pk=id)
    post_form = categoryForm(instance=post)
    if request.method == 'POST':
        post_form = categoryForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_task')
    return render(request, 'add_category.html', {'form': post_form, 'text': 'no', 'post': post})

def delete_category(request,id):
    category=Category.objects.get(pk=id)
    category.delete()
    return redirect('show_task')
