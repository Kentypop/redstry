from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

poststry= [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'Firsty post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'sean',
		'title': 'Blog Post 2',
		'content': 'second post contentttttttttt',
		'date_posted': 'August 28, 2018'
	}

]

girl= [
	{
	'name': 'mayaka',
	'country': 'japan',
	'love': '5'
	}
]

# Create your views here.
def home(request):
	context= {
		'posts': Post.objects.all()
	}
	return render(request, 'info/home.html', context)

def about(request):
	return render(request, 'info/about.html', {'title': 'About'})	

# Create your views here.
def hometry(request):
	context= {
		'posts': poststry,
		'girls': girl
	}
	return render(request, 'info/hometry.html', context)

def abouttry(request):
	return render(request, 'info/abouttry.html', {'title': 'About'})		