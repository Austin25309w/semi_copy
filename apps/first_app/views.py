from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import *
# Create your views here.

def index (request):
	context = {"users" : User.objects.all()}
	return render(request,"index.html", context)

def new(request):
	if request.method == "POST":
		newuser = User.objects.create(
		first_name = request.POST['first_name'],
		last_name = request.POST['last_name'],
		email = request.POST['email'])
		# newuser.save()
		return redirect("/")

def show(request, id):
	# if request.method == "POST":
	showuser = User.objects.get(id=id)
	user = {
		"id" : showuser.id,
		"name" : showuser.first_name + ' ' + showuser.last_name,
		"date" : showuser.created_at,
		'email' : showuser.email
		}
		
	return render(request, "show.html", user)


def edit(request, id):
	edituser = User.objects.get(id=id)
	showitem = {
		"edituser" : edituser
	}
	return render(request, "edit.html", showitem)

def update(request, id):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		# if the errors object contains anything, loop through each key-value pair and make a flash message
		return redirect("/edit/"+id)
	else:
		updatedUser = User.objects.get(id=id) 
		updatedUser.first_name =request.POST['first_name']
		updatedUser.last_name = request.POST['last_name']
		updatedUser.email = request.POST['email']
		updatedUser.save()
		return redirect("/")


def process(request):
	return render(request, 'newUser.html')



def delete(request, id):
	deleteuser =User.objects.get(id=id)
	deleteuser.delete()
	return redirect('/')