from django.shortcuts import render,HttpResponse,redirect
from .models import entries

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwordd = request.POST.get('passwordd')
        data = entries.objects.create(username=username,passwordd=passwordd)
        data.save()
    return render(request,'index.html')

def show(request):
    data= entries.objects.all()
    print(data)
    return render(request,'show.html',{'data':data})


def edit(request, id):
    if request.method=="POST":
        name = request.POST.get('username')
        passs = request.POST.get('passwordd')


        edit = entries.objects.get(id= id)
        edit.username = name
        edit.passwordd = passs
        edit.save()
        return redirect("/database")
    
    d = entries.objects.get(id= id)
    context = {"d":d}   
    return render(request, "edit.html", context)


def deletee(request, id):
    d = entries.objects.get(id= id)
    d.delete()
    return redirect("/database")