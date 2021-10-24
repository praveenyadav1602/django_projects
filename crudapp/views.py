from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student
from crudapp import forms
from django.contrib import messages


# Create your views here.

def globalhome(request):
    return render(request,'crudapp/home.html')




def index(request):
    st = Student.objects.all()
    if request.method == "GET":
        form = StudentRegistration
        return render(request,'crudapp/index.html',{'st':st,'form':form},)

    else:
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            form = StudentRegistration

    return render(request,'crudapp/index.html',{'st':st,'form':form},)


def delete(request,id):
    pi = Student.objects.get(id=id)
    print(pi.name)
    pi.delete()
    return HttpResponseRedirect('/crud/')

def update(request,id):    
    if request.method == "GET":
        pi = Student.objects.get(id=id)
        form = StudentRegistration(instance=pi)
        return render(request,'crudapp/update.html',{'form':form})

    else:
        pi = Student.objects.get(id=id)    
        form = StudentRegistration(request.POST,instance=pi)
        if form.is_valid():
            form.save()
        return redirect('/crud/')
        



