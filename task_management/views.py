from django.shortcuts import render

def home(request):
    return render(request,'show_task.html')