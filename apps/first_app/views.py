from django.shortcuts import render, redirect
from .models import Blog, Comment
# CONTROLLER !!!!
# Create your views here.
# def index(request):
# 	context = {
# 	"blogs" : Blog.objects.all()
# 	# select * from Blog
# 	}
# 	print ("*"*50)
# 	return render(request, "first_app/index.html", context )

def index(request):
	# context = {
	# "register" : Blog.objects.all()
	# # select * from Blog
	# }
	print ("*"*50)
	return render(request, "registration/registration_form.html", )

def blogs(request):
	# using ORM
	Blog.objects.create(title=request.POST['fl_name'], blog=request.POST['newest'])
	# insert into blogs (title, blog, created_at, updated_at) values (title, blog, now(), now() )
	print ("*"*50)
	print Blog.objects.all().last()
	return redirect('/')
