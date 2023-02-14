from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.models import Person
from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request,"index.html")

def about(request):
    return render(request ,"about.html")

def form(request):
    if request.method =="POST":
        name = request.POST["name"]
        age = request.POST["age"]
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/showdata")
    else :
        return render(request,"form.html")

def showdata(request):
    all_person = Person.objects.all()
    return render(request,"showdata.html",{"all_person": all_person})

def edit(request,person_id):
    if request.method =="POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST['age']
        person.save()
        messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
        return redirect("/showdata")
    else :
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/showdata")