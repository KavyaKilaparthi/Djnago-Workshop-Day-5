from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student
# Create your views here.

def insert(request):
	if request.method=="POST":
		name=request.POST['uname']
		roll=request.POST['rollno']
		ag=request.POST['age']
		mobile=request.POST['mbl']
		em=request.POST['email']
		add=request.POST['address']

		data=Student.objects.create(name=name,rollno=roll,age=ag,mobile=mobile,email=em,address=add)
		return redirect('/read')
		return HttpResponse("<h1> Data is inserted successfully!</h1>")
	return render(request,'insert.html',{})
def read(request):
	data=Student.objects.all()#get database data
	return render(request,'read.html',{'info':data})
