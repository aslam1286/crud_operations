from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from enroll.models import Student
from enroll.forms import StudentRegistration


def add_show(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        
        if fm.is_valid():
            rn = fm.cleaned_data['rollno']
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(rollno=rn, name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud })

def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestud.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
         pi = Student.objects.get(pk=id)
         pi.delete()
         return HttpResponseRedirect('/')
